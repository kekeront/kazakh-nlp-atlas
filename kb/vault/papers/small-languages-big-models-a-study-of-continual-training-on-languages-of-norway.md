---
kb_id: "arxiv:2412.06484"
type: "paper"
title: "Small Languages, Big Models: A Study of Continual Training on Languages of Norway"
arxiv_id: "2412.06484"
doi: null
hf_repo: null
year: 2024
topics: ["architecture-fork"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Small Languages, Big Models: A Study of Continual Training on Languages of Norway", "arXiv:2412.06484", "arxiv:2412.06484"]
tags: ["paper", "topic/architecture-fork"]
---
# Small Languages, Big Models: A Study of Continual Training on Languages of Norway

[arXiv](https://arxiv.org/abs/2412.06484)
**Topics:** [[architecture-fork]]

> [!abstract]
> Training large language models requires vast amounts of data, posing a challenge for less widely spoken languages like Norwegian and even more so for truly low-resource languages like Northern Sámi. To address this issue, we present a novel three-stage continual training approach that substantially improves the downstream performance together with the inference efficiency for the target languages.

## Claims

> [!note] CLAIM — architecture-fork
> The only published low-resource head-to-head that pits tokenizer-swap continual pretraining against from-scratch on the SAME data (NorMistral, Norwegian) favors continual on EVERY metric, including the knowledge-QA task most analogous to KazMMLU. Their 3-stage recipe = build new tokenizer, realign embeddings (only 1000 frozen-body steps), then full CPT.
>
> **Numbers:** Continual vs from-scratch: NorQuAD 64.8 vs 43.7 (+21.1 F1); NRK-Quiz-QA 57.9 vs 48.2 (+9.7); NoReC 84.9 vs 80.3 (+4.6); Tatoeba 57.2 vs 53.4 BLEU (+3.8). Full training 250B tokens / 60k steps; embedding realign = 1000 steps.
> **Relevance:** Closest experimental analog to the fork; adaptation-with-swapped-tokenizer beats from-scratch even on knowledge QA. Direction is strong; magnitude not transferable (11B model, 250B tokens >> Kazakh 600M / 9-10B budget).
> **Source:** arXiv 2412.06484 (Small Languages, Big Models / NorMistral-11B), Table 4 · **Sweep:** `slm-architecture-2026-07`

## Related
- [[lora-learns-less-and-forgets-less|LoRA Learns Less and Forgets Less]] — Both study continual pretraining for a new language; direct LoRA-vs-full evidence for the Kazakh CPT path
- [[simple-and-scalable-strategies-to-continually-pre-train-large-language-models|Simple and Scalable Strategies to Continually Pre-train Large Language Models]] — NorMistral's 3-stage tokenizer-swap + realign + full CPT instantiates the general continual-pretraining recipe this formalizes
- [[estllm-enhancing-estonian-capabilities-in-multilingual-llms-via-continued|EstLLM: Enhancing Estonian Capabilities in Multilingual LLMs via Continued Pretraining and…]] — Both continual-adapt a base to a low-resource language; NorMistral adds the from-scratch control EstLLM lacks

[[Home]]
