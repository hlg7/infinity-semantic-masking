"""Export per-scale semantic curves using frozen evaluator scores."""
import argparse
from collections import defaultdict
import csv
import json
from pathlib import Path
from common import evaluator_imports, read_json


def mean(values):
    values = [v for v in values if v is not None]
    return sum(values) / len(values) if values else None


def macro_mean(rows, field):
    groups = defaultdict(list)
    for row in rows:
        m = row['metadata']
        groups[m['prompt_id'], m['seed']].append(row.get(field))
    return mean([mean(v) for v in groups.values()])


def curves(records, scale_count):
    groups = defaultdict(list)
    for record in records:
        m = record['metadata']
        aliases = ([{'direction': 'prefix', 'boundary': 0}, {'direction': 'suffix', 'boundary': scale_count}]
                   if m['condition'] == 'baseline' else m['aliases'])
        for alias in aliases:
            for subtype in {'all', record['subtype']}:
                groups[record['semantic'], subtype, alias['direction'], alias['boundary']].append(record)
    result = []
    for (semantic, subtype, direction, boundary), rows in sorted(groups.items()):
        valid = [r for r in rows if r['success'] is not None]
        positive = [r for r in valid if r.get('baseline_success') == 1]
        result.append({'semantic': semantic, 'subtype': subtype, 'direction': direction, 'boundary': boundary,
                       'checks_total': len(rows), 'checks_valid': len(valid),
                       'prompt_seed_total': len({(r['metadata']['prompt_id'], r['metadata']['seed']) for r in rows}),
                       'success_rate': macro_mean(rows, 'success'), 'paired_delta': macro_mean(rows, 'paired_delta'),
                       'baseline_correct_checks': len(positive), 'retention': macro_mean(positive, 'success'),
                       'count_target_mae': macro_mean(rows, 'absolute_error')})
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--scores', type=Path, required=True)
    p.add_argument('--generation', type=Path, required=True)
    args = p.parse_args()
    evaluator_imports()
    from semantic_evaluators.summary import summarize
    summary = summarize(args.scores)
    records = [json.loads(line) for line in (args.scores/'results.jsonl').read_text().splitlines()]
    count = len(read_json(args.generation/'manifest.json')['scale_schedule'])
    rows = curves(records, count)
    with (args.scores/'scale_curves.csv').open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"{summary['status']}: {len(rows)} curve rows; {args.scores/'scale_curves.csv'}")


if __name__ == '__main__':
    main()
