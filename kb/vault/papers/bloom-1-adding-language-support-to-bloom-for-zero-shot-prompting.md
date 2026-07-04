---
kb_id: "arxiv:2212.09535"
type: "paper"
title: "BLOOM+1: Adding Language Support to BLOOM for Zero-Shot Prompting"
arxiv_id: "2212.09535"
doi: null
hf_repo: null
year: 2022
topics: ["continual-pt-lowres-qlora-vs-full-cpt-re"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["BLOOM+1: Adding Language Support to BLOOM for Zero-Shot Prompting", "arXiv:2212.09535", "arxiv:2212.09535"]
tags: ["paper", "topic/continual-pt-lowres-qlora-vs-full-cpt-re"]
---
# BLOOM+1: Adding Language Support to BLOOM for Zero-Shot Prompting

[arXiv](https://arxiv.org/abs/2212.09535)
**Topics:** [[continual-pt-lowres-qlora-vs-full-cpt-re]]

> [!abstract]
> The BLOOM model is a large publicly available multilingual language model, but its pretraining was limited to 46 languages. To extend the benefits of BLOOM to other languages without incurring prohibitively large costs, it is desirable to adapt BLOOM to new languages not seen during pretraining. In this work, we apply existing language adaptation strategies to BLOOM and benchmark its zero-shot pro …

## Claims

> [!note] CLAIM — continual-pt-lowres-qlora-vs-full-cpt-re
> [transferable-untested] At 560M params, FULL continued pretraining beats adapter/PEFT adaptation for adding new languages; adapters only win above ~3B. Exact quote (BLOOM+1, ACL 2023): 'For the smallest BLOOM model with 560 million parameters, we see that continued pretraining yields the best prompting performance... when model sizes increase beyond 3 billion parameters, adapter-based language adaptation methods outperform continued pretraining.' Adaptation data: 100K OSCAR samples/language, 8 new languages, BLOOM 560M–7.1B, methods: full CPT vs MAD-X vs (IA)3.
>
> **Numbers:** crossover at ~3B; tested sizes 560M/1.1B/1.7B/3B/7.1B; 100K samples/lang
> **Relevance:** Directly challenges the lab's default QLoRA-CPT plan: at 0.6B (exactly the BLOOM-560M regime) the published evidence says full-parameter CPT > PEFT. QLoRA on Qwen3-0.6B is a memory convenience, not a quality optimum.
> **Source:** arXiv:2212.09535 (BLOOM+1, ACL 2023) — verified from PDF text, aclanthology.org/2023.acl-long.653 · **Sweep:** `slm-arch-for-kazakh`

[[Home]]
