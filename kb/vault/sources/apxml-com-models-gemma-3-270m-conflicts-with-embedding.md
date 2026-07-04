---
kb_id: "title:apxml com models gemma 3 270m conflicts with embedding param arithmetic"
type: "source"
title: "apxml.com/models/gemma-3-270m (conflicts with embedding-param arithmet…"
doi: null
hf_repo: null
year: null
topics: ["sota-slm"]
claims: 1
uncertain_claims: 1
verdicts: []
aliases: ["title:apxml com models gemma 3 270m conflicts with embedding param arithmetic"]
tags: ["source", "topic/sota-slm"]
---
# apxml.com/models/gemma-3-270m (conflicts with embedding-param arithmet…

**Topics:** [[sota-slm]]

## Source URLs
- apxml.com/models/gemma-3-270m (conflicts with embedding-param arithmetic)

## Findings

> [!warning] UNCERTAIN — sota-slm
> Gemma 3 270M's exact layer count / d_model are inconsistently reported (apxml lists 12 layers, d_model 1024, but 256K×1024=262M would exceed the stated 170M embedding budget, implying d_model≈640). Head config also unverified.
>
> **Numbers:** claimed 12L/d1024/16 heads; embedding math implies d~640
> **Relevance:** Minor — the load-bearing fact (embeddings dominate params) holds regardless; exact depth only matters if directly cloning Gemma 270M, which is not recommended.
> **Source:** apxml.com/models/gemma-3-270m (conflicts with embedding-param arithmetic) · **Sweep:** `slm-architecture-2026-07`

[[Home]]
