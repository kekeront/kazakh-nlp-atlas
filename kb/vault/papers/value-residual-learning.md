---
kb_id: "arxiv:2410.17897"
type: "paper"
title: "Value Residual Learning"
arxiv_id: "2410.17897"
doi: null
hf_repo: null
year: 2024
topics: ["residual-stream-stability-qymyzlm-design"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Value Residual Learning", "arXiv:2410.17897", "arxiv:2410.17897"]
tags: ["paper", "topic/residual-stream-stability-qymyzlm-design"]
---
# Value Residual Learning

[arXiv](https://arxiv.org/abs/2410.17897)
**Topics:** [[residual-stream-stability-qymyzlm-design]]

> [!abstract]
> While Transformer models have achieved remarkable success in various domains, the effectiveness of information propagation through deep networks remains a critical challenge. Standard hidden state residuals often fail to adequately preserve initial token-level information in deeper layers. This paper introduces ResFormer, a novel architecture that enhances information flow by incorporating value r …

## Claims

> [!note] CLAIM — residual-stream-stability-qymyzlm-design
> [transferable-untested] Value Residual Learning (ResFormer): adding a residual from layer-1 values to every layer's values (v_l = v_l + lambda_l * v_1, learnable lambda) is the cheapest measured win at exactly our scale: at 468M params / 20B tokens it matches vanilla Transformer val loss with 16.11% fewer params or 20.3% less data, +1.7pt average downstream, with zero FLOP/memory overhead (only per-layer scalars). Validated up to 1.6B/200B tokens. SVFormer variant (all layers share layer-1 values, ~half KV cache) costs +12.2% params to match loss and underperforms at 2K context — skip SVFormer, keep ResFormer.
>
> **Numbers:** 82M-468M @ 20B tok SlimPajama; iso-loss with -16.11% params or -20.3% data at 468M; +1.7pt avg downstream; largest scale 1.6B/200B tok; SVFormer +12.2% params iso-loss, worse at 2,048 ctx, better at 64,000 ctx
> **Relevance:** 468M/20B-token is the closest published match to QymyzLM's 500M/10B regime of any residual innovation. Zero overhead means it fits T4 fp16 with no memory cost, unlike HC/mHC. ~10 lines of code. Verdict: worth it at 500M/10B — include, ablate at proxy scale.
> **Source:** arXiv:2410.17897 (ACL 2025 long, HTML full text fetched 2026-07-04) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[a-systematic-study-of-cross-layer-kv-sharing-for-efficient-llm-inference|A Systematic Study of Cross-Layer KV Sharing for Efficient LLM Inference]] — ResFormer's SVFormer shares layer-1 values across layers ~halving KV — same family as cross-layer KV sharing

[[Home]]
