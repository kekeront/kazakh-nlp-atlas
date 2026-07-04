---
kb_id: "arxiv:2405.12981"
type: "paper"
title: "Reducing Transformer Key-Value Cache Size with Cross-Layer Attention"
arxiv_id: "2405.12981"
doi: null
hf_repo: null
year: 2024
topics: ["hybrid-efficient-attention-architectures", "mla-at-sub-1b-scale", "kv-cache-architecture"]
claims: 5
uncertain_claims: 1
verdicts: []
aliases: ["Reducing Transformer Key-Value Cache Size with Cross-Layer Attention", "arXiv:2405.12981", "arxiv:2405.12981"]
tags: ["paper", "topic/hybrid-efficient-attention-architectures", "topic/mla-at-sub-1b-scale", "topic/kv-cache-architecture"]
---
# Reducing Transformer Key-Value Cache Size with Cross-Layer Attention

[arXiv](https://arxiv.org/abs/2405.12981)
**Topics:** [[hybrid-efficient-attention-architectures]], [[mla-at-sub-1b-scale]], [[kv-cache-architecture]]

> [!abstract]
> Key-value (KV) caching plays an essential role in accelerating decoding for transformer-based autoregressive large language models (LLMs). However, the amount of memory required to store the KV cache can become prohibitive at long sequence lengths and large batch sizes. Since the invention of the transformer, two of the most effective interventions discovered for reducing the size of the KV cache …

## Claims

> [!note] CLAIM — hybrid-efficient-attention-architectures
> Cross-Layer Attention (CLA) shares K/V across adjacent layers (only a subset of layers compute KV; others reuse the previous layer's), giving 2x KV reduction on top of MQA/GQA. At 1B scale H128-MQA-CLA2 costs only +0.04 validation perplexity; at 3B CLA2 actually beat the MQA baselines (9.34 vs 9.48-9.52 ppl).
>
> **Numbers:** CLA2 = share KV across 2 layers -> 2x KV cut; 1B: +0.04 ppl; 3B: 9.34 vs 9.52 ppl (better)
> **Relevance:** Orthogonal to sliding-window and GQA - stacks multiplicatively for KV savings. A near-free way to halve KV again on the global-attention layers of the Kazakh model, validated at the closest scale (1B).
> **Source:** arXiv:2405.12981 (Reducing Transformer KV-Cache Size with Cross-Layer Attention, NeurIPS 2024) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — mla-at-sub-1b-scale
> CLA (cross-layer KV sharing) exact 1B-scale numbers: models d_model=2048, 20 layers, head_dim 128, 16 Q heads. MQA baseline 10,240 B/token, val ppl 13.54; MQA-CLA2 (10 of 20 layers produce KV) 5,120 B/token, ppl 13.60 (+0.06); the iso-cache alternative H64-MQA (halved head dim) 5,120 B/token ppl 13.81 — CLA2 is Pareto-better by 0.21 ppl at equal cache. MHA reference 163,840 B/token, 13.15. Sharing factor sweep: CLA2 13.60, CLA3 13.77, CLA4 13.95 — only factor 2 is worth it. At 3B: H64-MQA-CLA2 12.99 vs H64-MQA 12.94 (+0.05 ppl) at half cache.
>
> **Numbers:** 1B: MQA 13.54@10240B -> CLA2 13.60@5120B; iso-cache H64-MQA 13.81; CLA3 13.77, CLA4 13.95; 3B: +0.05 ppl at 2x cut
> **Relevance:** CLA2 is a near-free 2x cache halving verified AT 1B dense scale — composable with the lab's GQA baseline with ~zero quality cost and far less engineering than MLA.
> **Source:** arXiv 2405.12981 (Reducing Transformer KV Cache Size with Cross-Layer Attention), HTML v1 tables · **Sweep:** `mla-sub1b-2026-07`

> [!note] CLAIM — kv-cache-architecture
> The CLA paper ITSELF contains a GQA+CLA2 ablation at 1B (missed by KB, which only pinned MQA rows): three GQA-CLA2 models trained on 30B SlimPajama tokens (GPT-NeoX BPE, fixed lr 3e-4, ppl on ~4M held-out tokens), tested at 1B ONLY (3B experiments are MQA/MHA only). Adding CLA2 to a fixed GQA config (halving KV layers 20->10) costs +0.12 ppl on GQA4 and +0.07 ppl on GQA2 — NOT the +0.04-0.06 the lab plan-B assumes (that figure is from the LR-tuned MQA-CLA2 section).
>
> **Numbers:** Baselines (20 KV layers): H128-MHA 13.15 (163,840 B/tok), H128-GQA4 13.36 (40,960), H128-GQA2 13.52 (20,480), H128-MQA 13.54 (10,240). CLA2 (10 KV layers): H256-GQA4-CLA2 13.38 (40,960), H128-GQA4-CLA2 13.48 (20,480), H128-GQA2-CLA2 13.59 (10,240); H256-MQA-CLA2 13.51 (10,240), H512-MQA-CLA2 13.49 (20,480)
> **Relevance:** Directly re-prices the lab's fallback 'GQA + CLA2 at +0.04-0.06 ppl': the only published GQA-CLA2 numbers at 1B say +0.07-0.12 ppl for the 2x cache cut. Also: at iso-cache 10,240 B/tok, GQA2-CLA2 (13.59) LOSES to plain MQA (13.54) and to H256-MQA-CLA2 (13.51) — the lab's exact planned combo is the weakest option at its footprint.
> **Source:** arXiv:2405.12981 (Brandon et al., NeurIPS 2024), Table 1 + Sec 3.1/3.2 'Ablation: GQA + CLA2'; verified from arxiv.org/html/2405.12981v1 · **Sweep:** `mla-sub1b-2026-07`

> [!warning] UNCERTAIN — kv-cache-architecture
> Internal contradiction in the CLA paper: its prose says 'only the GQA2-CLA2 configuration was able to achieve a perplexity better than the corresponding baseline model with the same KV cache footprint... the same (within 0.01 points) as our MQA-CLA2 model with the same footprint', but Table 1 numbers only support that sentence for GQA4-CLA2 (13.48 beats iso-footprint GQA2 13.52; within 0.01 of H512-MQA-CLA2 13.49), while GQA2-CLA2 (13.59) fails both tests (vs MQA 13.54, vs H256-MQA-CLA2 13.51). Almost certainly a naming typo — anyone citing the sentence without the table will draw the wrong conclusion about GQA2+CLA2.
>
> **Numbers:** Prose claims GQA2-CLA2; numbers support GQA4-CLA2: 13.48 vs baseline 13.52 (-0.04), |13.48-13.49|=0.01; GQA2-CLA2: 13.59 vs 13.54 (+0.05), |13.59-13.51|=0.08
> **Relevance:** The lab's plan-B ('GQA-2 + CLA2') matches the typo'd config name, not the config the numbers endorse. If plan-B keeps 2 KV heads + CLA2, published evidence says prefer either GQA4-CLA2 (at 2x that cache) or H256-MQA-CLA2 (same cache, -0.08 ppl better). Typo interpretation is mine, flagged uncertain; the numeric mismatch itself is verified.
> **Source:** arXiv:2405.12981, verbatim sentence extracted from arxiv.org/html/2405.12981v1 Sec 'Ablation: GQA + CLA2' vs Table 1 rows; footprint math verified (n_kv*d_head*2*2bytes*KV_layers) · **Sweep:** `mla-sub1b-2026-07`

> [!note] CLAIM — kv-cache-architecture
> CLA models have a higher optimal learning rate than non-CLA baselines, and the CLA paper's GQA-CLA2 rows were run at the UNTUNED fixed lr 3e-4 — so the +0.07/+0.12 ppl GQA-CLA2 costs are plausibly pessimistic. In the paper's LR-tuned 1B experiments, H128-MQA-CLA2's optimum was 2.25e-3 vs 1.5e-3 for the H128-MQA baseline (1.5x), which is where the KB's '+0.04 ppl' headline comes from.
>
> **Numbers:** Optimal LR: MQA-CLA2 2.25e-3 vs MQA 1.5e-3 at 1B; design-space table fixed at 3e-4; no LR-tuned GQA-CLA2 run exists
> **Relevance:** If the lab runs GQA+CLA2 at 600M, peak LR should be swept ~1-1.5x above the non-CLA baseline's optimum; the true GQA-CLA2 cost with tuned LR is unknown (gap the lab's ablation can close).
> **Source:** arXiv:2405.12981, learning-rate ablation section (verbatim: 'CLA models benefit from training with higher learning rates than comparable non-CLA models') · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[you-only-cache-once-decoder-decoder-architectures-for-language-models|You Only Cache Once: Decoder-Decoder Architectures for Language Models]] — Both reuse KV across depth; YOCO caches once globally for a decoder-decoder split, CLA shares pairwise between adjacent layers
- [[a-systematic-study-of-cross-layer-kv-sharing-for-efficient-llm-inference|A Systematic Study of Cross-Layer KV Sharing for Efficient LLM Inference]] — The Systematic Study of Cross-Layer KV Sharing generalizes and stress-tests CLA's adjacent-layer KV-reuse scheme
- [[multi-head-low-rank-attention|Multi-Head Low-Rank Attention]] — Different KV-reduction mechanism: cross-layer sharing vs multi-head low-rank projection of K/V
- [[hymba-a-hybrid-head-architecture-for-small-language-models|Hymba: A Hybrid-head Architecture for Small Language Models]] — Hymba explicitly cites CLA and supplies the only sub-1B GQA pairwise cross-layer sharing ablation missing from CLA

[[Home]]
