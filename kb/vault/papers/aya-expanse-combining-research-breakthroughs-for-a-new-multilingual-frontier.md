---
kb_id: "arxiv:2412.04261"
type: "paper"
title: "Aya Expanse: Combining Research Breakthroughs for a New Multilingual Frontier"
arxiv_id: "2412.04261"
doi: null
hf_repo: null
year: 2024
topics: ["training-recipes"]
claims: 1
uncertain_claims: 1
verdicts: []
aliases: ["Aya Expanse: Combining Research Breakthroughs for a New Multilingual Frontier", "arXiv:2412.04261", "arxiv:2412.04261"]
tags: ["paper", "topic/training-recipes"]
---
# Aya Expanse: Combining Research Breakthroughs for a New Multilingual Frontier

[arXiv](https://arxiv.org/abs/2412.04261)
**Topics:** [[training-recipes]]

> [!abstract]
> We introduce the Aya Expanse model family, a new generation of 8B and 32B parameter multilingual language models, aiming to address the critical challenge of developing highly performant multilingual models that match or surpass the capabilities of monolingual models. By leveraging several years of research at Cohere For AI and Cohere, including advancements in data arbitrage, multilingual prefere …

## Claims

> [!warning] UNCERTAIN — training-recipes
> Aya Expanse (8B/32B) does NOT support Kazakh (its 23 languages exclude it); empirically it collapses to 15.7% on Kazakh direct eval and frequently outputs Kyrgyz instead of Kazakh. Gemma 3 (140+ langs) and Qwen3 (119 langs) nominally include far more languages.
>
> **Numbers:** Aya Expanse: 23 langs, Kazakh excluded; 82.3% English vs 15.7% Kazakh; outputs Kyrgyz
> **Relevance:** Disqualifies Aya as a Kazakh teacher despite its multilingual reputation. Teacher selection for KD/synthetic data must be verified on actual Kazakh output — favor Sherkala-8B, or verify Qwen3/Gemma3 Kazakh fluency before committing.
> **Source:** arXiv 2412.04261 Aya Expanse; Kazakh failure numbers from arXiv 2603.21036 (Left Behind: Cross-Lingual Transfer) · **Sweep:** `slm-architecture-2026-07`

**Cited KB notes:** [[left-behind-cross-lingual-transfer-as-a-bridge-for-low-resource-languages-in]]

## Related
- [[qorgau-evaluating-llm-safety-in-kazakh-russian-bilingual-contexts|Qorgau: Evaluating LLM Safety in Kazakh-Russian Bilingual Contexts]] — Qorgau finds Aya101 lowest kk safety despite kk-tailoring; Aya Expanse is the successor whose kk safety is untested here
- [[left-behind-cross-lingual-transfer-as-a-bridge-for-low-resource-languages-in|Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Langua…]] — Aya Expanse is the model whose Kazakh collapse (15.7%, emits Kyrgyz) Left Behind diagnoses as sibling-language interference

[[Home]]
