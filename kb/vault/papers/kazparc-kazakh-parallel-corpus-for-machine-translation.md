---
kb_id: "arxiv:2403.19399"
type: "paper"
title: "KazParC: Kazakh Parallel Corpus for Machine Translation"
arxiv_id: "2403.19399"
doi: null
hf_repo: null
year: 2024
topics: ["embed-kazakh"]
claims: 2
uncertain_claims: 1
verdicts: []
aliases: ["KazParC: Kazakh Parallel Corpus for Machine Translation", "arXiv:2403.19399", "arxiv:2403.19399"]
tags: ["paper", "topic/embed-kazakh"]
---
# KazParC: Kazakh Parallel Corpus for Machine Translation

[arXiv](https://arxiv.org/abs/2403.19399)
**Topics:** [[embed-kazakh]]

> [!abstract]
> We introduce KazParC, a parallel corpus designed for machine translation across Kazakh, English, Russian, and Turkish. The first and largest publicly available corpus of its kind, KazParC contains a collection of 371,902 parallel sentences covering different domains and developed with the assistance of human translators. Our research efforts also extend to the development of a neural machine trans …

## Claims

> [!note] CLAIM — embed-kazakh
> Parallel data for contrastive pretraining: KazParC = 371,902 human-translated parallel sentences across kk/en/ru/tr (CC BY 4.0, largest human-quality kk corpus). OPUS kk-en totals ~35.66M pairs but is dominated by noisy mined NLLB v1 (34.59M) + CCAligned (690k) + XLEnt (162k). OPUS kk-ru is surprisingly thin: only ~771k pairs (MultiCCAligned 432k) despite pervasive kk-ru code-switching in the wild.
>
> **Numbers:** KazParC 371,902; OPUS kk-en 35,661,293 total (NLLB 34,589,761; CCAligned 689,653; XLEnt 161,706); OPUS kk-ru 771,081 (MultiCCAligned 431,953)
> **Relevance:** Stage-1 weakly-supervised contrastive data exists at ~35M scale (needs margin filtering); the kk-ru pair shortage means code-switch pairs must be constructed, not downloaded.
> **Source:** arXiv:2403.19399 / github.com/IS2AI/KazParC; opus.nlpl.eu opusapi queried 2026-07-03 · **Sweep:** `embeddings-2026-07`

> [!warning] UNCERTAIN — embed-kazakh
> Realistic total Kazakh pair budget for training: ~550-650k human-quality pairs (KazParC 372k + KazQAD 73k incl. MT-NQ + WebFAQ 12.5k + instructions ~100-150k) + ~0.5-1M synthetic Wikipedia pairs + ~5-8M usable mined bitext after margin-filtering the 34.6M NLLB kk-en pairs. This is 10-50x less supervised data than SOTA English/Chinese embedder recipes, which is why distillation from a strong multilingual teacher is structurally necessary.
>
> **Numbers:** ~0.6M clean + ~1M synthetic + 5-8M filtered mined = ~7-10M usable pairs
> **Relevance:** Directly sizes the two-stage contrastive training plan and justifies the teacher-distillation design choice in the paper.
> **Source:** Aggregated from arXiv:2403.19399, arXiv:2404.04487, PaDaS-Lab/webfaq, OPUS API, HF dataset metadata (this survey) · **Sweep:** `embeddings-2026-07`

**Cited KB notes:** [[kazqad-kazakh-open-domain-question-answering-dataset]]

## Related
- [[less-is-more-adapting-text-embeddings-for-low-resource-languages-with-small|Less is More: Adapting Text Embeddings for Low-Resource Languages with Small Scale Noisy S…]] — KazParC's 372k human parallel pairs are the contrastive supervision anchor the low-resource embedding-adaptation recipe depends on
- [[huggingface-co-api-datasets-issai-kazqad-retrieval-issai|huggingface.co/api/datasets/issai/kazqad-retrieval, .../issai/kazparc…]] — source-of: issai/kazparc is the HF release of the KazParC Kazakh parallel corpus paper

[[Home]]
