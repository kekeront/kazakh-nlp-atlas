---
kb_id: "arxiv:2510.19093"
type: "paper"
title: "Weight Decay may matter more than muP for Learning Rate Transfer in Practice"
arxiv_id: "2510.19093"
doi: null
hf_repo: null
year: 2025
topics: ["training-recipes"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Weight Decay may matter more than muP for Learning Rate Transfer in Practice", "arXiv:2510.19093", "arxiv:2510.19093"]
tags: ["paper", "topic/training-recipes"]
---
# Weight Decay may matter more than muP for Learning Rate Transfer in Practice

[arXiv](https://arxiv.org/abs/2510.19093)
**Topics:** [[training-recipes]]

> [!abstract]
> Transferring the optimal learning rate from small to large neural networks can enable efficient training at scales where hyperparameter tuning is otherwise prohibitively expensive. To this end, the Maximal Update Parameterization (muP) proposes a learning rate scaling designed to keep the update dynamics of internal representations stable across different model widths. However, the scaling rules o …

## Claims

> [!note] CLAIM — training-recipes
> muP alone does not guarantee learning-rate transfer in practice — recent work argues weight decay may matter more than muP for LR transfer. Combined with Step Law's directly-fitted LR/batch formulas, an explicit muP sweep is largely avoidable for a single 500M target.
>
> **Numbers:** muP width/depth transfer theoretically justified but WD-dependent empirically; u-muP adds unit-scaling for low precision
> **Relevance:** On a one-shot 500M/$264 budget, skip a costly muP proxy sweep: use Step Law's formula for LR/batch and tune weight decay (~0.1) instead. Keep muP-style init (from YuLan-Mini) only for stability, not for HP transfer.
> **Source:** arXiv 2510.19093 Weight Decay may matter more than muP; arXiv (ICLR 2025) u-muP · **Sweep:** `slm-architecture-2026-07`

## Related
- [[u-p-the-unit-scaled-maximal-update-parametrization|u-$μ$P: The Unit-Scaled Maximal Update Parametrization]] — u-muP claims muP fixes fp16 divergence; 2510.19093 argues weight decay not muP drives LR transfer — disputes muP's value
- [[don-t-be-lazy-completep-enables-compute-efficient-deep-transformers|Don't be lazy: CompleteP enables compute-efficient deep transformers]] — CompleteP extends muP transfer to depth; 2510.19093 says muP benefit is replaceable by modified warmup — direct disagreement

[[Home]]
