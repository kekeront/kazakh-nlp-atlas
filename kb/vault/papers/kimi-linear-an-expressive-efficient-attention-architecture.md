---
kb_id: "arxiv:2510.26692"
type: "paper"
title: "Kimi Linear: An Expressive, Efficient Attention Architecture"
arxiv_id: "2510.26692"
doi: null
hf_repo: null
year: 2025
topics: ["mla-at-sub-1b-scale", "attention-kv-architecture-sub-1b"]
claims: 2
uncertain_claims: 2
verdicts: []
aliases: ["Kimi Linear: An Expressive, Efficient Attention Architecture", "arXiv:2510.26692", "arxiv:2510.26692"]
tags: ["paper", "topic/mla-at-sub-1b-scale", "topic/attention-kv-architecture-sub-1b"]
---
# Kimi Linear: An Expressive, Efficient Attention Architecture

[arXiv](https://arxiv.org/abs/2510.26692)
**Topics:** [[mla-at-sub-1b-scale]], [[attention-kv-architecture-sub-1b]]

> [!abstract]
> We introduce Kimi Linear, a hybrid linear attention architecture that, for the first time, outperforms full attention under fair comparisons across various scenarios -- including short-context, long-context, and reinforcement learning (RL) scaling regimes. At its core lies Kimi Delta Attention (KDA), an expressive linear attention module that extends Gated DeltaNet with a finer-grained gating mech …

## Claims

> [!warning] UNCERTAIN — mla-at-sub-1b-scale
> The smallest PURE-MLA model with a published long-context quality number is Kimi Linear's identical-recipe full-MLA baseline at 3B-activated/48B-total MoE: RULER-128K 81.3 (vs 84.3 for the KDA:MLA 3:1 hybrid; long-context avg 52.2 vs 54.5) on a 1.4T-token fair-comparison run. Pure MLA does not collapse at 128K — but 3B-active is 5-6x the lab's scale and it is MoE, not dense.
>
> **Numbers:** MLA baseline RULER-128K = 81.3; Kimi Linear = 84.3 with 3.98x speedup; long-ctx avg (to 128K): MLA 52.2, KDA-hybrid 54.5, GDN-H 51.2; fair run 1.4T tokens, 48B total/3B active
> **Relevance:** Sets the smallest scale at which the rank-512-class latent is PROVEN to hold long-context retrieval: 3B-active. Everything below is extrapolation — this is the floor of the evidence, not proof at 500M.
> **Source:** arXiv 2510.26692 (abstract + secondary: themoonlight.io review, jianyuh.github.io KDA analysis); Kimi Linear hybrid 84.3 RULER-128K confirmed in github.com/MoonshotAI/Kimi-Linear README · **Sweep:** `mla-sub1b-2026-07`

> [!warning] UNCERTAIN — attention-kv-architecture-sub-1b
> [transferable-untested] Production hybrids converged on ~25% full/gated attention in 2025-2026: Qwen3-Next-80B-A3B uses 75% Gated DeltaNet layers / 25% gated-attention layers (official Qwen statement: 3:1 'consistently outperforms any monolithic architecture'), with head_dim raised 128→256 in the attention layers and sigmoid output gating; Kimi Linear (48B total / 3B active) uses 3:1 KDA:MLA, reports up to 75% KV cache reduction and up to 6x decoding throughput at 1M context, beating full-MLA across evaluated tasks (extends KB's RULER node). Research floor from KB stands at ~7-8% attention layers (Empirical Mamba study, Nemotron-H).
>
> **Numbers:** Qwen3-Next: 75%/25% GDN:gated-attn, attn head_dim 256; Kimi Linear: 3:1 KDA:MLA, -75% KV, 6x decode@1M; research floor 7-8% attention
> **Relevance:** If a hybrid v2 is ever built, the ratio prior is 25% full attention (production) with floor ~8% (research); exact Qwen3-Next layer counts (36+12 of 48) not primary-verified.
> **Source:** qwen.ai blog (Qwen3-Next-80B-A3B-Base) + arXiv:2510.26692 (abstract) + KB nodes arXiv:2406.07887, 2504.03624 · **Sweep:** `slm-arch-for-kazakh`

**Cited KB notes:** [[an-empirical-study-of-mamba-based-language-models]]

## Related
- [[native-sparse-attention-hardware-aligned-and-natively-trainable-sparse-attention|Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention]] — Both natively-trainable efficient-attention architectures validated at scale; NSA's block-sparse vs Kimi Linear's linear attention
- [[gated-delta-networks-improving-mamba2-with-delta-rule|Gated Delta Networks: Improving Mamba2 with Delta Rule]] — Kimi Linear's 3:1 hybrid pairs full-MLA with KDA, a gated-delta-rule linear layer from this Gated DeltaNet line
- [[zebra-llama-towards-extremely-efficient-hybrid-models|Zebra-Llama: Towards Extremely Efficient Hybrid Models]] — Both hybridize attention with linear layers; Kimi Linear reports full-MLA beats its own hybrid on RULER-128K, Zebra collapses
- [[empirical-this-session-crossover-py-fp16-b-1-d-768|Empirical, this session: crossover.py (fp16, B=1, d=768)]] — Refutes Kimi Linear's linear-attn speed premise on SM75: its KDA only beats SDPA at T~12-16K, far above CPT ctx 1024-4096

[[Home]]
