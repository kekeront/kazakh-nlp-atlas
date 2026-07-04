---
kb_id: "arxiv:2408.12503"
type: "paper"
title: "The Russian-focused embedders' exploration: ruMTEB benchmark and Russian embedding model design"
arxiv_id: "2408.12503"
doi: null
hf_repo: null
year: 2024
topics: ["decoder-to-embedder"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["The Russian-focused embedders' exploration: ruMTEB benchmark and Russian embedding model design", "arXiv:2408.12503", "arxiv:2408.12503"]
tags: ["paper", "topic/decoder-to-embedder"]
---
# The Russian-focused embedders' exploration: ruMTEB benchmark and Russian embedding model design

[arXiv](https://arxiv.org/abs/2408.12503)
**Topics:** [[decoder-to-embedder]]

> [!abstract]
> Embedding models play a crucial role in Natural Language Processing (NLP) by creating text embeddings used in various tasks such as information retrieval and assessing semantic text similarity. This paper focuses on research related to embedding models in the Russian language. It introduces a new Russian-focused embedding model called ru-en-RoSBERTa and the ruMTEB benchmark, the Russian version ex …

## Claims

> [!note] CLAIM — decoder-to-embedder
> ruMTEB is the best construction template for kkMTEB: 23 datasets across 7 task types, 17 newly created from native sources (reviews, maps, science) + 6 from multilingual MTEB, with cleaning/filtering. Their specialized model ru-en-RoSBERTa (404M encoder, tokenizer extended with English tokens, MLM + slerp anti-forgetting, then InfoNCE with 7 hard negatives, temp 0.02) scores 61.77 vs mE5-large 61.41 and BGE-M3 61.58 — winning overall but LOSING retrieval/reranking to BGE-M3.
>
> **Numbers:** 23 tasks / 7 types / 17 new; 61.77 vs 61.41 (mE5-large) vs 61.58 (BGE-M3).
> **Relevance:** Both a benchmark blueprint and a warning: a ~400-500M specialized model only marginally beats multilingual giants unless retrieval training data is strong. Also relevant for kk/ru code-switching: they deliberately kept the second language (English there, Russian for us) in the tokenizer and data.
> **Source:** arXiv 2408.12503 (ruMTEB / ru-en-RoSBERTa) · **Sweep:** `embeddings-2026-07`

## Related
- [[turkembed-turkish-embedding-model-on-nli-sts-tasks|TurkEmbed: Turkish Embedding Model on NLI & STS Tasks]] — ruMTEB is the kkMTEB construction template; TurkEmbed is the Turkic-family analogue — both test whether monolingual specialization beats mE5
- [[huggingface-co-ai-forever-frida|huggingface.co/ai-forever/FRIDA]] — FRIDA is a ruMTEB-lineage Russian embedder; node documents it excludes kk despite shared Cyrillic — cross-script ru→kk transfer is…

[[Home]]
