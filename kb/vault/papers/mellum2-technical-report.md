---
kb_id: "arxiv:2605.31268"
type: "paper"
title: "Mellum2 Technical Report"
arxiv_id: "2605.31268"
doi: null
hf_repo: null
year: 2026
topics: ["attention-kv-architecture-sub-1b"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Mellum2 Technical Report", "arXiv:2605.31268", "arxiv:2605.31268"]
tags: ["paper", "topic/attention-kv-architecture-sub-1b"]
---
# Mellum2 Technical Report

[arXiv](https://arxiv.org/abs/2605.31268)
**Topics:** [[attention-kv-architecture-sub-1b]]

> [!abstract]
> We present Mellum 2, an open-weight 12B-parameter Mixture-of-Experts (MoE) language model with 2.5B active parameters per token. Mellum 2 is a general-purpose language model specialized in software engineering, spanning code generation and editing, debugging, multi-step reasoning, tool use and function calling, agentic coding, and conversational programming assistance, and it is the successor to t …

## Claims

> [!note] CLAIM — attention-kv-architecture-sub-1b
> [transferable-untested] 2026 production ablation corroborates the SWA+GQA sweet spot at fixed inference budget: Mellum-2 (JetBrains, 12B MoE / 2.5B active, 28L, d2304) selected by ablation a 3:1 SWA pattern (3 of every 4 layers sliding window 1024, 1 full attention), window 1024 outperforming 512 on quality; GQA with 4 KV heads was the optimum — 8 KV heads 'caused significant throughput degradation' and 2 KV heads 'yielded insufficient quality on evaluation benchmarks'; plus QK-Norm. No numeric quality deltas published for the ablations.
>
> **Numbers:** 3:1 SWA, window 1024 > 512; GQA-4 optimal (8 too slow, 2 too weak); 12B MoE/2.5B active, 28 layers
> **Relevance:** Independent 2026 evidence against GQA-2 (quality floor) and for window 1024 — refines the lab's from-scratch GQA choice; scale caveat: 2.5B active, code-domain model.
> **Source:** arXiv:2605.31268 (Mellum 2 technical report, fetched) · **Sweep:** `slm-arch-for-kazakh`

[[Home]]
