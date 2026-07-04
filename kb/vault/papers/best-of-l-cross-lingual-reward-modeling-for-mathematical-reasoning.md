---
kb_id: "arxiv:2509.15811"
type: "paper"
title: "Best-of-L: Cross-Lingual Reward Modeling for Mathematical Reasoning"
arxiv_id: "2509.15811"
doi: null
hf_repo: null
year: 2025
topics: ["inference-tts"]
claims: 1
uncertain_claims: 1
verdicts: []
aliases: ["Best-of-L: Cross-Lingual Reward Modeling for Mathematical Reasoning", "arXiv:2509.15811", "arxiv:2509.15811"]
tags: ["paper", "topic/inference-tts"]
---
# Best-of-L: Cross-Lingual Reward Modeling for Mathematical Reasoning

[arXiv](https://arxiv.org/abs/2509.15811)
**Topics:** [[inference-tts]]

> [!abstract]
> While the reasoning abilities of large language models (LLMs) continue to advance, it remains unclear how such ability varies across languages in multilingual LLMs and whether different languages produce reasoning paths that complement each other. To investigate this question, we train a reward model to rank generated responses for a given question across languages. Our results show that our cross …

## Claims

> [!warning] UNCERTAIN — inference-tts
> A Kazakh process reward model is feasible but data-expensive; cross-lingual reward transfer is the pragmatic path. Multilingual PRMs (Wang et al., released Feb 2025) map chain-of-thought across languages, and Best-of-L does cross-lingual reward modeling for math reasoning — letting a high-resource (English/Russian) verifier score Kazakh candidates.
>
> **Numbers:** Multilingual PRM (Wang 2025); Best-of-L cross-lingual reward modeling
> **Relevance:** For the Kazakh SLM, skip training a from-scratch Kazakh PRM initially: use self-consistency first, then a cross-lingual/translated ORM, and only invest in a policy-matched Kazakh PRM if verifiable-answer data warrants it.
> **Source:** arXiv:2509.15811 (Best-of-L); Multilingual PRM via arXiv:2510.08049 survey · **Sweep:** `slm-architecture-2026-07`

## Related
- [[left-behind-cross-lingual-transfer-as-a-bridge-for-low-resource-languages-in|Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Langua…]] — Best-of-L routes a high-resource verifier to score Kazakh candidates; Left Behind frames cross-lingual transfer as the low-resource bridge

[[Home]]
