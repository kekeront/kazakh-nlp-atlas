---
kb_id: "arxiv:2511.01066"
type: "paper"
title: "HPLT 3.0: Very Large-Scale Multilingual Resources for LLMs and MT. Mono- and Bi-lingual Data, Multilingual Evaluation, and Pre-Trained Models"
arxiv_id: "2511.01066"
doi: null
hf_repo: null
year: 2025
topics: ["kazakh-turkic-nlp"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["HPLT 3.0: Very Large-Scale Multilingual Resources for LLMs and MT. Mono- and Bi-lingual Data, Multilingual Evaluation, and Pre-Trained Models", "arXiv:2511.01066", "arxiv:2511.01066"]
tags: ["paper", "topic/kazakh-turkic-nlp"]
---
# HPLT 3.0: Very Large-Scale Multilingual Resources for LLMs and MT. Mono- and Bi-lingual Data, Multilingual Evaluation, and Pre-Trained Models

[arXiv](https://arxiv.org/abs/2511.01066)
**Topics:** [[kazakh-turkic-nlp]]

> [!abstract]
> We present an ongoing initiative to provide open, very large, high-quality, and richly annotated textual datasets for almost 200 languages. At 30 trillion tokens, this is likely the largest generally available multilingual collection of LLM pre-training data. These datasets are derived from web crawls from different sources and accompanied with a complete, open-source pipeline for document selecti …

## Claims

> [!note] CLAIM — kazakh-turkic-nlp
> Real deduplicated Kazakh web-corpus sizes (ceiling is ~9-10B unique tokens, matching SozKZ's 9B): HPLT 2.0 kaz_Cyrl deduped 27.43 GB / 5.16M docs / 2.00B words (cleaned 20.24 GB); HPLT 3.0 kaz_Cyrl 7.34B tokens / 5.12M docs / 17.21B chars; FineWeb-2 Kazakh ~1.8B Cyrillic words. Overlap across CulturaX/HPLT/mC4/MADLAD is heavy (CulturaX<->FineWeb2 share 25.8B tokens globally), so naive concatenation double-counts.
>
> **Numbers:** HPLT2.0 kaz 2.00B words/27.43GB; HPLT3.0 kaz 7.34B tokens; FineWeb-2 kaz ~1.8B words
> **Relevance:** Budget realistically: HPLT 3.0 (7.34B) is the single largest clean Kazakh source; add FineWeb-2 (~2.5B tok) + curated (kz-transformers multidomain, news, Wiki) and cross-dedup to reach ~9-10B UNIQUE tokens. To train longer than ~1 epoch you MUST add English/Russian/Turkish co-data or synthetic — the pure-Kazakh well is ~10B and repeating it >2-3x risks overfitting.
> **Source:** hplt-project.org/datasets v2.0 & v3.0; arXiv 2511.01066 (HPLT 3.0); FineWeb-2 count via arXiv 2502.11020 · **Sweep:** `slm-architecture-2026-07`

**Cited KB notes:** [[tumlu-a-unified-and-native-language-understanding-benchmark-for-turkic-languages]]

## Related
- [[an-expanded-massive-multilingual-dataset-for-high-performance-language|An Expanded Massive Multilingual Dataset for High-Performance Language Technologies (HPLT)]] — HPLT 2.0 Kazakh token counts superseded by HPLT 3.0's larger monolingual resources
- [[fineweb2-one-pipeline-to-scale-them-all-adapting-pre-training-data-processing|FineWeb2: One Pipeline to Scale Them All -- Adapting Pre-Training Data Processing to Every…]] — Overlapping Kazakh web corpora: HPLT notes heavy dedup overlap with FineWeb-2, so naive concatenation double-counts tokens

[[Home]]
