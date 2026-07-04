---
kb_id: "arxiv:2506.20923"
type: "paper"
title: "KaLM-Embedding-V2: Superior Training Techniques and Data Inspire A Versatile Embedding Model"
arxiv_id: "2506.20923"
doi: null
hf_repo: "HIT-TMG/KaLM-embedding-multilingual-mini-instruct-v2"
year: 2025
topics: ["embed-sota", "embeddings-training"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["KaLM-Embedding-V2: Superior Training Techniques and Data Inspire A Versatile Embedding Model", "arXiv:2506.20923", "arxiv:2506.20923"]
tags: ["paper", "topic/embed-sota", "topic/embeddings-training"]
---
# KaLM-Embedding-V2: Superior Training Techniques and Data Inspire A Versatile Embedding Model

[arXiv](https://arxiv.org/abs/2506.20923)
**Topics:** [[embed-sota]], [[embeddings-training]]

> [!abstract]
> Recent advancements in Large Language Models (LLMs)-based text embedding models primarily focus on data scaling or synthesis, yet limited exploration of training techniques and data quality, thereby constraining performance. In this work, we propose KaLM-Embedding-V2, a series of versatile and compact embedding models, systematically incentivizing advanced embedding capability in LLMs by superior …

## Claims

> [!note] CLAIM — embed-sota
> KaLM-Embedding-V2 (HIT/Tencent) is the closest architectural template to the project's plan: Qwen2-0.5B decoder converted to a bidirectional-attention encoder with mean pooling, 896d with MRL (896/512/256/128/64), 32k context. Recipe: weakly-supervised pretraining on 20 data categories -> SFT on 100 categories -> model-soup averaging; innovations: focal-style reweighting of hard examples and ONLINE hard-negative mixing (no offline mining cost). SOTA under 1B on MTEB(cmn,v1) and MTEB(eng,v1). The same team's Gemma3-12B version is now MMTEB #1 (72.32), proving the recipe scales.
>
> **Numbers:** 0.5B params, 896d, 32k ctx; MMTEB #1 overall for the 12B sibling at 72.32.
> **Relevance:** Direct proof that a ~500M decoder SLM (like KazLLM-v2's backbone) converts into a top-tier embedder via bidirectional attention + mean pooling + 2-stage contrastive — the shared-backbone strategy in the project goal is validated practice.
> **Source:** https://arxiv.org/pdf/2506.20923; https://huggingface.co/HIT-TMG/KaLM-embedding-multilingual-mini-instruct-v2 · **Sweep:** `embeddings-2026-07`

> [!note] CLAIM — embeddings-training
> KaLM-Embedding-V2 is the current SOTA general embedder under 1B and the strongest published recipe on the SAME 0.5B-decoder class QymyzLM targets: Qwen2-0.5B (494M) with the causal mask REMOVED (bidirectional attention) + simple mean pooling + Matryoshka in both contrastive and KL losses. Trained ~470M pre-train pairs (InfoNCE, in-batch negatives) -> ~6M fine-tune pairs with hard negatives -> contrastive DISTILLATION from Qwen3-Embedding-8B teacher on the same 6M. Adds focal-style difficulty reweighting + online hard-negative mixing (Beta(2,2) pair-wise blend).
>
> **Numbers:** 494M (Qwen2-0.5B), emb dim 896; MTEB avg 67.81 (v2), SOTA <1B; beats gte-Qwen2-1.5B(3x), e5-mistral-7b(14x); pre-train ~470M pairs, fine-tune ~6M, distill teacher Qwen3-Embedding-8B; Matryoshka keeps quality at 256-dim; focal weight w=(1-e^{s/τ}/Z)^γ
> **Relevance:** TRANSFERABLE-UNTESTED. Directly contradicts Qwen3-Embedding's causal+EOS choice: at 0.5B, KaLM WINS with bidirectional+mean pooling + teacher distillation. Distilling from Qwen3-Embedding-8B (or mE5-large) is a free-compute-friendly way to lift a 0.5B Kazakh head. This is the single best-matched recipe for v1 (QymyzLM head).
> **Source:** arXiv:2506.20923 (KaLM-Embedding-V2, html v3); HF HIT-TMG/KaLM-embedding-multilingual-mini-instruct-v2 · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[llm2vec-large-language-models-are-secretly-powerful-text-encoders|LLM2Vec: Large Language Models Are Secretly Powerful Text Encoders]] — Both strip the causal mask (bidirectional) + mean pooling to convert a decoder; iso-scale 0.5B evidence bidir+mean beats causal+EOS
- [[qwen3-embedding-advancing-text-embedding-and-reranking-through-foundation-models|Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models]] — KaLM-V2 removes the causal mask (bidir+mean) and beats Qwen3-Emb-0.6B 67.81 vs 64.33, contesting 'causal attention is on par'
- [[kalm-embedding-superior-training-data-brings-a-stronger-embedding-model|KaLM-Embedding: Superior Training Data Brings A Stronger Embedding Model]] — KaLM-V2 succeeds KaLM-Embedding v1, adding focal reweighting, online hard-neg mixing, and Qwen3-Emb-8B distillation

[[Home]]
