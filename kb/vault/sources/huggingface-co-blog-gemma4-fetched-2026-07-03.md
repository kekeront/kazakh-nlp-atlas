---
kb_id: "hf:blog/gemma4"
type: "source"
title: "huggingface.co/blog/gemma4 (fetched 2026-07-03)"
doi: null
hf_repo: "blog/gemma4"
year: null
topics: ["kv-cache-architecture"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["hf:blog/gemma4"]
tags: ["source", "topic/kv-cache-architecture"]
---
# huggingface.co/blog/gemma4 (fetched 2026-07-03)

**Topics:** [[kv-cache-architecture]]

## Source URLs
- huggingface.co/blog/gemma4 (fetched 2026-07-03)
- corroborated by sglang issue #22277 (Gemma4 E4B num_kv_shared_layers > 0)

## Findings

> [!note] CLAIM — kv-cache-architecture
> Gemma 4 (released April 2, 2026) carries the same num_kv_shared_layers mechanism forward across its lineup (smallest tier E2B: 2.3B effective / 5.1B with embeddings, 128K ctx), again stating only 'minimal impact on quality' with no ablation numbers — two consecutive Google generations ship trailing-layer KV sharing without publishing the quality cost.
>
> **Numbers:** Sizes: E2B 2.3B eff/5.1B, E4B 4.5B eff/8B, 12B, 31B, 26B-A4B MoE; release 2026-04-02; quality ablation numbers published: none
> **Relevance:** Adoption evidence for the lab's fallback direction (trailing-layer sharing on GQA is the industry default at small scale, 2025-2026), but it cannot serve as quantitative support in the paper — the lab would be the first to publish the quality ablation at <=600M, which is itself a small paper-worthy artifact.
> **Source:** huggingface.co/blog/gemma4 (fetched 2026-07-03); corroborated by sglang issue #22277 (Gemma4 E4B num_kv_shared_layers > 0) · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[gemma-3-technical-report|Gemma 3 Technical Report]] — Direct Gemma lineage: Gemma 3 -> 3n -> 4, all shipping trailing KV sharing without published quality cost
- [[config-json-via-huggingface-co-unsloth-gemma-3n-e2b-mirror|config.json via huggingface.co/unsloth/gemma-3n-E2B (mirror]] — Gemma 4 carries the same num_kv_shared_layers mechanism forward, again with no ablation numbers

[[Home]]
