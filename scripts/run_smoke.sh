#!/usr/bin/env bash
# Explicit GPU command for later. Does not create/start any Runpod resources.
set -euo pipefail
cd "$(dirname "$0")/.."
EXPERIMENT_PYTHON="${EXPERIMENT_PYTHON:-.venv-gpu/bin/python}"
EXPERIMENT_OUTPUT="${1:-outputs/smoke}"
"$EXPERIMENT_PYTHON" generate.py --mode smoke --semantics color --output "$EXPERIMENT_OUTPUT/generation"
"$EXPERIMENT_PYTHON" evaluate.py --run "$EXPERIMENT_OUTPUT/generation" --output "$EXPERIMENT_OUTPUT/evaluation"
"$EXPERIMENT_PYTHON" summarize.py --scores "$EXPERIMENT_OUTPUT/evaluation/scores" --generation "$EXPERIMENT_OUTPUT/generation"
