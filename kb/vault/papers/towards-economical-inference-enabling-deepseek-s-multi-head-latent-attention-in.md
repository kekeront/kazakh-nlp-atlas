---
kb_id: "arxiv:2502.14837"
type: "paper"
title: "Towards Economical Inference: Enabling DeepSeek's Multi-Head Latent Attention in Any Transformer-based LLMs"
arxiv_id: "2502.14837"
doi: null
hf_repo: null
year: 2025
topics: ["mla-sub1b", "mla-vs-gqa-pretraining-cost-and-converge", "mla-at-sub-1b-scale", "mla-at-sub-1b", "mla-upcycling-at-1b-under-a-bespoke-toke"]
claims: 6
uncertain_claims: 0
verdicts: []
aliases: ["Towards Economical Inference: Enabling DeepSeek's Multi-Head Latent Attention in Any Transformer-based LLMs", "arXiv:2502.14837", "arxiv:2502.14837"]
tags: ["paper", "topic/mla-sub1b", "topic/mla-vs-gqa-pretraining-cost-and-converge", "topic/mla-at-sub-1b-scale", "topic/mla-at-sub-1b", "topic/mla-upcycling-at-1b-under-a-bespoke-toke"]
---
# Towards Economical Inference: Enabling DeepSeek's Multi-Head Latent Attention in Any Transformer-based LLMs

[arXiv](https://arxiv.org/abs/2502.14837)
**Topics:** [[mla-sub1b]], [[mla-vs-gqa-pretraining-cost-and-converge]], [[mla-at-sub-1b-scale]], [[mla-at-sub-1b]], [[mla-upcycling-at-1b-under-a-bespoke-toke]]

> [!abstract]
> Multi-head Latent Attention (MLA) is an innovative architecture proposed by DeepSeek, designed to ensure efficient and economical inference by significantly compressing the Key-Value (KV) cache into a latent vector. Compared to MLA, standard LLMs employing Multi-Head Attention (MHA) and its variants such as Grouped-Query Attention (GQA) exhibit significant cost disadvantages. Enabling well-trained …

## Claims

> [!note] CLAIM — mla-sub1b
> MLA works at 135M/360M via conversion (MHA2MLA): SmolLM-135M/360M (GQA) converted to MLA with joint-SVD init + partial-RoPE (keep r=d_h/16 dims by head-wise 2-norm), fine-tuned on 2.25B tokens = 0.38% (3.8 per mille) of the 600B pretraining data. SmolLM-360M: d_kv=32 -> KV cache -68.75%, avg score 47.91 vs 49.63 baseline (-1.72pp); d_kv=16 -> -81.25%, 46.94 (-2.69pp); d_kv=8 -> -87.5%, 45.04 (-4.59pp). SmolLM-135M: d_kv=32 -> -1.19pp; d_kv=16 -> -2.41pp; d_kv=8 -> -3.28pp. Public checkpoints exist for 135M/360M/1B7.
>
> **Numbers:** 360M: -68.75% cache/-1.72pp, -81.25%/-2.69pp, -87.5%/-4.59pp; 135M: -1.19/-2.41/-3.28pp; FT data 2.25B tokens (0.38%); partial-RoPE r=d_h/16
> **Relevance:** Pins the previously [UNVERIFIED] KB claim 'MLA works at sub-1B': yes, down to 135M — but aggressive ranks (8-16) cost 2.4-4.6pp, so a 600M Kazakh model should not go below rank ~256 (=d/6 at d=1536) without distillation.
> **Source:** arXiv 2502.14837 (MHA2MLA), HTML v1 results tables + github.com/JT-Ushio/MHA2MLA · **Sweep:** `mla-sub1b-2026-07`

> [!note] CLAIM — mla-vs-gqa-pretraining-cost-and-converge
> Escape hatch that decouples the decision: MHA2MLA converts pretrained GQA models to MLA with ~0.4% of original pretraining data. SmolLM-135M and SmolLM-360M (600B-token GQA models) were converted with 2.25B fine-tuning tokens: at d_kv=32 (-68.75% KV cache) avg score 43.06 vs 44.25 baseline (-1.19) for 135M and 47.91 vs 49.63 (-1.72) for 360M; at d_kv=8 (-87.5% KV) drops grow to -3.28/-4.59. SmolLM-1B7 (1T tokens): 6B ft tokens, -1.17 at d_kv=32.
>
> **Numbers:** 2.25B ft tokens (0.375% of 600B); 135M: 44.25->43.06 @ d_kv=32; 360M: 49.63->47.91 @ d_kv=32; 87.5% KV cut costs -3.28 to -4.59 avg pts
> **Relevance:** If the lab plays safe with GQA-4 from scratch (given <25B kk tokens), MLA-level cache can still be retrofitted later for ~2-3B tokens — the cache argument no longer forces a risky from-scratch bet.
> **Source:** arXiv 2502.14837 (MHA2MLA, HTML v1); checkpoints public at github.com/JT-Ushio/MHA2MLA · **Sweep:** `mla-sub1b-2026-07`

> [!note] CLAIM — mla-at-sub-1b-scale
> MHA2MLA shows an inverse-scale degradation trend for MLA conversion — smaller models lose MORE at equal KV compression — and ran its long-context eval (LongBench) ONLY on Llama2-7B; the sub-1B SmolLM conversions (135M/360M, fine-tuned at ctx 2048) got short commonsense evals only. At 7B, even modest latent compression costs measurable long-context quality.
>
> **Numbers:** At -81.25% KV (d_kv=16/32): 135M -2.24%, 360M -2.63%, 1B7 -1.43%, 7B -0.30%, 13B -0.23% avg commonsense drop. Llama2-7B LongBench (4K eval ctx): baseline 27.4; d_kv=64 -> 26.7 (-0.7); d_kv=32 -> 26.0 (-1.4); d_kv=16 -> 25.1 (-2.3); d_kv=64+Int4 HQQ = 92.19% cut -> 26.4 (-1.0)
> **Relevance:** Two warnings for a 500-600M Kazakh model: (a) whatever long-context cost MLA has, expect it amplified at small scale (the 7B LongBench drop of -0.7..-2.3 pts is the best-case anchor); (b) refines the KB's 'quality-neutral' MLA claim — conversions at sub-1B lose 2.2-2.6% even short-context.
> **Source:** arXiv 2502.14837 (html v2, Tables incl. LongBench Table 2) · **Sweep:** `mla-sub1b-2026-07`

> [!note] CLAIM — mla-at-sub-1b
> RESOLVED — MHA2MLA's d_kv is a PER-KV-HEAD unit, not a DeepSeek-style shared rank. The code builds ONE shared down-projection (structurally DeepSeek-style single latent per token) but sizes it as d_kv_mid = low_rank * num_key_value_heads (patching_model_load.py line 98, repo JT-Ushio/MHA2MLA). Paper notation confirms per-head SVD factors U_kv, V_kv ∈ R^{d_h × d_kv} (SVD_joint, Sec 3). So 'd_kv=32 on SmolLM-360M' = DeepSeek-equivalent shared kv_lora_rank of 32×5=160 (+5×8=40 rope dims → 200 cached elem/token/layer), exactly the parent's suspected ~160-200 elem. Arithmetic cross-check: per-head reading reproduces every published KV-reduction % (135M: 3×32+3×8=120/384=68.75% cut ✓; Llama2-7B d_kv=64: 32×64+32×16=2560/8192=68.75% ✓); shared reading reproduces none.
>
> **Numbers:** d_kv_mid = low_rank × n_kv; SmolLM-135M d_kv=8/16/32 → shared-equivalent 24/48/96; 360M → 40/80/160; 1B7 → 256/512/1024; Llama2-7B d_kv=16/32/64 → 512/1024/2048; rope dims cached separately per KV head (8/head SmolLM, 16/head Llama in main tables; released 135M cfg uses rope_dim_for_mla=4, low_rank=8)
> **Relevance:** Kills the misreading that 'rank 8-32 works at sub-1B'. MHA2MLA sweeps prove shared-equivalent latents of only 24-160 at 135M-360M scale — with real quality cost (see next finding) — and 512-2048 at 7B. The aggressive-option arithmetic must use total latent, not d_kv.
> **Source:** https://github.com/JT-Ushio/MHA2MLA (src/mha2mla/patching_model_load.py, src/mha2mla/arguments.py, cfgs/*.yml) + arXiv:2502.14837 Sec 3; SmolLM configs from HF (135M: 9h/3kv/d_h64; 360M: 15h/5kv/d_h64; 1.7B: 32h/32kv/d_h64) · **Sweep:** `mla-sub1b-2026-07`

> [!note] CLAIM — mla-at-sub-1b
> MHA2MLA conversion cost at SmolLM scale (fine-tune, NOT from scratch; 2.25B tokens for 135M/360M, 6B for 1B7/7B = 0.3-0.6% of pretrain data): 135M baseline 44.50 avg → d_kv=32: 43.06 (-1.19pp, -68.75% KV), d_kv=16: 41.84 (-2.41pp), d_kv=8: 40.97 (-3.28pp, -87.5% KV). 360M baseline 49.60 → 47.91/-1.72pp, 46.94/-2.69pp, 45.04/-4.59pp. 1B7 baseline 55.90 → 54.76/-1.17pp, 54.65/-1.28pp, 53.61/-2.32pp. The headline '92.19% KV cut, -0.5% LongBench' is Llama2-7B d_kv=64 COMBINED WITH Int4 HQQ quantization (26.9 vs 27.4 LongBench), not pure-MLA.
>
> **Numbers:** Drops at sub-1B: 1.2-4.6pp avg for 68.75-87.5% KV cuts; smaller models degrade more at equal d_kv; 92.19% figure = d_kv=64 + Int4HQQ
> **Relevance:** These drops are conversion-with-cheap-finetune numbers, so they lower-bound but do not measure from-scratch MLA quality at sub-1B. Also: pattern 'smaller model → bigger drop at same rank' warns against transplanting 7B ranks to 500M.
> **Source:** arXiv:2502.14837 Tables 1-2 (arxiv.org/html/2502.14837v1) · **Sweep:** `mla-sub1b-2026-07`

> [!note] CLAIM — mla-upcycling-at-1b-under-a-bespoke-toke
> Teacher-free MLA upcycling ABOVE 1.9x at sub-1B is published: MHA2MLA (ACL 2025) converts SmolLM-135M and SmolLM-360M (both GQA, i.e., same starting attention as the lab's plan) using plain full-parameter fine-tuning on 2.25B tokens (0.375% of the 600B pretraining corpus) with NO teacher and no distillation. SmolLM-360M (baseline avg ~49.63): d_kv=32 -> -68.75% KV (3.2x) avg 47.91 (-1.72); d_kv=16 -> -81.25% (5.3x) avg 46.94 (-2.69); d_kv=8 -> -87.5% (8x) avg 45.04 (-4.59). SmolLM-135M: 3.2x at -1.19. Method = joint SVD init of KV weights + partial-RoPE (head-wise 2-norm selection, r=d_h/16). Because no teacher is involved, a bespoke tokenizer is irrelevant — the only requirement is pretraining-distribution data, which the lab owns.
>
> **Numbers:** 360M: 3.2x/-1.72, 5.3x/-2.69, 8x/-4.59 avg pts; 135M: 3.2x/-1.19; 2.25B FT tokens = 3.75 per-mille of pretraining; Llama2-7B reference: -92.19% KV, -0.5% LongBench
> **Relevance:** Directly answers the research question: >1.9x MLA conversion at <=1B without any teacher exists — but it is lossy (~1.7 avg pts at 3.2x on a 360M model), whereas the lab needs every point to beat Qwen3-0.6B's 32.8% KazMMLU.
> **Source:** arXiv:2502.14837 (MHA2MLA, ACL 2025 Long), Tables for SmolLM-135M/360M; github.com/JT-Ushio/MHA2MLA (checkpoints d_kv=8/16/32/128 released) · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[deepseek-v2-a-strong-economical-and-efficient-mixture-of-experts-language-model|DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model]] — That work converts existing MHA models to V2-style MLA for economical inference — builds on this MLA formulation
- [[smollm2-when-smol-goes-big-data-centric-training-of-a-small-language-model|SmolLM2: When Smol Goes Big -- Data-Centric Training of a Small Language Model]] — MHA2MLA converts SmolLM-135M/360M/1B7 — these SmolLM2 GQA models are the from-scratch base it upcycles
- [[eg-mla-embedding-gated-multi-head-latent-attention-for-scalable-and-efficient|EG-MLA: Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs]] — Both target MLA at ~1B; EG-MLA builds MLA from scratch whereas MHA2MLA adapts pretrained GQA, trading data cost for accuracy
- [[kitty-accurate-and-efficient-2-bit-kv-cache-quantization-with-dynamic-channel|Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precis…]] — MHA2MLA's headline 92.19% cut stacks MLA with Int4 HQQ; Kitty is an orthogonal 2-bit KV-quant axis
- [[multi-head-low-rank-attention|Multi-Head Low-Rank Attention]] — Both are low-rank KV-compression attention; MHLA is an alternative decomposition to MLA conversion

[[Home]]
