---
kb_id: "title:hf datasets api metadata 2026 07 03"
type: "source"
title: "HF datasets API metadata 2026-07-03"
doi: null
hf_repo: null
year: null
topics: ["embed-kazakh"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:hf datasets api metadata 2026 07 03"]
tags: ["source", "topic/embed-kazakh"]
---
# HF datasets API metadata 2026-07-03

**Topics:** [[embed-kazakh]]

## Source URLs
- HF datasets API metadata 2026-07-03

## Findings

> [!note] CLAIM — embed-kazakh
> Kazakh instruction/dialogue pair data is small and mostly machine-translated: AmanMussa/kazakh-instruction-v2 (10k-100k self-instruct, updated Feb 2026), saillab/alpaca_kazakh_taco (10k-100k, MT Alpaca), DarkyMan/powerful-kazakh-dialogue (~10k) — roughly 100-150k instruction pairs total.
>
> **Numbers:** ~100-150k instruction pairs across 3 datasets, all size-tagged 10K<n<100K
> **Relevance:** Usable as instruction-tuning pairs for an instruct-embedder head, but quality audit needed (MT artifacts).
> **Source:** HF datasets API metadata 2026-07-03 · **Sweep:** `embeddings-2026-07`

## Related
- [[improving-text-embeddings-with-large-language-models|Improving Text Embeddings with Large Language Models]] — kk has only ~100-150k MT instruction pairs vs the LLM-synthesized instruction-data scale that E5-mistral's embedding recipe assumes

[[Home]]
