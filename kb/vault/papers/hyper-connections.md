---
kb_id: "arxiv:2409.19606"
type: "paper"
title: "Hyper-Connections"
arxiv_id: "2409.19606"
doi: null
hf_repo: null
year: 2024
topics: ["residual-stream-stability-qymyzlm-design"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Hyper-Connections", "arXiv:2409.19606", "arxiv:2409.19606"]
tags: ["paper", "topic/residual-stream-stability-qymyzlm-design"]
---
# Hyper-Connections

[arXiv](https://arxiv.org/abs/2409.19606)
**Topics:** [[residual-stream-stability-qymyzlm-design]]

> [!abstract]
> We present hyper-connections, a simple yet effective method that can serve as an alternative to residual connections. This approach specifically addresses common drawbacks observed in residual connection variants, such as the seesaw effect between gradient vanishing and representation collapse. Theoretically, hyper-connections allow the network to adjust the strength of connections between feature …

## Claims

> [!note] CLAIM — residual-stream-stability-qymyzlm-design
> [transferable-untested] Original Hyper-Connections (DHC) do show real gains at 1B DENSE — the scale mHC never tested — but the training-memory cost kills it on T4: OLMo-1B-DHCx4 at 500B tokens improves eval loss 2.811->2.781 and downstream avg 62.5%->63.8% with only +0.033% params/+0.2% FLOPs, yet +26.1% training memory (41.11 -> 51.86 GB across 8 GPUs) from materializing the n=4-wide residual stream. DHC n=1 is WORSE than baseline. HC paper reports no loss spikes at 1B (baseline spiked); mHC's instability critique of raw HC applies at larger scales.
>
> **Numbers:** OLMo-1B 500B tok: baseline V2/V3 loss 2.811/2.544, downstream 62.5%; DHCx4 2.781/2.515, 63.8%; DHCx8 2.778/2.516, 62.8% (saturates); DHCx1 2.819 (worse); +0.000394B params (+0.033%), +0.200% FLOPs, +26.1% memory
> **Relevance:** T4x2 = 2x16GB fp16; a 4x-wide residual stream on top of activations + fp32 master weights + Adam states does not fit for a 500M from-scratch run without heavy activation checkpointing that T4 throughput can't absorb. Verdict: scale-only / hardware-gated — reject for QymyzLM v1.
> **Source:** arXiv:2409.19606 (Hyper-Connections, ICLR 2025, HTML v3 full text fetched 2026-07-04) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[mhc-manifold-constrained-hyper-connections|mHC: Manifold-Constrained Hyper-Connections]] — mHC is the manifold-constrained successor that critiques raw HC's instability at larger scales

[[Home]]
