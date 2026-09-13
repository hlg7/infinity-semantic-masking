"""Audited postprocessing of six reviewed out-of-vocabulary pilot-independent scores."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'vendor/semantic-evaluators'))
from semantic_evaluators.scoring import parse_observation, judge
from semantic_evaluators.io import atomic_json

EXPECTED = {
    'color_008__s42__color__prefix_05--color_008__check': ('color', 'silver'),
    'color_008__s42__color__prefix_12--color_008__check': ('color', 'silver'),
    'color_008__s42__color__full_mask--color_008__check': ('color', 'silver'),
    'color_023__s42__color__prefix_05--color_023__check': ('color', 'gray'),
    'color_023__s42__color__prefix_06--color_023__check': ('color', 'gray'),
    'shape_048__s42__shape__prefix_02--shape_048__check': ('shape', 'octagonal'),
}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--scores', type=Path, required=True)
    p.add_argument('--apply', action='store_true')
    args = p.parse_args()
    out = args.scores
    assert not (out/'.running.lock').exists(), 'Scorer is still active'
    manifest = json.loads((out/'manifest.json').read_text())
    inputs = {r['id']: r for r in manifest['inputs']}
    assert len(inputs) == 7800
    paths = {f.stem:f for f in (out/'predictions').glob('*.json')}
    assert set(paths) == set(inputs)
    original_hashes = {i:hashlib.sha256(f.read_bytes()).hexdigest() for i,f in paths.items()}
    originals = {i:json.loads(f.read_text()) for i,f in paths.items()}
    assert {i for i,d in originals.items() if d['status']=='evaluation_error'} == set(EXPECTED)
    changes = []
    for i,(sem,answer) in EXPECTED.items():
        d = originals[i]; check = inputs[i]['check']
        assert d['error'] == 'Invalid answer category' and d['semantic'] == sem
        assert d['input_digest'] == inputs[i]['input_digest']
        allowed = check['evaluator_input']['allowed_answers']
        assert answer not in allowed and 'other' in allowed
        raw = json.loads(d['raw'])
        assert raw['answer'] == answer and raw['identity_status'] == 'present' and raw['status'] == 'ok'
        assert all(json.loads(a)['answer']==answer for a in d['attempts'])
        observation = dict(raw, answer='other')
        observation = parse_observation(json.dumps(observation), check)
        score = judge(observation, check)
        provenance = dict(method='reviewed_category_to_existing_other_v1', original_answer=answer,
                          normalized_answer='other', reason='Named color/shape outside enumerated vocabulary; existing other category applies.',
                          original_prediction_sha256=original_hashes[i])
        result = {k:v for k,v in d.items() if k not in ('error','status','success','absolute_error')}
        result.update(observation=observation, postprocessing=provenance, previous_errors=[d], **score)
        changes.append((i,result,provenance))
    report = dict(mode='apply' if args.apply else 'dry_run', changed_count=len(changes),
                  note='Post-hoc category normalization; raw Qwen answers preserved, no new model inference.',
                  changes=[dict(id=i,**a) for i,_,a in changes])
    if args.apply:
        backup = out/'repairs/category_other_v1'
        backup.mkdir(parents=True, exist_ok=False)
        for i,_,_ in changes:
            (backup/(i+'.json')).write_bytes(paths[i].read_bytes())
        atomic_json(backup/'original_hashes.json', original_hashes)
        for i,result,_ in changes:
            atomic_json(paths[i], result)
        for i,f in paths.items():
            if i not in EXPECTED:
                assert hashlib.sha256(f.read_bytes()).hexdigest() == original_hashes[i]
        report.update(unchanged_predictions_verified=7794, utc=datetime.now(timezone.utc).isoformat())
        atomic_json(backup/'repair_report.json', report)
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
