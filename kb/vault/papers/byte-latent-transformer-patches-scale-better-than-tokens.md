---
kb_id: "arxiv:2412.09871"
type: "paper"
title: "Byte Latent Transformer: Patches Scale Better Than Tokens"
arxiv_id: "2412.09871"
doi: null
hf_repo: null
year: 2024
topics: ["tokenizer-agglutinative"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Byte Latent Transformer: Patches Scale Better Than Tokens", "arXiv:2412.09871", "arxiv:2412.09871"]
tags: ["paper", "topic/tokenizer-agglutinative"]
---
# Byte Latent Transformer: Patches Scale Better Than Tokens

[arXiv](https://arxiv.org/abs/2412.09871)
**Topics:** [[tokenizer-agglutinative]]

> [!abstract]
> We introduce the Byte Latent Transformer (BLT), a new byte-level LLM architecture that, for the first time, matches tokenization-based LLM performance at scale with significant improvements in inference efficiency and robustness. BLT encodes bytes into dynamically sized patches, which serve as the primary units of computation. Patches are segmented based on the entropy of the next byte, allocating …

## Claims

> [!note] CLAIM — tokenizer-agglutinative
> Byte-level / tokenizer-free models are NOT competitive at sub-1B. BLT's FLOP-controlled scaling study (1B-8B, up to 4T bytes) shows large-patch byte models START BELOW BPE at 1B and only surpass BPE at larger scales; the 50% inference-FLOP saving needs patch sizes that hurt small-model quality.
>
> **Numbers:** scaling 1B-8B params, ≤4T bytes; large patch (6-8 bytes) -> up to -50% inference FLOPs but lower quality at 1B, crossing BPE only at larger sizes
> **Relevance:** transferable-untested (no Kazakh). Decision-relevant NEGATIVE: at ≤600M active a tokenizer-free/BLT backbone is expected to underperform a good subword tokenizer. Keep byte-latent as a research side-track, not the QymyzLM main tokenizer.
> **Source:** arXiv:2412.09871 (ACL 2025) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[h-net-hierarchical-dynamic-chunking-for-tokenizer-free-language-modelling-in|H-Net++: Hierarchical Dynamic Chunking for Tokenizer-Free Language Modelling in Morphologi…]] — BLT says byte starts below BPE at 1B; H-Net++ claims tokenizer-free beats BPE on morph-rich at 252M — direct sub-1B dispute
- [[kazbyte-adapting-qwen-models-to-kazakh-via-byte-level-adapter|KazByte: Adapting Qwen models to Kazakh via Byte-level Adapter]] — KazByte applies a byte-level adapter to Kazakh Qwen; BLT warns byte hurts quality exactly at that sub-1B scale

[[Home]]
