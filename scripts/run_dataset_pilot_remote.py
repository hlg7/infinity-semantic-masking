"""Background annotation/validation followed by a small dataset pilot only."""
from datetime import datetime,timezone
from pathlib import Path
import json,os,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
STATUS=ROOT/'reports/runpod_dataset_status.json'
OUT=ROOT/'outputs/csfm50_pilot'
DATA=ROOT/'data/csfm50_v1'


def status(phase,**extra):
    d=dict(phase=phase,pid=os.getpid(),updated_utc=datetime.now(timezone.utc).isoformat(),**extra)
    tmp=STATUS.with_suffix('.tmp');tmp.write_text(json.dumps(d,indent=2)+'\n');tmp.replace(STATUS)
    print(json.dumps(d),flush=True)


def main():
    os.chdir(ROOT);os.environ.update(PYTHONUNBUFFERED='1',HF_HOME=str(ROOT/'assets/hf-cache'),HF_HUB_DISABLE_XET='1')
    if OUT.exists():
        status('failed',reason='Pilot output already exists; refusing to overwrite');return 1
    py=str(ROOT/'.venv-gpu/bin/python')
    phases=[
        ('annotating_300_prompts',[py,'scripts/annotate_dataset_gpu.py']),
        ('validating_300_token_maps',[py,'tokenize_prompts.py','--annotations',str(DATA/'annotations_qwen3vl/annotations.json'),'--output',str(ROOT/'reports/csfm50_tokens.json')]),
        ('preparing_pilot',[py,'scripts/prepare_dataset.py']),
        ('generating_pilot',[py,'generate.py','--annotations',str(DATA/'pilot_annotations.json'),'--mode','smoke','--seeds','42','--output',str(OUT/'generation')]),
        ('evaluating_pilot',[py,'evaluate.py','--run',str(OUT/'generation'),'--checks',str(DATA/'pilot_checks.json'),'--output',str(OUT/'evaluation')]),
        ('summarizing_pilot',[py,'summarize.py','--scores',str(OUT/'evaluation/scores'),'--generation',str(OUT/'generation')]),
    ]
    for phase,command in phases:
        status(phase,command=command)
        code=subprocess.run(command,cwd=ROOT).returncode
        if code:
            status('failed',failed_phase=phase,exit_code=code,log='reports/runpod_dataset.log');return code
    status('completed',output=str(OUT),full_dataset_generation_started=False);return 0

if __name__=='__main__':sys.exit(main())
