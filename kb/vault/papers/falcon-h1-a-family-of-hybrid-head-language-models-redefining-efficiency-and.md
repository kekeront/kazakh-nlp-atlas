---
kb_id: "arxiv:2507.22448"
type: "paper"
title: "Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance"
arxiv_id: "2507.22448"
doi: null
hf_repo: "blog/tiiuae"
year: 2025
topics: ["sota-slm", "hybrid-efficient-attention-architectures"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance", "arXiv:2507.22448", "arxiv:2507.22448"]
tags: ["paper", "topic/sota-slm", "topic/hybrid-efficient-attention-architectures"]
---
# Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance

[arXiv](https://arxiv.org/abs/2507.22448)
**Topics:** [[sota-slm]], [[hybrid-efficient-attention-architectures]]

> [!abstract]
> In this report, we introduce Falcon-H1, a new series of large language models (LLMs) featuring hybrid architecture designs optimized for both high performance and efficiency across diverse use cases. Unlike earlier Falcon models built solely on Transformer or Mamba architectures, Falcon-H1 adopts a parallel hybrid approach that combines Transformer-based attention with State Space Models (SSMs), k …

## Claims

> [!note] CLAIM — sota-slm
> Falcon-H1-0.5B (0.52B): parallel-hybrid with BOTH attention and Mamba-2 in every layer — 36 layers, d_model 1024, 8 query / 2 KV attention heads + 24 Mamba-2 SSM heads (d_state 128, head dim 64), vocab 32,778, 16K trained context (256K max), 2.5T tokens. Leads sub-1B math/code (GSM8K 60.20, MATH-lvl5 15.18) and claims parity with 2024-era 7B models. Covers 18 languages but NONE are Turkic/Kazakh.
>
> **Numbers:** 0.52B: 36L, d1024, 8Q/2KV + 24 Mamba2, d_state128, vocab32778, 2.5T tok; GSM8K 60.2
> **Relevance:** Proves a very deep (36L), very thin (d1024) parallel-hybrid can top sub-1B reasoning on only 2.5T tokens. Its 18-language set excludes Turkic — a market gap the Kazakh paper fills. Its 8Q/2KV (GQA 4:1) plus SSM is an aggressive KV-saving template.
> **Source:** arXiv 2507.22448 (Falcon-H1) Table 1; huggingface.co/blog/tiiuae/falcon-h1 · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — hybrid-efficient-attention-architectures
> Falcon-H1-0.5B uses a PARALLEL hybrid block: attention and Mamba-2 run concurrently on the same input and their outputs are concatenated before projection, with channels split roughly SSM:Attention:MLP = 2:1:5. Exact 0.5B config: 36 layers, d_model=1024, Q/KV heads 8/2, 24 SSM heads, d_state=128, head_dim=64, 16K context, vocab 32,778, 2.5T tokens. Supports 18 languages but NOT Kazakh.
>
> **Numbers:** 36 layers, d=1024, attn 8/2 heads, 24 SSM heads, d_state=128, head_dim=64, ctx 16K, vocab 32,778, 2.5T tokens; channel ratio ~2:1:5
> **Relevance:** Alternative to sequential hybrids: parallel attention+SSM lets you tune attention/SSM channel budget independently. The compact vocab (32.7K) and 0.5B config is a concrete, sub-600M reference. Kazakh absence means a from-scratch Kazakh model has open room.
> **Source:** arXiv:2507.22448 (Falcon-H1 Technical Report), Table 1 · **Sweep:** `slm-architecture-2026-07`

## Related
- [[hymba-a-hybrid-head-architecture-for-small-language-models|Hymba: A Hybrid-head Architecture for Small Language Models]] — Both hybrid-head SLM architectures pairing attention with a linear/Mamba path; Falcon-H1 is the later family
- [[nemotron-h-a-family-of-accurate-and-efficient-hybrid-mamba-transformer-models|Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models]] — Falcon-H1 runs attention+Mamba-2 parallel per layer; Nemotron-H interleaves them sequentially
- [[ibm-announcement-marktechpost-2025-10-29|IBM announcement + MarkTechPost 2025-10-29]] — Both sub-1B Mamba-2/Transformer hybrids; Granite is mostly-Mamba+few-attn vs Falcon's every-layer parallel

[[Home]]
