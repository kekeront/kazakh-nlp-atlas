---
type: "moc"
topic: "embed-sota"
nodes: 14
papers: 9
sources: 5
uncertain_claims: 4
tags: ["moc"]
---
# Topic: embed-sota

The general-purpose SOTA has converged on a reproducible sub-1B recipe: multi-stage contrastive training (weak-supervision pretrain on ~150-470M pairs → hard-negative SFT), InfoNCE with in-batch negatives and false-negative masking, Matryoshka dims, instruction prefixes, distillation, and slerp/model-souping — no top model (Qwen3-Embedding-0.6B 64.34 MMTEB, KaLM-V2 67.81, EmbeddingGemma 61.15, Granite R2, Arctic 2.0) skips more than one. Qwen3-Embedding-0.6B is the stable, beatable sub-600M target and an existence proof for the shared-backbone (Qwen3-0.6B → embedder) path, though it discards generation. The load-bearing REFUTATION for the Kazakh pillar: the newest decoder-derived embedders COLLAPSE on low-resource languages while old XLM-R-based mE5 holds — on Belebele kaz Qwen3-Emb scores nDCG@10 0.7545 vs BGE-M3 0.9017 / mE5-large-instruct 0.8949, and the MMTEB rank order inverts on Armenian (Qwen3-0.6B 47.38 vs mE5-large-it 72.99); AfriMTEB independently confirms this on African LRLs, cause being synthetic contrastive data skewed to high-resource languages. The cheapest winning path is Less-is-More: full-FT of mE5-base on just 10k noisy MT synthetic pairs + 0.5/0.5 base-weight-averaging (+11-12% avg, retrieval +35% rel., 1M pairs adds <1%). Open questions: (1) does noisy-alignment hold for Cyrillic LRLs sharing script with a high-resource neighbor (Kazakh/Russian code-switching) — explicitly flagged untested; (2) full-corpus KazQAD dense retrieval is UNMEASURED under the lab's pinned protocol (only BM25+reranker NDCG@10 0.389 exists; mE5's 0.909 MRR is a third-party number with unpublished candidate pools, 0.449-0.919 depending on pool). KazQAD is not integrated into MTEB, which has only 2 Kazakh text-retrieval tasks.

## Frontier highlights
- [[less-is-more-adapting-text-embeddings-for-low-resource-languages-with-small|Less is More: Adapting Text Embeddings for Low-Resource Languages with Small Sca…]] — Refutes decoder-embedder SOTA on LRLs; 10k-noisy-pair mE5 full-FT is cheapest path, flags Cyrillic/Kazakh untested
- [[qwen3-embedding-advancing-text-embedding-and-reranking-through-foundation-models|Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Model…]] — Qwen3-Embedding-0.6B: stable sub-600M target (64.34 MMTEB), shared-backbone proof, but loses on Kazakh Belebele
- [[kalm-embedding-v2-superior-training-techniques-and-data-inspire-a-versatile|KaLM-Embedding-V2: Superior Training Techniques and Data Inspire A Versatile Emb…]] — KaLM-V2: closest architectural template — Qwen2-0.5B causal-mask-removed → bidir+mean, 67.81 MTEB
- [[kazqad-kazakh-open-domain-question-answering-dataset|KazQAD: Kazakh Open-Domain Question Answering Dataset]] — Only native Kazakh retrieval benchmark; weak baseline NDCG@10 0.389; not in MTEB — the headroom target
- [[https-arxiv-org-html-2412-04506v2|https://arxiv.org/html/2412.04506v2]] — Arctic-Embed 2.0: empirical off-the-shelf leader on Kazakh retrieval per KAZ-QA-RAG
- [[mteb-pypi-package-mteb-get-tasks-languages-kaz-verified|mteb PyPI package, mteb.get_tasks(languages=['kaz']), verified locally…]] — Verified MTEB Kazakh inventory: 16 tasks, only 2 text-retrieval, 0 STS/reranking, KazQAD absent

## Papers (9)
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] (2026) — tokenizer-morphology
- [[less-is-more-adapting-text-embeddings-for-low-resource-languages-with-small|Less is More: Adapting Text Embeddings for Low-Resource Languages with Small Scale Noisy Synthetic D…]] (2026) — embed-sota
- [[webfaq-a-multilingual-collection-of-natural-q-a-datasets-for-dense-retrieval|WebFAQ: A Multilingual Collection of Natural Q&A Datasets for Dense Retrieval]] (2025) — embed-sota
- [[qwen3-embedding-advancing-text-embedding-and-reranking-through-foundation-models|Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models]] (2025) — embed-sota
- [[kalm-embedding-v2-superior-training-techniques-and-data-inspire-a-versatile|KaLM-Embedding-V2: Superior Training Techniques and Data Inspire A Versatile Embedding Model]] (2025) — embed-sota
- [[mmbert-a-modern-multilingual-encoder-with-annealed-language-learning|mmBERT: A Modern Multilingual Encoder with Annealed Language Learning]] (2025) — embed-sota
- [[embeddinggemma-powerful-and-lightweight-text-representations|EmbeddingGemma: Powerful and Lightweight Text Representations]] (2025) — embed-sota
- [[m3-embedding-multi-linguality-multi-functionality-multi-granularity-text|M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-…]] (2024) — embed-sota
- [[kazqad-kazakh-open-domain-question-answering-dataset|KazQAD: Kazakh Open-Domain Question Answering Dataset]] (2024) — embed-sota

## Sources & findings (5)
- [[https-huggingface-co-blog-ibm-granite-granite-embedding|https://huggingface.co/blog/ibm-granite/granite-embedding-multilingual…]] — Granite Embedding Multilingual R2 (IBM, 2026, Apache 2.0): ModernBERT-style encoders (alternating attention, RoPE, FA2)…
- [[https-arxiv-org-html-2412-04506v2|https://arxiv.org/html/2412.04506v2]] — Arctic-Embed 2.0 (Snowflake, Dec 2024): M 305M and L 568M multilingual retrievers with MRL applied at a single truncated…
- [[https-github-com-arailym-ray-kaz-qa-rag|https://github.com/Arailym-ray/KAZ-QA-RAG]] — KAZ-QA-RAG (2025) benchmarked BM25, BGE-M3, Arctic-Embed, E5, LaBSE, and text-embedding-3-large on KazQAD-style retrieva…
- [[mteb-pypi-package-mteb-get-tasks-languages-kaz-verified|mteb PyPI package, mteb.get_tasks(languages=['kaz']), verified locally…]] — VERIFIED by running the mteb library locally (July 2026): MTEB contains exactly 16 Kazakh tasks, of which only 11 are te…
- [[qwen3-embedding-paper|(Qwen3 Embedding paper)]] — Qwen3-Embedding-0.6B full spec: 28-layer decoder (Qwen3 base), last-token [EOS] pooling, 1024-dim output, 32K context, i…

## Related topics
- [[embeddings-training]] — 3 shared nodes
- [[joint-generative-embedding-head-on-one-6]] — 3 shared nodes
- [[decoder-to-embedder]] — 2 shared nodes
- [[embed-kazakh]] — 2 shared nodes

[[Home]]
