---
kb_id: "arxiv:2603.17946"
type: "paper"
title: "CARE: Covariance-Aware and Rank-Enhanced Decomposition for Enabling Multi-Head Latent Attention"
arxiv_id: "2603.17946"
doi: null
hf_repo: null
year: 2026
topics: ["mla-upcycling-bespoke-tokenizer"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["CARE: Covariance-Aware and Rank-Enhanced Decomposition for Enabling Multi-Head Latent Attention", "arXiv:2603.17946", "arxiv:2603.17946"]
tags: ["paper", "topic/mla-upcycling-bespoke-tokenizer"]
---
# CARE: Covariance-Aware and Rank-Enhanced Decomposition for Enabling Multi-Head Latent Attention

[arXiv](https://arxiv.org/abs/2603.17946)
**Topics:** [[mla-upcycling-bespoke-tokenizer]]

> [!abstract]
> Converting pretrained attention modules such as grouped-query attention (GQA) into multi-head latent attention (MLA) can improve expressivity without increasing KV-cache cost, making it attractive for efficient inference. However, many practical conversion baselines rely on weight-only low-rank approximations (e.g., SVD-style initializations) and uniform rank allocation. They focus on minimizing t …

## Claims

> [!note] CLAIM — mla-upcycling-bespoke-tokenizer
> The teacher-free conversion line keeps improving in 2026 but has no sub-1B evidence: CARE (covariance-aware, rank-enhanced decomposition + brief post-SVD 'healing' fine-tune, no teacher) reduces one-shot perplexity up to 215x and improves mean accuracy up to 1.70x vs prior SVD-init conversion at matched KV budgets — but its smallest tested model is Qwen3-4B (also Qwen3-30B-A3B, Llama-3.1-8B/70B). TransMLA v1 similarly bottoms out at Qwen2.5-7B and in v1 preserves (not compresses) cache size. Whether CARE-style init shrinks MHA2MLA's ~1.7-pt loss at 360M is untested.
>
> **Numbers:** CARE: up to 215x ppl reduction, 1.70x mean-accuracy gain vs SVD init at matched KV; smallest models: CARE 4B, TransMLA 7B
> **Relevance:** Sets the frontier: better teacher-free init exists but is unverified at the lab's scale — copying CARE at 600M would be an extrapolation, not a cited result.
> **Source:** arXiv:2603.17946 (CARE, 2026); arXiv:2502.07864v1 (TransMLA) · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[multi-head-low-rank-attention|Multi-Head Low-Rank Attention]] — Both are 2026 low-rank/MLA decomposition methods; CARE is covariance-aware SVD conversion, Multi-Head Low-Rank Attention is an adjacent…

[[Home]]
