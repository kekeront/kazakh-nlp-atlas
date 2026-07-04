---
type: "moc"
topic: "llm-alignment-data"
nodes: 1
papers: 1
sources: 0
uncertain_claims: 0
tags: ["moc"]
---
# Topic: llm-alignment-data

This topic is anchored by a single node, Qorgau (arxiv:2502.13640, MBZUAI Feb 2025) — the first LLM-safety benchmark for the Kazakh-Russian bilingual context: a two-level taxonomy (6 risk areas / 17 harm types, incl. region-specific risk VI), ~1000 human-annotated prompts per language, and GPT-4o-judge + human scoring of 12 models across kk, ru and code-switched inputs. Its established, non-uncertain findings: closed models lead kk safety (Claude 96.5%, GPT-4o 95.8%; best open KazLLM-1.0-70B 87.5%), models are frequently SAFER in Kazakh than Russian because low-resource exposure yields vague generic answers, and region-specific risk VI dominates unsafe responses in both languages. The load-bearing caveat is adoption, not correctness: the repo declares NO license (default all-rights-reserved), so it is evaluation-only — no redistribution, HF re-hosting, or training on its annotations — plus practical parsing traps (question files are .xlsx; the code-switch column is typo'd 'code_swithced_version'). The open question for the lab is whether QymyzLM/other new Kazakh models can be run through Qorgau at all given the license, and how a ≤600M model's safety compares when its Kazakh answers are inherently vaguer. No claim here is REFUTED or flagged uncertain, but every downstream use is constrained by the licensing datapoint.

## Frontier highlights
- [[qorgau-evaluating-llm-safety-in-kazakh-russian-bilingual-contexts|Qorgau: Evaluating LLM Safety in Kazakh-Russian Bilingual Contexts]] — First Kazakh-Russian LLM safety benchmark: 6 risk / 17 harm taxonomy, ~1000/lang, 12 models, GPT-4o+human judge

## Papers (1)
- [[qorgau-evaluating-llm-safety-in-kazakh-russian-bilingual-contexts|Qorgau: Evaluating LLM Safety in Kazakh-Russian Bilingual Contexts]] (2025) — llm-alignment-data

[[Home]]
