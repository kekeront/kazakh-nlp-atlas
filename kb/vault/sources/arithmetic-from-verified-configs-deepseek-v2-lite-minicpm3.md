---
kb_id: "title:arithmetic from verified configs deepseek v2 lite minicpm3 qwen3 0 6b in kb kb cache math entry"
type: "source"
title: "Arithmetic from verified configs (DeepSeek-V2-Lite, MiniCPM3, Qwen3-0.…"
doi: null
hf_repo: null
year: null
topics: ["mla-at-sub-1b-scale"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:arithmetic from verified configs deepseek v2 lite minicpm3 qwen3 0 6b in kb kb cache math entry"]
tags: ["source", "topic/mla-at-sub-1b-scale"]
---
# Arithmetic from verified configs (DeepSeek-V2-Lite, MiniCPM3, Qwen3-0.…

**Topics:** [[mla-at-sub-1b-scale]]

## Source URLs
- Arithmetic from verified configs (DeepSeek-V2-Lite, MiniCPM3, Qwen3-0.6B in KB) + KB cache-math entry

## Findings

> [!note] CLAIM — mla-at-sub-1b-scale
> Cache-accounting nuance the design spec must not miss: MLA's cache advantage depends on the GQA baseline it replaces. Per layer per token, MLA caches (r_kv + rope_dim) elements TOTAL (shared across heads): 544 elem at r=512/rope32. Qwen3-0.6B-style GQA (8 KV heads x 128) caches 2,048 elem (K+V) -> MLA is 3.8x smaller; but an aggressive GQA with 2 KV heads x 64 caches 256 elem -> MLA r=512 is 2.1x LARGER. The KB's 'MLA r=256 = 480MB @32K, 4.7x smaller' math assumes the lab's GQA-2:1 with head_dim 128 (6 KV heads at d=1536) — valid, but only for that baseline.
>
> **Numbers:** MLA r512+rope32 = 544 elem/L/tok; GQA-8x128 = 2048; GQA-6x128 = 1536; GQA-2x64 = 256; MQA-1x64+CLA2 = 64 avg
> **Relevance:** Prevents a spec error: if the lab ever drops to head_dim-64 aggressive GQA or MQA+CLA2, MLA must go to r<=256 (with the MHA2MLA-documented 1-2pp risk) to still win on cache.
> **Source:** Arithmetic from verified configs (DeepSeek-V2-Lite, MiniCPM3, Qwen3-0.6B in KB) + KB cache-math entry · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[arxiv-org-html-2505-21487v1-gla-2-config-h-c-2-d-c-2-d-h|arxiv.org/html/2505.21487v1 (GLA-2 config: h_c=2, d_c=2*d_h per latent…]] — TP>=2-only per-device saving feeds lab KV menu; at TP=1 GLA-2 collapses to plain MLA's cache

[[Home]]
