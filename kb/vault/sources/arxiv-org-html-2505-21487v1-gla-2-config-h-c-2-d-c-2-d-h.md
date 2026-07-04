---
kb_id: "title:arxiv org html 2505 21487v1 gla 2 config h c 2 d c 2 d h per latent head d r 32 tp sharding analysis"
type: "source"
title: "arxiv.org/html/2505.21487v1 (GLA-2 config: h_c=2, d_c=2*d_h per latent…"
doi: null
hf_repo: null
year: null
topics: ["gla-2-gta-arxiv-2505-21487-zadouri-strau"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:arxiv org html 2505 21487v1 gla 2 config h c 2 d c 2 d h per latent head d r 32 tp sharding analysis"]
tags: ["source", "topic/gla-2-gta-arxiv-2505-21487-zadouri-strau"]
---
# arxiv.org/html/2505.21487v1 (GLA-2 config: h_c=2, d_c=2*d_h per latent…

**Topics:** [[gla-2-gta-arxiv-2505-21487-zadouri-strau]]

## Source URLs
- arxiv.org/html/2505.21487v1 (GLA-2 config: h_c=2, d_c=2*d_h per latent head, d_R=32
- TP sharding analysis)

## Findings

> [!note] CLAIM — gla-2-gta-arxiv-2505-21487-zadouri-strau
> GLA-2's cache advantage over MLA exists only per-device under tensor parallelism (TP>=2): total unsharded cache is the same as MLA (2 latent heads x 2*d_h = 4*d_h, decoupled RoPE d_R=32 default; GLA 'halves the cache footprint per device when TP>=2'). For single-GPU/edge serving of a <=600M model — the lab's regime — GLA-2 offers NO KV-cache saving over plain MLA; its raison d'etre does not apply.
>
> **Numbers:** GLA-2: h_c=2 latent heads x 2*d_h each = 4*d_h total (= MLA's cache); benefit = 2x per-device only at TP>=2; rope dim 32
> **Relevance:** Removes the last architectural argument for GLA-2 in this project: a 500-600M Kazakh model is served on one device, where MLA already delivers the identical cache footprint with universal stack support.
> **Source:** arxiv.org/html/2505.21487v1 (GLA-2 config: h_c=2, d_c=2*d_h per latent head, d_R=32; TP sharding analysis) · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[arithmetic-from-verified-configs-deepseek-v2-lite-minicpm3|Arithmetic from verified configs (DeepSeek-V2-Lite, MiniCPM3, Qwen3-0.…]] — TP>=2-only per-device saving feeds lab KV menu; at TP=1 GLA-2 collapses to plain MLA's cache

[[Home]]
