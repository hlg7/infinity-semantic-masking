"""Run the one-prompt, seed-42 full experiment with persistent stage status."""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'outputs/runpod_full'
STATUS = ROOT / 'reports/runpod_full_status.json'


def status(phase, **extra):
    payload = dict(phase=phase, pid=os.getpid(),
                   updated_utc=datetime.now(timezone.utc).isoformat(), **extra)
    temporary = STATUS.with_suffix('.tmp')
    temporary.write_text(json.dumps(payload, indent=2) + '\n')
    temporary.replace(STATUS)
    print(json.dumps(payload), flush=True)


def main():
    os.chdir(ROOT)
    os.environ.update(PYTHONUNBUFFERED='1', HF_HOME=str(ROOT/'assets/hf-cache'),
                      HF_HUB_DISABLE_XET='1')
    if OUTPUT.exists():
        status('failed', reason='Output directory already exists; refusing to overwrite.')
        return 1
    python = str(ROOT / '.venv-gpu/bin/python')
    phases = [
        ('generating', [python, 'generate.py', '--mode', 'full', '--seeds', '42',
                        '--output', str(OUTPUT/'generation')]),
        ('evaluating', [python, 'evaluate.py', '--run', str(OUTPUT/'generation'),
                        '--output', str(OUTPUT/'evaluation')]),
        ('summarizing', [python, 'summarize.py', '--scores', str(OUTPUT/'evaluation/scores'),
                         '--generation', str(OUTPUT/'generation')]),
    ]
    for phase, command in phases:
        status(phase, command=command, output=str(OUTPUT))
        result = subprocess.run(command, cwd=ROOT)
        if result.returncode:
            status('failed', failed_phase=phase, exit_code=result.returncode,
                   log='reports/runpod_full.log')
            return result.returncode
    status('completed', output=str(OUTPUT))
    return 0


if __name__ == '__main__':
    sys.exit(main())
