"""Apply 14 reviewed corrections, with exact prompt hashes and explicit provenance."""
from pathlib import Path
import json,sys,re,hashlib
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from common import ROOT,read_json,write_json
from annotate_semantics import split_words
from annotation_policy import validate_labels,POLICY
from semantic_masking import compile_records,render_review
DATA=ROOT/'data/csfm50_v1';OUT=DATA/'annotations_qwen3vl'
OFFICE=['office desk','computer monitor','wall']
SPECS={
 'object_015':{'object':['reading lamp','library','bookshelves','walls','window'],'spatial_relation':[('in a quiet library','in'),'along','through']},
 'shape_015':{'object':['picture frame']+OFFICE,'shape':['square'],'texture':['plain'],'spatial_relation':['on']},
 'shape_035':{'object':['picture frame']+OFFICE,'shape':['oval'],'texture':['plain'],'spatial_relation':['on']},
 'shape_039':{'object':['sign','courtyard','wall','path'],'shape':['oval'],'spatial_relation':[('in a quiet courtyard','in')]},
 'count_014':{'object':['hourglasses']+OFFICE,'count':['Three'],'texture':['plain'],'spatial_relation':['on']},
}
for identity,entities,relation in [
 ('spatial_relation_003',['toy car','box'],'to the left of'),
 ('spatial_relation_008',['box','toy car'],'to the left of'),
 ('spatial_relation_009',['pencil case','notebook'],'to the left of'),
 ('spatial_relation_013',['toy car','box'],'to the right of'),
 ('spatial_relation_018',['box','toy car'],'to the right of'),
 ('spatial_relation_019',['pencil case','notebook'],'to the right of'),
 ('spatial_relation_034',['notebook','pencil case'],'in front of'),
 ('spatial_relation_039',['notebook','pencil case'],'behind'),
 ('spatial_relation_048',['toy car','box'],'outside'),
]:
 SPECS[identity]={'object':entities+OFFICE,'texture':['plain'],'spatial_relation':[relation,'on']}
 if identity!='spatial_relation_048':SPECS[identity]['count']=['both']


def main():
 sources={x['id']:x for x in read_json(DATA/'source_prompts.json')}
 failures=read_json(OUT/'failures.json')
 assert {x['id'] for x in failures}==set(SPECS), 'Unexpected failed IDs; review them before applying corrections'
 write_json(OUT/'failures_before_manual_repair.json',failures)
 audit=[];annotations=[]
 for identity,groups in SPECS.items():
  source=sources[identity];prompt=source['prompt'];words=split_words(prompt);labels=['other']*len(words)
  for semantic,phrases in groups.items():
   for item in phrases:
    anchor,phrase=item if isinstance(item,tuple) else (item,item)
    matches=list(re.finditer(r'\b'+re.escape(anchor)+r'\b',prompt))
    assert len(matches)==1,(identity,anchor)
    start=matches[0].start();end=start+len(phrase);assert prompt[start:end]==phrase
    for word in words:
     if word['start']<end and word['end']>start:
      assert labels[word['i']]=='other',(identity,phrase)
      labels[word['i']]=semantic
  record={'id':identity,'prompt':prompt,'target_semantic':source['semantic']}
  labels,annotation,corrections=validate_labels(record,labels,source)
  assert not corrections,'Manual annotations should already follow the policy'
  annotation['notes']='Assistant-reviewed correction of failed model annotation; original response retained. Full compound nouns included; plain is texture, not object; brightness, abstract background and viewpoint descriptions are other.'
  target=OUT/'labels'/f'{identity}.json';assert not target.exists(),f'Refusing to replace a previously accepted label: {identity}'
  write_json(target,{'id':identity,'labels':labels,'origin':'manual_review_v1','policy_version':POLICY['version'],'corrections':[],'index_repairs':[],'review_note':annotation['notes']})
  annotations.append(annotation)
  audit.append({'id':identity,'prompt_sha256':hashlib.sha256(prompt.encode()).hexdigest(),'groups':groups,'annotation':annotation,'labels':labels,'review_note':annotation['notes']})
 write_json(DATA/'manual_corrections_v1.json',{'reviewer':'assistant','policy_version':POLICY['version'],'records':audit})
 (DATA/'manual_corrections_v1.md').write_text(render_review(compile_records(annotations)))
 print('Applied 14 reviewed corrections; original successful labels and model responses preserved')

if __name__=='__main__':main()
