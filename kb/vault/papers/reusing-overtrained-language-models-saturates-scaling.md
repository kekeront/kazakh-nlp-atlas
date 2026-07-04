---
kb_id: "arxiv:2510.06548"
type: "paper"
title: "Reusing Overtrained Language Models Saturates Scaling"
arxiv_id: "2510.06548"
doi: null
hf_repo: null
year: 2025
topics: ["architecture-fork"]
claims: 1
uncertain_claims: 1
verdicts: []
aliases: ["Reusing Overtrained Language Models Saturates Scaling", "arXiv:2510.06548", "arxiv:2510.06548"]
tags: ["paper", "topic/architecture-fork"]
---
# Reusing Overtrained Language Models Saturates Scaling

[arXiv](https://arxiv.org/abs/2510.06548)
**Topics:** [[architecture-fork]]

> [!abstract]
> Reusing pretrained base models for further pretraining, such as continual pretraining or model growth, is promising at reducing the cost of training language models from scratch. However, the effectiveness remains unclear, especially when applied to overtrained base models. In this work, we empirically study the scaling properties of model reuse and find that the scaling efficiency diminishes in a …

## Claims

> [!warning] UNCERTAIN — architecture-fork
> Under equal-budget framing, continual pretraining is Pareto-cheaper than from-scratch by extended scaling laws — it reaches the same loss with meaningfully fewer FLOPs — but the transfer benefit shrinks logarithmically the more the base was already pretrained (Qwen3-0.6B is heavily overtrained, so the edge is real but bounded).
>
> **Numbers:** Reported CP/reuse FLOP savings ~26% (progressive training to equal loss) up to ~40% (context CP with ~no loss); benefit decays log with base-model pretraining tokens.
> **Relevance:** At a fixed single-A100 budget, adaptation converts more of the 9-10B tokens into Kazakh gains rather than re-learning general competence. The heavy pretraining of Qwen3-0.6B caps but does not erase this advantage.
> **Source:** arXiv 2510.06548 (Reusing Overtrained LMs Saturates Scaling); arXiv 2407.07263 (Reuse, Don't Retrain); arXiv 2405.18392 · **Sweep:** `slm-architecture-2026-07`

**Cited KB notes:** [[reuse-don-t-retrain-a-recipe-for-continued-pretraining-of-language-models]]

## Related
- [[scaling-data-constrained-language-models|Scaling Data-Constrained Language Models]] — Overtrained-base saturation complicates the ≤4-epoch reuse law: reusing an overtrained model saturates continued scaling
- [[qwen3-technical-report|Qwen3 Technical Report]] — Qwen3-0.6B is overtrained ~60k tok/param; this paper warns overtrained models saturate when reused as CPT init — direct risk to the…
- [[reuse-don-t-retrain-a-recipe-for-continued-pretraining-of-language-models|Reuse, Don't Retrain: A Recipe for Continued Pretraining of Language Models]] — Bounds 'Reuse Don't Retrain': the reuse/transfer benefit saturates as base pretraining tokens grow, decaying the advantage
- [[marktechpost-2026-03-31|MarkTechPost 2026-03-31]] — Saturation result challenges LFM2.5-350M's 80,000:1 extreme-overtraining log-linear claim

[[Home]]
