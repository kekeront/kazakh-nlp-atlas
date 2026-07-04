---
type: "moc"
topic: "joint-generative-embedding-head-on-one-6"
nodes: 7
papers: 6
sources: 1
uncertain_claims: 1
tags: ["moc"]
---
# Topic: joint-generative-embedding-head-on-one-6

The frontier question is whether ONE model ≤600M active params can carry both a generative head and an MTEB-grade embedding head jointly. Positive evidence exists but only at large scale: GRIT (GritLM-7B) proves joint training loses nothing at 7B (MTEB 66.8 + gen 55.5, >60% RAG speedup via KV reuse, ~2x batch memory), and OneGen pushes the floor to Qwen2-1.5B where joint self-retrieval matches a Contriever pipeline WITHOUT degrading generation — but OneGen's retrieval is special-token contextual embedding, not a standalone dense embedder, and BPR beats InfoNCE precisely because InfoNCE restricts generation. The only controlled joint-vs-separate experiment near our scale REFUTES naive joint training: Hydra at 0.8B/4B found GritLM-style joint training collapses the generation mode, and its fix is NOT joint at all — freeze the base LM byte-for-byte (426/426 tensors) and switch to retrieval via a r=32 LoRA, i.e. two modes on shared weights (~-59% memory vs co-resident models). Qwen3-Embedding-0.6B confirms the shared-Qwen3-0.6B-backbone→embedder path but is embedding-ONLY (generation discarded, so a two-model datapoint, not joint) and loses badly on Kazakh (BelebeleRetrieval kaz nDCG@10 0.7545 vs BGE-M3 0.9017), the decoder-embedder LRL collapse that Less-is-More documents and fixes with 10k noisy pairs on mE5 — with Cyrillic code-switching Kazakh explicitly flagged untested. Open questions: no published joint gen+emb recipe below 1.5B, no recipe folding contrastive loss INTO pretraining at any scale, and KazQAD has ZERO measured dense-retrieval records under evallab's pinned protocols (KazQADRetrieval full-corpus, kazqad-hardneg-bm25-v1).

## Frontier highlights
- [[hydra-unifying-document-retrieval-and-generation-in-a-single-vision-language|Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Mo…]] — Only controlled joint-vs-separate at our scale: joint training collapses generation at 0.8B; fix is frozen base + r=32 LoRA
- [[generative-representational-instruction-tuning|Generative Representational Instruction Tuning]] — Positive existence proof of joint gen+emb (MTEB 66.8+gen 55.5, >60% RAG speedup) but ONLY at 7B+, no sub-7B replication
- [[onegen-efficient-one-pass-unified-generation-and-retrieval-for-llms|OneGen: Efficient One-Pass Unified Generation and Retrieval for LLMs]] — Smallest joint gen+retrieval without gen loss (Qwen2-1.5B); BPR>InfoNCE protects generation; not MTEB-grade embedder
- [[qwen3-embedding-advancing-text-embedding-and-reranking-through-foundation-models|Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Model…]] — Shared Qwen3-0.6B-backbone→embedder proof, but embedding-only (gen discarded) and fails Kazakh 0.7545 vs BGE-M3 0.9017
- [[less-is-more-adapting-text-embeddings-for-low-resource-languages-with-small|Less is More: Adapting Text Embeddings for Low-Resource Languages with Small Sca…]] — Decoder-embedder LRL collapse + the 10k-noisy-pair mE5 counter-recipe; Cyrillic code-switching Kazakh flagged untested
- [[kazqad-kazakh-open-domain-question-answering-dataset|KazQAD: Kazakh Open-Domain Question Answering Dataset]] — The Kazakh measurement target with ZERO dense-retrieval records under evallab's pinned full-corpus/hard-neg protocols

## Papers (6)
- [[less-is-more-adapting-text-embeddings-for-low-resource-languages-with-small|Less is More: Adapting Text Embeddings for Low-Resource Languages with Small Scale Noisy Synthetic D…]] (2026) — embed-sota
- [[hydra-unifying-document-retrieval-and-generation-in-a-single-vision-language|Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model]] (2026) — decoder-to-embedder
- [[qwen3-embedding-advancing-text-embedding-and-reranking-through-foundation-models|Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models]] (2025) — embed-sota
- [[generative-representational-instruction-tuning|Generative Representational Instruction Tuning]] (2024) — decoder-to-embedder
- [[kazqad-kazakh-open-domain-question-answering-dataset|KazQAD: Kazakh Open-Domain Question Answering Dataset]] (2024) — embed-sota
- [[onegen-efficient-one-pass-unified-generation-and-retrieval-for-llms|OneGen: Efficient One-Pass Unified Generation and Retrieval for LLMs]] (2024) — joint-generative-embedding-head-on-one-6

## Sources & findings (1)
- [[grep-of-home-altairzhambyl-projects-slms-qymyzlm-evallab|grep of /home/altairzhambyl/projects/SLMs/qymyzlm/evallab (2026-07-04)]] — PROTOCOL-NAME CONFLICT with the mission brief: the phrase 'TopK-PercPos protocol' appears NOWHERE in the evallab repo (g…

## Related topics
- [[decoder-to-embedder]] — 4 shared nodes
- [[embed-sota]] — 3 shared nodes

[[Home]]
