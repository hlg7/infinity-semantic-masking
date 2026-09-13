"""Audit the downloaded 10-prompt pilot and prepare visual review sheets."""
import collections
import csv
import hashlib
import json
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
R = ROOT / 'reports/csfm50_pilot'
O = ROOT / 'reports/pilot_review'
O.mkdir(exist_ok=True)
read = lambda p: json.loads(p.read_text())
runs = [json.loads(s) for s in (R/'generation/runs.jsonl').read_text().splitlines()]
scores = [json.loads(s) for s in (R/'evaluation/scores/results.jsonl').read_text().splitlines()]
tokens = {t['id']: t for t in read(R/'generation/tokens.json')['records']}
plan = read(R/'generation/plan.json')
assert len(runs) == len({r['id'] for r in runs}) == plan['image_count'] == 40
assert {r['id'] for r in runs} == {r['id'] for r in plan['rows']}
hashes = {}
for r in runs:
    p = R/'generation/images'/Path(r['image']).name
    hashes[r['id']] = hashlib.sha256(p.read_bytes()).hexdigest()
    assert hashes[r['id']] == r['image_sha256']
    t = tokens[r['prompt_id']]
    assert t['tokenization']['actual_encoder_ids_match']
    assert r['semantic'] in (None, t['target_semantic'])
    target = next(x for x in t['targets'] if x['semantic'] == t['target_semantic'])
    pos = target['token_positions'] if r['semantic'] else []
    assert r['token_positions'] == pos
    want = {'baseline': [], 'prefix_06': list(range(1, 7)),
            'suffix_06': list(range(7, 14)), 'full_mask': list(range(1, 14))}[r['condition']]
    assert r['masked_scales'] == want
    audit = read(R/'generation/audit'/Path(r['audit']).name)
    assert len(audit) == 416
    assert {(a['layer'], a['scale']) for a in audit} == {(l, s) for l in range(32) for s in range(1, 14)}
    for a in audit:
        assert a['masked'] == (a['scale'] in want)
        assert a['conditional_keys_before'] - a['conditional_keys_after'] == (len(pos) if a['masked'] else 0)
for s in scores:
    assert s['image_sha256'] == hashes[s['id'].split('--')[0]]
    assert s['observation']['status'] == 'ok'
assert len(scores) == len({s['id'] for s in scores}) == 40
diagnostics = read(R/'generation/summary.json')['diagnostics']
assert len(diagnostics) == 20
assert all(d.get('native_noop_equal', d.get('full_mask_repeat_equal')) is True for d in diagnostics)
curves = list(csv.DictReader((R/'evaluation/scores/scale_curves.csv').open()))
for c in curves:
    selected = []
    for s in scores:
        m = s['metadata']
        aliases = [{'direction':'prefix','boundary':0}, {'direction':'suffix','boundary':13}] if m['condition'] == 'baseline' else m['aliases']
        if s['semantic'] == c['semantic'] and c['subtype'] in ('all', s['subtype']) and {'direction':c['direction'],'boundary':int(c['boundary'])} in aliases:
            selected.append(s)
    assert len(selected) == int(c['checks_total'])
    assert abs(float(c['success_rate']) - sum(s['success'] for s in selected)/len(selected)) < 1e-8
    positive = [s for s in selected if s['baseline_success'] == 1]
    assert int(c['baseline_correct_checks']) == len(positive)
    assert (abs(float(c['retention']) - sum(s['success'] for s in positive)/len(positive)) < 1e-8) if positive else c['retention'] == ''
report = {'status':'passed','images_hash_verified':40,'layer_scale_records_verified':40*416,
          'score_rows_verified':40,'curve_rows_recomputed':len(curves),'diagnostics_passed':20,
          'score_status_counts':dict(collections.Counter(s['status'] for s in scores)),
          'baseline_correct':sum(s['success'] for s in scores if s['metadata']['condition']=='baseline'),
          'targets':{pid:next(t['target_fragments'] for t in r['targets'] if t['semantic']==r['target_semantic']) for pid,r in tokens.items()}}
(O/'audit_summary.json').write_text(json.dumps(report, indent=2)+'\n')
conditions = ['baseline','prefix_06','full_mask','suffix_06']
ids = list(tokens)
with (O/'score_table.csv').open('w', newline='') as f:
    w = csv.writer(f); w.writerow(['prompt_id','semantic','subtype']+conditions)
    for pid in ids:
        ss = {s['metadata']['condition']:s for s in scores if s['metadata']['prompt_id']==pid}
        w.writerow([pid, ss['baseline']['semantic'], ss['baseline']['subtype']]+[ss[c]['status'] for c in conditions])
for page in range(2):
    sheet = Image.new('RGB', (1440, 1950), 'white'); draw = ImageDraw.Draw(sheet)
    for ri, pid in enumerate(ids[page*5:(page+1)*5]):
        for ci, cond in enumerate(conditions):
            r = next(r for r in runs if r['prompt_id']==pid and r['condition']==cond)
            s = next(s for s in scores if s['id'].split('--')[0]==r['id'])
            im = Image.open(R/'generation/images'/Path(r['image']).name); im.thumbnail((360,360))
            sheet.paste(im, (ci*360, ri*390+30))
            draw.text((ci*360+5, ri*390+3), pid+' | '+cond, fill='black')
            draw.text((ci*360+5, ri*390+15), s['status']+' / '+str(s['observation']['answer']), fill='black')
    sheet.save(O/f'contact_sheet_{page+1}.jpg', quality=95)
print(json.dumps(report, indent=2))
