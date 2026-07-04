---
kb_id: "doi:10.36227/techrxiv.175942902.25827042"
type: "source"
title: "huggingface.co/kz-transformers/kaz-roberta-conversational"
doi: "10.36227/techrxiv.175942902.25827042"
hf_repo: "kz-transformers/kaz-roberta-conversational"
year: null
topics: ["embed-kazakh"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["doi:10.36227/techrxiv.175942902.25827042"]
tags: ["source", "topic/embed-kazakh"]
---
# huggingface.co/kz-transformers/kaz-roberta-conversational

**Topics:** [[embed-kazakh]]

## Source URLs
- huggingface.co/kz-transformers/kaz-roberta-conversational
- techrxiv.org/doi/full/10.36227/techrxiv.175942902.25827042

## Findings

> [!note] CLAIM — embed-kazakh
> Kaz-RoBERTa-conversational (kz-transformers) is the strongest monolingual kk encoder backbone: base-size RoBERTa pretrained from scratch on 25GB of Kazakh + kk-ru code-switched telecom dialogues, 52k BPE tokenizer, MLM objective (technical report Oct 2025). No sentence-embedding training was ever applied to it.
>
> **Numbers:** 25GB corpus; 52k BPE vocab; base size (~125M)
> **Relevance:** Useful ablation baseline (monolingual encoder + contrastive FT) against your decoder-backbone embedder; also evidence that code-switched kk-ru pretraining data exists.
> **Source:** huggingface.co/kz-transformers/kaz-roberta-conversational; techrxiv.org/doi/full/10.36227/techrxiv.175942902.25827042 · **Sweep:** `embeddings-2026-07`

## Related
- [[frontiers-pmc12741073-hybrid-ai-architectures-for-automatic|Frontiers/PMC12741073 (Hybrid AI architectures for automatic text corr…]] — The hybrid analyzer's top-accuracy stage (92.3%) stacks KazRoBERTa on FST+CRF — this is that KazRoBERTa model's card
- [[llm2vec-large-language-models-are-secretly-powerful-text-encoders|LLM2Vec: Large Language Models Are Secretly Powerful Text Encoders]] — kaz-roberta is the strongest monolingual kk encoder but never got sentence-embedding training; LLM2Vec-style conversion is the missing step

[[Home]]
