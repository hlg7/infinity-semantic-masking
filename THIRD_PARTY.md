# Third-party sources and provenance

## Infinity

Source: https://github.com/FoundationVision/Infinity

Pinned Git revision: `9f9fcd1de7ead377ddf1106db1249a35f3a59143`.

The upstream checkout is downloaded by `scripts/setup_sources.py` and excluded from Git. Its original LICENSE remains in that checkout. The experiment applies `reports/infinity_scale_index.patch` to forward `scale_ind` in the non-fused normalization path, for both baseline and interventions.

Weights: `FoundationVision/Infinity` at Hugging Face revision `e7108923249fb3c836ebfbc3f4b4d318d6131293`: `infinity_2b_reg.pth`, `infinity_vae_d32reg.pth`.

Text encoder: `google/flan-t5-xl` at `7d6315df2c2fb742f0f5b556879d730926ca9001`.

## Semantic evaluators

Source: https://github.com/hlg7/semantic-evaluators

Pinned revision: `55dd2cd614748b5962b5bc4c186d7865efef6285`. The vendored package is a self-contained frozen copy with its original README and provenance documents. This repository does not relicense that code.

Detector: `IDEA-Research/grounding-dino-base`, revision `12bdfa3120f3e7ec7b434d90674b3396eccf88eb`.

VLM: `Qwen/Qwen3-VL-8B-Instruct`, revision `0c351dd01ed87e9c1b53cbc748cba10e6187ff3b`.

Model weights are not included. Refer to upstream repositories for usage terms. Six reviewed output-category normalizations are separate, audited postprocessing; the vendored evaluator source was not edited for that repair.
