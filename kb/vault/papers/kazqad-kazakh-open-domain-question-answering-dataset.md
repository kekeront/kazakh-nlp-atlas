---
kb_id: "arxiv:2404.04487"
type: "paper"
title: "KazQAD: Kazakh Open-Domain Question Answering Dataset"
arxiv_id: "2404.04487"
doi: null
hf_repo: "issai/kazqad-retrieval"
year: 2024
topics: ["embed-sota", "embed-kazakh", "decoder-to-embedder", "joint-generative-embedding-head-on-one-6"]
claims: 5
uncertain_claims: 0
verdicts: []
aliases: ["KazQAD: Kazakh Open-Domain Question Answering Dataset", "arXiv:2404.04487", "arxiv:2404.04487"]
tags: ["paper", "topic/embed-sota", "topic/embed-kazakh", "topic/decoder-to-embedder", "topic/joint-generative-embedding-head-on-one-6"]
---
# KazQAD: Kazakh Open-Domain Question Answering Dataset

[arXiv](https://arxiv.org/abs/2404.04487)
**Topics:** [[embed-sota]], [[embed-kazakh]], [[decoder-to-embedder]], [[joint-generative-embedding-head-on-one-6]]

> [!abstract]
> We introduce KazQAD -- a Kazakh open-domain question answering (ODQA) dataset -- that can be used in both reading comprehension and full ODQA settings, as well as for information retrieval experiments. KazQAD contains just under 6,000 unique questions with extracted short answers and nearly 12,000 passage-level relevance judgements. We use a combination of machine translation, Wikipedia search, an …

## Claims

> [!note] CLAIM — embed-sota
> KazQAD (ISSAI, LREC 2024) is the only native Kazakh retrieval benchmark: ~6,000 unique questions (NQ-translated train + original Kazakh UNT exam dev/test), ~12,000 passage-level relevance judgments, 800k+ Kazakh Wikipedia passages. Published retrieval baselines are weak: NDCG@10 = 0.389, MRR = 0.382 — large headroom for a Kazakh-native embedder. CC BY-SA licensed.
>
> **Numbers:** 6k questions, 12k qrels, 800k passages; NDCG@10 0.389, MRR 0.382; reading comprehension EM 38.5 / F1 54.2.
> **Relevance:** Ready-made retrieval eval + training qrels for the Kazakh embedder; converting it to an MTEB task is a cheap, high-visibility contribution.
> **Source:** https://arxiv.org/abs/2404.04487; https://github.com/IS2AI/KazQAD · **Sweep:** `embeddings-2026-07`

> [!note] CLAIM — embed-kazakh
> KazQAD (ISSAI) is the only real Kazakh ODQA/IR dataset: ~6,000 unique questions, ~12,000 passage-level qrels, corpus of 800k+ Kazakh Wikipedia passages, plus 61k machine-translated Natural Questions triples. Splits in issai/kazqad-retrieval: 3,487 train / 548 val / 1,929 test queries. Published retrieval baseline is weak: NDCG@10 = 0.389, MRR = 0.382. It is NOT integrated into MTEB.
>
> **Numbers:** 6k questions; 12k qrels; 800k passages; 61k MT-NQ triples; baseline NDCG@10 0.389 / MRR 0.382; reading comprehension EM 38.5 / F1 54.2
> **Relevance:** Primary supervised retrieval train/test set AND the hard-negative mining corpus (800k passages); contributing it to MTEB is a free paper milestone.
> **Source:** arXiv:2404.04487; huggingface.co/datasets/issai/kazqad-retrieval (CC-BY-SA-4.0) · **Sweep:** `embeddings-2026-07`

> [!note] CLAIM — embed-kazakh
> Kazakh Wikipedia has 244,167 articles (668,261 pages) as of 2026-07-03 — the source of KazQAD's 800k-passage corpus — usable for ~0.5-1M synthetic title-lead/section-title/query-passage pairs and as the hard-negative mining pool.
>
> **Numbers:** 244,167 articles; 668,261 pages; 800k+ passages in KazQAD corpus
> **Relevance:** Only large clean monolingual pair source for synthetic query generation (doc2query with the project's own generative SLM closes the loop between the two deliverables).
> **Source:** kk.wikipedia.org siteinfo API (live query 2026-07-03); arXiv:2404.04487 · **Sweep:** `embeddings-2026-07`

> [!note] CLAIM — decoder-to-embedder
> KazQAD is ready-made raw material for the retrieval part of kkMTEB: ~6,000 questions, ~12,000 passage-level relevance judgments, 800K+ Kazakh Wikipedia passages; published baselines are weak (BM25/neural retrieval NDCG@10 = 0.389, MRR = 0.382; ODQA EM = 17.8).
>
> **Numbers:** 6K questions, 12K qrels, 800K passages; NDCG@10 0.389.
> **Relevance:** Drop-in retrieval benchmark + hard-negative mining source + the headroom (0.389 NDCG@10) shows how beatable current Kazakh retrieval is.
> **Source:** arXiv 2404.04487 (KazQAD); github.com/IS2AI/KazQAD · **Sweep:** `embeddings-2026-07`

> [!note] CLAIM — joint-generative-embedding-head-on-one-6
> [tested-on-Kazakh] The true KazQAD gap under the lab's pinned protocols is UNMEASURED: evallab's canonical protocols are (a) KazQADRetrieval — full 825,309-passage corpus, 1,929 test queries, issai/kazqad-retrieval @ a3999685, comparable to the paper's baselines, and (b) KazQAD-HardNeg 'kazqad-hardneg-bm25-v1' — judged-pool candidates, BM25 Lucene-idf k1=1.5 b=0.75, gold positives + top BM25 negatives to 100 candidates, seed 13, MRR@10. Under (a) the ONLY existing number for any model is the paper's BM25+reranker NDCG@10 0.389 / MRR 0.382 (provenance: reported); under (b) mE5-large's 0.909 MRR is a third-party model-card number with unpublished pools (same lineage reports 0.4490-0.9189 depending on candidate construction). Zero dense embedders have measured evallab records (results/ holds 3 JSONs, none dense-retrieval measured). Web search (2026-07-04, en+ru) confirms no published full-corpus KazQAD dense-retrieval numbers exist anywhere.
>
> **Numbers:** Full-corpus anchor: NDCG@10 0.389 / MRR 0.382 (BM25+reranker, reported). Hard-neg anchor: mE5-large MRR 0.909 [reported, pools unpublished; 0.4490 under HardTFIDF99 vs 0.9189 under KazQAD-100-local in successor card]. Measured dense baselines under lab protocol: 0.
> **Relevance:** The embedding deliverable's target number does not exist yet — the design panel cannot fix a win condition until mE5-large/BGE-M3/Qwen3-Emb-0.6B are run through evallab; this is a ~2-3 GPU-hour Kaggle job and the single highest-leverage prerequisite.
> **Source:** evallab/src/kazeval/hardneg.py, evallab/src/kazeval/tasks/kazqad_retrieval.py, evallab/README.md + results/*.json; arXiv:2404.04487; web sweep 2026-07-04 · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[kazmmlu-evaluating-language-models-on-kazakh-russian-and-regional-knowledge-of|KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhst…]] — The two Kazakh axes a joint ≤600M head must serve simultaneously — KazQAD (retrieval) and KazMMLU (generation)
- [[mmteb-massive-multilingual-text-embedding-benchmark|MMTEB: Massive Multilingual Text Embedding Benchmark]] — KazQAD is NOT integrated into MMTEB — the retrieval gap the lab's kkMTEB upstream PR is meant to fill
- [[huggingface-co-datasets-issai-ragbench-kazakh|huggingface.co/datasets/issai/RAGBench_Kazakh]] — Both ISSAI Kazakh retrieval resources; KazQAD supplies the ODQA questions + qrels, RAGBench the RAG eval layer
- [[huggingface-co-api-datasets-issai-kazqad-retrieval-issai|huggingface.co/api/datasets/issai/kazqad-retrieval, .../issai/kazparc…]] — source-of: issai/kazqad-retrieval is the HF release of the KazQAD paper's ~815k-passage open-domain QA corpus
- [[lm-eval-0-4-11-installed-package-registry-inspection-2026|lm-eval 0.4.11 installed-package registry inspection, 2026-07-03]] — kazqad is one of the three task names absent from the lm-eval registry, blocking KazQAD retrieval eval until custom-wired

[[Home]]
