---
kb_id: "title:mdpi make 8 5 128 hf issai qolda"
type: "source"
title: "MDPI MAKE 8(5):128"
doi: null
hf_repo: null
year: null
topics: ["kazakh-turkic-nlp"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:mdpi make 8 5 128 hf issai qolda"]
tags: ["source", "topic/kazakh-turkic-nlp"]
---
# MDPI MAKE 8(5):128

**Topics:** [[kazakh-turkic-nlp]]

## Source URLs
- MDPI MAKE 8(5):128
- HF issai/Qolda

## Findings

> [!note] CLAIM — kazakh-turkic-nlp
> Qolda (ISSAI, Qwen3-4B base, 4.3B params) is the strongest recent Kazakh SLM data point above 1B: zero-shot ~60.37 avg across KazMMLU+KazCulture, rising to 76.00 with naive-RAG web search in reasoning mode. It is a Qwen3 ADAPTATION, not from-scratch, reinforcing that adapting a strong base + Kazakh data beats building from zero.
>
> **Numbers:** 4.3B params; zero-shot 60.37 -> 76.00 with web-search RAG
> **Relevance:** Two takeaways: (1) at 4B, adapting Qwen3 reaches ~60 zero-shot — adaptation scales cleanly, supporting a Qwen3-0.6B warm-start hedge for the 600M model; (2) retrieval/RAG adds ~+16pp, a cheap orthogonal booster the paper could add as an inference-time option without extra params.
> **Source:** MDPI MAKE 8(5):128; HF issai/Qolda · **Sweep:** `slm-architecture-2026-07`

## Related
- [[qwen3-technical-report|Qwen3 Technical Report]] — Qolda is a Qwen3-4B adaptation that beats its own backbone; Qwen3 is the base model it adapts

[[Home]]
