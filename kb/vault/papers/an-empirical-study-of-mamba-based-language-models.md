---
kb_id: "arxiv:2406.07887"
type: "paper"
title: "An Empirical Study of Mamba-based Language Models"
arxiv_id: "2406.07887"
doi: null
hf_repo: null
year: 2024
topics: ["hybrid-efficiency-efficient-attention-se"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["An Empirical Study of Mamba-based Language Models", "arXiv:2406.07887", "arxiv:2406.07887"]
tags: ["paper", "topic/hybrid-efficiency-efficient-attention-se"]
---
# An Empirical Study of Mamba-based Language Models

[arXiv](https://arxiv.org/abs/2406.07887)
**Topics:** [[hybrid-efficiency-efficient-attention-se]]

> [!abstract]
> Selective state-space models (SSMs) like Mamba overcome some of the shortcomings of Transformers, such as quadratic computational complexity with sequence length and large inference-time memory requirements from the key-value cache. Moreover, recent studies have shown that SSMs can match or exceed the language modeling capabilities of Transformers, making them an attractive alternative. In a contr …

## Claims

> [!note] CLAIM — hybrid-efficiency-efficient-attention-se
> Pure Mamba/Mamba-2 models trail Transformers by ~15 points on 5-shot MMLU (recall/in-context tasks) even after 1.1T tokens, because SSMs must compress history into a fixed-size state. Adding only ~7-8% self-attention layers, evenly dispersed, closes AND exceeds the Transformer baseline across 12 tasks - attention layers absorb the 'gather-and-aggregate' recall operations.
>
> **Numbers:** ~15-pt 5-shot MMLU gap for pure Mamba vs Transformer @1.1T tokens; fixed with ~7-8% attention layers
> **Relevance:** Decisive for a KazMMLU-primary model: do NOT go pure-SSM or ultra-Mamba-heavy (Granite 9:1). Since the primary benchmark is knowledge/recall, keep attention share generous (LFM2's ~37%, or Nemotron's floor of ~8% only if maximizing throughput).
> **Source:** arXiv:2406.07887 (Empirical Study of Mamba LMs); arXiv:2510.26912; arXiv:2504.18574 (Gather-and-Aggregate) · **Sweep:** `slm-architecture-2026-07`

## Related
- [[hymba-a-hybrid-head-architecture-for-small-language-models|Hymba: A Hybrid-head Architecture for Small Language Models]] — Mamba study says ~7-8% attention layers recover recall; Hymba operationalizes this as a parallel hybrid-head SLM
- [[gated-delta-networks-improving-mamba2-with-delta-rule|Gated Delta Networks: Improving Mamba2 with Delta Rule]] — GDN improves Mamba2 with the delta rule; the empirical Mamba study is the from-scratch SSM baseline it beats at 1.3B
- [[model-card|model card +]] — Granite-4-H-350M is a 7:1 Mamba2:attention hybrid; empirical Mamba study is its architectural lineage and closest same-family baseline
- [[empirical-this-session-tmp-claude-1000-home-altairzhambyl-69058ff0|Empirical, this session: /tmp/claude-1000/-home-altairzhambyl-projects…]] — fla-Triton Mamba2 runs fwd+bwd on SM75; adds a hardware-gate datapoint to this paper's Mamba LM empirics

[[Home]]
