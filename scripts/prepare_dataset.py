"""Validate dataset annotations, preserve frozen checks, and select pilot prompts."""
from pathlib import Path
import sys,collections
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from common import ROOT,read_json,write_json,evaluator_imports
from semantic_masking import compile_records,SEMANTICS
from generate import make_plan
from evaluate import build_manifest


def main():
    data=ROOT/'data/csfm50_v1'
    annotations=read_json(data/'annotations_qwen3vl/annotations.json')
    sources=read_json(data/'prompts.json')
    assert len(annotations)==len(sources)==300
    assert {x['id']:x['prompt'] for x in annotations}=={x['id']:x['prompt'] for x in sources}
    records=compile_records(annotations)
    assert collections.Counter(x['target_semantic'] for x in records)=={s:50 for s in SEMANTICS}
    checks=read_json(data/'checks.json')
    full=make_plan(records,[42],SEMANTICS,13,'full')
    assert len(full)==7800
    # Validate imported questions and baseline pairing without loading images/models.
    placeholder=[dict(x,image='/unused.png',image_sha256='f'*64) for x in full]
    evaluation=build_manifest(placeholder,checks)
    assert len(evaluation)==7800
    selected={}
    for check in checks:
        key=(check['semantic'],check['check']['subtype'])
        selected.setdefault(key,check['prompt_id'])
    pilot_ids=set(selected.values())
    pilot=[x for x in annotations if x['id'] in pilot_ids]
    write_json(data/'annotations.json',annotations)
    write_json(data/'pilot_annotations.json',pilot)
    write_json(data/'pilot_checks.json',[x for x in checks if x['prompt_id'] in pilot_ids])
    write_json(data/'pilot_selection.json',{'selection':'First prompt of each semantic/subtype in source order; no generated-image filtering','ids':[x['id'] for x in pilot],'prompt_count':len(pilot),'planned_images':len(make_plan(compile_records(pilot),[42],SEMANTICS,13,'smoke'))})
    write_json(ROOT/'reports/csfm50_preparation.json',{'status':'prepared','prompt_count':300,'semantic_counts':{s:50 for s in SEMANTICS},'full_image_count':7800,'seed':42,'pilot_prompt_count':len(pilot),'scoring':'Frozen imported checks','full_dataset_generation_started':False})
    print(f'Prepared 300 prompts; pilot {len(pilot)} prompts / {len(pilot)*4} images; full plan 7800 images',flush=True)

if __name__=='__main__':main()
