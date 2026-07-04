---
kb_id: "arxiv:2401.06066"
type: "paper"
title: "DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models"
arxiv_id: "2401.06066"
doi: null
hf_repo: null
year: 2024
topics: ["deepseek-tech"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models", "arXiv:2401.06066", "arxiv:2401.06066"]
tags: ["paper", "topic/deepseek-tech"]
---
# DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models

[arXiv](https://arxiv.org/abs/2401.06066)
**Topics:** [[deepseek-tech]]

> [!abstract]
> In the era of large language models, Mixture-of-Experts (MoE) is a promising architecture for managing computational costs when scaling up model parameters. However, conventional MoE architectures like GShard, which activate the top-$K$ out of $N$ experts, face challenges in ensuring expert specialization, i.e. each expert acquires non-overlapping and focused knowledge. In response, we propose the …

## Claims

> [!note] CLAIM — deepseek-tech
> DeepSeekMoE (arXiv 2401.06066) = fine-grained expert segmentation (split each FFN into many small experts, e.g. 8.7M each vs Mixtral's 176.2M) + isolated always-on shared experts capturing common knowledge. It trades TOTAL params for ACTIVE params. At a <=600M TOTAL budget there is almost no room to separate active from total (you'd get e.g. ~600M total / ~200M active), so the MoE efficiency premise collapses; sparse budget is better spent on the Engram lookup axis.
>
> **Numbers:** fine-grained expert ~8.7M vs Mixtral 176.2M; MoE only pays off when total>>active
> **Relevance:** Concludes the user's dense choice is correct within the 600M cap. Don't add DeepSeekMoE; it needs a large total-param headroom the size class forbids. Engram is the sparsity axis that fits.
> **Source:** arXiv:2401.06066 (DeepSeekMoE) · **Sweep:** `slm-architecture-2026-07`

## Related
- [[mixtral-of-experts|Mixtral of Experts]] — DeepSeekMoE formalizes the expert-specialization sparsity Mixtral popularized; both report total as the size class
- [[scaling-embeddings-outperforms-scaling-experts-in-language-models|Scaling Embeddings Outperforms Scaling Experts in Language Models]] — Both argue the total-vs-active tradeoff; DeepSeekMoE says MoE collapses sub-600M, the latter that scaling embeddings beats scaling experts
- [[memory-layers-at-scale|Memory Layers at Scale]] — Memory Layers beats iso-param DeepSeekMoE-style MoE at 134M/373M on NQ/TQA — memory vs experts as competing sparse axes
- [[ultramemv2-memory-networks-scaling-to-120b-parameters-with-superior-long|UltraMemV2: Memory Networks Scaling to 120B Parameters with Superior Long-Context Learning]] — UltraMemV2 reaches parity with an 8-expert MoE at matched compute+params and wins on memorization/ICL

[[Home]]
