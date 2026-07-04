---
kb_id: "arxiv:2406.11794"
type: "paper"
title: "DataComp-LM: In search of the next generation of training sets for language models"
arxiv_id: "2406.11794"
doi: null
hf_repo: null
year: 2024
topics: ["small-lm-training-recipes-qymyzlm-design"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["DataComp-LM: In search of the next generation of training sets for language models", "arXiv:2406.11794", "arxiv:2406.11794"]
tags: ["paper", "topic/small-lm-training-recipes-qymyzlm-design"]
---
# DataComp-LM: In search of the next generation of training sets for language models

[arXiv](https://arxiv.org/abs/2406.11794)
**Topics:** [[small-lm-training-recipes-qymyzlm-design]]

> [!abstract]
> We introduce DataComp for Language Models (DCLM), a testbed for controlled dataset experiments with the goal of improving language models. As part of DCLM, we provide a standardized corpus of 240T tokens extracted from Common Crawl, effective pretraining recipes based on the OpenLM framework, and a broad suite of 53 downstream evaluations. Participants in the DCLM benchmark can experiment with dat …

## Claims

> [!note] CLAIM — small-lm-training-recipes-qymyzlm-design
> [transferable-untested] DCLM 400M-1x is the closest published, fully-specified analog to a 500M/10B-token Kazakh run (412M params trained on 8.2B tokens, Chinchilla-1x). Verified from Table 10 of the paper PDF: 24 layers, 8 heads, d_model=1024, d_head=128, warmup 2000 steps, peak LR 3e-3, weight decay 0.033, z-loss 1e-4, global batch 512 sequences x 2048 tokens (~1.05M tokens/step, ~7.8k total steps), seq len 2048, GPT-NeoX 50k vocab. Architecture: pre-norm, LayerNorm without bias, qk-LayerNorm, SwiGLU, depth-scaled init, cross-document attention allowed (masking gave 'little impact'). HPs were tuned (following Gadre et al.) to optimize validation perplexity.
>
> **Numbers:** 412M params / 8.2B tok; LR 3e-3; WD 0.033; z-loss 1e-4; warmup 2000 steps; batch 512x2048 = 1.05M tok; 24L/d1024/8H/dh128
> **Relevance:** Drop-in tuned hyperparameter set at exactly the lab's from-scratch scale (500M @ 10B tok); removes the need for a muP sweep on free compute.
> **Source:** arXiv:2406.11794 (DCLM), Table 10 + Appendix (read from PDF) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] — DCLM 400M-1x is the specified recipe analog; SozKZ is the real Kazakh from-scratch execution to compare against

[[Home]]
