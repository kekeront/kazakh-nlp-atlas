---
kb_id: "arxiv:2508.18756"
type: "paper"
title: "UltraMemV2: Memory Networks Scaling to 120B Parameters with Superior Long-Context Learning"
arxiv_id: "2508.18756"
doi: null
hf_repo: null
year: 2025
topics: ["sparse-memory-2026-engram-lineage-beyond"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["UltraMemV2: Memory Networks Scaling to 120B Parameters with Superior Long-Context Learning", "arXiv:2508.18756", "arxiv:2508.18756"]
tags: ["paper", "topic/sparse-memory-2026-engram-lineage-beyond"]
---
# UltraMemV2: Memory Networks Scaling to 120B Parameters with Superior Long-Context Learning

[arXiv](https://arxiv.org/abs/2508.18756)
**Topics:** [[sparse-memory-2026-engram-lineage-beyond]]

> [!abstract]
> While Mixture of Experts (MoE) models achieve remarkable efficiency by activating only subsets of parameters, they suffer from high memory access costs during inference. Memory-layer architectures offer an appealing alternative with very few memory access, but previous attempts like UltraMem have only matched the performance of 2-expert MoE models, falling significantly short of state-of-the-art 8 …

## Claims

> [!note] CLAIM — sparse-memory-2026-engram-lineage-beyond
> [transferable-untested] UltraMemV2 smallest validated scale is 227M activated / 1.2B total (open-sourced config, plus 1B/7B), with a memory layer in EVERY transformer block (not 2-3 insertion sites), top-m 256-768 activated values, value-dim ratio Dp:Dv = 1:3 optimal, single linear projector values. Reaches parity with 8-expert MoE at matched compute+params and wins on memorization/ICL, but only after 1.6-3.9T pretraining tokens + 250-500B high-quality continued-training tokens.
>
> **Numbers:** 227M act / 1.2B total smallest; +1.6 long-context memorization, +6.2 multi-round memorization, +7.9 in-context learning vs 8-expert MoE; top-m 256 (120B) to 768 (60B); pretraining 1.6-3.9T tokens.
> **Relevance:** Key design insight transfers even if the training regime does not: 'activation density has greater impact than total sparse parameter count' — for QymyzLM this argues for FEWER slots read MORE densely (higher top-k / more heads) rather than a maximally large table, which conveniently also shrinks the total-footprint problem. The 1.6T+ token requirement makes the full per-block UltraMem recipe infeasible on 10B Kazakh tokens + T4x2.
> **Source:** arXiv:2508.18756 (HTML v1, fetched 2026-07-04) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[deepseekmoe-towards-ultimate-expert-specialization-in-mixture-of-experts|DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models]] — UltraMemV2 reaches parity with an 8-expert MoE at matched compute+params and wins on memorization/ICL
- [[conditional-memory-via-scalable-lookup-a-new-axis-of-sparsity-for-large|Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models]] — Both scale static memory tables to huge param counts; UltraMemV2 is an alternate memory-network architecture reaching 120B
- [[tensorizing-engram-sharing-latents-across-n-gram-embeddings-is-beneficial-in|Tensorizing Engram: Sharing Latents Across N-Gram Embeddings is Beneficial in LLMs]] — both scale/compress memory networks; UltraMemV2 learned-slot keyed to 120B, TN-gram CP-factorizes n-gram tables, neither morpheme

[[Home]]
