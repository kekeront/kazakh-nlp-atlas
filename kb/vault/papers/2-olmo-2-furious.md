---
kb_id: "arxiv:2501.00656"
type: "paper"
title: "2 OLMo 2 Furious"
arxiv_id: "2501.00656"
doi: null
hf_repo: null
year: 2024
topics: ["residual-stream-stability-qymyzlm-design", "small-lm-training-recipes-qymyzlm-design"]
claims: 3
uncertain_claims: 2
verdicts: []
aliases: ["2 OLMo 2 Furious", "arXiv:2501.00656", "arxiv:2501.00656"]
tags: ["paper", "topic/residual-stream-stability-qymyzlm-design", "topic/small-lm-training-recipes-qymyzlm-design"]
---
# 2 OLMo 2 Furious

[arXiv](https://arxiv.org/abs/2501.00656)
**Topics:** [[residual-stream-stability-qymyzlm-design]], [[small-lm-training-recipes-qymyzlm-design]]

> [!abstract]
> We present OLMo 2, the next generation of our fully open language models. OLMo 2 includes a family of dense autoregressive language models at 7B, 13B and 32B scales with fully released artifacts -- model weights, full training data, training code and recipes, training logs and thousands of intermediate checkpoints. In this work, we describe our modified model architecture and training recipe, focu …

## Claims

> [!note] CLAIM — residual-stream-stability-qymyzlm-design
> [transferable-untested] OLMo 2 stability kit: reordered norm (normalize sublayer OUTPUTS, post-attention/post-MLP inside residual) and QK-norm give NO stability improvement in isolation but TOGETHER reduce gradient-norm growth and spikiness; separately, loss/gradient spikes were traced to training batches containing long REPEATED n-gram sequences in the data. Combined kit in OLMo 2: RMSNorm + reordered norm + QK-norm + z-loss + init changes, validated at 7B/13B.
>
> **Numbers:** reordered-norm + QK-norm: joint (not individual) reduction of gradient L2 growth and spikes; spike batches show high prevalence of long repeated n-grams; validated 7B/13B
> **Relevance:** Two actionable items: (a) QK-norm + output-side norm is peri-norm-family — converges with the Peri-LN recommendation; (b) the repeated-n-gram spike cause directly targets the Kazakh data plan: web-crawled kk corpora (CulturaX/HPLT/mC4/MADLAD) are boilerplate-heavy, and the ~10B-token plan includes deliberate 2-3x upsampling — exact-substring dedup within documents is a cheap fp16-spike mitigation for BOTH from-scratch and QLoRA-CPT.
> **Source:** arXiv:2501.00656 (2 OLMo 2 Furious, COLM 2025; search-verified 2026-07-04) · **Sweep:** `slm-arch-for-kazakh`

> [!warning] UNCERTAIN — small-lm-training-recipes-qymyzlm-design
> [transferable-untested] OLMo 2 stability stack (adopted after diagnosing loss spikes): (1) QK-norm — RMSNorm on query/key projections before attention; (2) z-loss regularizer 1e-4 * log^2(Z) where Z is the softmax denominator over output logits; (3) switch nonparametric LayerNorm -> RMSNorm and reorder norms; (4) improved init. High LR (3.0e-3) caused instability/loss spikes in their setting, motivating the stack. Matches DCLM's independent choice of qk-LayerNorm + z-loss 1e-4 and Qwen3/MobileLLM-R1's QK-norm — 4-way convergence across 2024-2025 open recipes.
>
> **Numbers:** z-loss coeff 1e-4; LR 3e-3 flagged unstable in OLMo2's config; QK-norm = RMSNorm on Q,K
> **Relevance:** fp16-only T4 training amplifies exactly the two failure modes these fix (attention-logit growth, output-logit divergence: overflow at fp16's 65504 max). QK-norm + z-loss 1e-4 should be non-negotiable in any from-scratch QymyzLM config; z-loss additionally keeps logits in fp16-safe range.
> **Source:** arXiv:2501.00656 (2 OLMo 2 Furious), Sec. on training stability (via search-verified summary of the paper) · **Sweep:** `slm-arch-for-kazakh`

> [!warning] UNCERTAIN — small-lm-training-recipes-qymyzlm-design
> [transferable-untested] fp16-only (pre-Ampere) training practice, synthesized from the verified stability stack (no single paper tests T4 specifically): dynamic loss scaling with fp32 master weights (standard AMP GradScaler), z-loss 1e-4 (bounds output logits well inside fp16 max 65504), QK-norm (bounds attention logits), RMSNorm and softmax computed in fp32, grad clip 1.0 (SmolLM3/OLMo2). AdamW eps 1e-8 is fine with fp32 optimizer states; never keep optimizer states in fp16. Flash-attention on T4 (SM75) is supported only by FlashAttention-1-era/xformers kernels, not FA2 — memory-efficient attention via PyTorch SDPA (efficient backend) is available.
>
> **Numbers:** z-loss 1e-4; grad clip 1.0; fp16 max 65504; FA2 requires SM80+, T4=SM75
> **Relevance:** The exact fp16 checklist the design spec needs; every element is individually sourced but the combined recipe on T4 for Kazakh is untested — pilot on the first 100M-token CPT run.
> **Source:** Synthesis of arXiv:2501.00656, 2406.11794, 2309.14322 + NVIDIA AMP documentation; SM75 FA2 exclusion is from flash-attention repo requirements (Ampere+) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[small-scale-proxies-for-large-scale-transformer-training-instabilities|Small-scale proxies for large-scale Transformer training instabilities]] — OLMo2 adopts this paper's qk-layernorm + z-loss stability pair as its production recipe
- [[peri-ln-revisiting-normalization-layer-in-the-transformer-architecture|Peri-LN: Revisiting Normalization Layer in the Transformer Architecture]] — OLMo2 reordered-norm and Peri-LN are the same normalize-sublayer-outputs family for residual-stream stability

[[Home]]
