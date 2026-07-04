---
kb_id: "hf:blog/ibm-granite"
type: "source"
title: "https://huggingface.co/blog/ibm-granite/granite-embedding-multilingual…"
doi: null
hf_repo: "blog/ibm-granite"
year: null
topics: ["embed-sota"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["hf:blog/ibm-granite"]
tags: ["source", "topic/embed-sota"]
---
# https://huggingface.co/blog/ibm-granite/granite-embedding-multilingual…

**Topics:** [[embed-sota]]

## Source URLs
- https://huggingface.co/blog/ibm-granite/granite-embedding-multilingual-r2
- https://arxiv.org/html/2605.13521v2

## Findings

> [!note] CLAIM — embed-sota
> Granite Embedding Multilingual R2 (IBM, 2026, Apache 2.0): ModernBERT-style encoders (alternating attention, RoPE, FA2) at 311M (768d, Gemma-3 262k tokenizer) and 97M (384d, pruned 180k vocab), 32K context, 200+ languages (52 retrieval-tuned). MTEB Multilingual Retrieval: 65.2 (311M, #2 open <500M; EmbeddingGemma 62.5, mE5-base 52.7) and 60.3 (97M, best sub-100M). Recipe: distillation from Granite/Mistral instruct teachers -> contrastive fine-tune -> model merging -> MRL (256d costs only -0.5 nDCG).
>
> **Numbers:** 311M: 65.2 MTEB-Multilingual-Retrieval; 97M: 60.3 (+9.4 over mE5-small 50.9); 32K ctx; MRL to 128d.
> **Relevance:** Shows a 97-311M ModernBERT encoder with a big-vocab tokenizer is the current efficiency frontier — and that vocabulary choice (their Gemma-3 262k vs your 50K Unigram kk-optimized) is a first-class design lever.
> **Source:** https://huggingface.co/blog/ibm-granite/granite-embedding-multilingual-r2; https://arxiv.org/html/2605.13521v2 · **Sweep:** `embeddings-2026-07`

[[Home]]
