---
kb_id: "arxiv:2411.15242"
type: "paper"
title: "The Zamba2 Suite: Technical Report"
arxiv_id: "2411.15242"
doi: null
hf_repo: null
year: 2024
topics: ["hybrid-efficiency-efficient-attention-se"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["The Zamba2 Suite: Technical Report", "arXiv:2411.15242", "arxiv:2411.15242"]
tags: ["paper", "topic/hybrid-efficiency-efficient-attention-se"]
---
# The Zamba2 Suite: Technical Report

[arXiv](https://arxiv.org/abs/2411.15242)
**Topics:** [[hybrid-efficiency-efficient-attention-se]]

> [!abstract]
> In this technical report, we present the Zamba2 series -- a suite of 1.2B, 2.7B, and 7.4B parameter hybrid Mamba2-transformer models that achieve state of the art performance against the leading open-weights models of their class, while achieving substantial gains in inference latency, throughput, and memory efficiency. The Zamba2 series builds upon our initial work with Zamba1-7B, optimizing its …

## Claims

> [!note] CLAIM — hybrid-efficiency-efficient-attention-se
> Zamba2 shows an extreme KV-cache-saving hybrid: a Mamba-2 backbone with a SINGLE shared attention block (weights reused via LoRA) applied every ~6 Mamba-2 layers, giving ~6x KV-cache reduction vs a pure transformer while staying competitive with same-size transformers.
>
> **Numbers:** 1:6 attention:Mamba-2; shared-attention weights reused with LoRA; ~6x KV reduction; sizes 1.2B/2.7B/7.4B
> **Relevance:** Parameter-sharing trick (one attention block reused) is attractive at 500M where param budget is tight - but 1:6 attention is likely too sparse for KazMMLU; more useful as a KV-saving idea than a ratio to copy.
> **Source:** arXiv:2411.15242 (Zamba2 Suite Technical Report) · **Sweep:** `slm-architecture-2026-07`

## Related
- [[simple-and-scalable-strategies-to-continually-pre-train-large-language-models|Simple and Scalable Strategies to Continually Pre-train Large Language Models]] — Zamba2 adopts 60% replay in a 50B-token decay phase — high-dose instance of Ibrahim's replay finding

[[Home]]
