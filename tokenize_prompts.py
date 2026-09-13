"""Map full semantic groups using Infinity's actual fast T5 tokenizer, on CPU."""
import argparse
from pathlib import Path
from common import ROOT, read_json, write_json
from semantic_masking import compile_records, map_tokens, render_review


def load_tokenizer(path):
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(str(path), legacy=True, local_files_only=True, use_fast=True)
    if not tokenizer.is_fast:
        raise ValueError('Infinity T5 tokenizer must expose offset mappings')
    tokenizer.model_max_length = 512
    return tokenizer


def tokenize_record(compiled, tokenizer):
    prompt = compiled['prompt']
    located = tokenizer(prompt, truncation=False, padding=False,
                        return_offsets_mapping=True, return_special_tokens_mask=True)
    # Match encode_prompt's actual batched/padded call, but refuse truncation first.
    if len(located['input_ids']) > 512:
        raise ValueError('Prompt exceeds Infinity text context (512); no truncation allowed')
    actual = tokenizer(text=[prompt], max_length=512, padding='max_length', truncation=True)
    actual_ids = [i for i, keep in zip(actual['input_ids'][0], actual['attention_mask'][0]) if keep]
    mapped = map_tokens(compiled, input_ids=located['input_ids'], offsets=located['offset_mapping'],
                        special_tokens_mask=located['special_tokens_mask'],
                        actual_input_ids=actual_ids, context_length=512)
    mapped['tokenization']['tokens'] = tokenizer.convert_ids_to_tokens(actual_ids)
    return mapped


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--annotations', type=Path, required=True)
    p.add_argument('--tokenizer', type=Path, default=ROOT/'assets/flan-t5-xl')
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    tokenizer = load_tokenizer(args.tokenizer)
    records = [tokenize_record(r, tokenizer)
               for r in compile_records(read_json(args.annotations))]
    write_json(args.output, {'token_mapping_status': 'validated_infinity_t5', 'records': records})
    args.output.with_suffix('.md').write_text(render_review(records))
    print(f'Validated {len(records)} prompts with Infinity T5; no image model loaded')


if __name__ == '__main__':
    main()
