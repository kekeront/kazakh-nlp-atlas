---
kb_id: "arxiv:2603.22290"
type: "paper"
title: "Less is More: Adapting Text Embeddings for Low-Resource Languages with Small Scale Noisy Synthetic Data"
arxiv_id: "2603.22290"
doi: null
hf_repo: null
year: 2026
topics: ["embed-sota", "joint-generative-embedding-head-on-one-6"]
claims: 4
uncertain_claims: 0
verdicts: []
aliases: ["Less is More: Adapting Text Embeddings for Low-Resource Languages with Small Scale Noisy Synthetic Data", "arXiv:2603.22290", "arxiv:2603.22290"]
tags: ["paper", "topic/embed-sota", "topic/joint-generative-embedding-head-on-one-6"]
---
# Less is More: Adapting Text Embeddings for Low-Resource Languages with Small Scale Noisy Synthetic Data

[arXiv](https://arxiv.org/abs/2603.22290)
**Topics:** [[embed-sota]], [[joint-generative-embedding-head-on-one-6]]

> [!abstract]
> Low-resource languages (LRLs) often lack high-quality, large-scale datasets for training effective text embedding models, hindering their application in tasks like retrieval-augmented generation (RAG) and semantic search. In this work, we challenge the prevailing assumption that effective semantic alignment requires massive datasets or pristine, human-verified translations. Focusing on Armenian (a …

## Claims

> [!note] CLAIM — embed-sota
> CRITICAL: the newest small decoder-based embedders COLLAPSE on low-resource languages while old XLM-R-based mE5 holds up. On a native Armenian benchmark (zero-shot): Qwen3-Embedding-0.6B averaged 47.38 and EmbeddingGemma-300m 52.43 vs multilingual-e5-base 64.30, mE5-large 72.11, mE5-large-instruct 72.99. AfriMTEB/AfriE5 independently found E5-family outperforming EmbeddingGemma and Qwen3-0.6B on African LRLs. Cause: XLM-R's CC100 pretraining + tokenizer cover LRLs; the new models' synthetic contrastive data skews to high-resource languages.
>
> **Numbers:** Armenian avg: Qwen3-0.6B 47.38, EmbGemma 52.43, mE5-base 64.30, mE5-large-it 72.99 (Table 1). MMTEB rank order (Qwen3-0.6B 64.34 > mE5-large-it 63.22) INVERTS on LRLs.
> **Relevance:** The headline MMTEB leaderboard is misleading for Kazakh; the real bar is mE5-large-instruct-class models plus adapted variants, and this inversion is the paper's core motivation for a Kazakh-native embedder.
> **Source:** https://arxiv.org/pdf/2603.22290 (Less is More, Mar 2026, Table 1); https://arxiv.org/pdf/2510.23896 (AfriMTEB/AfriE5) · **Sweep:** `embeddings-2026-07`

> [!note] CLAIM — embed-sota
> 'Less is More' (arXiv 2603.22290, Mar 2026) shows the cheapest known path to a SOTA LRL embedder: fine-tune mE5-base on just 10k NOISY synthetic pairs (English Reddit title-body machine-translated by Gemma-2-27B-it) -> +11-12% average, retrieval +35% relative, matching 1M-pair training. Scaling 10k->1M adds <1%; translation quality and domain diversity don't matter; 0.5/0.5 weight-averaging with the base model prevents catastrophic forgetting (+2-8 pts). Filtering: drop pair if |sim(q_en,p_en) - sim(q_lrl,p_lrl)| > 0.05 or translation similarity < 0.85 (measured with mE5). Setup: full FT, effective batch 512, lr 7e-5, 5 epochs; 10k pairs cost <$20 via Gemini Flash.
>
> **Numbers:** mE5 Armenian: retrieval 58.15->79.35, avg 64.30->76.42 (merged) with 10k pairs; 1M pairs gives 79.02 avg (no gain). EmbeddingGemma under same protocol: 52.43->67.19 at 10k but needs 1M to reach 77.06 — encoders adapt more data-efficiently than decoder-derived embedders.
> **Relevance:** Drop-in protocol for a day-one Kazakh baseline AND the strongest competitor your final model must beat; also defines the data-filtering recipe for all synthetic kk pairs.
> **Source:** https://arxiv.org/pdf/2603.22290 Tables 1-4, Appendix A · **Sweep:** `embeddings-2026-07`

> [!note] CLAIM — embed-sota
> The Less-is-More authors explicitly flag as UNTESTED whether noisy-alignment holds for 'languages sharing a script with a high-resource neighbor (e.g., low-resource Cyrillic languages), where token overlap might change the adaptation dynamics' — Kazakh (Cyrillic, heavy kk/ru code-switching) is exactly this case, and it is an open, publishable research question.
>
> **Numbers:** Validated only on Armenian (hye) and Georgian (kat), both unique-script isolates; Georgian: MTEB[kat] 71.02->77.18 with same 10k protocol.
> **Relevance:** A ready-made experimental contribution for the paper: replicate their 10k/50k/1M ablation on Kazakh and characterize how ru-script overlap changes alignment — novel either way it turns out.
> **Source:** https://arxiv.org/pdf/2603.22290 Section 6.2 Limitations · **Sweep:** `embeddings-2026-07`

> [!note] CLAIM — joint-generative-embedding-head-on-one-6
> [tested-on-Kazakh / tested-on-Turkic] Both existing warnings that the embedding win is not assured remain the state of the art after this sweep — nothing newer supersedes them: kazembed-v5 (mE5-base + 61,255 kk pairs, MNRL) gained only +2.1% MRR over base e5 on its own protocol, and TR-MTEB's Turkish specialization (34.2M weak pairs, contrastive PT + SFT) did not robustly beat mE5. The counter-recipe with the best LRL evidence is Less-is-More (10k noisy synthetic pairs, full FT of mE5, batch 512, lr 7e-5, 5 ep, 0.5/0.5 weight-average): Armenian retrieval 58.15->79.35; its authors explicitly flag Cyrillic LRLs with a high-resource script neighbor (= Kazakh, kk/ru code-switching) as untested.
>
> **Numbers:** kazembed-v5 MRR 0.835 (+2.1% vs base); TR-MTEB 34.2M pairs, no robust win over mE5; Less-is-More: 10k pairs, +11-12% avg, retrieval +35% rel., 1M pairs adds <1%
> **Relevance:** Defines the separate-model arm of the fork: mE5-large + Less-is-More-style 10k-pair adaptation is the highest-probability path to the market deliverable, is itself a publishable first (Kazakh = the paper's explicitly open Cyrillic case), and costs <$20 of synthesis + hours of T4 time.
> **Source:** KB nodes: hf:Nurlykhan/kazembed-v5; TR-MTEB aclanthology 2025.findings-emnlp.471; arXiv:2603.22290 — consolidated, web sweep found nothing newer · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[kazparc-kazakh-parallel-corpus-for-machine-translation|KazParC: Kazakh Parallel Corpus for Machine Translation]] — KazParC's 372k human parallel pairs are the contrastive supervision anchor the low-resource embedding-adaptation recipe depends on
- [[afrimteb-and-afrie5-benchmarking-and-adapting-text-embedding-models-for-african|AfriMTEB and AfriE5: Benchmarking and Adapting Text Embedding Models for African Languages]] — Both adapt mE5 to LRLs — AfriE5 by cross-lingual distillation (+1.1/+1.7), Less-is-More by base-weight averaging; same thin-margin regime
- [[turkembed-turkish-embedding-model-on-nli-sts-tasks|TurkEmbed: Turkish Embedding Model on NLI & STS Tasks]] — Turkic sibling: TurkEmbed's 34.2M pairs fail to beat mE5, tempering Less-is-More's claim of cheaply winning on a Kazakh-family LRL
- [[improving-text-embeddings-with-large-language-models|Improving Text Embeddings with Large Language Models]] — Both use LLM-synthetic pairs; L-i-M shows 10k noisy MT pairs suffice for LRLs, undercutting the massive-synthetic premise
- [[huggingface-co-nurlykhan-kazembed-v5-apache-2-0|huggingface.co/Nurlykhan/kazembed-v5 (apache-2.0)]] — Less-is-More 10k-pair full-FT+avg is the counter-recipe to kazembed-v5's 61k-pair MNRL that gained only +2.1% MRR

[[Home]]
