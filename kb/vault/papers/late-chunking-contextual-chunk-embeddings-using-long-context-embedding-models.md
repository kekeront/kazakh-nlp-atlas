---
kb_id: "arxiv:2409.04701"
type: "paper"
title: "Late Chunking: Contextual Chunk Embeddings Using Long-Context Embedding Models"
arxiv_id: "2409.04701"
doi: null
hf_repo: null
year: 2024
topics: ["decoder-to-embedder"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Late Chunking: Contextual Chunk Embeddings Using Long-Context Embedding Models", "arXiv:2409.04701", "arxiv:2409.04701"]
tags: ["paper", "topic/decoder-to-embedder"]
---
# Late Chunking: Contextual Chunk Embeddings Using Long-Context Embedding Models

[arXiv](https://arxiv.org/abs/2409.04701)
**Topics:** [[decoder-to-embedder]]

> [!abstract]
> Many use cases require retrieving smaller portions of text, and dense vector-based retrieval systems often perform better with shorter text segments, as the semantics are less likely to be over-compressed in the embeddings. Consequently, practitioners often split text documents into smaller chunks and encode them separately. However, chunk embeddings created in this way can lose contextual informa …

## Claims

> [!note] CLAIM — decoder-to-embedder
> Late chunking (encode whole document once with a long-context embedder, mean-pool per chunk afterwards) yields contextual chunk embeddings that improve long-document retrieval nDCG with NO extra training — but only works if the embedder has real long context.
>
> **Relevance:** Argues for giving the embedding variant at least 8K context (backbone likely trains at 2-4K) so Kazakh RAG over long documents works out of the box.
> **Source:** arXiv 2409.04701 (Late Chunking, Jina AI) · **Sweep:** `embeddings-2026-07`

[[Home]]
