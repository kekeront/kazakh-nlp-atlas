---
kb_id: "arxiv:2503.10267"
type: "paper"
title: "An Expanded Massive Multilingual Dataset for High-Performance Language Technologies (HPLT)"
arxiv_id: "2503.10267"
doi: null
hf_repo: "uonlp/CulturaX"
year: 2025
topics: ["data-efficiency-10b-kazakh-10b-token-pre"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["An Expanded Massive Multilingual Dataset for High-Performance Language Technologies (HPLT)", "arXiv:2503.10267", "arxiv:2503.10267"]
tags: ["paper", "topic/data-efficiency-10b-kazakh-10b-token-pre"]
---
# An Expanded Massive Multilingual Dataset for High-Performance Language Technologies (HPLT)

[arXiv](https://arxiv.org/abs/2503.10267)
**Topics:** [[data-efficiency-10b-kazakh-10b-token-pre]]

> [!abstract]
> Training state-of-the-art large language models requires vast amounts of clean and diverse textual data. However, building suitable multilingual datasets remains a challenge. In this work, we present HPLT v2, a collection of high-quality multilingual monolingual and parallel corpora, extending prior work of the HPLT project. The monolingual portion of the data contains 8T tokens covering 193 langu …

## Claims

> [!note] CLAIM — data-efficiency-10b-kazakh-10b-token-pre
> Exact unique-token counts for the three primary Kazakh web sources (for de-duplication budgeting): CulturaX kk = 2,733,982 docs / 2,802,485,195 tokens (~2.80B, mT5 tokenizer, 0.04% of CulturaX's 6.3T). HPLT 2.0 deduplicated kaz_Cyrl = 1.409e9 (~1.41B whitespace tokens); HPLT2.0_cleaned kaz_Cyrl = 2.64M docs. FineWeb-2 kaz_Cyrl = 3.38M docs (rehydrated).
>
> **Numbers:** CulturaX kk: 2,733,982 docs / 2,802,485,195 tok; HPLT2.0 dedup kk: 1.409B tok (cleaned 2.64M docs); FineWeb-2 kk: 3.38M docs
> **Relevance:** tested-on-Kazakh (corpus artifacts). These three overlap heavily (all CommonCrawl-derived) — after cross-source fuzzy dedup the union is ~9-10B unique tokens, matching SozKZ's 9.0B post-dedup. Sets the hard unique-token budget the recipe must respect.
> **Source:** huggingface.co/datasets/uonlp/CulturaX (kk row); arXiv:2503.10267 HPLT2.0 Table 5; HF HPLT/HPLT2.0_cleaned & HuggingFaceFW/fineweb-2 viewers · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[hplt-3-0-very-large-scale-multilingual-resources-for-llms-and-mt-mono-and-bi|HPLT 3.0: Very Large-Scale Multilingual Resources for LLMs and MT. Mono- and Bi-lingual Da…]] — HPLT 2.0 Kazakh token counts superseded by HPLT 3.0's larger monolingual resources
- [[fineweb2-one-pipeline-to-scale-them-all-adapting-pre-training-data-processing|FineWeb2: One Pipeline to Scale Them All -- Adapting Pre-Training Data Processing to Every…]] — FineWeb2 reports outperforming HPLT/CulturaX downstream and adds per-language rehydration over HPLT's raw Kazakh counts

[[Home]]
