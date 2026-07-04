---
kb_id: "title:ggml org llama cpp discussions 3167 4167 8273 xiongjiedai gpu benchmarks on llm inference"
type: "source"
title: "ggml-org/llama.cpp Discussions #3167/#4167/#8273"
doi: null
hf_repo: null
year: null
topics: ["inference-tts"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:ggml org llama cpp discussions 3167 4167 8273 xiongjiedai gpu benchmarks on llm inference"]
tags: ["source", "topic/inference-tts"]
---
# ggml-org/llama.cpp Discussions #3167/#4167/#8273

**Topics:** [[inference-tts]]

## Source URLs
- ggml-org/llama.cpp Discussions #3167/#4167/#8273
- XiongjieDai GPU-Benchmarks-on-LLM-Inference

## Findings

> [!note] CLAIM — inference-tts
> Realistic edge throughput for 0.5-1.5B models: ~30-60 tok/s at Q4 on M1/8GB-class GPU; 20-100 tok/s on CPU (memory-bandwidth bound, not compute bound). A 14B model can be squeezed into 8GB with llama.cpp resource management, and 0.5B-1.5B run comfortably on legacy laptops.
>
> **Numbers:** 0.5-1.5B: 30-60 tok/s GPU, 20-100 tok/s CPU (Q4); memory-bandwidth bound
> **Relevance:** Sets the latency envelope for the Kazakh SLM: with MTP self-spec (~2x) a 500M Q4 model can reach ~60-120 tok/s on modest hardware — but see the fertility multiplier below for words/s.
> **Source:** ggml-org/llama.cpp Discussions #3167/#4167/#8273; XiongjieDai GPU-Benchmarks-on-LLM-Inference · **Sweep:** `slm-architecture-2026-07`

## Related
- [[beyond-fertility-analyzing-strr-as-a-metric-for-multilingual-tokenization|Beyond Fertility: Analyzing STRR as a Metric for Multilingual Tokenization Evaluation]] — Edge tok/s → perceived words/s divides by tokenizer fertility; STRR reframes how to measure that multilingual fertility premium

[[Home]]
