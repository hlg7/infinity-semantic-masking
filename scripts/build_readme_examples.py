"""Build complete prefix/suffix figures from six existing full-run samples.

No inference or image content edits: verify source hashes, resize, and label.
Original PNG files are supplied separately and are not committed to Git.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEMANTICS = ["object", "color", "shape", "texture", "count", "spatial_relation"]


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def condition(direction, k):
    if (direction, k) in [("prefix", 0), ("suffix", 13)]:
        return "baseline"
    if (direction, k) in [("prefix", 13), ("suffix", 0)]:
        return "full_mask"
    return f"{direction}_{k:02d}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--images", type=Path,
                        default=ROOT / "reports/readme_example_sources/images")
    parser.add_argument("--output", type=Path,
                        default=ROOT / "reports/csfm50_full_review/examples")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("MPLCONFIGDIR", str(ROOT / "reports/csfm50_full_review/mpl-cache"))
    from matplotlib.font_manager import findfont
    from PIL import Image, ImageDraw, ImageFont

    runs = read_jsonl(ROOT / "reports/csfm50_full/generation/runs.jsonl")
    scores = read_jsonl(ROOT / "reports/csfm50_full/evaluation/scores/results.jsonl")
    annotations = {r["id"]: r for r in json.loads(
        (ROOT / "reports/csfm50_full/inputs/annotations.json").read_text())}
    font_path = findfont("DejaVu Sans")
    fonts = {size: ImageFont.truetype(font_path, size) for size in [18, 23, 27, 38]}
    selection = {
        "source": "reports/csfm50_full/generation/runs.jsonl",
        "selection_rule": "For each semantic, select the lexicographically first prompt ID "
                          "whose seed-42 baseline has status correct in the frozen scores. "
                          "No masked-condition scores are used for selection.",
        "seed": 42,
        "unique_source_images": 156,
        "displayed_panels": 168,
        "samples": [],
    }
    for semantic in SEMANTICS:
        candidates = sorted({r["metadata"]["prompt_id"] for r in scores
                             if r["semantic"] == semantic
                             and r["metadata"]["seed"] == 42
                             and r["metadata"]["condition"] == "baseline"
                             and r["status"] == "correct"})
        pid = candidates[0]
        selected = [r for r in runs if r["prompt_id"] == pid and r["seed"] == 42]
        by_condition = {r["condition"]: r for r in selected}
        expected = {condition(d, k) for d in ["prefix", "suffix"] for k in range(14)}
        assert len(selected) == len(by_condition) == 26
        assert set(by_condition) == expected
        annotation = annotations[pid]
        masked_spans = [s["text"] for s in annotation["segments"]
                        if s["semantic"] == semantic]
        thumbnails = {}
        records = []
        for r in selected:
            source = args.images / Path(r["image"]).name
            assert hashlib.sha256(source.read_bytes()).hexdigest() == r["image_sha256"], source
            with Image.open(source) as im:
                assert im.size == (1024, 1024), source
                thumbnails[r["condition"]] = im.convert("RGB").resize(
                    (320, 320), Image.Resampling.LANCZOS)
            records.append({"id": r["id"], "condition": r["condition"],
                            "image_filename": source.name,
                            "image_sha256": r["image_sha256"],
                            "masked_scales": r["masked_scales"]})

        # Four aligned rows: prefix 0..6, prefix 7..13, suffix 0..6, suffix 7..13.
        margin, gap, cell_w, cell_h = 24, 12, 320, 384
        width = margin * 2 + cell_w * 7 + gap * 6
        row_starts = [180, 576, 1044, 1440]
        sheet = Image.new("RGB", (width, 1858), "#f5f7fa")
        draw = ImageDraw.Draw(sheet)
        draw.text((margin, 18), f"{semantic.replace('_', ' ').title()} | {pid} | seed 42",
                  font=fonts[38], fill="#142235")
        draw.text((margin, 75), "Masked text: " + " + ".join(masked_spans),
                  font=fonts[23], fill="#334155")
        draw.text((margin, 127), "PREFIX(k): mask scales 1..k", font=fonts[27], fill="#1d4ed8")
        draw.text((margin, 991), "SUFFIX(k): mask scales k+1..13", font=fonts[27], fill="#b45309")
        panels = []
        for direction_index, direction in enumerate(["prefix", "suffix"]):
            color = "#1d4ed8" if direction == "prefix" else "#b45309"
            for k in range(14):
                cond = condition(direction, k)
                r = by_condition[cond]
                scales = list(range(1, k + 1)) if direction == "prefix" else list(range(k + 1, 14))
                assert r["masked_scales"] == scales, (pid, direction, k)
                row, col = direction_index * 2 + k // 7, k % 7
                x, y = margin + col * (cell_w + gap), row_starts[row]
                draw.rounded_rectangle((x, y, x + cell_w, y + cell_h), radius=7, fill="white")
                extra = " | baseline" if cond == "baseline" else " | full mask" if cond == "full_mask" else ""
                draw.text((x + 8, y + 4), f"{direction.title()}({k}){extra}", font=fonts[23], fill=color)
                mask_label = "none" if not scales else str(scales[0]) if len(scales) == 1 else f"{scales[0]}-{scales[-1]}"
                draw.text((x + 8, y + 33), f"Masked scales: {mask_label}", font=fonts[18], fill="#475569")
                sheet.paste(thumbnails[cond], (x, y + 64))
                panels.append({"direction": direction, "boundary": k,
                               "source_id": r["id"], "masked_scales": scales})
        draw.text((margin, 1825), "28 panels / 26 unique images: baseline and full mask are shared endpoints. Original generation; display resized only.",
                  font=fonts[18], fill="#475569")
        filename = f"{semantic}_all_scales.jpg"
        sheet.save(args.output / filename, quality=95, subsampling=0, optimize=True)
        selection["samples"].append({"semantic": semantic, "prompt_id": pid,
                                     "prompt": annotation["prompt"], "masked_spans": masked_spans,
                                     "figure": filename, "sources": records, "panels": panels})
        print(f"{pid}: verified 26 PNG hashes, rendered 28 panels -> {filename}")
    (args.output / "manifest.json").write_text(
        json.dumps(selection, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
