"""Audit downloaded full-run outputs and render review figures."""
from pathlib import Path
import json, hashlib, csv, collections, os
ROOT=Path(__file__).resolve().parents[1]
R=ROOT/'reports/runpod_full'; O=ROOT/'reports/full_review';O.mkdir(exist_ok=True)
os.environ['MPLCONFIGDIR']=str(O/'mpl-cache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image,ImageDraw
read=lambda p:json.loads(p.read_text())
runs=[json.loads(x) for x in (R/'generation/runs.jsonl').read_text().splitlines()]
scores=[json.loads(x) for x in (R/'evaluation/scores/results.jsonl').read_text().splitlines()]
tokens=read(R/'generation/tokens.json')['records'][0]
targets={x['semantic']:x for x in tokens['targets']}
plan=read(R/'generation/plan.json')
assert len(runs)==len({x['id'] for x in runs})==plan['image_count']==151
expected={ (l,s) for l in range(32) for s in range(1,14) }
hashes={}
for row in runs:
 image=R/'generation/images'/Path(row['image']).name
 digest=hashlib.sha256(image.read_bytes()).hexdigest()
 assert digest==row['image_sha256'],row['id']
 hashes[row['id']]=digest
 positions=targets[row['semantic']]['token_positions'] if row['semantic'] else []
 assert positions==row['token_positions']
 for alias in row['aliases']:
  k=alias['boundary'];want=list(range(1,k+1)) if alias['direction']=='prefix' else list(range(k+1,14))
  assert want==row['masked_scales']
 audit=read(R/'generation/audit'/Path(row['audit']).name)
 assert len(audit)==416 and {(a['layer'],a['scale']) for a in audit}==expected
 for a in audit:
  assert a['masked']==(a['scale'] in row['masked_scales'])
  assert a['conditional_keys_before']-a['conditional_keys_after']==(len(positions) if a['masked'] else 0)
for s in scores:
 image_id=s['id'].split('--')[0]
 assert s['image_sha256']==hashes[image_id]
 assert s['status'] in ('correct','incorrect','missing')
assert len(scores)==len({x['id'] for x in scores})==260
curves=list(csv.DictReader((R/'evaluation/scores/scale_curves.csv').open()))
semantics=list(targets)
for sem in semantics:
 for direction in ['prefix','suffix']:
  rows=[x for x in curves if x['semantic']==sem and x['subtype']=='all' and x['direction']==direction]
  assert sorted(int(x['boundary']) for x in rows)==list(range(14))
  for x in rows:
   matching=[s for s in scores if s['semantic']==sem and any(a['direction']==direction and a['boundary']==int(x['boundary']) for a in next(r for r in runs if r['id']==s['id'].split('--')[0])['aliases'])]
   if not matching:
    assert (direction,int(x['boundary'])) in [('prefix',0),('suffix',13)]
    matching=[s for s in scores if s['semantic']==sem and s['metadata']['condition']=='baseline']
   assert abs(float(x['success_rate'])-sum(s['success'] for s in matching)/len(matching))<1e-8
report={'status':'passed','images_hash_verified':151,'layer_scale_records_verified':151*416,'score_rows_verified':260,'curve_rows':len(curves),'semantic_all_curve_points_recomputed':168,'semantic_targets':{k:v['target_fragments'] for k,v in targets.items()},'score_status_counts':dict(collections.Counter(x['status'] for x in scores)),'baseline_scores':{x['metadata']['check_id']:{'status':x['status'],'answer':x['observation'].get('answer')} for x in scores if x['metadata']['condition']=='baseline'}}
(O/'audit_summary.json').write_text(json.dumps(report,indent=2)+'\n')
fig,axes=plt.subplots(2,3,figsize=(13,7),sharex=True,sharey=True)
for ax,sem in zip(axes.flat,semantics):
 for d,c in [('prefix','#2563eb'),('suffix','#d97706')]:
  rs=sorted([x for x in curves if x['semantic']==sem and x['subtype']=='all' and x['direction']==d],key=lambda x:int(x['boundary']))
  ax.plot([int(x['boundary']) for x in rs],[float(x['success_rate']) for x in rs],'-o',ms=3,label=d,color=c)
 ax.set_title(sem.replace('_',' '));ax.set_ylim(-.05,1.05);ax.set_xticks([0,3,6,9,13]);ax.grid(alpha=.2);ax.set_xlabel('Boundary k');ax.set_ylabel('Success rate')
axes.flat[0].legend()
fig.suptitle('Infinity | one prompt, seed 42 | six semantic classes\nPrefix masks 1..k; suffix masks k+1..13. Count baseline is incorrect.',fontsize=12)
fig.tight_layout();fig.savefig(O/'semantic_curves.png',dpi=170);fig.savefig(O/'semantic_curves.pdf');plt.close(fig)
# Contact sheet: unchanged generated images, resized for inspection.
W,H=320,350
sheet=Image.new('RGB',(W*4,H*6),'white');draw=ImageDraw.Draw(sheet)
for ri,sem in enumerate(semantics):
 for ci,cond in enumerate(['baseline','prefix_06','suffix_06','full_mask']):
  ident='scene01__s42__baseline' if cond=='baseline' else f'scene01__s42__{sem}__{cond}'
  im=Image.open(R/'generation/images'/f'{ident}.png');im.thumbnail((320,320))
  sheet.paste(im,(ci*W,ri*H+30));draw.text((ci*W+5,ri*H+8),f'{sem} | {cond}',fill='black')
sheet.save(O/'image_contact_sheet.jpg',quality=92)
print(json.dumps(report,indent=2))
