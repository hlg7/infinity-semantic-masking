"""Mask-selection regressions; synthetic offsets are NOT Infinity tokenization."""
import copy
import json
from pathlib import Path
import re
import unittest

from semantic_masking import compile_annotation, compile_records, map_tokens, SEMANTICS
from common import schedules as schedule_records

def schedules(count):
    return [(tuple(p["masked_scales"]), p["aliases"]) for p in schedule_records(count)]


ROOT = Path(__file__).resolve().parents[1]


def fixture_tokens(prompt):
    # Stand-in with subwords and punctuation plus BOS/EOS, for selection tests only.
    offsets = [(0, 0)]
    for match in re.finditer(r"\w+|[^\w\s]", prompt):
        start, end = match.span()
        if end - start > 4:
            offsets.extend([(start, start + 3), (start + 3, end)])
        else:
            offsets.append((start, end))
    offsets.append((0, 0))
    ids = list(range(len(offsets)))
    return dict(input_ids=ids, actual_input_ids=ids[:], offsets=offsets,
                special_tokens_mask=[1] + [0] * (len(ids) - 2) + [1], context_length=256)


class SemanticMaskingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.annotations = json.loads((ROOT / "data/annotation_prototype/annotations.json").read_text())

    def record(self, identity):
        return compile_annotation(next(x for x in self.annotations if x["id"] == identity))

    def test_lossless_partition_and_full_group_union(self):
        for compiled in compile_records(self.annotations):
            with self.subTest(compiled["id"]):
                prompt = compiled["prompt"]
                fragments = sorted((x for v in compiled["groups"].values() for x in v), key=lambda x: x["span"])
                self.assertEqual("".join(x["text"] for x in fragments), prompt)
                mapped = map_tokens(compiled, **fixture_tokens(prompt))
                selected = set()
                for target in mapped["targets"]:
                    self.assertIn(target["semantic"], SEMANTICS)
                    indices = set(target["token_positions"])
                    self.assertFalse(selected & indices)
                    selected |= indices
                    actual_chars = set()
                    for index in indices:
                        self.assertEqual(mapped["tokenization"]["special_tokens_mask"][index], 0)
                        start, end = mapped["tokenization"]["offset_mapping"][index]
                        actual_chars |= {i for i in range(start, end) if not prompt[i].isspace()}
                    expected_chars = {i for a, b in target["spans"] for i in range(a, b) if not prompt[i].isspace()}
                    self.assertEqual(actual_chars, expected_chars)
                for fragment in compiled["groups"]["other"]:
                    a, b = fragment["span"]
                    for index in selected:
                        start, end = mapped["tokenization"]["offset_mapping"][index]
                        self.assertFalse(a < end and b > start)

    def test_same_spelling_different_classes(self):
        record = self.record("contextual_orange")
        by_semantic = {t["semantic"]: t for t in record["targets"]}
        self.assertEqual(by_semantic["object"]["target_fragments"], ["orange", "cup"])
        self.assertEqual(by_semantic["color"]["spans"], [[22, 28]])
        self.assertEqual(by_semantic["object"]["spans"][0], [3, 9])

    def test_repeats_not_deduplicated(self):
        record = self.record("repeated_color")
        color = next(t for t in record["targets"] if t["semantic"] == "color")
        self.assertEqual(color["target_fragments"], ["red"] * 3)
        self.assertEqual(len({tuple(s) for s in color["spans"]}), 3)
        self.assertEqual(len(next(t for t in record["targets"] if t["semantic"] == "object")["spans"]), 4)

    def test_multiword_identity_and_relation(self):
        record = self.record("compound_nouns")
        self.assertEqual(next(t for t in record["targets"] if t["semantic"] == "object")["target_fragments"],
                         ["remote control", "picture frame", "pencil case"])
        mapped = map_tokens(self.record("all_six"), **fixture_tokens(self.record("all_six")["prompt"]))
        relation = next(t for t in mapped["targets"] if t["semantic"] == "spatial_relation")
        self.assertEqual(relation["target_fragments"], ["to the left of"])
        self.assertEqual(len(relation["token_positions"]), 4)

    def test_real_legacy_prompt_expands_background_objects(self):
        legacy = json.loads((ROOT / "data/legacy_prompt_example.json").read_text())[0]
        record = self.record("legacy_scene_expanded")
        self.assertEqual(record["prompt"], legacy["prompt"])
        obj = next(t for t in record["targets"] if t["semantic"] == "object")
        self.assertEqual(obj["target_fragments"], ["dog", "garden", "wall", "trees"])
        self.assertEqual(obj["spans"][0], legacy["spans"][0])

    def test_other_only_has_no_targets(self):
        record = self.record("only_other")
        self.assertEqual(record["targets"], [])
        self.assertEqual(record["skipped_semantics"], list(SEMANTICS))
        self.assertEqual(map_tokens(record, **fixture_tokens(record["prompt"]))["targets"], [])

    def test_reject_lossy_or_invalid_annotations(self):
        for change in ("missing", "rewrite", "label", "empty", "whitespace"):
            record = copy.deepcopy(self.annotations[0])
            if change == "missing":
                record["segments"].pop()
            elif change == "rewrite":
                record["segments"][0]["text"] = "two"
            elif change == "label":
                record["segments"][0]["semantic"] = "material"
            elif change == "empty":
                record["segments"][0]["text"] = ""
            else:
                record["segments"][1]["semantic"] = "object"
            with self.subTest(change), self.assertRaises(ValueError):
                compile_annotation(record)
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            compile_records([self.annotations[0]] * 2)

    def test_reject_id_mismatch_overflow_and_missing_offsets(self):
        record = self.record("all_six")
        for mode in ("ids", "overflow", "missing", "special", "length"):
            tokens = fixture_tokens(record["prompt"])
            if mode == "ids":
                tokens["actual_input_ids"][1] = 9999
            elif mode == "overflow":
                tokens["context_length"] = len(tokens["input_ids"]) - 1
            elif mode == "missing":
                tokens["offsets"][1] = (0, 0)
            elif mode == "special":
                tokens["special_tokens_mask"][1] = 1
            else:
                tokens["offsets"].pop()
            with self.subTest(mode), self.assertRaises(ValueError):
                map_tokens(record, **tokens)

    def test_reject_tokens_crossing_classes_or_punctuation(self):
        record = compile_annotation({"id": "small", "prompt": "red car.", "segments": [
            {"text": "red", "semantic": "color"}, {"text": " ", "semantic": "other"},
            {"text": "car", "semantic": "object"}, {"text": ".", "semantic": "other"}]})
        for offsets in ([(0, 7), (7, 8)], [(0, 3), (4, 8)]):
            with self.assertRaisesRegex(ValueError, "crosses"):
                map_tokens(record, input_ids=[1, 2], actual_input_ids=[1, 2], offsets=offsets,
                           special_tokens_mask=[0, 0], context_length=2)

    def test_allow_tokenizer_leading_whitespace(self):
        record = compile_annotation({"id": "leading", "prompt": "A red car", "segments": [
            {"text": "A ", "semantic": "other"}, {"text": "red", "semantic": "color"},
            {"text": " ", "semantic": "other"}, {"text": "car", "semantic": "object"}]})
        mapped = map_tokens(record, input_ids=[5, 6, 7, 8], actual_input_ids=[5, 6, 7, 8],
                            offsets=[(0, 1), (1, 5), (5, 9), (0, 0)],
                            special_tokens_mask=[0, 0, 0, 1], context_length=4)
        by_semantic = {t["semantic"]: t for t in mapped["targets"]}
        self.assertEqual(by_semantic["color"]["token_positions"], [1])
        self.assertEqual(by_semantic["object"]["token_positions"], [2])

    def test_historical_boundary_definition(self):
        # Check the reusable old schedule against the established protocol.
        for count in (1, 3, 10, 13):
            plans = schedules(count)
            self.assertEqual(len(plans), 2 * count)
            by_alias = {(a["direction"], a["boundary"]): selected
                        for selected, aliases in plans for a in aliases}
            for k in range(count + 1):
                self.assertEqual(by_alias["prefix", k], tuple(range(1, k + 1)))
                self.assertEqual(by_alias["suffix", k], tuple(range(k + 1, count + 1)))


if __name__ == "__main__":
    unittest.main()
