---
kb_id: "arxiv:2404.03608"
type: "paper"
title: "Sailor: Open Language Models for South-East Asia"
arxiv_id: "2404.03608"
doi: null
hf_repo: null
year: 2024
topics: ["continual-pt-lowres-qlora-vs-full-cpt-re"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Sailor: Open Language Models for South-East Asia", "arXiv:2404.03608", "arxiv:2404.03608"]
tags: ["paper", "topic/continual-pt-lowres-qlora-vs-full-cpt-re"]
---
# Sailor: Open Language Models for South-East Asia

[arXiv](https://arxiv.org/abs/2404.03608)
**Topics:** [[continual-pt-lowres-qlora-vs-full-cpt-re]]

> [!abstract]
> We present Sailor, a family of open language models ranging from 0.5B to 7B parameters, tailored for South-East Asian (SEA) languages. These models are continually pre-trained from Qwen1.5, a great language model for multilingual use cases. From Qwen1.5, Sailor models accept 200B to 400B tokens, primarily covering the languages of English, Chinese, Vietnamese, Thai, Indonesian, Malay, and Lao. The …

## Claims

> [!note] CLAIM — continual-pt-lowres-qlora-vs-full-cpt-re
> [transferable-untested] Sailor is the closest published precedent at the lab's exact scale: Qwen1.5-0.5B continually pretrained on 200B tokens (SEA languages ~140B + 30% replay = SlimPajama-EN 37.2B + SkyPile-ZH 22.6B), constant LR 1e-4 after 500-step warmup (chosen explicitly for 'easier recovery from interrupted training'), BPE-dropout 0.1 applied for an extra 2B tokens. Result at 0.5B: big reading/QA gains (TydiQA-id F1 +22.1, XQuAD-th F1 +4.2, XCOPA +3.3, Belebele +2.9) but exam-style knowledge FLAT (M3Exam −0.05). English loss behaves as a quadratic in log(replay proportion)−log(LR).
>
> **Numbers:** 200B tok; replay 60B/200B=30%; LR 1e-4 constant; 0.5B deltas: TydiQA +9.73 EM/+22.10 F1, XCOPA +3.34, Belebele +2.88, M3Exam −0.05
> **Relevance:** Calibrates expectations: at ~0.6B even 140B target-language tokens did not move MMLU-style exams. The +3.2pp KazMMLU target cannot come from raw-web CPT volume alone — needs knowledge-dense data and/or the Engram memory axis.
> **Source:** arXiv:2404.03608 (Sailor), HTML v1 — mixture, LR, and 0.5B tables read directly · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[kazmmlu-evaluating-language-models-on-kazakh-russian-and-regional-knowledge-of|KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhst…]] — Sailor's exam-flat result (M3Exam -0.05) at 0.5B directly threatens the exam-style KazMMLU target
- [[multilingual-language-model-pretraining-using-machine-translated-data|Multilingual Language Model Pretraining using Machine-translated Data]] — both scale multilingual open-model data; TransWebEdu fully MT from-scratch vs Sailor continual-PT on native SE-Asian web

[[Home]]
