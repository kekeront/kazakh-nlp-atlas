---
kb_id: "arxiv:2402.14905"
type: "paper"
title: "MobileLLM: Optimizing Sub-billion Parameter Language Models for On-Device Use Cases"
arxiv_id: "2402.14905"
doi: null
hf_repo: null
year: 2024
topics: ["sota-slm"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["MobileLLM: Optimizing Sub-billion Parameter Language Models for On-Device Use Cases", "arXiv:2402.14905", "arxiv:2402.14905"]
tags: ["paper", "topic/sota-slm"]
---
# MobileLLM: Optimizing Sub-billion Parameter Language Models for On-Device Use Cases

[arXiv](https://arxiv.org/abs/2402.14905)
**Topics:** [[sota-slm]]

> [!abstract]
> This paper addresses the growing need for efficient large language models (LLMs) on mobile devices, driven by increasing cloud costs and latency concerns. We focus on designing top-quality LLMs with fewer than a billion parameters, a practical choice for mobile deployment. Contrary to prevailing belief emphasizing the pivotal role of data and parameter quantity in determining model quality, our in …

## Claims

> [!note] CLAIM — sota-slm
> MobileLLM's founding result: at sub-1B scale, DEPTH beats WIDTH — 30-42 layer models significantly outperform 12-layer models at equal ~125M params — and embedding sharing (tie input=output) plus GQA and SwiGLU give +2.7%/+4.3% accuracy at 125M/350M over prior SOTA. Contradicts the 'data/params are all that matter' view for tiny models.
>
> **Numbers:** 30-42L >> 12L at 125M; +2.7%/+4.3% at 125M/350M vs SOTA
> **Relevance:** Core design law for the Kazakh SLM: prefer ~30-40 layers at moderate d_model (~1024-1280) over a shallow wide net. Tie embeddings. This is the highest-confidence architecture recommendation in the sub-1B literature.
> **Source:** arXiv 2402.14905 (MobileLLM); ar5iv/aimodels summaries · **Sweep:** `slm-architecture-2026-07`

## Related
- [[the-curse-of-depth-in-large-language-models|The Curse of Depth in Large Language Models]] — Curse of Depth warns Pre-LN deep layers underperform — tension with MobileLLM's depth-over-width thesis
- [[mobilellm-r1-exploring-the-limits-of-sub-billion-language-model-reasoners-with|MobileLLM-R1: Exploring the Limits of Sub-Billion Language Model Reasoners with Open Train…]] — Same Meta lineage that founded deep-narrow MobileLLM shipped a shallow-wide 360M in R1 — reversed shape choice

[[Home]]
