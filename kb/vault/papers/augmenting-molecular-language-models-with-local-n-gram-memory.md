---
kb_id: "arxiv:2606.12113"
type: "paper"
title: "Augmenting Molecular Language Models with Local $n$-gram Memory"
arxiv_id: "2606.12113"
doi: null
hf_repo: null
year: 2026
topics: ["sparse-memory-2026-engram-lineage-beyond"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Augmenting Molecular Language Models with Local $n$-gram Memory", "arXiv:2606.12113", "arxiv:2606.12113"]
tags: ["paper", "topic/sparse-memory-2026-engram-lineage-beyond"]
---
# Augmenting Molecular Language Models with Local $n$-gram Memory

[arXiv](https://arxiv.org/abs/2606.12113)
**Topics:** [[sparse-memory-2026-engram-lineage-beyond]]

> [!abstract]
> Transformer-based language models for SMILES strings suffer from a locality gap: standard character-level tokenization fragments chemically meaningful motifs, forcing models to repeatedly learn local syntax at the expense of long-range dependencies. To address this without disrupting standard tokenizers, we propose MolGram, which integrates a conditional $n$-gram memory module into molecular langu …

## Claims

> [!note] CLAIM — sparse-memory-2026-engram-lineage-beyond
> [transferable-untested] MolGram is the smallest validated Engram instance ever: dense GPT (6.7M/25.5M/85.4M) and T5 (14.7M/44.1M) backbones with CHARACTER-level vocab 100, Engram-style memory with K=4 hash heads, 64-dim per head, n-gram orders 2-6, insertion layers [1,4] (GPT) / [0,2] or [0..3] (T5 encoder), conv kernel 4, table capacity = 5x vocab multiplier. A 6.7M MolGram-GPT beats a 3.8x larger MolGPT-25.5M on USPTO-50k retrosynthesis; 15.0M MolGram-T5 beats 44.1M T5Chem on USPTO-MIT.
>
> **Numbers:** Retrosynthesis top-1: MolGram-GPT 6.7M = 42.09% vs MolGPT 25.5M = 41.68%. Forward reaction top-1: MolGram-T5 15.0M = 90.43% vs T5Chem 44.1M = 89.63%. Training sets: 40k-1.5M sequences.
> **Relevance:** Strongest quality-per-memory-param evidence at micro scale on dense backbones, and the ONLY Engram work on sub-lexical (character) units — the closest published analogue to morpheme-granular Kazakh keys. Its framing ('memory captures local motifs that char tokenization fragments') is exactly the vowel-harmony/suffix-chain argument for Kazakh. Config template (K=4, 64d/head) is the right size class for a <=600M budget.
> **Source:** arXiv:2606.12113 (HTML v1, fetched 2026-07-04) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[adaptive-engram-memory-system-for-indonesian-language-model-generative-ai-based|Adaptive Engram Memory System for Indonesian Language Model: Generative AI Based on TOBA L…]] — closest fragmenting-tokenizer Engram analogs (syllable vs char n-grams); both post-hoc frame sub-lexical capture, no segmenter integrated
- [[tensorizing-engram-sharing-latents-across-n-gram-embeddings-is-beneficial-in|Tensorizing Engram: Sharing Latents Across N-Gram Embeddings is Beneficial in LLMs]] — both micro-scale dense Engram configs on fragmenting vocabs; MolGram char-level n={4,6}, TN-gram CP-shares latents across orders

[[Home]]
