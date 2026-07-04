---
kb_id: "arxiv:2502.13640"
type: "paper"
title: "Qorgau: Evaluating LLM Safety in Kazakh-Russian Bilingual Contexts"
arxiv_id: "2502.13640"
doi: null
hf_repo: null
year: 2025
topics: ["llm-alignment-data", "eval-benchmarks"]
claims: 3
uncertain_claims: 0
verdicts: []
aliases: ["Qorgau: Evaluating LLM Safety in Kazakh-Russian Bilingual Contexts", "arXiv:2502.13640", "arxiv:2502.13640"]
tags: ["paper", "topic/llm-alignment-data", "topic/eval-benchmarks"]
---
# Qorgau: Evaluating LLM Safety in Kazakh-Russian Bilingual Contexts

[arXiv](https://arxiv.org/abs/2502.13640)
**Topics:** [[llm-alignment-data]], [[eval-benchmarks]]

> [!abstract]
> Large language models (LLMs) are known to have the potential to generate harmful content, posing risks to users. While significant progress has been made in developing taxonomies for LLM risks and safety evaluation prompts, most studies have focused on monolingual contexts, primarily in English. However, language- and region-specific risks in bilingual contexts are often overlooked, and core findi …

## Claims

> [!note] CLAIM — llm-alignment-data
> Qorgau (MBZUAI, Feb 2025): the first LLM safety benchmark for the Kazakh-Russian bilingual context — two-level taxonomy of 6 high-level risk areas + 17 fine-grained harm types incl. region-specific sensitive topics (risk type VI); ~1000 human-annotated samples per language plus responses of 12 models (xlsx/csv in repo); evaluated with GPT-4o judge + human assessment across kk, ru and code-switched prompts.
>
> **Numbers:** 6 risk areas / 17 harm types; 12 models; ~1000 annotated per language; kk leaders: Claude 96.5% safe, GPT-4o 95.8%; ru leader YandexGPT 93.57%; best open: KazLLM-1.0-70B 87.5%
> **Relevance:** Partially closes the 'zero kk safety data' gap from the sector decomposition: a safety EVAL exists; still missing an open kk safety CLASSIFIER — Qorgau's taxonomy+annotations are the natural training substrate for it (paper milestone update).
> **Source:** arXiv 2502.13640 — Qorgau: Evaluating LLM Safety in Kazakh-Russian Bilingual Contexts; github.com/mbzuai-nlp/qorgau-kaz-ru-safety · **Sweep:** `qorgau-2026-07`

> [!note] CLAIM — llm-alignment-data
> Qorgau key result: models are often SAFER in Kazakh than Russian because low-resource exposure yields vague generic answers; region-specific topics (risk VI) dominate unsafe responses in both languages; code-switching can both amplify (access to unsafe ru content) and reduce risk. Caveats: repo has NO license (usability unclear), 2 stars, last push 2025-09 — a citable claim-vs-adoption datapoint for the atlas.
>
> **Numbers:** risk VI = majority of unsafe answers; Aya101 lowest kk safety despite kk-tailoring; license: none declared
> **Relevance:** For QymyzLM: safety eval protocol to adopt at SFT stage; for the survey: evaluation-territory entry; for backlog: kk safety classifier task now reads 'train on Qorgau taxonomy' instead of 'create eval from scratch'.
> **Source:** arXiv 2502.13640 — Qorgau; github.com/mbzuai-nlp/qorgau-kaz-ru-safety README · **Sweep:** `qorgau-2026-07`

> [!note] CLAIM — eval-benchmarks
> Qorgau's GitHub repo has NO declared license (GitHub API license: null, no LICENSE file) — default all-rights-reserved: internal evaluation only, no redistribution, no re-hosting on HF, no training on its annotations. Practical parsing notes: question files are .xlsx; the code-switched CSV column is typo'd in the actual file as 'code_swithced_version'.
>
> **Numbers:** license: null; 6 risk areas / 17 harm types; column name 'code_swithced_version' (sic)
> **Relevance:** Hard usage boundary for the safety track; column typo is a live integration detail.
> **Source:** api.github.com/repos/mbzuai-nlp/qorgau-kaz-ru-safety (2026-07-03); arXiv 2502.13640 · **Sweep:** `2026-07-eval-provenance`

## Related
- [[aya-expanse-combining-research-breakthroughs-for-a-new-multilingual-frontier|Aya Expanse: Combining Research Breakthroughs for a New Multilingual Frontier]] — Qorgau finds Aya101 lowest kk safety despite kk-tailoring; Aya Expanse is the successor whose kk safety is untested here
- [[kazmmlu-evaluating-language-models-on-kazakh-russian-and-regional-knowledge-of|KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhst…]] — Companion MBZUAI Kazakh benchmarks: Qorgau measures safety, KazMMLU measures capability — two axes of the same eval suite
- [[sherkala-chat-building-a-state-of-the-art-llm-for-kazakh-in-a-moderately|Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Settin…]] — Qorgau evaluates Kazakh LLM safety (best open = KazLLM-70B 87.5%); Sherkala is the SOTA Kazakh LLM whose safety this benchmark would score
- [[huggingface-co-datasets-issai-ragbench-kazakh|huggingface.co/datasets/issai/RAGBench_Kazakh]] — Both are Kazakh eval resources with adoption/usability caveats; Qorgau's no-license all-rights-reserved status is a claim-vs-adoption…
- [[huggingface-co-nurlykhan-kazembed-v5-apache-2-0|huggingface.co/Nurlykhan/kazembed-v5 (apache-2.0)]] — Adoption/license contrast: Qorgau has NO license (eval-only) vs apache-2.0 Kazakh artifact — the atlas's claim-vs-usability datapoint

[[Home]]
