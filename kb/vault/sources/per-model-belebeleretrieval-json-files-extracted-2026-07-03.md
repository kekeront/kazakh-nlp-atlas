---
kb_id: "title:per model belebeleretrieval json files extracted 2026 07 03"
type: "source"
title: "per-model BelebeleRetrieval.json files (extracted 2026-07-03)"
doi: null
hf_repo: null
year: null
topics: ["embed-kazakh"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:per model belebeleretrieval json files extracted 2026 07 03"]
tags: ["source", "topic/embed-kazakh"]
---
# per-model BelebeleRetrieval.json files (extracted 2026-07-03)

**Topics:** [[embed-kazakh]]

## Source URLs
- per-model BelebeleRetrieval.json files (extracted 2026-07-03)

## Findings

> [!note] CLAIM — embed-kazakh
> Current best scores on the main public Kazakh retrieval signal, BelebeleRetrieval kaz_Cyrl→kaz_Cyrl (nDCG@10, official mteb results repo): Qwen3-Embedding-8B 0.956; BGE-M3 0.9017; multilingual-e5-large-instruct 0.8949; multilingual-e5-large 0.8269; Qwen3-Embedding-0.6B 0.7545; EmbeddingGemma-300m 0.6839. In the ≤600M class the bar is BGE-M3 (568M); the same-size Qwen3-Embedding-0.6B is ~15 points behind it on Kazakh.
>
> **Numbers:** nDCG@10: 0.956 (8B) / 0.9017 (BGE-M3) / 0.8949 (e5-large-instr) / 0.8269 (e5-large) / 0.7545 (Qwen3-0.6B) / 0.6839 (gemma-300m); crosslingual e5-large: kaz→eng 0.9255, eng→kaz 0.7881
> **Relevance:** Defines the exact victory condition for deliverable (2): beat BGE-M3 0.9017 at ≤600M and approach the 8B's 0.956.
> **Source:** github.com/embeddings-benchmark/results — per-model BelebeleRetrieval.json files (extracted 2026-07-03) · **Sweep:** `embeddings-2026-07`

## Related
- [[qwen3-embedding-advancing-text-embedding-and-reranking-through-foundation-models|Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models]] — Belebele kaz nDCG@10 behind Qwen3-Emb's Kazakh loss (0.7545 vs mE5-large-instruct 0.8949) comes from these extracted per-model JSONs
- [[m3-embedding-multi-linguality-multi-functionality-multi-granularity-text|M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Thr…]] — BGE-M3 (M3-Embedding, 568M) is the concrete ≤600M bar at 0.9017 on BelebeleRetrieval kaz that QymyzLM's embedder must clear
- [[embeddinggemma-powerful-and-lightweight-text-representations|EmbeddingGemma: Powerful and Lightweight Text Representations]] — EmbeddingGemma-300m measured at 0.6839 — the sub-600M laggard showing size alone doesn't buy kk retrieval quality

[[Home]]
