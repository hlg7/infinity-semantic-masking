import ast
import json
from pathlib import Path
import tempfile
import unittest

import torch
from torch import nn
from common import ROOT, read_json, square_schedule, schedules
from semantic_masking import compile_records
from annotate_semantics import annotation_from_labels, decode_labels, response_text
from tokenize_prompts import load_tokenizer, tokenize_record
from infinity_mask import filter_conditional_keys, ScaleMask
from generate import make_plan
from evaluate import build_manifest


class PipelineTests(unittest.TestCase):
    def test_real_t5_tokenization_all_fixtures(self):
        tokenizer = load_tokenizer(ROOT/'assets/flan-t5-xl')
        for record in compile_records(read_json(ROOT/'data/fixtures_annotations.json') + read_json(ROOT/'data/smoke_annotations.json')):
            mapped = tokenize_record(record, tokenizer)
            tokens = mapped['tokenization']
            for target in mapped['targets']:
                self.assertTrue(target['token_positions'])
                self.assertTrue(all(tokens['special_tokens_mask'][i] == 0 for i in target['token_positions']))

    def test_real_qwen_saved_response(self):
        response = read_json(ROOT/'reports/annotation_responses/p000.json')
        labels = decode_labels(response_text(response), 8)
        record = {'id': 'qwen', 'prompt': 'An orange is above an orange cup.'}
        compiled = compile_records([annotation_from_labels(record, labels)])[0]
        target = {t['semantic']: t['target_fragments'] for t in compiled['targets']}
        self.assertEqual(target, {'object': ['orange', 'cup'], 'color': ['orange'], 'spatial_relation': ['above']})

    def test_attention_equivalence_and_unconditional_branch(self):
        torch.manual_seed(17)
        kv = torch.randn(14, 4, dtype=torch.float64)
        original = kv.clone()
        cu = torch.tensor([0, 7, 14], dtype=torch.int32)
        filtered, bounds, maximum = filter_conditional_keys((kv, cu, 7), [1, 3, 5])
        self.assertTrue(torch.equal(kv, original))
        self.assertTrue(torch.equal(filtered[4:], kv[7:]))
        self.assertEqual(bounds.tolist(), [0, 4, 11])
        self.assertEqual(maximum, 7)
        q = torch.randn(3, 4, dtype=torch.float64)
        logits = q @ kv[:7].T / 2
        logits[:, [1, 3, 5]] = -torch.inf
        masked = logits.softmax(-1) @ kv[:7]
        actual = (q @ filtered[:4].T / 2).softmax(-1) @ filtered[:4]
        torch.testing.assert_close(masked, actual, rtol=1e-12, atol=1e-12)

    def test_hook_scale_gating_and_noop(self):
        class Block(nn.Module):
            def __init__(self):
                super().__init__()
                self.ca = type('CA', (), {'for_attn_pool': False})()
            def forward(self, x, ca_kv, cond_BD, scale_ind):
                return ca_kv, cond_BD
        block = Block()
        schedule = [(1, 1, 1), (1, 2, 2)]
        kv = (torch.randn(10, 3), torch.tensor([0, 5, 10], dtype=torch.int32), 5)
        global_cond = torch.randn(2, 3)
        with ScaleMask([block], schedule) as mask:
            mask.set_plan([2], [1, 3])
            first, g1 = block(x=torch.zeros(2, 1, 3), ca_kv=kv, cond_BD=global_cond, scale_ind=0)
            second, g2 = block(x=torch.zeros(2, 4, 3), ca_kv=kv, cond_BD=global_cond, scale_ind=1)
            self.assertIs(first, kv)
            self.assertIs(g1, global_cond)
            self.assertIs(g2, global_cond)
            self.assertEqual(second[1].tolist(), [0, 3, 8])
            mask.verify()
        self.assertFalse(block._forward_pre_hooks)

    def test_schedule_and_baseline_reuse(self):
        records = compile_records(read_json(ROOT/'data/smoke_annotations.json'))
        from semantic_masking import SEMANTICS
        plans = schedules(13)
        self.assertEqual(len(plans), 26)
        for plan in plans:
            for alias in plan['aliases']:
                k = alias['boundary']
                expected = list(range(1, k+1)) if alias['direction'] == 'prefix' else list(range(k+1, 14))
                self.assertEqual(plan['masked_scales'], expected)
        full = make_plan(records, [42], SEMANTICS, 13, 'full')
        smoke = make_plan(records, [42], SEMANTICS, 13, 'smoke')
        self.assertEqual(len(full), 151)
        self.assertEqual(len(smoke), 19)
        self.assertEqual(sum(r['condition'] == 'baseline' for r in full), 1)

    def test_manifest_multiple_checks_one_image(self):
        from semantic_masking import SEMANTICS
        records = compile_records(read_json(ROOT/'data/smoke_annotations.json'))
        runs = make_plan(records, [42], SEMANTICS, 13, 'smoke')
        for run in runs:
            run.update(image='/placeholder.png', image_sha256='f'*64)
        rows = build_manifest(runs, read_json(ROOT/'data/smoke_checks.json'))
        self.assertEqual(len(rows), 40)
        by_id = {r['id']: r for r in rows}
        self.assertEqual(len(by_id), 40)
        for row in rows:
            base = by_id[row['baseline_id']]
            self.assertEqual(base['expected'], row['expected'])
            self.assertEqual(base['objects'], row['objects'])
        color_runs = [r for r in runs if r['semantic'] in (None, 'color')]
        color_rows = build_manifest(color_runs, read_json(ROOT/'data/smoke_checks.json'))
        self.assertEqual(len(color_rows), 8)
        self.assertTrue(all(r['semantic'] == 'color' for r in color_rows))

    def test_dataset_semantic_selection_and_frozen_checks(self):
        from semantic_masking import SEMANTICS
        from common import evaluator_imports
        evaluator_imports()
        from semantic_evaluators.protocol import build_check
        annotation = dict(read_json(ROOT/'data/smoke_annotations.json')[0], target_semantic='color')
        records = compile_records([annotation])
        plan = make_plan(records, [42], SEMANTICS, 13, 'full')
        self.assertEqual(len(plan), 26)
        self.assertEqual({r['semantic'] for r in plan}, {None, 'color'})
        self.assertEqual(make_plan(records, [42], ['object'], 13, 'full'), [])
        self.assertEqual(next(t for t in records[0]['targets'] if t['semantic']=='color')['target_fragments'], ['red','blue'])
        frozen = build_check({'semantic':'color', 'objects':['plate'], 'expected':'red'})
        checks = [{'id':'frozen', 'prompt_id':records[0]['id'], 'semantic':'color', 'check':frozen}]
        for row in plan:
            row.update(image='/placeholder.png', image_sha256='f'*64)
        output = build_manifest(plan, checks)
        self.assertEqual(len(output),26)
        self.assertTrue(all(row['check']==frozen for row in output))
        bad = dict(annotation, target_semantic='other')
        with self.assertRaises(ValueError):
            compile_records([bad])

    def test_reject_empty_attention_or_invalid_indices(self):
        ca = (torch.randn(4, 3), torch.tensor([0, 4], dtype=torch.int32), 4)
        for positions in ([4], [-1], [0, 1, 2, 3]):
            with self.assertRaises(ValueError):
                filter_conditional_keys(ca, positions)

    def test_curve_endpoints_and_equal_prompt_weight(self):
        from summarize import curves
        rows = []
        for identity, score in [('p1', 1), ('p1', 0), ('p2', 1)]:
            rows.append({'semantic': 'object', 'subtype': 'identity', 'success': score,
                         'baseline_success': score, 'paired_delta': 0, 'absolute_error': None,
                         'metadata': {'prompt_id': identity, 'seed': 42, 'condition': 'baseline', 'aliases': []}})
        result = curves(rows, 13)
        overall = [r for r in result if r['subtype'] == 'all']
        self.assertEqual({(r['direction'], r['boundary']) for r in overall}, {('prefix', 0), ('suffix', 13)})
        self.assertTrue(all(r['success_rate'] == 0.75 for r in overall))
        self.assertTrue(all(r['checks_valid'] == 3 for r in overall))

    def test_pinned_infinity_interfaces(self):
        root = ROOT/'vendor/Infinity'
        module = ast.parse((root/'infinity/models/basic.py').read_text())
        block = next(n for n in module.body if isinstance(n, ast.ClassDef) and n.name == 'CrossAttnBlock')
        forward = next(n for n in block.body if isinstance(n, ast.FunctionDef) and n.name == 'forward')
        sa_calls = [n for n in ast.walk(forward) if isinstance(n, ast.Call)
                    and isinstance(n.func, ast.Attribute) and n.func.attr == 'sa']
        self.assertEqual(len(sa_calls), 2)
        self.assertTrue(all(any(k.arg == 'scale_ind' for k in n.keywords) for n in sa_calls))
        infer = ast.parse((root/'infinity/models/infinity.py').read_text())
        calls = [n for n in ast.walk(infer) if isinstance(n, ast.Call)
                 and isinstance(n.func, ast.Name) and n.func.id == 'm']
        self.assertTrue(any({'scale_ind', 'ca_kv', 'x'} <= {k.arg for k in n.keywords} for n in calls))
        dynamic = ast.parse((root/'infinity/utils/dynamic_resolution.py').read_text())
        assignment = next(n for n in dynamic.body if isinstance(n, ast.Assign)
                          and any(isinstance(t, ast.Name) and t.id == 'ratio2hws' for t in n.targets))
        square = ast.literal_eval(assignment.value)[1.0]
        self.assertEqual(square_schedule('1M'), [(1,h,w) for h,w in square])


if __name__ == '__main__':
    unittest.main()
