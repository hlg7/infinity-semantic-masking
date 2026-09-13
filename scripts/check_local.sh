#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
export PYTHONPYCACHEPREFIX="$PWD/.venv/pycache"
EXPERIMENT_PYTHON="${EXPERIMENT_PYTHON:-.venv/bin/python}"
"$EXPERIMENT_PYTHON" -m unittest discover -s tests -v
PYTHONPATH=vendor/semantic-evaluators "$EXPERIMENT_PYTHON" -m unittest discover -s vendor/semantic-evaluators/tests -q
"$EXPERIMENT_PYTHON" tokenize_prompts.py --annotations data/smoke_annotations.json --output reports/smoke_tokens.json
"$EXPERIMENT_PYTHON" generate.py --mode smoke --semantics color --plan-only --output reports/plan_smoke
"$EXPERIMENT_PYTHON" generate.py --mode full --plan-only --output reports/plan_full
"$EXPERIMENT_PYTHON" -m compileall -q annotate_semantics.py common.py evaluate.py generate.py infinity_mask.py semantic_masking.py summarize.py tokenize_prompts.py scripts/download_weights.py
bash -n scripts/setup_gpu.sh scripts/run_smoke.sh scripts/run_full.sh
