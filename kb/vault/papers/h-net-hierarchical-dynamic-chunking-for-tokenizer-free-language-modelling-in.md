---
kb_id: "arxiv:2508.05628"
type: "paper"
title: "H-Net++: Hierarchical Dynamic Chunking for Tokenizer-Free Language Modelling in Morphologically-Rich Languages"
arxiv_id: "2508.05628"
doi: null
hf_repo: null
year: 2025
topics: ["novelty-check", "tokenizer-agglutinative"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["H-Net++: Hierarchical Dynamic Chunking for Tokenizer-Free Language Modelling in Morphologically-Rich Languages", "arXiv:2508.05628", "arxiv:2508.05628"]
tags: ["paper", "topic/novelty-check", "topic/tokenizer-agglutinative"]
---
# H-Net++: Hierarchical Dynamic Chunking for Tokenizer-Free Language Modelling in Morphologically-Rich Languages

[arXiv](https://arxiv.org/abs/2508.05628)
**Topics:** [[novelty-check]], [[tokenizer-agglutinative]]

> [!abstract]
> Byte-level language models eliminate fragile tokenizers but face computational challenges in morphologically-rich languages (MRLs), where words span many bytes. We propose H-NET++, a hierarchical dynamic-chunking model that learns linguistically-informed segmentation through end-to-end training. Key innovations include: (1) a lightweight Transformer context-mixer (1.9M parameters) for cross-chunk …

## Claims

> [!note] CLAIM — novelty-check
> Tokenizer-free / byte-level modeling on agglutinative languages is already demonstrated by H-Net++ (hierarchical dynamic chunking), which specifically targets morphologically-rich languages and beats subword baselines. A byte-level angle for Kazakh is NOT novel.
>
> **Numbers:** H-Net++ 252M base (variants 125M/500M/1.1B); Persian: BPB 1.183 vs 1.342 GPT-2-fa (12% better), ParsGLUE 76.6% vs 71.2% (+5.4pp), 8-10x hierarchical compression to ~subword sequence lengths; zero-shot transfer to Turkish/Arabic degrades
> **Relevance:** Reinforces that the user should stay tokenizer-BASED with morpheme-aware memory, and explicitly contrast against byte-level H-Net++ as the competing paradigm. Also a template for reporting BPB + downstream + robustness.
> **Source:** arXiv:2508.05628 (H-Net++) · **Sweep:** `slm-architecture-2026-07`

> [!note] CLAIM — tokenizer-agglutinative
> Tokenizer-free dynamic chunking CAN work on a morphologically-rich language at small data scale: H-Net++ on Persian (1.4B tokens) beats BPE GPT-2-fa by 0.159 BPB (12% better compression), +5.4pp ParsGLUE, learns morpheme boundaries at F1 73.8%, and is 53% more robust to orthographic corruption (ZWNJ) — using only a 1.9M-param context-mixer.
>
> **Numbers:** Persian 1.4B tokens; -0.159 BPB (12%); +5.4pp ParsGLUE; morph-boundary F1 73.8%; +53% ZWNJ robustness; 1.9M-param mixer; two-level latent hyper-prior
> **Relevance:** transferable-untested for Kazakh (tested on Persian, morph-rich but Indo-European, not Turkic). Best evidence that end-to-end chunking handles agglutination + code-switching orthography; a candidate for a from-scratch QymyzLM variant, but unproven on Turkic and at the exact 500M budget.
> **Source:** arXiv:2508.05628 (Aug 7 2025, CC BY 4.0) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[byte-latent-transformer-patches-scale-better-than-tokens|Byte Latent Transformer: Patches Scale Better Than Tokens]] — BLT says byte starts below BPE at 1B; H-Net++ claims tokenizer-free beats BPE on morph-rich at 252M — direct sub-1B dispute

[[Home]]
