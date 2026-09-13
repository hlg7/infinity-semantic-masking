"""Run the frozen 300-prompt, seed-42 full-scale experiment in the background."""
from datetime import datetime, timezone
from pathlib import Path
import collections
import fcntl
import hashlib
import json
import os
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
STATUS = ROOT/'reports/runpod_dataset_full_status.json'
OUT = ROOT/'outputs/csfm50_full'
DATA = ROOT/'data/csfm50_v1'


def status(phase, **extra):
    payload = dict(phase=phase, pid=os.getpid(), updated_utc=datetime.now(timezone.utc).isoformat(),
                   output=str(OUT), planned_images=7800, seed=42, **extra)
    temporary = STATUS.with_suffix('.tmp')
    temporary.write_text(json.dumps(payload, indent=2)+'\n')
    temporary.replace(STATUS)
    print(json.dumps(payload), flush=True)


def main():
    os.chdir(ROOT)
    os.environ.update(PYTHONUNBUFFERED='1', HF_HOME=str(ROOT/'assets/hf-cache'), HF_HUB_DISABLE_XET='1')
    lock = (ROOT/'reports/runpod_dataset_full.lock').open('w')
    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        print('Full dataset supervisor already running', flush=True)
        return 1
    if OUT.exists():
        print('Full dataset output already exists; refusing to overwrite', flush=True)
        return 1
    status('validating_frozen_inputs')
    from semantic_masking import compile_records, SEMANTICS
    from generate import make_plan
    from evaluate import build_manifest
    annotations = json.loads((DATA/'annotations.json').read_text())
    checks = json.loads((DATA/'checks.json').read_text())
    records = compile_records(annotations)
    assert len(records) == 300
    assert collections.Counter(r['target_semantic'] for r in records) == {s:50 for s in SEMANTICS}
    plan = make_plan(records, [42], SEMANTICS, 13, 'full')
    assert len(plan) == 7800
    assert set(collections.Counter(r['prompt_id'] for r in plan).values()) == {26}
    placeholder = [dict(r, image='/unused.png', image_sha256='f'*64) for r in plan]
    assert len(build_manifest(placeholder, checks)) == 7800
    inputs = OUT/'inputs'
    inputs.mkdir(parents=True)
    hashes = {}
    for name in ('annotations.json', 'checks.json'):
        shutil.copy2(DATA/name, inputs/name)
        hashes[name] = hashlib.sha256((inputs/name).read_bytes()).hexdigest()
    (inputs/'manifest.json').write_text(json.dumps(dict(sha256=hashes, prompt_count=300, planned_images=7800, seed=42), indent=2)+'\n')
    python = str(ROOT/'.venv-gpu/bin/python')
    phases = [
        ('generating', [python, 'generate.py', '--annotations', str(inputs/'annotations.json'), '--mode', 'full', '--seeds', '42', '--output', str(OUT/'generation')]),
        ('evaluating', [python, 'evaluate.py', '--run', str(OUT/'generation'), '--checks', str(inputs/'checks.json'), '--output', str(OUT/'evaluation')]),
        ('summarizing', [python, 'summarize.py', '--scores', str(OUT/'evaluation/scores'), '--generation', str(OUT/'generation')]),
    ]
    for phase, command in phases:
        status(phase, command=command)
        result = subprocess.run(command, cwd=ROOT)
        if result.returncode:
            status('failed', failed_phase=phase, exit_code=result.returncode, log='reports/runpod_dataset_full.log')
            return result.returncode
    status('completed')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as exc:
        status('failed', reason=str(exc), log='reports/runpod_dataset_full.log')
        raise
