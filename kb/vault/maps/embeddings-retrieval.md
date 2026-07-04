---
type: "moc"
topic: "embeddings-retrieval"
nodes: 4
papers: 0
sources: 4
uncertain_claims: 1
tags: ["moc"]
---
# Topic: embeddings-retrieval

The Kazakh embedding frontier is thin and protocol-fragile. Only one dedicated Kazakh embedder exists — Nurlykhan/kazembed-v5, mE5-base (278M) fine-tuned on 61,255 pairs with MultipleNegativesRankingLoss, reporting KazQAD MRR 0.835 (+2.1% over base e5); no from-scratch Kazakh embedder exists anywhere. The widely-cited "mE5-large MRR 0.909 on KazQAD hard negatives" is REFUTED as a stable number: it traces solely to the kazembed-v5 model card (a 289-download hobby artifact, one-line protocol), and its own successor lineage (shyngys879) shows the same model swings from MRR 0.4490 under HardTFIDF99 to 0.9189 under an easier KazQAD-100 local pool — so hard-negative MRR is protocol-defined, not model-defined, and evallab therefore pins BOTH full-corpus retrieval (paper baseline MRR 0.382) and a fixed BM25 hard-negative recipe. Feedstock is real but constrained: issai/kazqad-retrieval, issai/kazqad, issai/kazparc are all HF-gated (cc-by-sa-4.0 share-alike propagates; KazParC HF license is UNVERIFIED), splitting 3487/548/1929 queries over ~815k passages. Eval infrastructure is weak: MTEB's WebFAQRetrieval kaz split is only 300 queries / 2,995 docs / 1 qrel each (secondary-eval only), and PaDaS-Lab webfaq kaz (12,510 pairs) is usable for training but must be deduped against those test queries. Open question: fixing and publishing the canonical candidate-pool construction so any "beat 0.909" target becomes meaningful.

## Frontier highlights
- [[huggingface-co-shyngys879-kazakh-e5-rag-embedding-model|huggingface.co/shyngys879/kazakh-e5-rag-embedding (model card, fetched…]] — Proves hard-negative MRR is protocol-defined: same mE5-large is 0.449 vs 0.919 by candidate pool
- [[huggingface-co-nurlykhan-kazembed-v5-apache-2-0|huggingface.co/Nurlykhan/kazembed-v5 (apache-2.0)]] — Only dedicated Kazakh embedder (278M, MRR 0.835) AND sole origin of the disputed 0.909 planka number
- [[huggingface-co-api-datasets-issai-kazqad-retrieval-issai|huggingface.co/api/datasets/issai/kazqad-retrieval, .../issai/kazparc…]] — KazQAD/KazParC feedstock is HF-gated with cc-by-sa share-alike; ~815k passages, 3487/548/1929 splits
- [[huggingface-co-datasets-mteb-webfaqretrieval|huggingface.co/datasets/mteb/WebFAQRetrieval]] — MTEB kaz retrieval eval too tiny (300q/2995d) for a headline; webfaq pairs need dedup vs test

## Sources & findings (4)
- [[huggingface-co-api-datasets-issai-kazqad-retrieval-issai|huggingface.co/api/datasets/issai/kazqad-retrieval, .../issai/kazparc…]] — All three ISSAI feedstock datasets are GATED on HF (gated:auto — instant self-approval, but load_dataset() raises GatedR…
- [[huggingface-co-datasets-mteb-webfaqretrieval|huggingface.co/datasets/mteb/WebFAQRetrieval]] — MTEB's existing WebFAQRetrieval kaz split is tiny (300 queries, 2,995 docs, 1 qrel/query) — usable only as a secondary e…
- [[huggingface-co-nurlykhan-kazembed-v5-apache-2-0|huggingface.co/Nurlykhan/kazembed-v5 (apache-2.0)]] — The only dedicated Kazakh embedder found is Nurlykhan/kazembed-v5: multilingual-e5-base (278M) fine-tuned on just 61,255…
- [[huggingface-co-shyngys879-kazakh-e5-rag-embedding-model|huggingface.co/shyngys879/kazakh-e5-rag-embedding (model card, fetched…]] — Hard-negatives MRR on KazQAD is protocol-defined, not model-defined: the successor card of the same lineage (shyngys879/…

[[Home]]
