"""Verify full-dataset score aggregation and plot success/retention curves."""
from pathlib import Path
import collections
import csv
import json
import os

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT/'reports/csfm50_full/evaluation/scores'
OUT = ROOT/'reports/csfm50_full_review'
OUT.mkdir(exist_ok=True)
os.environ['MPLCONFIGDIR'] = str(OUT/'mpl-cache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

scores = [json.loads(s) for s in (DATA/'results.jsonl').read_text().splitlines()]
summary = json.loads((DATA/'summary.json').read_text())
curves = list(csv.DictReader((DATA/'scale_curves.csv').open()))
assert summary['status'] == 'complete' and summary['n_valid'] == 7800
assert len(scores) == len({s['id'] for s in scores}) == 7800
assert not any(s['status'] in ('evaluation_error','missing_output') for s in scores)
assert sum('postprocessing' in s for s in scores) == 6
semantics = ['object','color','shape','texture','count','spatial_relation']
byid = {s['id']:s for s in scores}
baselines = {}
for sem in semantics:
    ss = [s for s in scores if s['semantic']==sem]
    assert len(ss)==1300
    base = [s for s in ss if s['metadata']['condition']=='baseline']
    assert len(base)==50
    baselines[sem] = sum(s['success'] for s in base)
    for s in ss:
        assert s['baseline_success']==byid[s['baseline_id']]['success']
        assert s['paired_delta']==s['success']-s['baseline_success']
    for direction in ['prefix','suffix']:
        rs = [r for r in curves if r['semantic']==sem and r['subtype']=='all' and r['direction']==direction]
        assert sorted(int(r['boundary']) for r in rs)==list(range(14))
groups = collections.defaultdict(list)
for s in scores:
    m=s['metadata']
    aliases = [{'direction':'prefix','boundary':0},{'direction':'suffix','boundary':13}] if m['condition']=='baseline' else m['aliases']
    for a in aliases:
        for sub in {'all',s['subtype']}:
            groups[s['semantic'],sub,a['direction'],a['boundary']].append(s)
assert len(groups)==len(curves)
for r in curves:
    ss=groups[r['semantic'],r['subtype'],r['direction'],int(r['boundary'])]
    assert len(ss)==int(r['checks_total'])==int(r['checks_valid'])
    assert len({(s['metadata']['prompt_id'],s['metadata']['seed']) for s in ss})==len(ss)
    assert abs(float(r['success_rate'])-sum(s['success'] for s in ss)/len(ss))<1e-9
    assert abs(float(r['paired_delta'])-sum(s['paired_delta'] for s in ss)/len(ss))<1e-9
    positive=[s for s in ss if s['baseline_success']==1]
    assert len(positive)==int(r['baseline_correct_checks'])
    if positive:
        assert abs(float(r['retention'])-sum(s['success'] for s in positive)/len(positive))<1e-9
    else:
        assert r['retention']==''
    if r['semantic']=='count':
        errors=[s['absolute_error'] for s in ss if s['absolute_error'] is not None]
        if errors:assert abs(float(r['count_target_mae'])-sum(errors)/len(errors))<1e-9

for metric,label in [('success_rate','Success rate'),('retention','Retention')]:
    fig,axes=plt.subplots(2,3,figsize=(12,7),sharex=True,sharey=True)
    for ax,sem in zip(axes.flat,semantics):
        for d,c,marker in [('prefix','#2563eb','o'),('suffix','#d97706','s')]:
            rs=sorted([r for r in curves if r['semantic']==sem and r['subtype']=='all' and r['direction']==d],key=lambda r:int(r['boundary']))
            ax.plot([int(r['boundary']) for r in rs],[float(r[metric]) if r[metric] else float('nan') for r in rs],color=c,marker=marker,markersize=3.5,label=d)
        if metric=='success_rate':ax.axhline(baselines[sem]/50,color='#64748b',ls=':',lw=1)
        ax.set_title(f'{sem.replace("_"," ").title()} | baseline {baselines[sem]}/50',fontsize=11)
        ax.set_ylim(-.05,1.05);ax.set_xticks([0,3,6,9,13]);ax.grid(alpha=.2)
        ax.set_xlabel('Boundary k');ax.set_ylabel(label);ax.tick_params(labelbottom=True)
    handles,labels=axes.flat[0].get_legend_handles_labels()
    fig.legend(handles,['Prefix: mask 1..k','Suffix: mask k+1..13'],loc='upper center',bbox_to_anchor=(.5,.94),ncol=2,frameon=False)
    fig.suptitle(f'Infinity 2B | 300 prompts, seed 42 | {label}',fontsize=15,y=.99)
    note='Each class: 50 prompts. Dotted line: unmasked baseline success.' if metric=='success_rate' else 'Retention includes only baseline-correct prompts; denominator shown in each panel.'
    fig.text(.5,.02,note+'\nSix reviewed out-of-vocabulary answers normalized to existing "other"; original responses retained.',ha='center',fontsize=9)
    fig.tight_layout(rect=(0,.075,1,.88))
    fig.savefig(OUT/(metric+'.png'),dpi=180);fig.savefig(OUT/(metric+'.pdf'));plt.close(fig)
report=dict(status='passed',score_rows_verified=7800,curve_rows_recomputed=len(curves),baseline_correct=baselines,
            status_counts=dict(collections.Counter(s['status'] for s in scores)),category_normalizations=6)
(OUT/'audit_summary.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
