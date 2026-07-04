---
kb_id: "hf:blog/smollm3"
type: "source"
title: "huggingface.co/blog/smollm3"
doi: null
hf_repo: "blog/smollm3"
year: null
topics: ["sota-slm"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["hf:blog/smollm3"]
tags: ["source", "topic/sota-slm"]
---
# huggingface.co/blog/smollm3

**Topics:** [[sota-slm]]

## Source URLs
- huggingface.co/blog/smollm3
- learnopencv SmolLM3 explainer

## Findings

> [!note] CLAIM — sota-slm
> SmolLM3-3B architecture innovations transferable downward: GQA with 4 KV groups, NoPE (remove RoPE from every 4th layer) for long context, tied embeddings, no weight decay on embeddings, intra-document masking; trained 11.2T tokens, 128K context, but only 6 European languages (en/fr/es/de/it/pt) — no Kazakh.
>
> **Numbers:** 3B, GQA 4 groups, NoPE every 4th layer, 11.2T tok, 6 langs
> **Relevance:** NoPE-every-4th-layer and no-weight-decay-on-embeddings are cheap, proven tricks to fold into the Kazakh backbone. Confirms even a 2025 SOTA small model ignores Turkic — reinforcing the novelty of the target.
> **Source:** huggingface.co/blog/smollm3; learnopencv SmolLM3 explainer · **Sweep:** `slm-architecture-2026-07`

## Related
- [[hardware-efficient-attention-for-fast-decoding|Hardware-Efficient Attention for Fast Decoding]] — GLA paper shows MLA beats GQA-4 sub-1B, yet SmolLM3 shipped GQA-4 without ablating MLA (not in nanotron at the time)

[[Home]]
