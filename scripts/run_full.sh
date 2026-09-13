#!/usr/bin/env bash
# All six semantics and all prefix/suffix boundaries; default seed 42.
set -euo pipefail
cd "$(dirname "$0")/.."
EXPERIMENT_PYTHON="${EXPERIMENT_PYTHON:-.venv-gpu/bin/python}"
EXPERIMENT_OUTPUT="${1:-outputs/full}"
"$EXPERIMENT_PYTHON" generate.py --mode full --output "$EXPERIMENT_OUTPUT/generation"
"$EXPERIMENT_PYTHON" evaluate.py --run "$EXPERIMENT_OUTPUT/generation" --output "$EXPERIMENT_OUTPUT/evaluation"
"$EXPERIMENT_PYTHON" summarize.py --scores "$EXPERIMENT_OUTPUT/evaluation/scores" --generation "$EXPERIMENT_OUTPUT/generation"
