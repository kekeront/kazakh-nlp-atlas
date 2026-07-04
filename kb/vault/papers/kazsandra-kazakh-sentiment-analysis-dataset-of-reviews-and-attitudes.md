---
kb_id: "arxiv:2403.19335"
type: "paper"
title: "KazSAnDRA: Kazakh Sentiment Analysis Dataset of Reviews and Attitudes"
arxiv_id: "2403.19335"
doi: null
hf_repo: null
year: 2024
topics: ["embed-kazakh"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["KazSAnDRA: Kazakh Sentiment Analysis Dataset of Reviews and Attitudes", "arXiv:2403.19335", "arxiv:2403.19335"]
tags: ["paper", "topic/embed-kazakh"]
---
# KazSAnDRA: Kazakh Sentiment Analysis Dataset of Reviews and Attitudes

[arXiv](https://arxiv.org/abs/2403.19335)
**Topics:** [[embed-kazakh]]

> [!abstract]
> This paper presents KazSAnDRA, a dataset developed for Kazakh sentiment analysis that is the first and largest publicly available dataset of its kind. KazSAnDRA comprises an extensive collection of 180,064 reviews obtained from various sources and includes numerical ratings ranging from 1 to 5, providing a quantitative representation of customer attitudes. The study also pursued the automation of …

## Claims

> [!note] CLAIM — embed-kazakh
> Existing kk classification/clustering eval resources that can seed MTEB(kaz): KazSAnDRA sentiment (180,064 reviews, 1-5 ratings; best baseline F1 0.81 polarity / 0.39 score), Belebele kaz_Cyrl (900 questions), SIB200 kaz_Cyrl (~205 sentences, 7 topics), TurkicClassification kk news (e5-large accuracy 0.516), CyrillicTurkicLangClassification (8 Turkic languages).
>
> **Numbers:** KazSAnDRA 180,064; Belebele-kaz 900; SIB200 ~205/lang; e5-large TurkicClassification kk = 0.516
> **Relevance:** Enough raw material for classification/clustering tracks of a Kazakh MTEB suite without new annotation; only STS/reranking/retrieval-beyond-wiki need building.
> **Source:** arXiv:2403.19335 (KazSAnDRA); embeddings-benchmark/results TurkicClassification.json; mteb repo task files · **Sweep:** `embeddings-2026-07`

[[Home]]
