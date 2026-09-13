#!/usr/bin/env bash
# Run manually on Linux CUDA only, after local preparation is accepted.
set -euo pipefail
cd "$(dirname "$0")/.."
# FlashAttention moves its downloaded wheel into pip's cache with os.rename.
# Keep build files and the cache on the same filesystem on Runpod.
export PIP_CACHE_DIR="${PIP_CACHE_DIR:-$PWD/assets/pip-cache}"
export TMPDIR="$PIP_CACHE_DIR/build-tmp"
mkdir -p "$TMPDIR"
python3 -m venv .venv-gpu
.venv-gpu/bin/python -m pip install --upgrade pip setuptools wheel
.venv-gpu/bin/python -m pip install -r requirements-gpu.txt
MAX_JOBS=4 .venv-gpu/bin/python -m pip install 'flash-attn==2.7.4.post1' --no-build-isolation
.venv-gpu/bin/python -c 'import torch, flash_attn; assert torch.cuda.is_available(); print(torch.cuda.get_device_name())'
