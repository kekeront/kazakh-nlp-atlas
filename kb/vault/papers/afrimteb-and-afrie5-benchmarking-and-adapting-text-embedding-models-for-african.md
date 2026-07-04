---
kb_id: "arxiv:2510.23896"
type: "paper"
title: "AfriMTEB and AfriE5: Benchmarking and Adapting Text Embedding Models for African Languages"
arxiv_id: "2510.23896"
doi: null
hf_repo: null
year: 2025
topics: ["decoder-to-embedder", "embeddings-training"]
claims: 3
uncertain_claims: 0
verdicts: []
aliases: ["AfriMTEB and AfriE5: Benchmarking and Adapting Text Embedding Models for African Languages", "arXiv:2510.23896", "arxiv:2510.23896"]
tags: ["paper", "topic/decoder-to-embedder", "topic/embeddings-training"]
---
# AfriMTEB and AfriE5: Benchmarking and Adapting Text Embedding Models for African Languages

[arXiv](https://arxiv.org/abs/2510.23896)
**Topics:** [[decoder-to-embedder]], [[embeddings-training]]

> [!abstract]
> Text embeddings are an essential building component of several NLP tasks such as retrieval-augmented generation which is crucial for preventing hallucinations in LLMs. Despite the recent release of massively multilingual MTEB (MMTEB), African languages remain underrepresented, with existing tasks often repurposed from translation benchmarks such as FLORES clustering or SIB-200. In this paper, we i …

## Claims

> [!note] CLAIM — decoder-to-embedder
> AfriE5 shows targeted low-resource adaptation DOES beat the giants: cross-lingual contrastive distillation from instruction-tuned mE5 achieved state-of-the-art on AfriMTEB (59 languages, 14 tasks, 38 datasets), outperforming Gemini-Embedding and mE5 itself.
>
> **Relevance:** The proven playbook for our situation: distill a big teacher's embedding space into the Kazakh-specialized student using kk and kk-ru parallel text (KazParC) as the bridge.
> **Source:** arXiv 2510.23896 (AfriMTEB and AfriE5, EACL 2026) · **Sweep:** `embeddings-2026-07`

> [!note] CLAIM — embeddings-training
> AfriE5 is the closest published analogue of qymyz-embed's task (adapt mE5 to low-resource languages) and gives a full transferable recipe: FINE-TUNE mE5-large-instruct via cross-lingual contrastive distillation from a BGE-reranker-v2-m3 cross-encoder teacher PLUS machine-translated NLI (MNLI/SNLI -> target langs via NLLB-200), quality-filtered by COMET>=0.75, ~60k pairs, 9 languages.
>
> **Numbers:** ~60,066 pairs after COMET>=0.75 filter; 9 langs; AfriMTEB-Lite AfriE5 63.7 vs mE5-large-instruct 62.0 (+1.7); AfriMTEB-Full 62.4 vs 61.3 (+1.1)
> **Relevance:** TRANSFERABLE-UNTESTED on Kazakh (AfriMTEB has NO Turkic/Central-Asian langs). The +1.1/+1.7 gain from only ~60k MT+distilled pairs is a realistic ceiling estimate for a Kazakh mE5 fine-tune at the lab's ~61k real-pair scale — modest, matching the KB's kazembed +2.1% MRR datapoint. Distill-from-reranker + NLLB-MT of NLI is directly reusable for kk.
> **Source:** arXiv:2510.23896 (AfriMTEB and AfriE5) · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — embeddings-training
> The lab's mE5-large bar on KazQAD is protocol-bound, not a single number, and the only dedicated Kazakh embedder (kazembed-v5, mE5-base 278M) beat base mE5 by just +2.1% MRR from 61,255 pairs — consistent with AfriE5's +1.1/+1.7 and TR-MTEB's failure to surpass mE5.
>
> **Numbers:** mE5-large KazQAD: 0.4490 (HardTFIDF99) vs 0.9189 (KazQAD-100 local); kazembed-v5 MRR 0.835 (+2.1% over base); 61,255 pairs; full-corpus paper baseline MRR 0.382
> **Relevance:** TESTED-ON-KAZAKH. Grounds the win-bar: small-pair fine-tunes yield only ~2% gains on same-family/low-resource langs. To beat mE5-large convincingly on KazQAD, qymyz-embed needs the FULL stack (TopK-PercPos hard negatives + teacher distillation + synthetic pair scaling + slerp), not just more real pairs.
> **Source:** KB: HF Nurlykhan/kazembed-v5, shyngys879/kazakh-e5-rag-embedding cards; cross-ref AfriE5 arXiv:2510.23896 · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[mmteb-massive-multilingual-text-embedding-benchmark|MMTEB: Massive Multilingual Text Embedding Benchmark]] — AfriMTEB is the regional-MTEB template proving a kk-MTEB is buildable; MMTEB itself currently has zero native kk tasks
- [[embeddinggemma-powerful-and-lightweight-text-representations|EmbeddingGemma: Powerful and Lightweight Text Representations]] — AfriMTEB finds EmbeddingGemma underperforms the E5 family on African LRLs — external evidence its lightweight-decoder gains don't transfer…
- [[less-is-more-adapting-text-embeddings-for-low-resource-languages-with-small|Less is More: Adapting Text Embeddings for Low-Resource Languages with Small Scale Noisy S…]] — Both adapt mE5 to LRLs — AfriE5 by cross-lingual distillation (+1.1/+1.7), Less-is-More by base-weight averaging; same thin-margin regime
- [[huggingface-co-nurlykhan-kazembed-v5-apache-2-0|huggingface.co/Nurlykhan/kazembed-v5 (apache-2.0)]] — AfriE5 +1.1/+1.7 is consistent with kazembed-v5's +2.1% MRR — the only dedicated Kazakh embedder, same modest LRL-adaptation ceiling

[[Home]]
