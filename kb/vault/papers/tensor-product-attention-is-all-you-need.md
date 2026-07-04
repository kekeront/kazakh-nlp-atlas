---
kb_id: "arxiv:2501.06425"
type: "paper"
title: "Tensor Product Attention Is All You Need"
arxiv_id: "2501.06425"
doi: null
hf_repo: null
year: 2025
topics: ["mla-at-sub-1b-scale", "mla-vs-gqa-convergence-cost"]
claims: 4
uncertain_claims: 0
verdicts: []
aliases: ["Tensor Product Attention Is All You Need", "arXiv:2501.06425", "arxiv:2501.06425"]
tags: ["paper", "topic/mla-at-sub-1b-scale", "topic/mla-vs-gqa-convergence-cost"]
---
# Tensor Product Attention Is All You Need

[arXiv](https://arxiv.org/abs/2501.06425)
**Topics:** [[mla-at-sub-1b-scale]], [[mla-vs-gqa-convergence-cost]]

> [!abstract]
> Scaling language models to handle longer input sequences typically necessitates large key-value (KV) caches, resulting in substantial memory overhead during inference. In this paper, we propose Tensor Product Attention (TPA), a novel attention mechanism that uses tensor decompositions to represent queries, keys, and values compactly, substantially shrinking the KV cache size at inference time. By …

## Claims

> [!note] CLAIM — mla-at-sub-1b-scale
> First from-scratch MLA-vs-GQA head-to-head inside the lab's d_model window: TPA/T6 paper pretrains iso-param models at 353M (24L, d_model=1024, head_dim=64) and 772M (36L, d_model=1280) on FineWeb-Edu (~49B tokens, nanoGPT recipe). Zero-shot 11-task avg (lm-eval): at 353M MLA 50.13 vs GQA(2 KV heads) 50.35 vs MHA 50.11 vs MQA 50.44 (MLA ~parity, slightly below GQA); at 772M MLA 53.32 BEATS GQA 52.30, MHA 52.52, MQA 52.13. MLA config used: kv latent d_c=512, q latent d'_c=1024, decoupled rope dim d_R=32, MLA head count raised to 23/34 for iso-params. Caveat: authors (competing method) note MLA converges slower with higher val loss at these scales.
>
> **Numbers:** 353M: MLA 50.13 / GQA 50.35 / MHA 50.11; 772M: MLA 53.32 / GQA 52.30 / MHA 52.52; d_c=512, d'_c=1024, d_R=32, head_dim 64; 24L/d1024 and 36L/d1280; ~49B tokens
> **Relevance:** Direct evidence at d_model 1024-1280 (lab target 1024-1536): MLA is quality-neutral at ~350M and +1.0pp over GQA at ~770M — MLA does not break at sub-1B, but the DeepSeek-scale superiority is not guaranteed either.
> **Source:** arXiv 2501.06425 (Tensor Product Attention Is All You Need), Tables 2-3 + Appendix H Tables 9-10 (PDF read directly) · **Sweep:** `mla-sub1b-2026-07`

> [!note] CLAIM — mla-at-sub-1b-scale
> Synthesis vs KB: the KB's verified 'MLA outperforms MHA/MQA/GQA' comes from DeepSeek-V2 ablations at large scale and does NOT transfer monotonically below 1B. Across all from-scratch evidence: 353M parity (TPA: MLA 50.13 vs GQA 50.35), 433M +0.4pp (GLA paper), 772M +1.0pp (TPA), 876M -0.2pp (GLA paper), 1B +1.1pp MC / -1.1 Wiki ppl (Youtu), 1.47B -1.1pp (GLA paper). Envelope: MLA quality is within about +/-1pp of GQA at 350M-1.5B — never catastrophic, never the clear DeepSeek-scale win. The KB's own small-scale entry (arXiv 2506.09342, 30-202M: r=d/2 -> +0.3% loss) is consistent with this envelope.
>
> **Numbers:** MLA-minus-GQA downstream: -0.22pp@353M, +0.4@433M, +1.0@772M, -0.2@876M, +1.1@1B, -1.1@1.47B
> **Relevance:** This is the verdict the mission asked for and the exact expected-effect-size table for powering the lab's own ablation (differences are sub-1pp — needs seeds/token-budget discipline to detect).
> **Source:** Cross-comparison of arXiv 2501.06425, 2505.21487, 2512.24618, 2506.09342 (all read this session or verified in KB) · **Sweep:** `mla-sub1b-2026-07`

**Cited KB notes:** [[latent-multi-head-attention-for-small-language-models]]

> [!note] CLAIM — mla-vs-gqa-convergence-cost
> The counter-evidence (TPA/ICML 2025) is real but weaker than the KB summary implies. Exact quote: 'Multi-Head Latent Attention (MLA) (blue curves) generally trains more slowly and yields higher validation losses.' This is FIGURE-level only (Figures 4/9) — the paper publishes NO numeric loss/ppl table. Its own downstream tables show MLA at parity or better: 0-shot 9-bench avg at 353M: MLA 50.13 vs GQA 50.35 vs MHA 50.11; at 773M: MLA 53.32 vs GQA 52.30 vs MHA 52.52 (MLA best non-TPA). Config caveats: GQA had only 2 KV heads (cache 256 elem/layer) while MLA used d_c=512 + rope 32 (544 elem, 2.1x GQA's cache); MLA was param-matched by inflating head count (h=23 at 353M vs MHA's 16); nanoGPT recipe, all sizes 50B tokens of FineWeb-Edu-100B.
>
> **Numbers:** 353M: d_model=1024, 24L, d_c=512, d'_c(q_lora)=1024, rope 32, d_h=64, h_MLA=23; max LR 3e-4, batch 480, 50B tokens, 8x A100. Downstream avg: MLA 50.13 / GQA-2kv 50.35 / MHA 50.11 (353M); MLA 53.32 / GQA 52.30 (773M)
> **Relevance:** This is the paper behind the lab's fear that MLA needs extra tokens at sub-1B. Verified: the slow-convergence claim exists but is curve-only, uses a cache-disadvantaged MLA config (d_c=8*d_h), and its own benchmarks contradict a quality deficit at 50B tokens. Do not let this alone flip the architecture to GQA.
> **Source:** arXiv 2501.06425 v4 PDF, Section 6 lines + Tables 2-3 + Appendix H.1 (Tables 9-10), read directly; extracted text tpa.txt (convergence quote at lines 808-812) · **Sweep:** `mla-sub1b-2026-07`

> [!note] CLAIM — mla-vs-gqa-convergence-cost
> No published wall-clock throughput or training-memory comparison of MLA vs GQA exists at sub-1B (or anywhere below production scale) as of 2026-07. All three head-to-head pretraining papers (TPA 2501.06425, GLA/GTA 2505.21487, latent-MHA-SLM 2506.09342) report inference metrics only; targeted searches for tokens/sec / wall-clock MLA-vs-GQA training benchmarks returned nothing. The only published compute accounting is TPA's symbolic Table 1: at d=2048, H=32, d_h=64, absorbed-form MLA attention arithmetic is M*H*(2*d_c+d_R) = 17408M FLOPs/token vs 4096M for MHA/GQA (4.25x); unabsorbed training form instead pays extra down/up projections (~5.0M vs 5.2M projection params at that scale, roughly parity).
>
> **Numbers:** MLA absorbed attention FLOPs 17408M vs GQA 4096M per token at d=2048/H=32 (4.25x); training-form projection FLOPs ~5.0e6 (MLA) vs 5.2e6 (GQA) per token at same scale; zero published tokens/sec or GB-of-optimizer-state numbers for either
> **Relevance:** The lab's open question #1 (wall-clock + training memory) is literally unmeasured in the literature — the lab must benchmark it itself on its A100/BF16 setup; a 1-2B-token measured comparison would be a small publishable contribution and takes <1 GPU-week at 500M.
> **Source:** arXiv 2501.06425 Table 1 / Appendix FLOPs derivations (lines 1955-1984 of extracted text); absence verified across arXiv 2505.21487 full text, 2506.09342, and web searches (July 2026) · **Sweep:** `mla-sub1b-2026-07`

**Cited KB notes:** [[hardware-efficient-attention-for-fast-decoding]]

## Related
- [[deepseek-v2-a-strong-economical-and-efficient-mixture-of-experts-language-model|DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model]] — TPA synthesis: DeepSeek-V2's MLA>MHA/MQA/GQA ablation does not transfer monotonically below 1B

[[Home]]
