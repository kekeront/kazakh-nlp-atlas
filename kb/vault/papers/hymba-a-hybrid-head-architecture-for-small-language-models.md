---
kb_id: "arxiv:2411.13676"
type: "paper"
title: "Hymba: A Hybrid-head Architecture for Small Language Models"
arxiv_id: "2411.13676"
doi: null
hf_repo: "nvidia/Hymba-1.5B-Base"
year: 2024
topics: ["kv-cache-architecture"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Hymba: A Hybrid-head Architecture for Small Language Models", "arXiv:2411.13676", "arxiv:2411.13676"]
tags: ["paper", "topic/kv-cache-architecture"]
---
# Hymba: A Hybrid-head Architecture for Small Language Models

[arXiv](https://arxiv.org/abs/2411.13676)
**Topics:** [[kv-cache-architecture]]

> [!abstract]
> We propose Hymba, a family of small language models featuring a hybrid-head parallel architecture that integrates transformer attention mechanisms with state space models (SSMs) for enhanced efficiency. Attention heads provide high-resolution recall, while SSM heads enable efficient context summarization. Additionally, we introduce learnable meta tokens that are prepended to prompts, storing criti …

## Claims

> [!note] CLAIM — kv-cache-architecture
> Hymba (NVIDIA, ICLR 2025) provides the only sub-1B ablation of pairwise cross-layer KV sharing on top of GQA: on a 300M-param model trained on 100B tokens, adding cross-layer KV sharing (citing CLA) to a GQA + SWA + 3-full-attention hybrid IMPROVED commonsense avg by +0.60 while costing -0.75 recall avg, with 1.15x throughput; saved KV params were reallocated (attn:Mamba 1:3.6 -> 1:5.23). Shipped Hymba-125M/350M/1.5B all use GQA + KV sharing: 1.5B config.json has 25 Q heads / 5 KV heads, kv_reuse_group = 14 groups (mostly consecutive pairs, one triple [16,17,18]), sliding_window 1024, global attention only at layers {0,15,31}.
>
> **Numbers:** Row 8 (GQA+SWA+full-attn): commonsense 44.56, recall 48.79, 2399.7 tok/s, cache 41.2 MB -> Row 9 (+cross-layer KV sharing): 45.16 (+0.60), 48.04 (-0.75), 2756.5 tok/s, 39.4 MB. Ablation scale: 300M params / 100B tokens. Shipped: 125M (8 heads/4 KV groups), 350M (12/4), 1.5B (25/5)
> **Relevance:** Closest scale to the lab's 600M target: KV sharing on GQA is accuracy-NEUTRAL-to-POSITIVE at 300M when most layers are sliding-window and freed KV params are reallocated — a recipe the lab can copy (its Kinetics finding already says cache, not FLOPs, is the sub-1B bottleneck). Caveat: hybrid Mamba+attention, sharing mostly across SWA layers; cache cut itself is small (4%) because SWA already bounds it — the win is params+throughput.
> **Source:** arXiv:2411.13676 (Hymba), Table 1 roadmap rows 8->9 + Table (Appendix) model configs, verified from arxiv.org/html/2411.13676v1; huggingface.co/nvidia/Hymba-1.5B-Base config.json · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[an-empirical-study-of-mamba-based-language-models|An Empirical Study of Mamba-based Language Models]] — Mamba study says ~7-8% attention layers recover recall; Hymba operationalizes this as a parallel hybrid-head SLM
- [[reducing-transformer-key-value-cache-size-with-cross-layer-attention|Reducing Transformer Key-Value Cache Size with Cross-Layer Attention]] — Hymba explicitly cites CLA and supplies the only sub-1B GQA pairwise cross-layer sharing ablation missing from CLA
- [[falcon-h1-a-family-of-hybrid-head-language-models-redefining-efficiency-and|Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance]] — Both hybrid-head SLM architectures pairing attention with a linear/Mamba path; Falcon-H1 is the later family
- [[lfm2-technical-report|LFM2 Technical Report]] — Rival small-LM hybrids: LFM2 conv+few-GQA vs Hymba parallel hybrid-head attention+SSM

[[Home]]
