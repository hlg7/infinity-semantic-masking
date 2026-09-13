"""Batch semantic annotation with shared rules and reuse of validated earlier work."""
from pathlib import Path
import argparse,hashlib,json,os,sys,time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from common import ROOT,read_json,write_json
from annotate_semantics import split_words
from annotation_policy import POLICY,system_prompt,request_messages,decode_groups,decode_legacy,validate_labels
from semantic_masking import compile_records,render_review
DATA=ROOT/'data/csfm50_v1'
OUT=DATA/'annotations_qwen3vl'
PREVIOUS=DATA/'annotations_qwen3vl_serial_v3'
PROBE_IDS=['object_026','object_038','object_041','color_001','shape_001','texture_001','count_001','spatial_relation_001']


def main():
    p=argparse.ArgumentParser();p.add_argument('--batch-size',type=int,default=8);p.add_argument('--probe',action='store_true');args=p.parse_args()
    if not 1<=args.batch_size<=8:p.error('batch size must be 1..8')
    records=read_json(DATA/'prompts.json');sources={r['id']:r for r in read_json(DATA/'source_prompts.json')}
    config=read_json(ROOT/'vendor/semantic-evaluators/semantic_evaluators/defaults.json')['qwen_vlm']
    fingerprint=hashlib.sha256(json.dumps({'records':records,'system':system_prompt(),'model':config['checkpoint'],'revision':config['revision']},sort_keys=True).encode()).hexdigest()
    OUT.mkdir(parents=True,exist_ok=True);manifest=OUT/'manifest.json'
    if manifest.exists() and read_json(manifest)['fingerprint']!=fingerprint:raise ValueError('Different labeling rules or prompts; archive the previous output first')
    meta={'fingerprint':fingerprint,'model':config['checkpoint'],'revision':config['revision'],'policy':POLICY,'batch_size':args.batch_size,'format':'six groups of [index,word] pairs; unlisted words are other','status':'running','prompt_count':len(records)}
    write_json(manifest,meta)
    selected=[r for r in records if r['id'] in PROBE_IDS] if args.probe else records
    annotations={};failures={};pending=[];reused=0;recovered=0
    started=time.monotonic()

    def progress(last_id=None):
        write_json(OUT/'progress.json',{'processed':len(annotations)+len(failures),'total':len(selected),'successful':len(annotations),'failed':len(failures),'last_id':last_id,'reused':reused,'recovered_legacy':recovered,'elapsed_seconds':round(time.monotonic()-started,1),'probe':args.probe})
        write_json(OUT/'failures.json',[{'id':k,'error':v} for k,v in failures.items()])

    def accept(record,labels,origin,repairs=None):
        labels,annotation,corrections=validate_labels(record,labels,sources[record['id']])
        annotations[record['id']]=annotation
        if repairs:annotation['notes']=annotation.get('notes','')+' Unique exact-word index repairs: '+json.dumps(repairs)
        write_json(OUT/'labels'/f"{record['id']}.json",{'id':record['id'],'labels':labels,'origin':origin,'corrections':corrections,'index_repairs':repairs or [],'policy_version':POLICY['version']})

    for record in selected:
        identity=record['id'];saved=OUT/'labels'/f'{identity}.json'
        try:
            if saved.exists():
                entry=read_json(saved);assert entry['id']==identity
                accept(record,entry['labels'],entry.get('origin','current_cache'),entry.get('index_repairs'));reused+=1;continue
            for response in sorted((OUT/'responses').glob(f'{identity}.attempt*.json'),reverse=True):
                try:
                    repairs=[]
                    labels=decode_groups(read_json(response)['text'],split_words(record['prompt']),repairs)
                    accept(record,labels,str(response),repairs);recovered+=1;break
                except (ValueError,KeyError,TypeError):continue
            if identity in annotations:continue
            if not args.probe:
                old=PREVIOUS/'labels'/f'{identity}.json'
                if old.exists():
                    accept(record,read_json(old)['labels'],str(old));reused+=1;continue
                responses=sorted((PREVIOUS/'responses').glob(f'{identity}.attempt*.json'),reverse=True)
                for response in responses:
                    try:
                        labels=decode_legacy(read_json(response)['text'],split_words(record['prompt']))
                        accept(record,labels,str(response));recovered+=1;break
                    except (ValueError,KeyError,TypeError):continue
                if identity in annotations:continue
        except (ValueError,KeyError,TypeError):pass
        pending.append(record)
    progress()
    print(f'Reused {reused}; recovered {recovered} legacy responses; pending {len(pending)}; batch size {args.batch_size}',flush=True)
    if pending:
        import torch
        from transformers import AutoProcessor,Qwen3VLForConditionalGeneration
        processor=AutoProcessor.from_pretrained(config['checkpoint'],revision=config['processor_revision'],local_files_only=True)
        processor.tokenizer.padding_side='left'
        if processor.tokenizer.pad_token_id is None:processor.tokenizer.pad_token=processor.tokenizer.eos_token
        model=Qwen3VLForConditionalGeneration.from_pretrained(config['checkpoint'],revision=config['revision'],local_files_only=True,torch_dtype=torch.bfloat16,attn_implementation='sdpa').to('cuda').eval()
        torch.manual_seed(42)
        for offset in range(0,len(pending),args.batch_size):
            active=[(r,None) for r in pending[offset:offset+args.batch_size]]
            for attempt in range(1,3):
                if not active:break
                messages=[request_messages(record,error) for record,error in active]
                for (record,_),msg in zip(active,messages):write_json(OUT/'requests'/f"{record['id']}.attempt{attempt}.json",msg)
                texts=[processor.apply_chat_template(msg,tokenize=False,add_generation_prompt=True) for msg in messages]
                inputs=processor.tokenizer(texts,padding=True,return_tensors='pt').to('cuda')
                start=time.monotonic()
                with torch.inference_mode():result=model.generate(**inputs,do_sample=False,max_new_tokens=768,pad_token_id=processor.tokenizer.pad_token_id)
                answers=processor.tokenizer.batch_decode(result[:,inputs['input_ids'].shape[1]:],skip_special_tokens=True)
                print(f'Batch {offset//args.batch_size+1}, attempt {attempt}: {len(active)} prompts in {time.monotonic()-start:.1f}s',flush=True)
                retry=[]
                for (record,_),raw in zip(active,answers):
                    identity=record['id'];write_json(OUT/'responses'/f'{identity}.attempt{attempt}.json',{'text':raw})
                    try:
                        repairs=[]
                        labels=decode_groups(raw,split_words(record['prompt']),repairs)
                        accept(record,labels,f'batch_model_attempt{attempt}',repairs)
                        print(f'[{len(annotations)+len(failures)}/{len(selected)}] annotated {identity}',flush=True)
                    except (ValueError,KeyError,TypeError) as exc:
                        if attempt==1:retry.append((record,str(exc)))
                        else:
                            failures[identity]=str(exc);print(f'FAILED {identity}: {exc}',flush=True)
                    progress(identity)
                active=retry
    ordered=[annotations[r['id']] for r in selected if r['id'] in annotations]
    write_json(OUT/'annotations.json',ordered)
    if ordered:(OUT/'review.md').write_text(render_review(compile_records(ordered)))
    meta.update(status='failed' if failures else ('partial' if args.probe else 'completed'),successful=len(ordered),failed=len(failures),reused=reused,recovered_legacy=recovered,elapsed_seconds=round(time.monotonic()-started,1))
    write_json(manifest,meta);progress()
    return 1 if failures else 0

if __name__=='__main__':sys.exit(main())
