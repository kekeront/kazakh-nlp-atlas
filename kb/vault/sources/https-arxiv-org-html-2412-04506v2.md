---
kb_id: "title:https arxiv org html 2412 04506v2 https www snowflake com en engineering blog snowflake arctic embed 2 multilingual"
type: "source"
title: "https://arxiv.org/html/2412.04506v2"
doi: null
hf_repo: null
year: null
topics: ["embed-sota"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:https arxiv org html 2412 04506v2 https www snowflake com en engineering blog snowflake arctic embed 2 multilingual"]
tags: ["source", "topic/embed-sota"]
---
# https://arxiv.org/html/2412.04506v2

**Topics:** [[embed-sota]]

## Source URLs
- https://arxiv.org/html/2412.04506v2
- https://www.snowflake.com/en/engineering-blog/snowflake-arctic-embed-2-multilingual

## Findings

> [!note] CLAIM — embed-sota
> Arctic-Embed 2.0 (Snowflake, Dec 2024): M 305M and L 568M multilingual retrievers with MRL applied at a single truncated dim of 256 during BOTH pretraining and fine-tuning, plus quantization-aware embedding training, enabling ~128 bytes/vector at high quality; strong on MTEB-R (55.6), MIRACL (55.8), CLEF (52.9/54.3) without sacrificing English — and per KAZ-QA-RAG it is the empirical leader on Kazakh retrieval among off-the-shelf models.
>
> **Numbers:** 305M/568M; MRL-256 + int quantization = 128 bytes/vector (~4x compression); MIRACL 55.8.
> **Relevance:** Its train-time single-dim MRL + quantization trick is the cheapest way to make the Kazakh embedder RAG-deployable on modest hardware (relevant for Kazakhstan-market adoption claims).
> **Source:** https://arxiv.org/html/2412.04506v2; https://www.snowflake.com/en/engineering-blog/snowflake-arctic-embed-2-multilingual/ · **Sweep:** `embeddings-2026-07`

## Related
- [[https-github-com-arailym-ray-kaz-qa-rag|https://github.com/Arailym-ray/KAZ-QA-RAG]] — KAZ-QA-RAG benchmark names Arctic-Embed the best off-the-shelf Kazakh retriever (best pair: KazLLM-8B + Arctic-Embed)

[[Home]]
