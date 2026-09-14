"""Build image/task manifests and reuse the frozen six-semantic evaluators."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

from common import ROOT, read_json, evaluator_imports


def build_manifest(runs, checks):
    evaluator_imports()
    from semantic_evaluators.protocol import build_check, validate_check
    ids = set()
    for check in checks:
        if check['id'] in ids:
            raise ValueError('Check IDs must be unique')
        ids.add(check['id'])
        if 'check' in check:
            validate_check(check['check'])
            if check['semantic'] != check['check']['semantic']:
                raise ValueError('Imported check semantic mismatch')
        else:
            build_check(check)
    active = {}
    for run in runs:
        if run['semantic'] is not None:
            active.setdefault(run['prompt_id'], set()).add(run['semantic'])
    rows = []
    for run in runs:
        selected = [c for c in checks if c['prompt_id'] == run['prompt_id']
                    and c['semantic'] in active.get(run['prompt_id'], set())
                    and (run['semantic'] is None or c['semantic'] == run['semantic'])]
        if not selected:
            raise ValueError(f"No evaluation checks for {run['id']}")
        for check in selected:
            row = {key: check[key] for key in ('semantic', 'objects', 'expected', 'subtype') if key in check}
            if 'check' in check:
                row = {'check': check['check']}
            row.update(id=f"{run['id']}--{check['id']}", image=run['image'],
                       image_sha256=run['image_sha256'],
                       baseline_id=f"{run['baseline_id']}--{check['id']}",
                       metadata={'backbone': 'Infinity', 'prompt_id': run['prompt_id'],
                                 'check_id': check['id'], 'seed': run['seed'],
                                 'condition': run['condition'], 'aliases': run['aliases'],
                                 'masked_scales': run['masked_scales']})
            rows.append(row)
    return rows


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--run', type=Path, required=True)
    p.add_argument('--checks', type=Path, default=ROOT/'data/smoke_checks.json')
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--manifest-only', action='store_true')
    p.add_argument('--tool', choices=['all', 'grounding_dino', 'qwen_vlm'], default='all')
    args = p.parse_args()
    summary = read_json(args.run / 'summary.json')
    if summary['status'] != 'completed':
        raise ValueError('Generation must complete before evaluation')
    runs = [json.loads(line) for line in (args.run / 'runs.jsonl').read_text().splitlines() if line.strip()]
    if len(runs) != summary['images']:
        raise ValueError('Generation row count mismatch')
    rows = build_manifest(runs, read_json(args.checks))
    args.output.mkdir(parents=True, exist_ok=True)
    path = args.output / 'input.jsonl'
    path.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows))
    evaluator_imports()
    from semantic_evaluators.io import load_manifest
    load_manifest(path)  # Validate baseline pairing, questions and actual image files.
    print(f'Validated {len(rows)} evaluation checks')
    if not args.manifest_only:
        # Vendored package is self-contained; no external evaluator checkout needed.
        import os
        env = dict(os.environ, PYTHONPATH=str(ROOT/'vendor/semantic-evaluators'),
                   HF_HOME=str(ROOT/'assets/hf-cache'))
        subprocess.run([sys.executable, '-m', 'semantic_evaluators', 'run', '--manifest', str(path),
                        '--output', str(args.output/'scores'), '--tool', args.tool], env=env, check=True)


if __name__ == '__main__':
    main()
