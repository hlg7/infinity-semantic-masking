"""Plan locally or generate Infinity semantic-class prefix/suffix interventions."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
from types import SimpleNamespace

from common import ROOT, INFINITY_REVISION, read_json, write_json, sha256, square_schedule, selected_plans
from semantic_masking import SEMANTICS, compile_records


def make_plan(records, seeds, semantics, scale_count, mode):
    rows = []
    for record in records:
        dataset_semantic = record.get('target_semantic')
        if dataset_semantic is not None and dataset_semantic not in semantics:
            continue
        for seed in seeds:
            base = f"{record['id']}__s{seed}__baseline"
            rows.append({'id': base, 'prompt_id': record['id'], 'prompt': record['prompt'],
                         'seed': seed, 'semantic': None, 'condition': 'baseline',
                         'masked_scales': [], 'aliases': [], 'baseline_id': base})
            for target in record['targets']:
                if target['semantic'] not in semantics:
                    continue
                if dataset_semantic is not None and target['semantic'] != dataset_semantic:
                    continue
                for condition in selected_plans(scale_count, mode):
                    if condition['name'] == 'baseline':
                        continue
                    name = f"{record['id']}__s{seed}__{target['semantic']}__{condition['name']}"
                    rows.append({'id': name, 'prompt_id': record['id'], 'prompt': record['prompt'],
                                 'seed': seed, 'semantic': target['semantic'],
                                 'condition': condition['name'], 'masked_scales': condition['masked_scales'],
                                 'aliases': condition['aliases'], 'baseline_id': base})
    if len({r['id'] for r in rows}) != len(rows):
        raise ValueError('Duplicate seeds or generated image IDs')
    return rows


def tensor_hash(tensor):
    return hashlib.sha256(tensor.detach().contiguous().cpu().view(dtype=__import__('torch').uint8).numpy().tobytes()).hexdigest()


def generate(args, config, records, plan):
    import torch
    if not torch.cuda.is_available():
        raise RuntimeError('Actual Infinity generation requires CUDA; use --plan-only for local preparation')
    repo = ROOT / 'vendor/Infinity'
    revision = subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD'], text=True).strip()
    if revision != INFINITY_REVISION:
        raise RuntimeError('Infinity checkout differs from the pinned revision')
    for key in ('model_path', 'vae_path', 'text_encoder_ckpt', 'cache_dir'):
        path = Path(config[key])
        config[key] = str(path if path.is_absolute() else ROOT / path)
    for key in ('model_path', 'vae_path', 'text_encoder_ckpt'):
        if not Path(config[key]).exists():
            raise FileNotFoundError(f'Missing {key}: {config[key]}; download assets separately first')
    if (args.output / 'runs.jsonl').exists():
        raise ValueError('Use a fresh output directory; generation does not resume')
    sys.path.insert(0, str(repo))
    from tools.run_infinity import load_tokenizer, load_visual_tokenizer, load_transformer, encode_prompt
    from infinity.utils.dynamic_resolution import dynamic_resolution_h_w
    from infinity_mask import ScaleMask
    from tokenize_prompts import tokenize_record
    from PIL import Image

    scale_schedule = [(1, h, w) for _, h, w in dynamic_resolution_h_w[1.0][config['pn']]['scales']]
    if scale_schedule != square_schedule(config['pn']):
        raise RuntimeError('Official scale schedule differs from planned schedule')
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    torch.backends.cudnn.benchmark = False
    tokenizer, encoder = load_tokenizer(t5_path=config['text_encoder_ckpt'])
    mapped = {r['id']: tokenize_record(r, tokenizer) for r in records}
    write_json(args.output / 'tokens.json', {'records': list(mapped.values())})
    vae = load_visual_tokenizer(SimpleNamespace(**config)).eval().requires_grad_(False)
    model = load_transformer(vae, SimpleNamespace(**config))
    write_json(args.output / 'manifest.json', {
        'backbone': 'Infinity', 'upstream_revision': revision, 'config': config,
        'basic_py_sha256': sha256(repo/'infinity/models/basic.py'),
        'local_patch': 'Forward scale_ind in CrossAttnBlock non-fused normalization path',
        'annotations_sha256': sha256(args.annotations), 'mode': args.mode, 'seeds': args.seeds,
        'scale_schedule': scale_schedule, 'mask_unit': 'semantic_class',
        'intervention': 'Remove selected conditional CA keys at generation blocks only; native flash attention',
        'text_policy': 'Full prompt, no augmentation, no truncation; pooled/global and uncond inputs unchanged',
        'plan': plan,
    })

    def save_image(image, path):
        path.parent.mkdir(parents=True, exist_ok=True)
        # Official Infinity output is uint8 BGR, not RGB.
        Image.fromarray(image.cpu().numpy()[..., ::-1].copy()).save(path)
        return sha256(path)

    def infer(text, seed):
        with torch.inference_mode(), torch.autocast('cuda', dtype=torch.bfloat16):
            _, _, images = model.autoregressive_infer_cfg(
                vae=vae, scale_schedule=scale_schedule, label_B_or_BLT=text, B=1,
                negative_label_B_or_BLT=None, g_seed=seed,
                cfg_list=[config['cfg']] * len(scale_schedule),
                tau_list=[config['tau']] * len(scale_schedule),
                cfg_insertion_layer=[config['cfg_insertion_layer']],
                top_k=config['top_k'], top_p=config['top_p'],
                vae_type=config['vae_type'], sampling_per_bits=config['sampling_per_bits'],
                returns_vemb=1, ret_img=True, inference_mode=True, gt_leak=0,
            )
        return images[0]

    completed, diagnostics = 0, []
    for record in records:
        if not any(r['prompt_id'] == record['id'] for r in plan):
            continue
        with torch.inference_mode():
            text = encode_prompt(tokenizer, encoder, record['prompt'], enable_positive_prompt=False)
        frozen = tensor_hash(text[0])
        if text[1] != [mapped[record['id']]['tokenization']['sequence_length']]:
            raise RuntimeError('Encoded text length differs from token map')
        targets = {t['semantic']: t for t in mapped[record['id']]['targets']}
        for seed in args.seeds:
            reference = infer(text, seed)
            reference_hash = tensor_hash(reference)
            save_image(reference, args.output / 'diagnostics' / f"{record['id']}__s{seed}__reference.png")
            with ScaleMask(model.unregistered_blocks, scale_schedule) as mask:
                for row in [r for r in plan if r['prompt_id'] == record['id'] and r['seed'] == seed]:
                    positions = targets[row['semantic']]['token_positions'] if row['semantic'] else []
                    mask.set_plan(row['masked_scales'], positions)
                    image = infer(text, seed)
                    mask.verify()
                    if tensor_hash(text[0]) != frozen:
                        raise RuntimeError('Original text embeddings changed')
                    if row['condition'] == 'baseline' and tensor_hash(image) != reference_hash:
                        raise RuntimeError('No-op hook differs from native baseline')
                    path = args.output / 'images' / (row['id'] + '.png')
                    image_hash = save_image(image, path)
                    audit_path = args.output / 'audit' / (row['id'] + '.json')
                    write_json(audit_path, mask.audit)
                    result = dict(row, image=str(path.resolve()), image_sha256=image_hash,
                                  token_positions=positions, audit=str(audit_path.resolve()),
                                  text_sha256=frozen, backbone='Infinity')
                    with (args.output / 'runs.jsonl').open('a') as stream:
                        stream.write(json.dumps(result) + '\n')
                    completed += 1
                    print(f"[{completed}/{len(plan)}] {row['id']}", flush=True)
                    if row['condition'] == 'full_mask':
                        mask.set_plan(row['masked_scales'], positions)
                        repeated = infer(text, seed)
                        mask.verify()
                        if tensor_hash(repeated) != tensor_hash(image):
                            raise RuntimeError('Full-mask repeat differs')
                        diagnostics.append({'id': row['id'], 'full_mask_repeat_equal': True})
            diagnostics.append({'prompt_id': record['id'], 'seed': seed, 'native_noop_equal': True})
    write_json(args.output / 'summary.json', {'status': 'completed', 'images': completed, 'diagnostics': diagnostics})


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--annotations', type=Path, default=ROOT/'data/smoke_annotations.json')
    p.add_argument('--config', type=Path, default=ROOT/'configs/infinity_2b.json')
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--seeds', nargs='+', type=int, default=[42])
    p.add_argument('--semantics', nargs='+', choices=SEMANTICS, default=list(SEMANTICS))
    p.add_argument('--mode', choices=['smoke', 'full'], default='smoke')
    p.add_argument('--plan-only', action='store_true', help='No GPU, weights or network; just list all images')
    args = p.parse_args()
    if any(not 0 <= s < 2**32 for s in args.seeds):
        p.error('Seeds must be in [0, 2**32)')
    config = read_json(args.config)
    if config['model_type'] != 'infinity_2b' or config['apply_spatial_patchify'] != 0:
        p.error('Initial adapter supports the official 2B non-patchified model')
    records = compile_records(read_json(args.annotations))
    schedule = square_schedule(config['pn'])
    plan = make_plan(records, args.seeds, args.semantics, len(schedule), args.mode)
    args.output.mkdir(parents=True, exist_ok=True)
    write_json(args.output / 'plan.json', {'mode': args.mode, 'scale_schedule': schedule,
                                         'image_count': len(plan), 'rows': plan})
    if args.plan_only:
        print(f'Local plan: {len(plan)} images, {len(schedule)} scales; no generation performed')
        return
    generate(args, config, records, plan)


if __name__ == '__main__':
    main()
