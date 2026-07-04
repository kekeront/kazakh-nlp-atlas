---
kb_id: "arxiv:2510.15103"
type: "paper"
title: "Continual Learning via Sparse Memory Finetuning"
arxiv_id: "2510.15103"
doi: null
hf_repo: null
year: 2025
topics: ["post-hoc-attachment-of-engram-style-cond"]
claims: 1
uncertain_claims: 1
verdicts: []
aliases: ["Continual Learning via Sparse Memory Finetuning", "arXiv:2510.15103", "arxiv:2510.15103"]
tags: ["paper", "topic/post-hoc-attachment-of-engram-style-cond"]
---
# Continual Learning via Sparse Memory Finetuning

[arXiv](https://arxiv.org/abs/2510.15103)
**Topics:** [[post-hoc-attachment-of-engram-style-cond]]

> [!abstract]
> Modern language models are powerful, but typically static after deployment. A major obstacle to building models that continually learn over time is catastrophic forgetting, where updating on new data erases previously acquired capabilities. Motivated by the intuition that mitigating forgetting is challenging because trainable parameters are shared across all tasks, we investigate whether sparse pa …

## Claims

> [!warning] UNCERTAIN — post-hoc-attachment-of-engram-style-cond
> [transferable-untested] Memory slots are a low-interference substrate for injecting new knowledge into a converged model — the property QymyzLM needs to add Kazakh facts without destroying the kk/ru/en base: sparse memory finetuning drops NaturalQuestions F1 by only 11% after learning new facts, vs 71% for LoRA and 89% for full finetuning (Meta, on Berges-et-al memory-layer models, sparsely updated by design). Caveat: these base models were pretrained WITH memory layers from scratch (adaptation substrate, not retrofit), so this bounds the best case, not the retrofit case.
>
> **Numbers:** NQ F1 drop after new-fact learning: full FT -89%, LoRA -71%, sparse memory FT -11%
> **Relevance:** Reframes the memory pillar's payoff for CPT: even if raw KazMMLU gain from memory is modest (Lngram +1.4 to +5.1pp frozen-backbone), the forgetting protection vs QLoRA alone may be the winning axis for a 10B-token Kazakh CPT on a multilingual base — measurable in the same ablation at zero extra cost (just keep an English/Russian probe).
> **Source:** arXiv:2510.15103 (Continual Learning via Sparse Memory Finetuning, Lin et al., Meta, Oct 2025), abstract verbatim; memory-layer base per arXiv:2412.09764 · **Sweep:** `slm-arch-for-kazakh`

**Cited KB notes:** [[memory-layers-at-scale]]

## Related
- [[lora-learns-less-and-forgets-less|LoRA Learns Less and Forgets Less]] — both frame method choice around forgetting; A's sparse-mem NQ F1 -11% directly beats B's 'LoRA forgets less' claim (-71%)
- [[memory-layers-at-scale|Memory Layers at Scale]] — A sparsely finetunes the Berges-et-al memory-layer models B introduces; B is the from-scratch substrate A adapts (best-case bound, not…
- [[lngram-n-gram-conditional-memory-in-latent-space|Lngram: N-gram Conditional Memory in Latent Space]] — both adapt memory over a converged backbone; Lngram's frozen-backbone +5.14pp is the lineage's one post-hoc-attach datapoint
- [[lab-measurement-peak-vram-standard-adam-state-arithmetic-2|Lab measurement (peak VRAM) + standard Adam state arithmetic (2+2+4+4+…]] — VRAM rules out QLoRA as the PEFT; sparse-memory finetuning is the competing low-forgetting alternative to full-FT

[[Home]]
