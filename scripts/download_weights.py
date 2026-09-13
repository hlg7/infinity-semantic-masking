"""Explicit download command for later GPU setup; never called by generation."""
from pathlib import Path
import argparse
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common import ROOT, read_json, write_json


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tokenizer-only', action='store_true', help='Download T5 tokenizer files for CPU tests; no model weights')
    args = parser.parse_args()
    from huggingface_hub import HfApi, snapshot_download
    source = read_json(ROOT/'configs/weights_source.json')
    model_repo, revision, files = source['infinity_repo'], source['revision'], source['files']
    if not args.tokenizer_only:
        info = HfApi().model_info(model_repo, revision=revision)
        available = {entry.rfilename for entry in info.siblings}
        missing = set(files) - available
        if missing:
            raise FileNotFoundError(f'Model repository is missing requested files: {sorted(missing)}')
        snapshot_download(model_repo, revision=revision, local_dir=ROOT/'assets', allow_patterns=files)
        for filename in files:
            if not (ROOT/'assets'/filename).is_file():
                raise FileNotFoundError(f'Model repository did not supply {filename}')
    t5 = read_json(ROOT/'reports/t5_source.json')
    snapshot_download(t5['repo'], revision=t5['revision'], local_dir=ROOT/'assets/flan-t5-xl',
                      allow_patterns=['*.json', 'spiece.model'] + ([] if args.tokenizer_only else ['*.safetensors']),
                      ignore_patterns=['*flax*', '*tf_*'])
    if not args.tokenizer_only:
        write_json(ROOT/'assets/weights_source.json', source)


if __name__ == '__main__':
    main()
