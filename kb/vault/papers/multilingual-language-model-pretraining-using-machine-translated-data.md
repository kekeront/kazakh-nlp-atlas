---
kb_id: "arxiv:2502.13252"
type: "paper"
title: "Multilingual Language Model Pretraining using Machine-translated Data"
arxiv_id: "2502.13252"
doi: null
hf_repo: null
year: 2025
topics: ["data-efficiency-10b-kazakh-10b-token-pre"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Multilingual Language Model Pretraining using Machine-translated Data", "arXiv:2502.13252", "arxiv:2502.13252"]
tags: ["paper", "topic/data-efficiency-10b-kazakh-10b-token-pre"]
---
# Multilingual Language Model Pretraining using Machine-translated Data

[arXiv](https://arxiv.org/abs/2502.13252)
**Topics:** [[data-efficiency-10b-kazakh-10b-token-pre]]

> [!abstract]
> High-resource languages such as English, enables the pretraining of high-quality large language models (LLMs). The same can not be said for most other languages as LLMs still underperform for non-English languages, likely due to a gap in the quality and diversity of the available multilingual pretraining corpora. In this work, we find that machine-translated texts from a single high-quality source …

## Claims

> [!note] CLAIM — data-efficiency-10b-kazakh-10b-token-pre
> Machine-translated pretraining data works at scale but for languages NOT including Kazakh/Turkic. TransWebEdu = FineWeb-Edu translated into 9 langs (Arabic, French, German, Indonesian, Italian, Russian, Spanish, Swahili, Welsh) = 1.7T tokens; a 1.3B model (Llama2 tokenizer) trained from scratch hit 45.08 avg vs Llama-3.2-1B 42.20 and Qwen2.5-1.5B 44.39, using ~10x less data. Russian portion = 157.4B tokens.
>
> **Numbers:** 9 langs, 1.7T tokens total (Russian 157.4B); 1.3B model avg 45.08 vs Llama3.2-1B 42.20 / Qwen2.5-1.5B 44.39; NO Kazakh/Turkic
> **Relevance:** transferable-untested for Kazakh. Confirms MT-synthetic pretraining can match closed-data models — supports using English->Kazakh MT to inflate the ~9-10B pool. Russian is a covered high-resource language, relevant as kk's transfer/code-switch partner.
> **Source:** arXiv:2502.13252 (Multilingual LM Pretraining using MT Data), Tables 2&8 · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[textbooks-are-all-you-need|Textbooks Are All You Need]] — Quantifies the translationese risk in Sherkala's 24% synthetic-MT Kazakh; assesses viability of MT-data pretraining
- [[sailor-open-language-models-for-south-east-asia|Sailor: Open Language Models for South-East Asia]] — both scale multilingual open-model data; TransWebEdu fully MT from-scratch vs Sailor continual-PT on native SE-Asian web

[[Home]]
