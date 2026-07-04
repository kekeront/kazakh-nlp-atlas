---
type: "moc"
topic: "embed-kazakh"
nodes: 15
papers: 6
sources: 9
uncertain_claims: 5
tags: ["moc"]
---
# Topic: embed-kazakh

Kazakh embedding is a near-greenfield with a thin but concrete evidence base. Established: KazQAD is the ONLY native kk retrieval benchmark (800k Wikipedia passages, ~6k questions, weak published baseline NDCG@10 0.389 / MRR 0.382), with WebFAQRetrieval-kaz as the second signal (~12.5k QA pairs, mE5-large nDCG@10 0.7269); the real ≤600M competitive bar on the main public signal (BelebeleRetrieval kaz_Cyrl) is BGE-M3 (568M) at 0.9017, with same-size Qwen3-Embedding-0.6B ~15 pts behind (0.7545) and EmbeddingGemma-300m at 0.6839. The only dedicated kk embedder that exists is Nurlykhan/kazembed-v5 — a naive mE5-base (278M) MNRL fine-tune on 61k pairs (KazQAD MRR 0.835); no from-scratch kk embedder, no kk reranker, and no kk STS/NLI dataset exist at all (XNLI's 15 and MUSTS's 13 languages both exclude kk). Contested/not-a-foundation: the widely-cited "mE5-large MRR 0.909 on KazQAD hard-negs" traces solely to that hobby HF card with unpublished candidate pools (same lineage spans 0.449–0.919), and no dense embedder has a measured record under evallab's pinned full-corpus + hardneg-bm25-v1 protocols (uncertain). The data ceiling — ~0.6M clean pairs (KazParC 372k anchor) + synthetic Wikipedia + filtered NLLB, 10–50x below SOTA English/Chinese recipes — makes teacher distillation structurally necessary (flagged uncertain). Open question: stand up native kk retrieval SOTA and a kk-MTEB from the KazQAD/WebFAQ/Belebele/KazSAnDRA seeds under reproducible protocols.

## Frontier highlights
- [[huggingface-co-nurlykhan-kazembed-v5-apache-2-0|huggingface.co/Nurlykhan/kazembed-v5 (apache-2.0)]] — The only dedicated kk embedder that exists: naive mE5-base fine-tune, MRR 0.835 — the entire field's current artifact
- [[kazqad-kazakh-open-domain-question-answering-dataset|KazQAD: Kazakh Open-Domain Question Answering Dataset]] — Only native kk retrieval benchmark (800k passages); weak 0.389 baseline = the headroom the embed pillar targets
- [[per-model-belebeleretrieval-json-files-extracted-2026-07-03|per-model BelebeleRetrieval.json files (extracted 2026-07-03)]] — Sets the real ≤600M bar: BGE-M3 0.9017 vs Qwen3-0.6B 0.7545 on BelebeleRetrieval kaz
- [[xnli-evaluating-cross-lingual-sentence-representations|XNLI: Evaluating Cross-lingual Sentence Representations]] — Structural gap: zero kk STS and zero kk NLI datasets exist anywhere — blocks a TurkEmbed-style recipe
- [[mmteb-massive-multilingual-text-embedding-benchmark|MMTEB: Massive Multilingual Text Embedding Benchmark]] — Kazakh is absent from MTEB/MMTEB as first-class; kk-MTEB must be built, not found
- [[webfaq-a-multilingual-collection-of-natural-q-a-datasets-for-dense-retrieval|WebFAQ: A Multilingual Collection of Natural Q&A Datasets for Dense Retrieval]] — Second kk retrieval task and largest NATURAL kk paired data (~12.5k WebFAQ QA pairs)

## Papers (6)
- [[mmteb-massive-multilingual-text-embedding-benchmark|MMTEB: Massive Multilingual Text Embedding Benchmark]] (2025) — embed-kazakh
- [[webfaq-a-multilingual-collection-of-natural-q-a-datasets-for-dense-retrieval|WebFAQ: A Multilingual Collection of Natural Q&A Datasets for Dense Retrieval]] (2025) — embed-sota
- [[kazsandra-kazakh-sentiment-analysis-dataset-of-reviews-and-attitudes|KazSAnDRA: Kazakh Sentiment Analysis Dataset of Reviews and Attitudes]] (2024) — embed-kazakh
- [[kazparc-kazakh-parallel-corpus-for-machine-translation|KazParC: Kazakh Parallel Corpus for Machine Translation]] (2024) — embed-kazakh
- [[kazqad-kazakh-open-domain-question-answering-dataset|KazQAD: Kazakh Open-Domain Question Answering Dataset]] (2024) — embed-sota
- [[xnli-evaluating-cross-lingual-sentence-representations|XNLI: Evaluating Cross-lingual Sentence Representations]] (2018) — embed-kazakh

## Sources & findings (9)
- [[huggingface-co-kz-transformers-kaz-roberta-conversational|huggingface.co/kz-transformers/kaz-roberta-conversational]] — Kaz-RoBERTa-conversational (kz-transformers) is the strongest monolingual kk encoder backbone: base-size RoBERTa pretrai…
- [[huggingface-co-ai-forever-frida|huggingface.co/ai-forever/FRIDA]] — Russian embedders do not cover Kazakh: FRIDA (ai-forever) and ru-en-RoSBERTa are ru/en models; Giga-Embeddings developer…
- [[huggingface-co-datasets-issai-ragbench-kazakh|huggingface.co/datasets/issai/RAGBench_Kazakh]] — issai/RAGBench_Kazakh (Apr 2026) is a machine-translated Kazakh port of RAGBench: 11,431 test examples in 12 domain subs…
- [[huggingface-co-nurlykhan-kazembed-v5-apache-2-0|huggingface.co/Nurlykhan/kazembed-v5 (apache-2.0)]] — The only dedicated Kazakh embedder found is Nurlykhan/kazembed-v5: multilingual-e5-base (278M) fine-tuned on just 61,255…
- [[huggingface-co-spaces-batyrme-kazteb-401|huggingface.co/spaces/batyrme/kazteb (401)]] — A Kazakh text-embedding leaderboard named KazTEB exists in name (HF Space batyrme/kazteb, indexed by Google) but returns…
- [[hf-datasets-api-metadata-2026-07-03|HF datasets API metadata 2026-07-03]] — Kazakh instruction/dialogue pair data is small and mostly machine-translated: AmanMussa/kazakh-instruction-v2 (10k-100k…
- [[hf-models-api-search-2026-07-03|HF models API search 2026-07-03]] — Zero Kazakh rerankers exist: HF search for 'kazakh reranker' returns no models; no cross-encoder trained on KazQAD is pu…
- [[huggingface-co-models-language-kk-library-sentence|huggingface.co/models?language=kk&library=sentence-transformers (2026-…]] — 289 sentence-transformers models on HF are tagged kk, but the top-downloaded ones are all generic multilingual models (m…
- [[per-model-belebeleretrieval-json-files-extracted-2026-07-03|per-model BelebeleRetrieval.json files (extracted 2026-07-03)]] — Current best scores on the main public Kazakh retrieval signal, BelebeleRetrieval kaz_Cyrl→kaz_Cyrl (nDCG@10, official m…

## Related topics
- [[decoder-to-embedder]] — 2 shared nodes
- [[embed-sota]] — 2 shared nodes

[[Home]]
