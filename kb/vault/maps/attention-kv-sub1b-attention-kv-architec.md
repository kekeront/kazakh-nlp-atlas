---
type: "moc"
topic: "attention-kv-sub1b-attention-kv-architec"
nodes: 12
papers: 10
sources: 2
uncertain_claims: 8
tags: ["moc"]
---
# Topic: attention-kv-sub1b-attention-kv-architec

The sub-1B attention/KV frontier has three cheap, scale-independent wins that are well-established: QK-Norm as the fp16-stability consensus (2309.14322, now shipped in Qwen3/OLMo2/Gemma3/Mellum2), a headwise sigmoid SDPA gate that collapses attention-sink from ~47% to ~5% for ~1.6M params and <2% latency (2505.06708), and sliding-window attention at 3:1–5:1 with window 512–1024 for a pure KV win (Gemma3 cuts KV from ~60% to <15% at 32K; Gemma3-270M's SWA recipe caches ~108MB@32K vs Qwen3-0.6B's 3.75GB, ~35x). The contested question is MLA: the strongest from-scratch head-to-head (2505.21487, Dao group, 183M–1.47B on FineWeb-Edu) shows MLA matches or beats GQA-4 at ≤876M while caching less (kv_lora=4×d_h, rope_dim 32, no q-compression), but MLA LOSES 1.1pp to GQA-4 at 1.47B — so the sub-1B MLA advantage is real but does not extend up, and its GLA-2/GTA-4 variants actually win at 433M/876M. Pure-MLA long-context is only validated at 3B-active MoE (Kimi Linear, uncertain), and GDN/Mamba2 hybrids replicate quality gains at 340M–1.3B (GDN-H1 56.4 vs Transformer++ 52.25 avg; Granite-4-H-350M +1.2 MMLU over its transformer twin) but are kernel-blocked on the lab's T4 (SM75) since FlashAttention-2 requires SM80+ and Triton FLA kernels are unverified there. The dominant open question is that NO non-vanilla attention mechanism has ever been trained or ablated on Kazakh — SozKZ-600M and Sherkala-8B are both stock attention — making even a small GQA-vs-MLA-vs-gated ablation on 9–10B Kazakh tokens a first-on-Kazakh publishable result.

## Frontier highlights
- [[hardware-efficient-attention-for-fast-decoding|Hardware-Efficient Attention for Fast Decoding]] — From-scratch 183M-1.47B MLA/GLA/GTA vs GQA head-to-head; MLA wins sub-1B but loses at 1.47B; pins kv_lora=4xd_h recipe
- [[gated-attention-for-large-language-models-non-linearity-sparsity-and-attention|Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attentio…]] — Gated SDPA output (sink 47%->5%, ~0 cost) + the synthesis of which attention tricks pay off at 500M vs only at scale
- [[gemma-3-technical-report|Gemma 3 Technical Report]] — Gemma3-270M SWA recipe pinned from config: 15:3 local:global, window 512, KV ~108MB@32K vs 3.75GB (~35x)
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] — Only from-scratch Kazakh SLM: fully vanilla attention, 2K ctx, zero ablations — entire attention axis untested on Kazakh
- [[gated-delta-networks-improving-mamba2-with-delta-rule|Gated Delta Networks: Improving Mamba2 with Delta Rule]] — GDN hybrids beat Transformer++ at 1.3B on ppl/recall/throughput, but FLA kernels are T4-blocked
- [[github-com-dao-ailab-flash-attention-readme-issues-887-1608|github.com/Dao-AILab/flash-attention README + issues #887, #1608]] — Hardware gate: FA2 needs SM80+, T4=SM75; any FA2-throughput or FLA-hybrid claim does not transfer to free compute

## Papers (10)
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] (2026) — tokenizer-morphology
- [[mellum2-technical-report|Mellum2 Technical Report]] (2026) — attention-kv-sub1b-attention-kv-architec
- [[gemma-3-technical-report|Gemma 3 Technical Report]] (2025) — sota-slm
- [[gated-attention-for-large-language-models-non-linearity-sparsity-and-attention|Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free]] (2025) — attention-kv-sub1b-attention-kv-architec
- [[qwen3-technical-report|Qwen3 Technical Report]] (2025) — sota-slm
- [[hardware-efficient-attention-for-fast-decoding|Hardware-Efficient Attention for Fast Decoding]] (2025) — mla-sub1b
- [[kimi-linear-an-expressive-efficient-attention-architecture|Kimi Linear: An Expressive, Efficient Attention Architecture]] (2025) — mla-at-sub-1b-scale
- [[base-of-rope-bounds-context-length|Base of RoPE Bounds Context Length]] (2024) — attention-kv-sub1b-attention-kv-architec
- [[gated-delta-networks-improving-mamba2-with-delta-rule|Gated Delta Networks: Improving Mamba2 with Delta Rule]] (2024) — attention-kv-sub1b-attention-kv-architec
- [[small-scale-proxies-for-large-scale-transformer-training-instabilities|Small-scale proxies for large-scale Transformer training instabilities]] (2023) — attention-kv-sub1b-attention-kv-architec

## Sources & findings (2)
- [[model-card|model card +]] — [transferable-untested] Closest published same-data hybrid-vs-transformer head-to-head inside the lab's size class: IBM…
- [[github-com-dao-ailab-flash-attention-readme-issues-887-1608|github.com/Dao-AILab/flash-attention README + issues #887, #1608]] — [hardware fact, verified] FlashAttention-2 does NOT support Turing (SM75 = Kaggle T4): the official Dao-AILab repo state…

## Related topics
- [[residual-stream-stability-qymyzlm-design]] — 2 shared nodes
- [[small-lm-training-recipes-qymyzlm-design]] — 2 shared nodes
- [[sota-slm]] — 2 shared nodes
- [[training-recipes]] — 2 shared nodes

[[Home]]
