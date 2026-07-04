---
kb_id: "hf:mbzuai/kazmmlu"
type: "source"
title: "huggingface.co/datasets/MBZUAI/KazMMLU (dataset inspection 2026-07-03)"
doi: null
hf_repo: "MBZUAI/KazMMLU"
year: null
topics: ["eval-benchmarks"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["hf:mbzuai/kazmmlu"]
tags: ["source", "topic/eval-benchmarks"]
---
# huggingface.co/datasets/MBZUAI/KazMMLU (dataset inspection 2026-07-03)

**Topics:** [[eval-benchmarks]]

## Source URLs
- huggingface.co/datasets/MBZUAI/KazMMLU (dataset inspection 2026-07-03)
- qymyzlm scripts/benchmark_baselines.py

## Findings

> [!note] CLAIM — eval-benchmarks
> KazMMLU's dev split holds only 3 exemplars per subject config, so any 'N-shot' run sourcing shots from dev is capped at 3-shot: qymyzlm's April-2026 baseline table (Qwen3-0.6B-Base 32.8% etc.) silently truncated [:5] to 3 and was mislabeled '5-shot' — relabeled to 3-shot on 2026-07-03. Additional quirks: 'Reading Literacy (High School in kaz)' has only 7 test questions; options are variable 4-5 per row (Option E may be empty), so fixed 5-choice task configs mis-score.
>
> **Numbers:** dev = 3 exemplars/config; 9,870 kk-language test questions; smallest config 7 test questions; 4-5 variable options
> **Relevance:** Every published KazMMLU number of the lab must carry the true shot count; cross-paper comparisons (Sherkala 41.4%) are cross-protocol until re-run.
> **Source:** huggingface.co/datasets/MBZUAI/KazMMLU (dataset inspection 2026-07-03); qymyzlm scripts/benchmark_baselines.py · **Sweep:** `2026-07-eval-provenance`

## Related
- [[sherkala-chat-building-a-state-of-the-art-llm-for-kazakh-in-a-moderately|Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Settin…]] — Sherkala's 9,870-Q eval subset equals the dataset's Kazakh-language test split, aligning ceiling and baseline on subset
- [[tumlu-a-unified-and-native-language-understanding-benchmark-for-turkic-languages|TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages]] — KazMMLU and TUMLU are parallel MMLU-style native benchmarks for Turkic languages; TUMLU covers the same regional-knowledge evaluation niche
- [[huggingface-co-qwen-qwen3-0-6b-base-config-json-fetched-raw|huggingface.co/Qwen/Qwen3-0.6B-Base config.json (fetched raw, 2026-07-…]] — Qwen3-0.6B-Base is the model scored 32.8% on this benchmark — the canonical generative target to beat
- [[evallab-results-2026-04-30-kazmmlu-kk-qwen-qwen3-0-6b-base|evallab/results/2026-04-30__KazMMLU-kk__Qwen-Qwen3-0.6B-Base.json]] — This dataset quirk (dev=3) is exactly what caused that eval run's [:5] truncation and the 5-shot→3-shot mislabel
- [[lm-eval-0-4-11-installed-package-registry-inspection-2026|lm-eval 0.4.11 installed-package registry inspection, 2026-07-03]] — The empty task registry is why KazMMLU needed a custom task YAML + include_path to load at all

[[Home]]
