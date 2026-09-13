"""Local experiment paths, scale plans and JSON helpers; no model imports."""
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
INFINITY_REVISION = "9f9fcd1de7ead377ddf1106db1249a35f3a59143"


def read_json(path):
    return json.loads(Path(path).read_text())


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def sha256(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def evaluator_imports():
    sys.path.insert(0, str(ROOT / 'vendor/semantic-evaluators'))


def schedules(count):
    """k is a boundary: prefix 1..k, suffix k+1..N; deduplicate endpoints."""
    if type(count) is not int or count < 1:
        raise ValueError('Scale count must be positive')
    groups = {}
    for direction in ('prefix', 'suffix'):
        for boundary in range(count + 1):
            selected = tuple(range(1, boundary + 1) if direction == 'prefix'
                             else range(boundary + 1, count + 1))
            groups.setdefault(selected, []).append({'direction': direction, 'boundary': boundary})
    return [{'name': ('baseline' if not selected else 'full_mask' if len(selected) == count
                      else f"{aliases[0]['direction']}_{aliases[0]['boundary']:02d}"),
             'masked_scales': list(selected), 'aliases': aliases}
            for selected, aliases in groups.items()]


def selected_plans(count, mode):
    plans = schedules(count)
    if mode == 'smoke':
        boundary = max(1, count // 2)
        names = {'baseline', 'full_mask', f'prefix_{boundary:02d}', f'suffix_{boundary:02d}'}
        return [p for p in plans if p['name'] in names]
    return plans


def square_schedule(pn):
    # Pinned official dynamic_resolution.py, ratio=1.0; video time axis is 1.
    sizes = [1, 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64]
    lengths = {'0.06M': 7, '0.25M': 10, '1M': 13}
    if pn not in lengths:
        raise ValueError('Supported pn: 0.06M, 0.25M, 1M')
    return [(1, n, n) for n in sizes[:lengths[pn]]]
