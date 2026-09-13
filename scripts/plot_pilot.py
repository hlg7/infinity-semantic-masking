"""Present pilot images and the three measured boundary points."""
import csv
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'reports/pilot_review'
os.environ['MPLCONFIGDIR'] = str(OUT/'mpl-cache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

rows = list(csv.DictReader((ROOT/'reports/csfm50_pilot/evaluation/scores/scale_curves.csv').open()))
semantics = ['object', 'color', 'shape', 'texture', 'count', 'spatial_relation']
fig, axes = plt.subplots(2, 3, figsize=(12, 7), sharex=True, sharey=True)
for ax, sem in zip(axes.flat, semantics):
    for direction, color, marker in [('prefix', '#2563eb', 'o'), ('suffix', '#dc6b14', 's')]:
        rs = sorted([r for r in rows if r['semantic']==sem and r['subtype']=='all' and r['direction']==direction], key=lambda r:int(r['boundary']))
        assert [int(r['boundary']) for r in rs] == [0, 6, 13]
        n = int(rs[0]['prompt_seed_total'])
        ax.plot([int(r['boundary']) for r in rs], [float(r['success_rate']) for r in rs],
                color=color, marker=marker, linestyle='--', linewidth=1.7, markersize=8,
                markerfacecolor='none' if direction=='suffix' else color,
                label='Prefix: mask 1..k' if direction=='prefix' else 'Suffix: mask k+1..13')
    ax.set_title(f'{sem.replace("_", " ").title()} (n={n})', fontsize=12)
    ax.set_xticks([0, 6, 13]); ax.set_yticks([0, .25, .5, .75, 1])
    ax.set_ylim(-.07, 1.07); ax.set_xlim(-.4, 13.4); ax.grid(alpha=.18)
    ax.set_xlabel('Boundary k'); ax.set_ylabel('Success rate')
handles, labels = axes.flat[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(.5, .94), ncol=2, frameon=False)
fig.suptitle('Infinity pilot | 10 prompts, seed 42 | frozen evaluator scores', fontsize=15, y=.99)
fig.text(.5, .015, 'Measured boundaries: 0, 6, 13 only. Dashed lines connect observations; intermediate scales were not measured.\nTexture averages 2 prompts; spatial relation averages 4. Other classes use 1 prompt each.', ha='center', fontsize=10)
fig.tight_layout(rect=(0, .07, 1, .88))
fig.savefig(OUT/'pilot_curves.png', dpi=180)
fig.savefig(OUT/'pilot_curves.pdf')
plt.close(fig)

R = ROOT/'reports/csfm50_pilot/generation'
runs = [json.loads(s) for s in (R/'runs.jsonl').read_text().splitlines()]
from matplotlib.font_manager import findfont
font = ImageFont.truetype(findfont('DejaVu Sans'), 20)
samples = [('object_001', 'Object: dog'), ('texture_001', 'Texture: striped shirt'),
           ('color_001', 'Color: red dog'), ('spatial_relation_021', 'Spatial: frame ABOVE clock')]
conditions = [('baseline','Baseline'), ('prefix_06','Prefix: mask scales 1-6'),
              ('full_mask','Full: mask scales 1-13'), ('suffix_06','Suffix: mask scales 7-13')]
sheet = Image.new('RGB', (1440, 4*405+40), 'white'); draw = ImageDraw.Draw(sheet)
for ci, (_, title) in enumerate(conditions):
    draw.text((ci*360+10, 10), title, font=font, fill='black')
for ri, (pid, title) in enumerate(samples):
    y = 40+ri*405
    draw.text((10, y+7), title, font=font, fill='black')
    for ci, (cond, _) in enumerate(conditions):
        r = next(r for r in runs if r['prompt_id']==pid and r['condition']==cond)
        im = Image.open(R/'images'/Path(r['image']).name).convert('RGB')
        im.thumbnail((356, 356))
        sheet.paste(im, (ci*360+2, y+39))
sheet.save(OUT/'selected_examples.jpg', quality=95)
print(OUT/'pilot_curves.png')
print(OUT/'selected_examples.jpg')
