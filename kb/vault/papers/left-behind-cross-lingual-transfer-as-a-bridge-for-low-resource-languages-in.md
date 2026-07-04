---
kb_id: "arxiv:2603.21036"
type: "paper"
title: "Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models"
arxiv_id: "2603.21036"
doi: null
hf_repo: null
year: 2026
topics: ["kazakh-turkic-nlp"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models", "arXiv:2603.21036", "arxiv:2603.21036"]
tags: ["paper", "topic/kazakh-turkic-nlp"]
---
# Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models

[arXiv](https://arxiv.org/abs/2603.21036)
**Topics:** [[kazakh-turkic-nlp]]

> [!abstract]
> We investigate how large language models perform on low-resource languages by benchmarking eight LLMs across five experimental conditions in English, Kazakh, and Mongolian. Using 50 hand-crafted questions spanning factual, reasoning, technical, and culturally grounded categories, we evaluate 2,000 responses on accuracy, fluency, and completeness. We find a consistent performance gap of 13.8-16.7 p …

## Claims

> [!note] CLAIM — kazakh-turkic-nlp
> Broad multilingual coverage HURTS Kazakh via sibling-language interference: Aya Expanse (100+ languages, incl. Turkic) collapses to 15.7% on Kazakh (vs 82.3% English) because it frequently emits KYRGYZ instead of Kazakh. Cross-lingual-transfer pipelines give only marginal Kazakh gains (+0.4pp CLT aggregate; +2.2pp for bilingual models). Kazakh-Kyrgyz-Turkish proximity causes generation leakage, not free transfer.
>
> **Numbers:** Aya Expanse Kazakh 15.7% vs English 82.3%; CLT +0.4pp; bilingual +2.2pp
> **Relevance:** Design implication: do NOT chase broad Turkic multilinguality. Use CONTROLLED co-training (Kazakh-dominant + English for knowledge + limited Russian/Turkish), exactly Sherkala's mix — not an Aya-style 100-language soup. Add a language-ID / script guard in eval to catch Kyrgyz leakage. Turkish co-data helps tokenizer/morphology sharing but must be capped to avoid output drift.
> **Source:** arXiv 2603.21036 (cross-lingual transfer); Aya numbers corroborated across 2 sources · **Sweep:** `slm-architecture-2026-07`

## Related
- [[best-of-l-cross-lingual-reward-modeling-for-mathematical-reasoning|Best-of-L: Cross-Lingual Reward Modeling for Mathematical Reasoning]] — Best-of-L routes a high-resource verifier to score Kazakh candidates; Left Behind frames cross-lingual transfer as the low-resource bridge
- [[aya-expanse-combining-research-breakthroughs-for-a-new-multilingual-frontier|Aya Expanse: Combining Research Breakthroughs for a New Multilingual Frontier]] — Aya Expanse is the model whose Kazakh collapse (15.7%, emits Kyrgyz) Left Behind diagnoses as sibling-language interference

[[Home]]
