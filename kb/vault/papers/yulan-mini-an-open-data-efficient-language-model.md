---
kb_id: "arxiv:2412.17743"
type: "paper"
title: "YuLan-Mini: An Open Data-efficient Language Model"
arxiv_id: "2412.17743"
doi: null
hf_repo: null
year: 2024
topics: ["training-recipes"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["YuLan-Mini: An Open Data-efficient Language Model", "arXiv:2412.17743", "arxiv:2412.17743"]
tags: ["paper", "topic/training-recipes"]
---
# YuLan-Mini: An Open Data-efficient Language Model

[arXiv](https://arxiv.org/abs/2412.17743)
**Topics:** [[training-recipes]]

> [!abstract]
> Effective pre-training of large language models (LLMs) has been challenging due to the immense resource demands and the complexity of the technical processes involved. This paper presents a detailed technical report on YuLan-Mini, a highly capable base model with 2.42B parameters that achieves top-tier performance among models of similar parameter scale. Our pre-training approach focuses on enhanc …

## Claims

> [!note] CLAIM — training-recipes
> YuLan-Mini (2.42B from scratch, 1.08T tokens, ~447 tok/param) reaches MMLU 49.1 / MATH-500 37.8 / HumanEval 64 — competitive with far-more-data models — using a documented small-scale stability kit: muP-style init sigma=sqrt(2/5d), WeSaR learnable-scalar reparam, embedding-output scaled x10, residual scaling 1.4/sqrt(n_layers), z-loss (1e-4), 10B-token warmup, embedding tying; WSD split 10B warm / 990B stable / 80B anneal (8%).
>
> **Numbers:** 2.42B, 1.08T tok (~447/param); init sigma=sqrt(2/5d); residual 1.4/sqrt(L); z-loss 1e-4; anneal=8% of stable; MMLU 49.1
> **Relevance:** Turnkey recipe to prevent loss spikes when training 500M from scratch on a tiny compute budget (spikes waste money). Adopt z-loss, residual/embedding scaling, muP-style init, long warmup, and an ~8-10% anneal tail wholesale.
> **Source:** arXiv 2412.17743 YuLan-Mini (arxiv.org/html/2412.17743) · **Sweep:** `slm-architecture-2026-07`

## Related
- [[small-scale-proxies-for-large-scale-transformer-training-instabilities|Small-scale proxies for large-scale Transformer training instabilities]] — YuLan-Mini's stability kit (muP init, z-loss, residual scaling) operationalizes the small-scale training-instability diagnostics of this…
- [[the-curse-of-depth-in-large-language-models|The Curse of Depth in Large Language Models]] — LNS explicitly incompatible with YuLan-Mini's residual scaling 1.4/sqrt(n_layers) — pick one, never stack

[[Home]]
