---
kb_id: "arxiv:2010.02534"
type: "paper"
title: "An Empirical Study of Tokenization Strategies for Various Korean NLP Tasks"
arxiv_id: "2010.02534"
doi: null
hf_repo: null
year: 2020
topics: ["decoder-to-embedder"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["An Empirical Study of Tokenization Strategies for Various Korean NLP Tasks", "arXiv:2010.02534", "arxiv:2010.02534"]
tags: ["paper", "topic/decoder-to-embedder"]
---
# An Empirical Study of Tokenization Strategies for Various Korean NLP Tasks

[arXiv](https://arxiv.org/abs/2010.02534)
**Topics:** [[decoder-to-embedder]]

> [!abstract]
> Typically, tokenization is the very first step in most text processing works. As a token serves as an atomic unit that embeds the contextual information of text, how to define a token plays a decisive role in the performance of a model.Even though Byte Pair Encoding (BPE) has been considered the de facto standard tokenization method due to its simplicity and universality, it still remains unclear …

## Claims

> [!note] CLAIM — decoder-to-embedder
> Morphology-aware tokenization measurably helps sentence-level semantics in agglutinative languages: for Korean, hybrid morpheme-segmentation-then-BPE beat pure BPE on KorSTS/KorNLI (AACL 2020); for Turkish/Finnish, linguistically informed segmentation improves embedding-space semantic coherence and OOV compositionality; for Kazakh specifically, the CSE-guided framework (Complete Set of Endings + vowel-harmony-aware FEMSeg-CRF, SentencePiece fine-tuned on CSE-segmented corpus) cuts neural training time ~33% via shorter sequences. No one has yet ablated morphology-aware tokenization on Kazakh EMBEDDING quality — that experiment is free novelty for us.
>
> **Numbers:** ~33% training-time reduction for Kazakh CSE-guided tokenization; Korean hybrid morpheme+BPE best on KorSTS (exception: pure BPE best on KorQuAD).
> **Relevance:** Supports the <2.0 fertility target AND motivates a tokenizer ablation (Unigram-50K vs CSE/morpheme-guided Unigram-50K) measured on kk-STS/KazQAD.
> **Source:** arXiv 2010.02534 (Korean tokenization, AACL 2020); MDPI Information 17(2):128 Jan 2026 (Kazakh CSE-guided); github.com/walsher46/Kazakh-tokenizer; arXiv 2509.14238 (Turkish/Finnish); arXiv 2606.18717 (Morpheus) · **Sweep:** `embeddings-2026-07`

**Cited KB notes:** [[morpheus-a-morphology-aware-neural-tokenizer-and-word-embedder-for-turkish]]

[[Home]]
