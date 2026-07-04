---
kb_id: "arxiv:2502.11020"
type: "paper"
title: "TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages"
arxiv_id: "2502.11020"
doi: null
hf_repo: null
year: 2025
topics: ["sota-slm", "kazakh-turkic-nlp"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages", "arXiv:2502.11020", "arxiv:2502.11020"]
tags: ["paper", "topic/sota-slm", "topic/kazakh-turkic-nlp"]
---
# TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages

[arXiv](https://arxiv.org/abs/2502.11020)
**Topics:** [[sota-slm]], [[kazakh-turkic-nlp]]

> [!abstract]
> Being able to thoroughly assess massive multi-task language understanding (MMLU) capabilities is essential for advancing the applicability of multilingual language models. However, preparing such benchmarks in high quality native language is often costly and therefore limits the representativeness of evaluation datasets. While recent efforts focused on building more inclusive MMLU benchmarks, thes …

## Claims

> [!note] CLAIM — sota-slm
> TUMLU-mini is the right Turkic cross-lingual eval: a natively-authored (not translated) benchmark of 4-choice middle/high-school questions across 8 Turkic languages incl. Kazakh, Azerbaijani, Uzbek, Kyrgyz, Tatar, Uyghur, Karakalpak, Crimean Tatar; 38,139 total questions across 11 subjects.
>
> **Numbers:** 8 Turkic langs, 11 subjects, 38,139 Qs, 4-choice
> **Relevance:** Confirms the paper's secondary eval choice and enables a 'Turkic transfer' story — training on Kazakh + related Turkic data and reporting TUMLU-mini would strengthen the SOTA claim beyond a single language.
> **Source:** arXiv 2502.11020 (TUMLU, ACL 2025); github.com/ceferisbarov/TUMLU · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — kazakh-turkic-nlp
> TUMLU-mini is the Turkic secondary eval: Kazakh subset = 700 Q (7 subjects x 100, Cyrillic). All models score higher on Kazakh in CYRILLIC than Latin. Best small-open on Kazakh: Gemma-2-9B 49.1, Llama-3.1-8B 46.4, Qwen2.5-7B 45.0; frontier Claude-3.5-Sonnet 83.0 (87.1 with 5-shot CoT). No <=1B model was tested. FineWeb-2 has 1.8B Kazakh Cyrillic words and 0 Latin.
>
> **Numbers:** Kazakh TUMLU-mini 700 Q; Gemma-2-9B 49.1 / Llama-3.1-8B 46.4 / Qwen2.5-7B 45.0; Claude-3.5-Sonnet 83.0
> **Relevance:** Train and evaluate in Cyrillic only for now — Latin Kazakh web data is essentially nonexistent, so the 2031 Latin transition is a pure data gap, not something to pre-train on. Handle Latin via deterministic Cyrillic<->Latin transliteration augmentation, not native Latin corpora.
> **Source:** arXiv 2502.11020 (TUMLU), html v2, Table 2 + Appendix B · **Sweep:** `slm-architecture-2026-07`

## Related
- [[huggingface-co-datasets-mbzuai-kazmmlu-dataset-inspection|huggingface.co/datasets/MBZUAI/KazMMLU (dataset inspection 2026-07-03)]] — KazMMLU and TUMLU are parallel MMLU-style native benchmarks for Turkic languages; TUMLU covers the same regional-knowledge evaluation niche

[[Home]]
