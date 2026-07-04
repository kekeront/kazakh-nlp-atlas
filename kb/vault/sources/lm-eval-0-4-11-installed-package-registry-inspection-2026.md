---
kb_id: "title:lm eval 0 4 11 installed package registry inspection 2026 07 03"
type: "source"
title: "lm-eval 0.4.11 installed-package registry inspection, 2026-07-03"
doi: null
hf_repo: null
year: null
topics: ["eval-benchmarks"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:lm eval 0 4 11 installed package registry inspection 2026 07 03"]
tags: ["source", "topic/eval-benchmarks"]
---
# lm-eval 0.4.11 installed-package registry inspection, 2026-07-03

**Topics:** [[eval-benchmarks]]

## Source URLs
- lm-eval 0.4.11 installed-package registry inspection, 2026-07-03

## Findings

> [!note] CLAIM — eval-benchmarks
> Installed lm-eval 0.4.11 ships NO tasks named kazmmlu, tumlu_mini, or kazqad (verified against the default TaskManager registry) — custom task YAMLs plus TaskManager(include_path=...) are required; qymyzlm's src/kazllm/eval plumbing referencing those names failed for every benchmark until reconciled on 2026-07-03.
>
> **Numbers:** 0 matching tasks in registry; lm-eval 0.4.11
> **Relevance:** evallab ships the canonical custom task configs; engine eval plumbing must not silently reference ghosts.
> **Source:** lm-eval 0.4.11 installed-package registry inspection, 2026-07-03 · **Sweep:** `2026-07-eval-provenance`

## Related
- [[kazqad-kazakh-open-domain-question-answering-dataset|KazQAD: Kazakh Open-Domain Question Answering Dataset]] — kazqad is one of the three task names absent from the lm-eval registry, blocking KazQAD retrieval eval until custom-wired
- [[huggingface-co-datasets-mbzuai-kazmmlu-dataset-inspection|huggingface.co/datasets/MBZUAI/KazMMLU (dataset inspection 2026-07-03)]] — The empty task registry is why KazMMLU needed a custom task YAML + include_path to load at all

[[Home]]
