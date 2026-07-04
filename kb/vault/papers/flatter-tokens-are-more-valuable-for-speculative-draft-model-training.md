---
kb_id: "arxiv:2601.18902"
type: "paper"
title: "Flatter Tokens are More Valuable for Speculative Draft Model Training"
arxiv_id: "2601.18902"
doi: null
hf_repo: null
year: 2026
topics: ["inference-tts"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Flatter Tokens are More Valuable for Speculative Draft Model Training", "arXiv:2601.18902", "arxiv:2601.18902"]
tags: ["paper", "topic/inference-tts"]
---
# Flatter Tokens are More Valuable for Speculative Draft Model Training

[arXiv](https://arxiv.org/abs/2601.18902)
**Topics:** [[inference-tts]]

> [!abstract]
> Speculative Decoding (SD) is a key technique for accelerating Large Language Model (LLM) inference, but it typically requires training a draft model on a large dataset. We approach this problem from a data-centric perspective, finding that not all training samples contribute equally to the SD acceptance rate. Specifically, our theoretical analysis and empirical validation reveals that tokens induc …

## Claims

> [!note] CLAIM — inference-tts
> Speculative decoding needs a 10-20x target:draft size ratio and >=60% acceptance to pay off (<50% acceptance = net loss from verification overhead). A 500M target has no viable external draft (would need a ~25-50M model, too weak to align with the target distribution).
>
> **Numbers:** ratio 10-20x; acceptance >=60% good, <50% loss; 0.5B draft + 8B target = 1.5-2.5x on RTX4090
> **Relevance:** External draft models are OFF the table for a 500M Kazakh model. The only viable acceleration is self-speculation (MTP/Medusa/EAGLE heads on the model itself).
> **Source:** Practitioner consensus + arXiv:2601.18902; benchmark figures from llama.cpp draft-model results · **Sweep:** `slm-architecture-2026-07`

[[Home]]
