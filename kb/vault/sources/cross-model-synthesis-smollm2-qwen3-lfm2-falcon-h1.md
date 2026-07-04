---
kb_id: "title:cross model synthesis smollm2 qwen3 lfm2 falcon h1 mobilellm cards papers cited above"
type: "source"
title: "cross-model synthesis: SmolLM2/Qwen3/LFM2/Falcon-H1/MobileLLM cards &…"
doi: null
hf_repo: null
year: null
topics: ["sota-slm"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:cross model synthesis smollm2 qwen3 lfm2 falcon h1 mobilellm cards papers cited above"]
tags: ["source", "topic/sota-slm"]
---
# cross-model synthesis: SmolLM2/Qwen3/LFM2/Falcon-H1/MobileLLM cards &…

**Topics:** [[sota-slm]]

## Source URLs
- cross-model synthesis: SmolLM2/Qwen3/LFM2/Falcon-H1/MobileLLM cards & papers cited above

## Findings

> [!note] CLAIM — sota-slm
> GQA head-group ratios cluster tightly across 2025-2026 sub-1B SOTA: SmolLM2-360M 15:5 (3:1), Qwen3-0.6B 16:8 (2:1), LFM2 16:8, Falcon-H1-0.5B 8:2 (4:1), MobileLLM-R1 24:6 (4:1). Deeper/thinner models tend to push to 4:1 to reclaim KV memory; head_dim is consistently 64.
>
> **Numbers:** GQA ratios 2:1-4:1; head_dim=64 universal at this scale
> **Relevance:** Gives a defensible design band: GQA 4:1 with head_dim 64 (or MLA) is the memory-lean choice; the current 2:1 plan is conservative and could go to 4:1 to fund more depth or Engram memory.
> **Source:** cross-model synthesis: SmolLM2/Qwen3/LFM2/Falcon-H1/MobileLLM cards & papers cited above · **Sweep:** `slm-architecture-2026-07`

[[Home]]
