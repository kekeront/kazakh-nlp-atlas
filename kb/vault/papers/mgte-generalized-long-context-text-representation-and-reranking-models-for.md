---
kb_id: "arxiv:2407.19669"
type: "paper"
title: "mGTE: Generalized Long-Context Text Representation and Reranking Models for Multilingual Text Retrieval"
arxiv_id: "2407.19669"
doi: null
hf_repo: null
year: 2024
topics: ["embeddings-training"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["mGTE: Generalized Long-Context Text Representation and Reranking Models for Multilingual Text Retrieval", "arXiv:2407.19669", "arxiv:2407.19669"]
tags: ["paper", "topic/embeddings-training"]
---
# mGTE: Generalized Long-Context Text Representation and Reranking Models for Multilingual Text Retrieval

[arXiv](https://arxiv.org/abs/2407.19669)
**Topics:** [[embeddings-training]]

> [!abstract]
> We present systematic efforts in building long-context multilingual text representation model (TRM) and reranker from scratch for text retrieval. We first introduce a text encoder (base size) enhanced with RoPE and unpadding, pre-trained in a native 8192-token context (longer than 512 of previous multilingual encoders). Then we construct a hybrid TRM and a cross-encoder reranker by contrastive lea …

## Claims

> [!note] CLAIM — embeddings-training
> gte-multilingual-base is a viable lighter alternative v0 base to mE5-large: 305M encoder (BERT+RoPE+GLU, XLM-R vocab), 8192 context, native MRL (128-768), and hybrid dense+sparse output, apache-2.0.
>
> **Numbers:** 305M params; emb dim 768 (MRL 128-768); 8192 ctx; 70+ langs; apache-2.0; dense+sparse hybrid
> **Relevance:** TRANSFERABLE-UNTESTED on Kazakh. Half the size of mE5-large (560M) with long context + MRL + permissive license; a strong candidate if v0 needs a smaller/faster base than mE5, and the sparse head aids lexical Kazakh matching (agglutinative surface forms).
> **Source:** arXiv:2407.19669 (mGTE); HF Alibaba-NLP/gte-multilingual-base · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[embeddinggemma-powerful-and-lightweight-text-representations|EmbeddingGemma: Powerful and Lightweight Text Representations]] — mGTE (305M) and EmbeddingGemma (308M) are competing lightweight multilingual v0 base options with MRL and instruction prefixes

[[Home]]
