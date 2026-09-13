"""Background GPU setup, weight download, then the smallest complete experiment."""
from datetime import datetime, timezone
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / 'reports/runpod_status.json'


def status(phase, **extra):
    payload = {'phase': phase, 'pid': os.getpid(),
               'updated_utc': datetime.now(timezone.utc).isoformat(), **extra}
    temporary = STATUS.with_suffix('.tmp')
    temporary.write_text(json.dumps(payload, indent=2) + '\n')
    temporary.replace(STATUS)
    print(json.dumps(payload), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--skip-setup', action='store_true', help='Resume after a verified environment setup.')
    args = parser.parse_args()
    os.chdir(ROOT)
    os.environ['PYTHONUNBUFFERED'] = '1'
    os.environ['HF_HOME'] = str(ROOT/'assets/hf-cache')
    os.environ['PIP_CACHE_DIR'] = str(ROOT/'assets/pip-cache')
    os.environ['HF_HUB_DISABLE_XET'] = '1'
    phases = [
        ('installing_environment', ['bash', 'scripts/setup_gpu.sh']),
        ('downloading_weights', ['.venv-gpu/bin/python', 'scripts/download_weights.py']),
        ('validating_tokenizer', ['.venv-gpu/bin/python', 'tokenize_prompts.py',
                                  '--annotations', 'data/smoke_annotations.json',
                                  '--output', 'reports/gpu_tokens.json']),
        ('running_smoke_experiment', ['bash', 'scripts/run_smoke.sh', 'outputs/runpod_smoke']),
    ]
    for phase, command in phases:
        if phase == 'installing_environment' and args.skip_setup:
            continue
        status(phase, command=command)
        result = subprocess.run(command, cwd=ROOT)
        if result.returncode:
            status('failed', failed_phase=phase, exit_code=result.returncode,
                   log='reports/runpod_bootstrap.log')
            return result.returncode
        if phase == 'installing_environment':
            # Remove only disposable setup files after the CUDA/import check passes.
            cache = ROOT / 'assets/pip-cache'
            if cache.exists():
                shutil.rmtree(cache)
            bundle = ROOT.parent / 'infinity_semantic_bundle.tar.gz'
            bundle.unlink(missing_ok=True)
            (ROOT / '.DS_Store').unlink(missing_ok=True)
            print('Setup verified; removed pip cache, upload archive and .DS_Store.', flush=True)
    status('completed', output='outputs/runpod_smoke')
    return 0


if __name__ == '__main__':
    sys.exit(main())
