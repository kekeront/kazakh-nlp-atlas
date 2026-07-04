---
kb_id: "arxiv:2412.21140"
type: "paper"
title: "Facilitating large language model Russian adaptation with Learned Embedding Propagation"
arxiv_id: "2412.21140"
doi: null
hf_repo: null
year: 2024
topics: ["continual-pt-lowres-qlora-vs-full-cpt-re"]
claims: 1
uncertain_claims: 1
verdicts: []
aliases: ["Facilitating large language model Russian adaptation with Learned Embedding Propagation", "arXiv:2412.21140", "arxiv:2412.21140"]
tags: ["paper", "topic/continual-pt-lowres-qlora-vs-full-cpt-re"]
---
# Facilitating large language model Russian adaptation with Learned Embedding Propagation

[arXiv](https://arxiv.org/abs/2412.21140)
**Topics:** [[continual-pt-lowres-qlora-vs-full-cpt-re]]

> [!abstract]
> Rapid advancements of large language model (LLM) technologies led to the introduction of powerful open-source instruction-tuned LLMs that have the same text generation quality as the state-of-the-art counterparts such as GPT-4. While the emergence of such models accelerates the adoption of LLM technologies in sensitive-information environments the authors of such models don not disclose the traini …

## Claims

> [!warning] UNCERTAIN — continual-pt-lowres-qlora-vs-full-cpt-re
> [tested-on-Russian, kk/ru-adjacent] Learned Embedding Propagation (LEP, Tikhomirov & Chernyshev 2024): after vocab adaptation + limited CPT of the BASE model (deliberately limiting which parameters move), the learned embeddings are propagated/implanted directly into any existing INSTRUCT-tuned variant, skipping instruction tuning entirely. Tested on LLaMa-3-8B and Mistral-7B across 4 Russian tokenization variants; regains and sometimes exceeds the original instruct model's quality (Darumeru benchmark; competitive with OpenChat-3.5 and Llama-3-8B-Instruct); further gains from self-calibration + light continued instruct-tuning.
>
> **Numbers:** 2 backbones × 4 tokenization variants; benchmark = Darumeru (Russian); exact deltas in Fig.1/paper tables
> **Relevance:** Cheap route to a QymyzLM-Chat: do vocab+CPT once on Qwen3-0.6B-Base, then implant embeddings into Qwen3-0.6B (instruct) instead of building a Kazakh SFT corpus — untested on Kazakh and at 0.6B.
> **Source:** arXiv:2412.21140 (LEP) — method and results read from PDF text; exact per-benchmark numbers not extracted · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[trans-tokenization-and-cross-lingual-vocabulary-transfers-language-adaptation|Trans-Tokenization and Cross-lingual Vocabulary Transfers: Language Adaptation of LLMs for…]] — Both reinit embeddings for a vocab swap; LEP learns Russian embeddings, trans-tok uses translation-aligned source averages — rival inits…

[[Home]]
