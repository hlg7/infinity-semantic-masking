"""Block target conditional text keys at selected Infinity scales.

Filter already-encoded keys before each CrossAttnBlock. Removing these keys from
softmax attention is mathematically equivalent to assigning them -inf bias.
This preserves native FlashAttention, the unconditional branch and global pooling.
"""
import torch


def filter_conditional_keys(ca_kv, positions):
    kv, cu, max_length = ca_kv
    bounds = cu.tolist()
    if len(bounds) not in (2, 3) or bounds[0] != 0 or bounds[-1] != len(kv):
        raise ValueError('This experiment supports B=1 with one or two CFG branches')
    length = bounds[1]
    if any(type(p) is not int or not 0 <= p < length for p in positions):
        raise ValueError('Target index outside the conditional text sequence')
    positions = sorted(set(positions))
    if not positions:
        return ca_kv
    keep = torch.ones(len(kv), dtype=torch.bool, device=kv.device)
    keep[positions] = False
    remaining = length - len(positions)
    if remaining <= 0:
        raise ValueError('Cannot mask the entire text sequence; retain EOS/special tokens')
    new_bounds = [0, remaining] + ([bounds[2] - len(positions)] if len(bounds) == 3 else [])
    new_cu = torch.tensor(new_bounds, dtype=cu.dtype, device=cu.device)
    new_max = max(b - a for a, b in zip(new_bounds, new_bounds[1:]))
    return kv[keep].contiguous(), new_cu, new_max


class ScaleMask:
    def __init__(self, blocks, scale_schedule):
        self.blocks = list(blocks)
        self.scale_schedule = scale_schedule
        self.handles = []
        self.set_plan([], [])

    def set_plan(self, masked_scales, positions):
        if any(type(s) is not int or not 1 <= s <= len(self.scale_schedule) for s in masked_scales):
            raise ValueError('Scale outside schedule')
        if masked_scales and not positions:
            raise ValueError('Masked scales require nonempty semantic token positions')
        self.masked_scales = set(masked_scales)
        self.positions = sorted(set(positions))
        self.audit = []
        self._original = self._filtered = None

    def _hook(self, layer):
        def hook(module, args, kwargs):
            if args or 'scale_ind' not in kwargs or 'ca_kv' not in kwargs:
                raise RuntimeError('Unexpected Infinity block interface; expected keyword scale_ind/ca_kv')
            scale = kwargs['scale_ind'] + 1
            if not 1 <= scale <= len(self.scale_schedule):
                raise RuntimeError('Invalid scale_ind')
            t, h, w = self.scale_schedule[scale - 1]
            if kwargs['x'].shape[1] != t * h * w:
                raise RuntimeError('Query length does not match scale')
            ca_kv = kwargs['ca_kv']
            masked = scale in self.masked_scales
            before = int(ca_kv[1][1])
            if masked:
                if self._original is not ca_kv:
                    self._filtered = filter_conditional_keys(ca_kv, self.positions)
                    self._original = ca_kv
                kwargs = dict(kwargs, ca_kv=self._filtered)
            after = int(kwargs['ca_kv'][1][1])
            self.audit.append({'layer': layer, 'scale': scale, 'masked': masked,
                               'conditional_keys_before': before, 'conditional_keys_after': after})
            return args, kwargs
        return hook

    def __enter__(self):
        for layer, block in enumerate(self.blocks):
            if not hasattr(block, 'ca') or getattr(block.ca, 'for_attn_pool', True):
                raise RuntimeError('Expected only Infinity CrossAttnBlock generation layers')
            self.handles.append(block.register_forward_pre_hook(self._hook(layer), with_kwargs=True))
        return self

    def verify(self):
        expected = {(layer, s) for layer in range(len(self.blocks))
                    for s in range(1, len(self.scale_schedule) + 1)}
        if len(self.audit) != len(expected) or {(a['layer'], a['scale']) for a in self.audit} != expected:
            raise RuntimeError('Incomplete or duplicate layer/scale mask audit')
        for a in self.audit:
            delta = a['conditional_keys_before'] - a['conditional_keys_after']
            if delta != (len(self.positions) if a['masked'] else 0):
                raise RuntimeError('Wrong number of semantic keys removed')

    def __exit__(self, *exc):
        for handle in self.handles:
            handle.remove()
        self.handles.clear()
        self._original = self._filtered = None
