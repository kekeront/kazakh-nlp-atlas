---
kb_id: "arxiv:2401.00368"
type: "paper"
title: "Improving Text Embeddings with Large Language Models"
arxiv_id: "2401.00368"
doi: null
hf_repo: null
year: 2023
topics: ["decoder-to-embedder"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Improving Text Embeddings with Large Language Models", "arXiv:2401.00368", "arxiv:2401.00368"]
tags: ["paper", "topic/decoder-to-embedder"]
---
# Improving Text Embeddings with Large Language Models

[arXiv](https://arxiv.org/abs/2401.00368)
**Topics:** [[decoder-to-embedder]]

> [!abstract]
> In this paper, we introduce a novel and simple method for obtaining high-quality text embeddings using only synthetic data and less than 1k training steps. Unlike existing methods that often depend on multi-stage intermediate pre-training with billions of weakly-supervised text pairs, followed by fine-tuning with a few labeled datasets, our method does not require building complex training pipelin …

## Claims

> [!note] CLAIM — decoder-to-embedder
> E5-Mistral's synthetic-data recipe is fully replicable for Kazakh: 500K synthetic examples with 150K unique instructions across 93 languages, generated 25% by GPT-3.5-Turbo and 75% by GPT-4 via two-step prompting (brainstorm task list, then generate query/positive/hard-negative triplets), then plain contrastive fine-tuning.
>
> **Numbers:** 500K examples, 150K instructions, 93 languages; +2.4 MTEB points over prior SOTA at the time.
> **Relevance:** Kazakh has almost no native paired data — synthetic generation with a strong teacher is the main way to manufacture the missing contrastive corpus.
> **Source:** arXiv 2401.00368 / ACL 2024 (Improving Text Embeddings with Large Language Models) · **Sweep:** `embeddings-2026-07`

## Related
- [[less-is-more-adapting-text-embeddings-for-low-resource-languages-with-small|Less is More: Adapting Text Embeddings for Low-Resource Languages with Small Scale Noisy S…]] — Both use LLM-synthetic pairs; L-i-M shows 10k noisy MT pairs suffice for LRLs, undercutting the massive-synthetic premise
- [[hf-datasets-api-metadata-2026-07-03|HF datasets API metadata 2026-07-03]] — kk has only ~100-150k MT instruction pairs vs the LLM-synthesized instruction-data scale that E5-mistral's embedding recipe assumes

[[Home]]
