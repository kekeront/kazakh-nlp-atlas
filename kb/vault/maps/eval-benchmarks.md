---
type: "moc"
topic: "eval-benchmarks"
nodes: 3
papers: 1
sources: 2
uncertain_claims: 0
tags: ["moc"]
---
# Topic: eval-benchmarks

This topic is dominated by operational, inspection-verified facts about how Kazakh eval benchmarks actually behave in the lab, not contested research claims — all three nodes carry uncertain=false with null verdicts, i.e. CONFIRMED-by-direct-inspection. The load-bearing finding is that KazMMLU's dev split holds only 3 exemplars per subject config, so the qymyzlm April-2026 baseline table (Qwen3-0.6B-Base 32.8%) was capped at 3-shot yet mislabeled "5-shot" (relabeled 3-shot on 2026-07-03); further quirks (a 7-question config, variable 4-5 options, empty Option E) break fixed 5-choice task configs. Tooling is a second confirmed trap: installed lm-eval 0.4.11 ships NO kazmmlu/tumlu_mini/kazqad tasks, so every benchmark failed until custom YAMLs + TaskManager(include_path=...) were wired in. On safety, Qorgau (MBZUAI, Feb 2025) is the first kk-ru bilingual safety benchmark (6 risk areas / 17 harm types, 12 models; models often SAFER in Kazakh because low-resource exposure yields vague answers) but ships NO license — internal evaluation only, no re-hosting or training on annotations, plus a typo'd 'code_swithced_version' column. The open question is cross-protocol comparability: the canonical 32.8% target and the Sherkala 41.4% ceiling are only meaningful once both are re-run under evallab's pinned protocol.

## Frontier highlights
- [[huggingface-co-datasets-mbzuai-kazmmlu-dataset-inspection|huggingface.co/datasets/MBZUAI/KazMMLU (dataset inspection 2026-07-03)]] — dev=3 exemplars/config caps 'N-shot' at 3; the 32.8% baseline was mislabeled 5-shot until relabeled 3-shot
- [[lm-eval-0-4-11-installed-package-registry-inspection-2026|lm-eval 0.4.11 installed-package registry inspection, 2026-07-03]] — lm-eval 0.4.11 ships zero kazmmlu/tumlu/kazqad tasks — custom YAMLs mandatory; every eval failed until reconciled
- [[qorgau-evaluating-llm-safety-in-kazakh-russian-bilingual-contexts|Qorgau: Evaluating LLM Safety in Kazakh-Russian Bilingual Contexts]] — first kk-ru safety benchmark, but NO license = internal-only; models safer in kk via vague low-resource answers

## Papers (1)
- [[qorgau-evaluating-llm-safety-in-kazakh-russian-bilingual-contexts|Qorgau: Evaluating LLM Safety in Kazakh-Russian Bilingual Contexts]] (2025) — llm-alignment-data

## Sources & findings (2)
- [[huggingface-co-datasets-mbzuai-kazmmlu-dataset-inspection|huggingface.co/datasets/MBZUAI/KazMMLU (dataset inspection 2026-07-03)]] — KazMMLU's dev split holds only 3 exemplars per subject config, so any 'N-shot' run sourcing shots from dev is capped at…
- [[lm-eval-0-4-11-installed-package-registry-inspection-2026|lm-eval 0.4.11 installed-package registry inspection, 2026-07-03]] — Installed lm-eval 0.4.11 ships NO tasks named kazmmlu, tumlu_mini, or kazqad (verified against the default TaskManager r…

[[Home]]
