"""Compile complete prompt annotations into whole-semantic mask targets.

This module does not infer semantic labels or generate images. Offsets are Python
character offsets in the exact, unmodified prompt, with exclusive end positions.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re


SEMANTICS = ("object", "color", "shape", "texture", "count", "spatial_relation")
LABELS = (*SEMANTICS, "other")
VERSION = "semantic_groups_v1"


def compile_annotation(record):
    """Validate a lossless partition and combine every occurrence of each class."""
    identity, prompt = record.get("id"), record.get("prompt")
    if not isinstance(identity, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,95}", identity):
        raise ValueError("Annotation needs a safe, nonempty id of at most 96 characters")
    if not isinstance(prompt, str) or not prompt.strip():
        raise ValueError(f"{identity}: prompt must be nonempty")
    segments = record.get("segments")
    if not isinstance(segments, list) or not segments:
        raise ValueError(f"{identity}: segments must be a nonempty list")
    groups = {label: [] for label in LABELS}
    cursor = 0
    for segment in segments:
        if not isinstance(segment, dict):
            raise ValueError(f"{identity}: segment must be an object")
        label, text = segment.get("semantic"), segment.get("text")
        if not isinstance(label, str) or label not in LABELS:
            raise ValueError(f"{identity}: unknown semantic {label!r}")
        if not isinstance(text, str) or not text:
            raise ValueError(f"{identity}: segment text must be nonempty")
        if label != "other" and (text != text.strip() or not any(c.isalnum() for c in text)):
            raise ValueError(f"{identity}: semantic spans need text without outer whitespace")
        end = cursor + len(text)
        if prompt[cursor:end] != text:
            raise ValueError(f"{identity}: segment does not match prompt at character {cursor}")
        groups[label].append({"span": [cursor, end], "text": text})
        cursor = end
    if cursor != len(prompt):
        raise ValueError(f"{identity}: segments do not cover the entire prompt")
    targets = []
    for semantic in SEMANTICS:
        fragments = groups[semantic]
        if not fragments:
            continue
        targets.append({
            "id": f"{identity}__{semantic}", "prompt_id": identity,
            "prompt": prompt, "semantic": semantic,
            "mask_unit": "semantic_class", "spans": [f["span"] for f in fragments],
            "target_text": " ".join(f["text"] for f in fragments),
            "target_fragments": [f["text"] for f in fragments],
        })
    target_semantic = record.get('target_semantic')
    if target_semantic is not None and (target_semantic not in SEMANTICS or not groups[target_semantic]):
        raise ValueError(f'{identity}: dataset target semantic must exist in the complete annotation')
    return {"id": identity, "prompt": prompt, "annotation_notes": record.get("notes", ""),
            "target_semantic": target_semantic,
            "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
            "groups": groups, "targets": targets,
            "skipped_semantics": [s for s in SEMANTICS if not groups[s]]}


def map_tokens(compiled, *, input_ids, offsets, special_tokens_mask,
               actual_input_ids, context_length):
    """Validate locator vs actual encoder IDs and return whole-class token unions.

    Supply unpadded, untruncated tokenization of compiled['prompt'] from the actual
    encoder and an offset-capable locator. No guessed or legacy token indices.
    Tokens may consume adjacent whitespace, but may not consume another class's
    content or punctuation. Fail on normalization loss rather than silently masking
    only part of a semantic. Special tokens are never targets.
    """
    if type(context_length) is not int or context_length < 1:
        raise ValueError("An explicit positive encoder context length is required")
    if not input_ids or any(type(i) is not int or i < 0 for i in input_ids):
        raise ValueError("Token IDs must be a nonempty list of nonnegative integers")
    if list(input_ids) != list(actual_input_ids):
        raise ValueError("Locator and actual encoder token IDs differ")
    if len(input_ids) > context_length:
        raise ValueError("Prompt exceeds encoder context; refusing truncation")
    if len(offsets) != len(input_ids) or len(special_tokens_mask) != len(input_ids):
        raise ValueError("Token IDs, offsets and special-token mask lengths differ")
    prompt = compiled["prompt"]
    owners = [None] * len(prompt)
    for semantic, fragments in compiled["groups"].items():
        for fragment in fragments:
            start, end = fragment["span"]
            owners[start:end] = [semantic] * (end - start)
    positions = {s: [] for s in SEMANTICS}
    covered = set()
    for index, (offset, special) in enumerate(zip(offsets, special_tokens_mask)):
        if (not isinstance(offset, (list, tuple)) or len(offset) != 2
                or any(type(v) is not int for v in offset)
                or not 0 <= offset[0] <= offset[1] <= len(prompt)):
            raise ValueError(f"Invalid offset at token {index}")
        if type(special) is not int or special not in (0, 1):
            raise ValueError("Special-token mask must contain integer zeros/ones")
        if special:
            continue
        start, end = offset
        chars = {i for i in range(start, end) if not prompt[i].isspace()}
        labels = {owners[i] for i in chars}
        selected = labels.intersection(SEMANTICS)
        if selected and len(labels) != 1:
            raise ValueError(f"Token {index} crosses semantic/other boundaries: {sorted(labels)}")
        if selected:
            semantic = next(iter(selected))
            positions[semantic].append(index)
            covered.update(chars)
    required = {i for i, owner in enumerate(owners)
                if owner in SEMANTICS and not prompt[i].isspace()}
    if required - covered:
        raise ValueError(f"Semantic text is missing from token offsets at {sorted(required - covered)}")
    targets = []
    for target in compiled["targets"]:
        indices = positions[target["semantic"]]
        if not indices:
            raise ValueError(f"No tokens for {target['semantic']}")
        targets.append(dict(target, token_positions=indices,
                            target_token_ids=[input_ids[i] for i in indices]))
    return dict(compiled, targets=targets, tokenization={
        "input_ids": list(input_ids), "offset_mapping": [list(x) for x in offsets],
        "special_tokens_mask": list(special_tokens_mask),
        "sequence_length": len(input_ids), "context_length": context_length,
        "actual_encoder_ids_match": True,
    })


def compile_records(records):
    if not isinstance(records, list) or not records:
        raise ValueError("Input must be a nonempty JSON list of annotations")
    result, seen = [], set()
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Annotation must be an object")
        compiled = compile_annotation(record)
        if compiled["id"] in seen:
            raise ValueError(f"Duplicate prompt id: {compiled['id']}")
        seen.add(compiled["id"])
        result.append(compiled)
    return result


def render_review(records):
    lines = ["# 整类 semantic mask 清单", "",
             "这是文本标注和 mask 目标的检查结果，不是生成实验或语义评分结果。",
             "`other` 永不 mask；未出现的 semantic 跳过。字符位置采用左闭右开区间。", ""]
    for record in records:
        lines.extend([f"## {record['id']}", "", record["prompt"], ""])
        if record.get("annotation_notes"):
            lines.extend([f"标注说明：{record['annotation_notes']}", ""])
        for target in record["targets"]:
            fragments = " + ".join(f"`{text}`" for text in target["target_fragments"])
            lines.append(f"- **{target['semantic']}**：{fragments}；位置 `{target['spans']}`")
            if "token_positions" in target:
                lines.append(f"  token 位置：`{target['token_positions']}`")
        other = " + ".join(f"`{x['text']}`" for x in record["groups"]["other"])
        lines.extend(["", f"保留的 other：{other or '无'}", "",
                      f"跳过：{', '.join(record['skipped_semantics']) or '无'}", ""])
        if "tokenization" not in record:
            lines.extend(["Token 映射：待接入实际 backbone tokenizer 后验证。", ""])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True, help="JSON review artifact")
    parser.add_argument("--review", type=Path, help="Optional Markdown mask checklist")
    parser.add_argument("--tokenizer", type=Path, help="Actual encoder's local tokenizer directory")
    parser.add_argument("--locator", type=Path, help="Optional local fast tokenizer directory")
    parser.add_argument("--context-length", type=int, help="Actual encoder's configured context length")
    args = parser.parse_args()
    if args.tokenizer and (args.context_length is None or args.context_length < 1):
        parser.error("--tokenizer requires a positive --context-length")
    if not args.tokenizer and (args.locator or args.context_length is not None):
        parser.error("--locator and --context-length require --tokenizer")
    paths = [args.output.resolve()]
    if args.review:
        paths.append(args.review.resolve())
    if args.input.resolve() in paths or len(set(paths)) != len(paths):
        parser.error("Input, output and review must use distinct paths")
    raw = args.input.read_bytes()
    records = compile_records(json.loads(raw))
    if args.tokenizer:
        # Optional: the annotation-only path needs no ML packages or network.
        from transformers import AutoTokenizer
        actual = AutoTokenizer.from_pretrained(str(args.tokenizer), use_fast=False, local_files_only=True)
        locator = AutoTokenizer.from_pretrained(str(args.locator or args.tokenizer),
                                                use_fast=True, local_files_only=True)
        if not locator.is_fast:
            raise ValueError("Locator must support fast-tokenizer character offsets")
        mapped = []
        for record in records:
            prompt = record["prompt"]
            official = actual(prompt, padding=False, truncation=False)["input_ids"]
            located = locator(prompt, padding=False, truncation=False,
                              return_offsets_mapping=True, return_special_tokens_mask=True)
            mapped.append(map_tokens(record, input_ids=located["input_ids"],
                                     offsets=located["offset_mapping"],
                                     special_tokens_mask=located["special_tokens_mask"],
                                     actual_input_ids=official, context_length=args.context_length))
        records = mapped
    artifact = {
        "version": VERSION, "input_sha256": hashlib.sha256(raw).hexdigest(),
        "mask_unit": "semantic_class", "mask_other": False,
        "annotation_source": "provided_segments_not_automatic_inference",
        "token_mapping_status": "validated_local_tokenizers" if args.tokenizer else "pending_backbone_tokenizer",
        "tokenizer": str(args.tokenizer.resolve()) if args.tokenizer else None,
        "locator": str((args.locator or args.tokenizer).resolve()) if args.tokenizer else None,
        "backbone_generation_verified": False,
        "prompt_count": len(records), "target_count": sum(len(r["targets"]) for r in records),
        "records": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(artifact, ensure_ascii=False, indent=2) + "\n")
    if args.review:
        args.review.parent.mkdir(parents=True, exist_ok=True)
        args.review.write_text(render_review(records))
    print(json.dumps({k: artifact[k] for k in ("prompt_count", "target_count", "token_mapping_status")}))


if __name__ == "__main__":
    main()
