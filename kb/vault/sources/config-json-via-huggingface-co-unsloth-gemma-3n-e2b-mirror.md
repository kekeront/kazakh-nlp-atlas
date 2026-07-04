---
kb_id: "hf:unsloth/gemma-3n-e2b"
type: "source"
title: "config.json via huggingface.co/unsloth/gemma-3n-E2B (mirror"
doi: null
hf_repo: "unsloth/gemma-3n-E2B"
year: null
topics: ["kv-cache-architecture"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["hf:unsloth/gemma-3n-e2b"]
tags: ["source", "topic/kv-cache-architecture"]
---
# config.json via huggingface.co/unsloth/gemma-3n-E2B (mirror

**Topics:** [[kv-cache-architecture]]

## Source URLs
- config.json via huggingface.co/unsloth/gemma-3n-E2B (mirror
- google original is gated) + developers.googleblog.com/en/introducing-gemma-3n-developer-guide/

## Findings

> [!note] CLAIM — kv-cache-architecture
> Gemma 3n ships trailing-layer KV sharing ON GQA in production at effective-2B scale with NO public quality ablation: E2B text config has 30 layers, 8 Q heads / 2 KV heads (GQA 4:1), head_dim 256, num_kv_shared_layers=10 (last third of layers compute no KV; each reuses K/V from the last non-shared layer of the same attention type), sliding_window 512. Google's only published number for the feature is a 2x prefill speedup vs Gemma 3 4B plus an unquantified 'minimal impact on quality' claim.
>
> **Numbers:** num_hidden_layers=30, num_attention_heads=8, num_key_value_heads=2, num_kv_shared_layers=10, head_dim=256, hidden_size=2048, sliding_window=512; '2x improvement on prefill performance' vs Gemma 3 4B; zero quality-delta numbers published
> **Relevance:** Confirms the mission's premise: Gemma-3n-style trailing sharing is production-adopted on GQA but quality-unquantified by Google. The quantified stand-in is arXiv:2410.14442's pizza-bottom at 1.1B GQA: -0.55 avg downstream at 2x — the lab should cite that, not Gemma, for the quality price.
> **Source:** config.json via huggingface.co/unsloth/gemma-3n-E2B (mirror; google original is gated) + developers.googleblog.com/en/introducing-gemma-3n-developer-guide/ · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[a-systematic-study-of-cross-layer-kv-sharing-for-efficient-llm-inference|A Systematic Study of Cross-Layer KV Sharing for Efficient LLM Inference]] — Gemma-3n's trailing-layer reuse = study's pizza-bottom layout (-0.55), which it finds strictly better than CLA2
- [[decoder-hybrid-decoder-architecture-for-efficient-reasoning-with-long-generation|Decoder-Hybrid-Decoder Architecture for Efficient Reasoning with Long Generation]] — Same Gemma 3n shared-KV mechanism corroborated in the fetched E2B config.json
- [[huggingface-co-blog-gemma4-fetched-2026-07-03|huggingface.co/blog/gemma4 (fetched 2026-07-03)]] — Gemma 4 carries the same num_kv_shared_layers mechanism forward, again with no ablation numbers
- [[gemma-3-technical-report|Gemma 3 Technical Report]] — Gemma-3n's headline 2x prefill speedup is measured against Gemma 3 4B (same lineage, no cross-layer sharing)

[[Home]]
