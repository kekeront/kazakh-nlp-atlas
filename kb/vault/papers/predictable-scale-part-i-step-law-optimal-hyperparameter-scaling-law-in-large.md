---
kb_id: "arxiv:2503.04715"
type: "paper"
title: "Predictable Scale: Part I, Step Law -- Optimal Hyperparameter Scaling Law in Large Language Model Pretraining"
arxiv_id: "2503.04715"
doi: null
hf_repo: null
year: 2025
topics: ["training-recipes"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Predictable Scale: Part I, Step Law -- Optimal Hyperparameter Scaling Law in Large Language Model Pretraining", "arXiv:2503.04715", "arxiv:2503.04715"]
tags: ["paper", "topic/training-recipes"]
---
# Predictable Scale: Part I, Step Law -- Optimal Hyperparameter Scaling Law in Large Language Model Pretraining

[arXiv](https://arxiv.org/abs/2503.04715)
**Topics:** [[training-recipes]]

> [!abstract]
> The impressive capabilities of Large Language Models (LLMs) across diverse tasks are now well established, yet their effective deployment necessitates careful hyperparameter optimization. Although existing methods have explored the influence of hyperparameters on model performance, a principled and generalizable framework across model architectures and data recipes remains absent. In this study, w …

## Claims

> [!note] CLAIM — training-recipes
> Step Law gives directly usable fitted formulas for optimal hyperparameters: learning rate eta(N,D)=1.79*N^-0.713*D^0.307 and batch size B(D)=0.58*D^0.571 (N=non-embedding params, D=tokens). Claimed within ~0.09-0.5% of the exhaustive optimum, and shown topology-invariant across model shapes, robust across bilingual/code-heavy data mixes and MoE sparsity levels.
>
> **Numbers:** eta=1.79*N^-0.713*D^0.307; B=0.58*D^0.571; error ~0.09% dense, <=0.5% MoE; for N~3.5e8, D~20B my plug-in gives eta~2e-3 and batch ~0.4-0.5M tokens
> **Relevance:** Removes the need for an expensive muP sweep on the $264 budget: plug in N,D to get LR~2e-3 and batch ~0.4-0.5M tokens for a 500M/~20-40B run. Explicitly validated on bilingual corpora, matching the kk/ru code-switching setting.
> **Source:** arXiv 2503.04715 Predictable Scale Part I: Step Law (arxiv.org/html/2503.04715) · **Sweep:** `slm-architecture-2026-07`

## Related
- [[muon-is-scalable-for-llm-training|Muon is Scalable for LLM Training]] — Both give sub-2B optimizer/LR scaling laws; Step-Law's AdamW HP transfer complements Muon's FLOPs-efficiency claim
- [[u-p-the-unit-scaled-maximal-update-parametrization|u-$μ$P: The Unit-Scaled Maximal Update Parametrization]] — Competing routes to hyperparameter transfer: Step Law's directly-fitted LR/batch formulas vs u-muP's unit-scaled parametrization
- [[don-t-be-lazy-completep-enables-compute-efficient-deep-transformers|Don't be lazy: CompleteP enables compute-efficient deep transformers]] — both are HP-transfer/scaling recipes for picking LR on a small proxy before the full run

[[Home]]
