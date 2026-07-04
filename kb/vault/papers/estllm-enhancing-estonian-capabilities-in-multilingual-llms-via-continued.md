---
kb_id: "arxiv:2603.02041"
type: "paper"
title: "EstLLM: Enhancing Estonian Capabilities in Multilingual LLMs via Continued Pretraining and Post-Training"
arxiv_id: "2603.02041"
doi: null
hf_repo: null
year: 2026
topics: ["continual-pt-lowres-qlora-vs-full-cpt-re"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["EstLLM: Enhancing Estonian Capabilities in Multilingual LLMs via Continued Pretraining and Post-Training", "arXiv:2603.02041", "arxiv:2603.02041"]
tags: ["paper", "topic/continual-pt-lowres-qlora-vs-full-cpt-re"]
---
# EstLLM: Enhancing Estonian Capabilities in Multilingual LLMs via Continued Pretraining and Post-Training

[arXiv](https://arxiv.org/abs/2603.02041)
**Topics:** [[continual-pt-lowres-qlora-vs-full-cpt-re]]

> [!abstract]
> Large language models (LLMs) are predominantly trained on English-centric data, resulting in uneven performance for smaller languages. We study whether continued pretraining (CPT) can substantially improve Estonian capabilities in a pretrained multilingual LLM while preserving its English and general reasoning performance. Using Llama 3.1 8B as the main base model, we perform CPT on a mixture that …

## Claims

> [!note] CLAIM — continual-pt-lowres-qlora-vs-full-cpt-re
> [transferable-untested, agglutinative-Uralic] EstLLM (2026) Llama-3.1-8B CPT for Estonian: 35.7B-token mixture with Estonian only 8.6B (~24%); the rest is English replay (synthetic Cosmopedia), code, math, and instruction-augmented data (Instruction Pre-Training, Cheng et al. 2024), citing evidence that code and in-CPT instructions preserve task-solving and improve reasoning transfer. Trapezoidal/WSD LR schedule chosen so training can stop at any point. Key data finding: the curated Estonian National Corpus beat much larger FineWeb-2/CulturaX/MADLAD web mixes on discriminative tasks — FineWeb-2 was found full of machine-translated spam by manual inspection.
>
> **Numbers:** 35.7B total; Estonian 8.6B (24%); components 6.9B/3.3B/9.5B/7.4B (en/code/math/instr per Table 1); SFT LR 2.0e-5; 4096 ctx; LUMI 16 nodes
> **Relevance:** 2026-standard recipe for an agglutinative low-resource language: target language is a MINORITY (~24%) of the CPT mix, instruction-augmented CPT is included, and curated national corpora beat bigger MT-polluted web dumps — directly applicable to the CulturaX/MADLAD/mC4 Kazakh data plan.
> **Source:** arXiv:2603.02041 (EstLLM) — mixture table and Section 3/6 read from PDF text · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[small-languages-big-models-a-study-of-continual-training-on-languages-of-norway|Small Languages, Big Models: A Study of Continual Training on Languages of Norway]] — Both continual-adapt a base to a low-resource language; NorMistral adds the from-scratch control EstLLM lacks
- [[chocollama-lessons-learned-from-teaching-llamas-dutch|ChocoLlama: Lessons Learned From Teaching Llamas Dutch]] — Both continual-pretrain a base into a new EU language; ChocoLlama swaps the tokenizer at 32B tokens, EstLLM adapts Estonian — comparable…
- [[fineweb2-one-pipeline-to-scale-them-all-adapting-pre-training-data-processing|FineWeb2: One Pipeline to Scale Them All -- Adapting Pre-Training Data Processing to Every…]] — EstLLM refutes FineWeb-2 quality for discriminative tasks — found it full of machine-translated spam by inspection

[[Home]]
