---
kb_id: "hf:nurlykhan/kazembed-v5"
type: "source"
title: "huggingface.co/Nurlykhan/kazembed-v5 (apache-2.0)"
doi: null
hf_repo: "Nurlykhan/kazembed-v5"
year: null
topics: ["embed-kazakh", "embeddings-retrieval"]
claims: 2
uncertain_claims: 1
verdicts: []
aliases: ["hf:nurlykhan/kazembed-v5"]
tags: ["source", "topic/embed-kazakh", "topic/embeddings-retrieval"]
---
# huggingface.co/Nurlykhan/kazembed-v5 (apache-2.0)

**Topics:** [[embed-kazakh]], [[embeddings-retrieval]]

## Source URLs
- huggingface.co/Nurlykhan/kazembed-v5 (apache-2.0)

## Findings

> [!note] CLAIM — embed-kazakh
> The only dedicated Kazakh embedder found is Nurlykhan/kazembed-v5: multilingual-e5-base (278M) fine-tuned on just 61,255 pairs (KazQAD 6,640 + KazQAD-Retrieval 44,615 + Powerful-Kazakh-Dialogue 10,000) with MultipleNegativesRankingLoss; KazQAD test Hits@1 72%, Hits@5 96%, MRR 0.835 (+2.1% MRR over base e5). No MTEB evaluation, no STS/clustering eval, 289 downloads. No from-scratch Kazakh embedding model exists anywhere.
>
> **Numbers:** 278M params; 61,255 training pairs; MRR 0.835; Hits@1 0.72; Hits@5 0.96
> **Relevance:** This is the entire 'dedicated competition' — a small fine-tune. Beating it and BGE-M3 makes the 'best Kazakh embedder on the market' claim defensible.
> **Source:** huggingface.co/Nurlykhan/kazembed-v5 (apache-2.0) · **Sweep:** `embeddings-2026-07`

> [!warning] UNCERTAIN — embeddings-retrieval
> The widely-cited planka 'mE5-large MRR 0.909 on KazQAD hard negatives' originates SOLELY from the HF model card Nurlykhan/kazembed-v5 (Dec 2025, 289 downloads, boilerplate residue in citation block) — a hobby artifact, not a lab release. Its entire protocol description is one line: 'Evaluated on KazQAD test set with TF-IDF hard negatives (100 candidates per query)'; the 99-negative candidate pools are not published anywhere, Hits are rounded to whole percent.
>
> **Numbers:** mE5-large MRR 0.909 (reported); kazembed-v5 MRR 0.835; 100 candidates/query; 289 downloads
> **Relevance:** Campaign headline target provenance — must be treated as reported/unverified until re-measured by evallab runners with a pinned, published hard-negative mining recipe.
> **Source:** huggingface.co/Nurlykhan/kazembed-v5 (model card, fetched 2026-07-03) · **Sweep:** `2026-07-eval-provenance`

## Related
- [[qorgau-evaluating-llm-safety-in-kazakh-russian-bilingual-contexts|Qorgau: Evaluating LLM Safety in Kazakh-Russian Bilingual Contexts]] — Adoption/license contrast: Qorgau has NO license (eval-only) vs apache-2.0 Kazakh artifact — the atlas's claim-vs-usability datapoint
- [[afrimteb-and-afrie5-benchmarking-and-adapting-text-embedding-models-for-african|AfriMTEB and AfriE5: Benchmarking and Adapting Text Embedding Models for African Languages]] — AfriE5 +1.1/+1.7 is consistent with kazembed-v5's +2.1% MRR — the only dedicated Kazakh embedder, same modest LRL-adaptation ceiling
- [[less-is-more-adapting-text-embeddings-for-low-resource-languages-with-small|Less is More: Adapting Text Embeddings for Low-Resource Languages with Small Scale Noisy S…]] — Less-is-More 10k-pair full-FT+avg is the counter-recipe to kazembed-v5's 61k-pair MNRL that gained only +2.1% MRR
- [[turkembed-turkish-embedding-model-on-nli-sts-tasks|TurkEmbed: Turkish Embedding Model on NLI & STS Tasks]] — Turkic-sibling target: TurkEmbed is a Turkish embedding model, closest-language comparator for Kazakh
- [[huggingface-co-shyngys879-kazakh-e5-rag-embedding-model|huggingface.co/shyngys879/kazakh-e5-rag-embedding (model card, fetched…]] — refutes: same lineage shows mE5-large collapses 0.919->0.449 by pool, so kazembed-v5 card's 0.909 is a protocol artifact

[[Home]]
