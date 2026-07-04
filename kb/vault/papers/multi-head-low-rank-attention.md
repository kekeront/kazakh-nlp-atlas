---
kb_id: "arxiv:2603.02188"
type: "paper"
title: "Multi-Head Low-Rank Attention"
arxiv_id: "2603.02188"
doi: null
hf_repo: null
year: 2026
topics: ["gla-2-gta-arxiv-2505-21487-zadouri-strau"]
claims: 1
uncertain_claims: 1
verdicts: []
aliases: ["Multi-Head Low-Rank Attention", "arXiv:2603.02188", "arxiv:2603.02188"]
tags: ["paper", "topic/gla-2-gta-arxiv-2505-21487-zadouri-strau"]
---
# Multi-Head Low-Rank Attention

[arXiv](https://arxiv.org/abs/2603.02188)
**Topics:** [[gla-2-gta-arxiv-2505-21487-zadouri-strau]]

> [!abstract]
> Long-context inference in large language models is bottlenecked by Key--Value (KV) cache loading during the decoding stage, where the sequential nature of generation requires repeatedly transferring the KV cache from off-chip High-Bandwidth Memory (HBM) to on-chip Static Random-Access Memory (SRAM) at each step. While Multi-Head Latent Attention (MLA) significantly reduces the total KV cache size, …

## Claims

> [!warning] UNCERTAIN — gla-2-gta-arxiv-2505-21487-zadouri-strau
> MLRA paper acceptance venue: the first author refers to it as 'Liu et al., ICLR 2026' in the flash-attention issue, but the arXiv v1 page (2026-03-02) states no venue; acceptance not confirmed in a primary source.
>
> **Numbers:** arXiv v1 2026-03-02; venue claim unverified
> **Relevance:** Affects citation weight of the only independent GLA reproduction in the lab's survey paper.
> **Source:** github.com/Dao-AILab/flash-attention/issues/2372 (author's self-citation) vs arxiv.org/abs/2603.02188 (no venue listed) · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[deepseek-v2-a-strong-economical-and-efficient-mixture-of-experts-language-model|DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model]] — Multi-Head Low-Rank Attention is a successor to V2's MLA; competing low-rank KV-compression at equal cache
- [[reducing-transformer-key-value-cache-size-with-cross-layer-attention|Reducing Transformer Key-Value Cache Size with Cross-Layer Attention]] — Different KV-reduction mechanism: cross-layer sharing vs multi-head low-rank projection of K/V
- [[towards-economical-inference-enabling-deepseek-s-multi-head-latent-attention-in|Towards Economical Inference: Enabling DeepSeek's Multi-Head Latent Attention in Any Trans…]] — Both are low-rank KV-compression attention; MHLA is an alternative decomposition to MLA conversion
- [[eg-mla-embedding-gated-multi-head-latent-attention-for-scalable-and-efficient|EG-MLA: Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs]] — MLRA trains GLA-2 with added gating; EG-MLA gates MLA embeddings — same gate-the-latent-attention trend
- [[care-covariance-aware-and-rank-enhanced-decomposition-for-enabling-multi-head|CARE: Covariance-Aware and Rank-Enhanced Decomposition for Enabling Multi-Head Latent Atte…]] — Both are 2026 low-rank/MLA decomposition methods; CARE is covariance-aware SVD conversion, Multi-Head Low-Rank Attention is an adjacent…

[[Home]]
