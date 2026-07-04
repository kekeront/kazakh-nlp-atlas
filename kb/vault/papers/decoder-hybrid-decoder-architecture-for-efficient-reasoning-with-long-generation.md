---
kb_id: "arxiv:2507.06607"
type: "paper"
title: "Decoder-Hybrid-Decoder Architecture for Efficient Reasoning with Long Generation"
arxiv_id: "2507.06607"
doi: null
hf_repo: "blog/gemma4"
year: 2025
topics: ["mla-sub1b"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Decoder-Hybrid-Decoder Architecture for Efficient Reasoning with Long Generation", "arXiv:2507.06607", "arxiv:2507.06607"]
tags: ["paper", "topic/mla-sub1b"]
---
# Decoder-Hybrid-Decoder Architecture for Efficient Reasoning with Long Generation

[arXiv](https://arxiv.org/abs/2507.06607)
**Topics:** [[mla-sub1b]]

> [!abstract]
> Recent advances in language modeling have demonstrated the effectiveness of State Space Models (SSMs) for efficient sequence modeling. While hybrid architectures such as Samba and the decoder-decoder architecture, YOCO, have shown promising performance gains over Transformers, prior works have not investigated the efficiency potential of representation sharing between SSM layers. In this paper, we …

## Claims

> [!note] CLAIM — mla-sub1b
> Cross-layer KV sharing is shipped in production on-device models: Gemma 3n (E2B/E4B) uses num_kv_shared_layers=15 — the last 15 layers compute NO KV projections and reuse the KV of the last non-shared local/global layer of the same attention type (on top of Gemma-3-style 4-local(SWA):1-global pattern, 32K ctx). Per HF blog, Gemma 4 edge models retain shared KV cache + PLE. Phi-4-mini-flash-reasoning (3.8B, SambaY decoder-hybrid-decoder) applies the YOCO principle: a single full-attention layer's KV cache is shared by the whole cross-decoder via Gated Memory Units.
>
> **Numbers:** Gemma 3n: 15 trailing layers share KV, 4:1 local:global SWA, 32K ctx; Phi-4-mini-flash: 1 global-attention KV cache for entire cross-decoder, 3.8B params
> **Relevance:** Deployment argument: cross-layer sharing has mainline llama.cpp support precedent (gemma3n arch), whereas MLA GGUF still needs the ik_llama.cpp fork (KB fact) — matters for shipping a Kazakh on-device model.
> **Source:** HF transformers docs Gemma3nTextConfig (num_kv_shared_layers default 15); huggingface.co/blog/gemma4; arXiv 2507.06607 + Azure blog (Phi-4-mini-flash) · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[you-only-cache-once-decoder-decoder-architectures-for-language-models|You Only Cache Once: Decoder-Decoder Architectures for Language Models]] — Decoder-Hybrid-Decoder (SambaY) directly builds on YOCO's decoder-decoder single-global-KV design for long reasoning
- [[gemma-3-technical-report|Gemma 3 Technical Report]] — Gemma 3n's shared-KV (num_kv_shared_layers=15) is layered on top of Gemma-3's 5:1 local-SWA:global attention pattern
- [[config-json-via-huggingface-co-unsloth-gemma-3n-e2b-mirror|config.json via huggingface.co/unsloth/gemma-3n-E2B (mirror]] — Same Gemma 3n shared-KV mechanism corroborated in the fetched E2B config.json

[[Home]]
