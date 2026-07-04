---
kb_id: "arxiv:2502.05795"
type: "paper"
title: "The Curse of Depth in Large Language Models"
arxiv_id: "2502.05795"
doi: null
hf_repo: null
year: 2025
topics: ["residual-stream-stability-qymyzlm-design"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["The Curse of Depth in Large Language Models", "arXiv:2502.05795", "arxiv:2502.05795"]
tags: ["paper", "topic/residual-stream-stability-qymyzlm-design"]
---
# The Curse of Depth in Large Language Models

[arXiv](https://arxiv.org/abs/2502.05795)
**Topics:** [[residual-stream-stability-qymyzlm-design]]

> [!abstract]
> In this paper, we introduce the Curse of Depth, a concept that highlights, explains, and addresses the recent observation in modern Large Language Models (LLMs) where nearly half of the layers are less effective than expected. We first confirm the wide existence of this phenomenon across the most popular families of LLMs such as Llama, Mistral, DeepSeek, and Qwen. Our analysis, theoretically and e …

## Claims

> [!note] CLAIM — residual-stream-stability-qymyzlm-design
> [transferable-untested] LayerNorm Scaling (Curse of Depth): multiplying each layer's LN output by 1/sqrt(layer_index) gives the largest published perplexity gains of any zero-parameter stability trick at sub-1B, measured at token budgets similar to ours: LLaMA-1B ppl 17.02 -> 15.71 on only 8.9B tokens. No hyperparameters, no learnable params, stable where Mix-LN/Post-LN/DeepNorm diverge (ppl >1300 at 350M+). Explicitly INCOMPATIBLE with scaled initialization (combining is worse than LNS alone) — conflicts with YuLan-Mini's residual scaling 1.4/sqrt(n_layers) already in KB; pick one, never stack.
>
> **Numbers:** Pre-LN -> LNS ppl: 130M/2.2B tok 26.73->25.76; 250M/3.9B 21.92->20.35; 350M/6.0B 19.58->18.20; 1B/8.9B 17.02->15.71 (-1.31); Mix-LN diverges at 350M (1363.21), Post-LN at 250M (1409.79)
> **Relevance:** Measured at 2.2-8.9B tokens — the ONLY stability result whose token budget matches the ~10B Kazakh data ceiling instead of extrapolating from 100B+ regimes. Zero cost on T4. Verdict: worth it IF Pre-LN is kept; if Peri-LN is chosen, LNS+Peri-LN combination is unpublished — choose one variance-control mechanism at the 50M proxy, do not stack (also drop YuLan-Mini 1.4/sqrt(L) residual scaling if LNS is used).
> **Source:** arXiv:2502.05795 (The Curse of Depth in LLMs, HTML full text fetched 2026-07-04, Table 1); code github.com/lmsdss/LayerNorm-Scaling · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[mobilellm-optimizing-sub-billion-parameter-language-models-for-on-device-use|MobileLLM: Optimizing Sub-billion Parameter Language Models for On-Device Use Cases]] — Curse of Depth warns Pre-LN deep layers underperform — tension with MobileLLM's depth-over-width thesis
- [[yulan-mini-an-open-data-efficient-language-model|YuLan-Mini: An Open Data-efficient Language Model]] — LNS explicitly incompatible with YuLan-Mini's residual scaling 1.4/sqrt(n_layers) — pick one, never stack

[[Home]]
