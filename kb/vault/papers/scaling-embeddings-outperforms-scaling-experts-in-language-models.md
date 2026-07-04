---
kb_id: "arxiv:2601.21204"
type: "paper"
title: "Scaling Embeddings Outperforms Scaling Experts in Language Models"
arxiv_id: "2601.21204"
doi: null
hf_repo: null
year: 2026
topics: ["novelty-check"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Scaling Embeddings Outperforms Scaling Experts in Language Models", "arXiv:2601.21204", "arxiv:2601.21204"]
tags: ["paper", "topic/novelty-check"]
---
# Scaling Embeddings Outperforms Scaling Experts in Language Models

[arXiv](https://arxiv.org/abs/2601.21204)
**Topics:** [[novelty-check]]

> [!abstract]
> While Mixture-of-Experts (MoE) architectures have become the standard for sparsity scaling in large language models, they increasingly face diminishing returns and system-level bottlenecks. In this work, we explore embedding scaling as a potent, orthogonal dimension for scaling sparsity. Through a comprehensive analysis and experiments, we identify specific regimes where embedding scaling achieves …

## Claims

> [!note] CLAIM — novelty-check
> 'Scaling Embeddings Outperforms Scaling Experts' provides the strongest theoretical backing that embedding/memory scaling beats MoE — useful as supporting citation, but it is a >68B model, so it does NOT pre-empt an SLM claim. UltraMemV2 adds the key design insight that activation density matters more than total sparse-param count.
>
> **Numbers:** LongCat-Flash-Lite: 68.5B total, ~3B activated, >30B params in embeddings, surpasses parameter-equivalent MoE. UltraMemV2: validated to 120B total / 2.5B activated; 'activation density > total sparse parameter count'
> **Relevance:** Cite both to justify why a memory-augmented SLM should beat a same-active-param dense model. UltraMemV2's density insight argues for FEWER, denser memory lookups than many sparse ones — informs how many Engram layers to place.
> **Source:** arXiv:2601.21204; arXiv:2508.18756 (UltraMemV2) · **Sweep:** `slm-architecture-2026-07`

**Cited KB notes:** [[ultramemv2-memory-networks-scaling-to-120b-parameters-with-superior-long]]

## Related
- [[deepseekmoe-towards-ultimate-expert-specialization-in-mixture-of-experts|DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models]] — Both argue the total-vs-active tradeoff; DeepSeekMoE says MoE collapses sub-600M, the latter that scaling embeddings beats scaling experts
- [[scaling-laws-with-vocabulary-larger-models-deserve-larger-vocabularies|Scaling Laws with Vocabulary: Larger Models Deserve Larger Vocabularies]] — both address param allocation between embeddings/vocab and the transformer body; disagree on whether scaling embeddings pays off
- [[memory-layers-at-scale|Memory Layers at Scale]] — Both scale explicit embedding/lookup memory as a sparsity axis; parallel lineage entries to Memory Layers' product-key result
- [[gemma-3-technical-report|Gemma 3 Technical Report]] — Gemma3-270M spends ~63% of params on 256K-vocab embeddings; this paper argues scaling embeddings beats experts — corroborating allocation

[[Home]]
