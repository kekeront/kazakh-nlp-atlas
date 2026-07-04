---
kb_id: "title:evallab kazmmlu kk qwen3 0 6b base measurement 2026 04 30"
type: "source"
title: "evallab/results/2026-04-30__KazMMLU-kk__Qwen-Qwen3-0.6B-Base.json"
doi: null
hf_repo: null
year: null
topics: ["win-bar-protocol-audit"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:evallab kazmmlu kk qwen3 0 6b base measurement 2026 04 30"]
tags: ["source", "topic/win-bar-protocol-audit"]
---
# evallab/results/2026-04-30__KazMMLU-kk__Qwen-Qwen3-0.6B-Base.json

**Topics:** [[win-bar-protocol-audit]]

## Source URLs
- evallab/results/2026-04-30__KazMMLU-kk__Qwen-Qwen3-0.6B-Base.json
- evallab/src/kazeval/run_kazmmlu.py
- evallab/src/kazeval/lm_eval_tasks/kazmmlu_kaz/_kazmmlu_kaz_template_yaml

## Findings

> [!note] CLAIM — win-bar-protocol-audit
> [tested-on-Kazakh] The lab's canonical protocol is fully pinned in code and a committed result record: KazMMLU Kazakh-language subset only (12 subjects, 9,870 test questions), 3-shot with shots drawn from the dev split via lm-eval first_n sampler (dev holds exactly 3 exemplars per subject, so 3-shot is the hard maximum — num_fewshot=5 raises AssertionError, verified live), next-token letter-logit argmax (lm-eval output_type multiple_choice, metric acc, micro-averaged), fp16. Qwen3-0.6B-Base = 0.328 under this exact protocol (measured 2026-04-30, RTX 2070). Both the 32.8% baseline and any future QymyzLM number run through the same runner, so the primary win comparison IS base-to-base, same shots, same split, same subset, same scoring — well-defined.
>
> **Numbers:** 12 subjects; 9,870 test Q; num_fewshot=3 (dev=3 exemplars/config); acc=0.328; fp16; lm-eval 0.4.11 with bundled task YAMLs (no built-in kazmmlu task)
> **Relevance:** The success definition for the generative deliverable is NOT undefined at the primary-target level: beat-32.8 is apples-to-apples by construction. Only the ceiling references are cross-protocol.
> **Source:** evallab/results/2026-04-30__KazMMLU-kk__Qwen-Qwen3-0.6B-Base.json; evallab/src/kazeval/run_kazmmlu.py; evallab/src/kazeval/lm_eval_tasks/kazmmlu_kaz/_kazmmlu_kaz_template_yaml · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[huggingface-co-datasets-mbzuai-kazmmlu-dataset-inspection|huggingface.co/datasets/MBZUAI/KazMMLU (dataset inspection 2026-07-03)]] — This dataset quirk (dev=3) is exactly what caused that eval run's [:5] truncation and the 5-shot→3-shot mislabel
- [[hf-qwen-qwen3-0-6b-config|HF Qwen/Qwen3-0.6B config]] — Lab's measured 0.328 confirms the user-provided Qwen3-0.6B KazMMLU baseline figure under a fully specified runner

[[Home]]
