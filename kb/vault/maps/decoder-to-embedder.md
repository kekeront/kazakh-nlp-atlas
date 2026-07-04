---
type: "moc"
topic: "decoder-to-embedder"
nodes: 19
papers: 16
sources: 3
uncertain_claims: 2
tags: ["moc"]
---
# Topic: decoder-to-embedder

The topic covers converting causal decoder LMs into text embedders, directly relevant to reusing a QymyzLM Qwen3-0.6B backbone as the embedding head. Established mechanics: post-hoc conversion works cheaply (LLM2Vec: S-LLaMA-1.3B hits 49.42 unsup / 61.96 sup MTEB, MNTP in 1000 steps), a 0.5B decoder can be a top multilingual embedder (KaLM), and Qwen3-Embedding-0.6B (64.33 MMTEB, causal + last-token EOS pooling, initialized from Qwen3-0.6B-Base) is the concrete sub-600M target. There is broad recipe convergence (multi-stage contrastive pretrain → hard-negative SFT → slerp checkpoint merge → MRL → instruction prefixes → distillation). The contested frontier is two-fold: (1) pooling/attention at ≤1B is unsettled — Qwen3 reports causal+EOS "on par," but LLM2Vec/KaLM-V2 strip the causal mask (bidirectional+mean) and score higher, though never iso-controlled; and (2) joint generation+embedding — GRIT proves it lossless at 7B (MTEB 66.8 + gen 55.5), but Hydra's controlled 0.8B/4B ablation finds joint training COLLAPSES generation under LoRA, motivating a frozen-base + LoRA-adapter switch instead. Open questions: no recipe integrates contrastive objectives INTO pretraining at scale (LLM-JEPA only exploratory), no GRIT replication below 7B exists, and on the only public Kazakh signal Qwen3-Emb-0.6B loses badly to same-size encoders (Belebele kaz nDCG@10 0.7545 vs BGE-M3 0.9017) — LRL specialization yields only thin margins (AfriE5 +1.1/+1.7, kazembed-v5 +2.1%, TR-MTEB fails to beat mE5).

## Frontier highlights
- [[qwen3-embedding-advancing-text-embedding-and-reranking-through-foundation-models|Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Model…]] — Qwen3-Embedding-0.6B: the sub-600M target, shared-backbone decoder→embedder, and the unsettled causal+EOS vs bidir+mean ablation
- [[hydra-unifying-document-retrieval-and-generation-in-a-single-vision-language|Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Mo…]] — Hydra: only controlled joint-vs-separate test at OUR scale — generation collapses at 0.8B, fix is frozen base + LoRA adapter
- [[generative-representational-instruction-tuning|Generative Representational Instruction Tuning]] — GRIT: joint gen+embed lossless proof, but ONLY at 7B+; the claim Hydra contests at sub-1B
- [[llm2vec-large-language-models-are-secretly-powerful-text-encoders|LLM2Vec: Large Language Models Are Secretly Powerful Text Encoders]] — LLM2Vec: cheapest conversion with sub-2B numbers; mean>last-token, bidirectional-without-training hurts
- [[causal2vec-improving-decoder-only-llms-as-embedding-models-through-a-contextual|Causal2Vec: Improving Decoder-only LLMs as Embedding Models through a Contextual…]] — Causal2Vec: contextual token, zero surgery on causal mask, cuts sequence 85% vs echo-style
- [[kalm-embedding-superior-training-data-brings-a-stronger-embedding-model|KaLM-Embedding: Superior Training Data Brings A Stronger Embedding Model]] — KaLM-Embedding: existence proof a 0.5B decoder (our size) tops sub-1B multilingual after mask removal

## Papers (16)
- [[hydra-unifying-document-retrieval-and-generation-in-a-single-vision-language|Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model]] (2026) — decoder-to-embedder
- [[kalm-embedding-superior-training-data-brings-a-stronger-embedding-model|KaLM-Embedding: Superior Training Data Brings A Stronger Embedding Model]] (2025) — decoder-to-embedder
- [[mmteb-massive-multilingual-text-embedding-benchmark|MMTEB: Massive Multilingual Text Embedding Benchmark]] (2025) — embed-kazakh
- [[qwen3-embedding-advancing-text-embedding-and-reranking-through-foundation-models|Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models]] (2025) — embed-sota
- [[causal2vec-improving-decoder-only-llms-as-embedding-models-through-a-contextual|Causal2Vec: Improving Decoder-only LLMs as Embedding Models through a Contextual Token]] (2025) — decoder-to-embedder
- [[llm-jepa-large-language-models-meet-joint-embedding-predictive-architectures|LLM-JEPA: Large Language Models Meet Joint Embedding Predictive Architectures]] (2025) — decoder-to-embedder
- [[afrimteb-and-afrie5-benchmarking-and-adapting-text-embedding-models-for-african|AfriMTEB and AfriE5: Benchmarking and Adapting Text Embedding Models for African Languages]] (2025) — decoder-to-embedder
- [[generative-representational-instruction-tuning|Generative Representational Instruction Tuning]] (2024) — decoder-to-embedder
- [[repetition-improves-language-model-embeddings|Repetition Improves Language Model Embeddings]] (2024) — decoder-to-embedder
- [[kazqad-kazakh-open-domain-question-answering-dataset|KazQAD: Kazakh Open-Domain Question Answering Dataset]] (2024) — embed-sota
- [[llm2vec-large-language-models-are-secretly-powerful-text-encoders|LLM2Vec: Large Language Models Are Secretly Powerful Text Encoders]] (2024) — decoder-to-embedder
- [[nv-embed-improved-techniques-for-training-llms-as-generalist-embedding-models|NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models]] (2024) — decoder-to-embedder
- [[the-russian-focused-embedders-exploration-rumteb-benchmark-and-russian|The Russian-focused embedders' exploration: ruMTEB benchmark and Russian embedding model design]] (2024) — decoder-to-embedder
- [[late-chunking-contextual-chunk-embeddings-using-long-context-embedding-models|Late Chunking: Contextual Chunk Embeddings Using Long-Context Embedding Models]] (2024) — decoder-to-embedder
- [[improving-text-embeddings-with-large-language-models|Improving Text Embeddings with Large Language Models]] (2023) — decoder-to-embedder
- [[an-empirical-study-of-tokenization-strategies-for-various-korean-nlp-tasks|An Empirical Study of Tokenization Strategies for Various Korean NLP Tasks]] (2020) — decoder-to-embedder

## Sources & findings (3)
- [[huggingface-co-blog-embedding-quantization|huggingface.co/blog/embedding-quantization]] — Matryoshka + quantization is a near-free market feature: int8 scalar quantization loses almost nothing (recall -1.46%, M…
- [[aclanthology-org-2025-findings-emnlp-471-tr-mteb-emnlp-2025|aclanthology.org/2025.findings-emnlp.471 (TR-MTEB, EMNLP 2025 Findings…]] — TR-MTEB (closest Turkic analogue) is a second warning: 26 Turkish datasets, 6 task types, a corpus of 34.2M weakly super…
- [[researchgate-publication-396213005-comparative-analysis-of|ResearchGate publication 396213005 (Comparative Analysis of Embedding…]] — Multilingual embedders underperform on Kazakh today: a 2025 comparative study on ~7,700 Kazakh question-context pairs (i…

## Related topics
- [[joint-generative-embedding-head-on-one-6]] — 4 shared nodes
- [[embed-kazakh]] — 2 shared nodes
- [[embed-sota]] — 2 shared nodes
- [[embeddings-training]] — 2 shared nodes

[[Home]]
