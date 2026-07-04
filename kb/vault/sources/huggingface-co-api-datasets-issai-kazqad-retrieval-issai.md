---
kb_id: "hf:api/datasets"
type: "source"
title: "huggingface.co/api/datasets/issai/kazqad-retrieval, .../issai/kazparc…"
doi: null
hf_repo: "api/datasets"
year: null
topics: ["embeddings-retrieval"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["hf:api/datasets"]
tags: ["source", "topic/embeddings-retrieval"]
---
# huggingface.co/api/datasets/issai/kazqad-retrieval, .../issai/kazparc…

**Topics:** [[embeddings-retrieval]]

## Source URLs
- huggingface.co/api/datasets/issai/kazqad-retrieval, .../issai/kazparc (API responses, 2026-07-03)
- 403 responses verified with authenticated token

## Findings

> [!note] CLAIM — embeddings-retrieval
> All three ISSAI feedstock datasets are GATED on HF (gated:auto — instant self-approval, but load_dataset() raises GatedRepoError and datasets-server refuses /info and /rows until 'Agree and access' is clicked per account): issai/kazqad-retrieval, issai/kazqad, issai/kazparc. Licenses: KazQAD repos cc-by-sa-4.0 (share-alike propagates to derived corpora); KazParC HF repo carries NO license tag — the GitHub badge claims CC BY 4.0 but this is unverified on HF.
>
> **Numbers:** 3 gated datasets; kazqad-retrieval splits 3487/548/1929 queries; corpus file kazqad-corpus-v1.0-kk.jsonl.gz = 136.7MB gz (~815k passages per paper, exact count unverified)
> **Relevance:** Blocks any training/eval run until one-click gate acceptance under the lab's HF account; also licensing input for model release (share-alike).
> **Source:** huggingface.co/api/datasets/issai/kazqad-retrieval, .../issai/kazparc (API responses, 2026-07-03); 403 responses verified with authenticated token · **Sweep:** `2026-07-eval-provenance`

## Related
- [[kazparc-kazakh-parallel-corpus-for-machine-translation|KazParC: Kazakh Parallel Corpus for Machine Translation]] — source-of: issai/kazparc is the HF release of the KazParC Kazakh parallel corpus paper
- [[kazqad-kazakh-open-domain-question-answering-dataset|KazQAD: Kazakh Open-Domain Question Answering Dataset]] — source-of: issai/kazqad-retrieval is the HF release of the KazQAD paper's ~815k-passage open-domain QA corpus
- [[huggingface-co-datasets-issai-ragbench-kazakh|huggingface.co/datasets/issai/RAGBench_Kazakh]] — sibling ISSAI Kazakh retrieval/RAG feedstock dataset from the same lab lineage
- [[grep-of-evallab-2026-07-04|grep of evallab (2026-07-04)]] — The pinned protocol reads issai/kazqad-retrieval @ a3999685; this dataset-API source is the provenance for the 825k-passage full corpus

[[Home]]
