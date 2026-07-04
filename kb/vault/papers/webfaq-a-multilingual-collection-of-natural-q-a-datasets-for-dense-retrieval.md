---
kb_id: "arxiv:2502.20936"
type: "paper"
title: "WebFAQ: A Multilingual Collection of Natural Q&A Datasets for Dense Retrieval"
arxiv_id: "2502.20936"
doi: null
hf_repo: "PaDaS-Lab/webfaq"
year: 2025
topics: ["embed-sota", "embed-kazakh"]
claims: 2
uncertain_claims: 1
verdicts: []
aliases: ["WebFAQ: A Multilingual Collection of Natural Q&A Datasets for Dense Retrieval", "arXiv:2502.20936", "arxiv:2502.20936"]
tags: ["paper", "topic/embed-sota", "topic/embed-kazakh"]
---
# WebFAQ: A Multilingual Collection of Natural Q&A Datasets for Dense Retrieval

[arXiv](https://arxiv.org/abs/2502.20936)
**Topics:** [[embed-sota]], [[embed-kazakh]]

> [!abstract]
> We present WebFAQ, a large-scale collection of open-domain question answering datasets derived from FAQ-style schema.org annotations. In total, the data collection consists of 96 million natural question-answer (QA) pairs across 75 languages, including 47 million (49%) non-English samples. WebFAQ further serves as the foundation for 20 monolingual retrieval benchmarks with a total size of 11.2 mil …

## Claims

> [!warning] UNCERTAIN — embed-sota
> WebFAQ (96M natural QA pairs, 75 languages, 49% non-English) and WebFAQ 2.0 (198M pairs, 104-108 languages, hard negatives mined via BM25 top-200 -> BGE-M3 reranking) include Kazakh — MTEB's WebFAQRetrieval task has a kaz split — making it the largest known source of NATURAL (non-synthetic) Kazakh paired training data. Caveat from WebFAQ 2.0: with MNR contrastive loss, random negatives often beat their mined hard negatives due to false negatives; hard negatives helped mainly via MarginMSE distillation.
>
> **Numbers:** 96M pairs/75 langs (v1); 198M/104-108 langs (v2); every language has >=1,000 samples; exact kk count not published in the papers' tables.
> **Relevance:** Primary natural kk pair source for stage-1 contrastive training; the false-negative caveat directly informs the negative-sampling design (prefer online mixing / FN-masking over naive offline mining).
> **Source:** https://arxiv.org/abs/2502.20936; https://arxiv.org/html/2602.17327v1; mteb WebFAQRetrieval task (kaz split verified locally) · **Sweep:** `embeddings-2026-07`

> [!note] CLAIM — embed-kazakh
> WebFAQRetrieval-kaz is the second public Kazakh retrieval task: multilingual-e5-large scores nDCG@10 0.7269; the WebFAQ corpus contains ~12.5k Kazakh QA pairs (of 96M pairs / 75 languages total).
>
> **Numbers:** e5-large WebFAQ-kaz nDCG@10 = 0.7269; kaz subset = 12.5k QA pairs
> **Relevance:** Second eval axis plus 12.5k natural kk QA pairs usable as fine-tuning data (dev/test hygiene needed to avoid train-test leak).
> **Source:** embeddings-benchmark/results WebFAQRetrieval.json; huggingface.co/datasets/PaDaS-Lab/webfaq; arXiv:2502.20936 · **Sweep:** `embeddings-2026-07`

## Related
- [[nv-retriever-improving-text-embedding-models-with-effective-hard-negative-mining|NV-Retriever: Improving text embedding models with effective hard-negative mining]] — Both on hard-negative mining; WebFAQ 2.0 finds random negatives beat mined hard-negs under MNR (false negatives), tension with…
- [[huggingface-co-datasets-mteb-webfaqretrieval|huggingface.co/datasets/mteb/WebFAQRetrieval]] — WebFAQ supplies the WebFAQRetrieval-kaz MTEB task (~12.5k kk natural pairs; e5-large nDCG@10 0.7269)

[[Home]]
