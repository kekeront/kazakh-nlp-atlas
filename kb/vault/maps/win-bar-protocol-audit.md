---
type: "moc"
topic: "win-bar-protocol-audit"
nodes: 3
papers: 2
sources: 1
uncertain_claims: 3
tags: ["moc"]
---
# Topic: win-bar-protocol-audit

The audit resolves how the lab's 32.8% KazMMLU baseline and the Sherkala "ceiling" relate, and the answer is: they are NOT directly comparable. CONFIRMED and pinned in code — the lab protocol is the Kazakh-only 12-subject test split (9,870 questions), 3-shot (the dev split holds exactly 3 exemplars, so num_fewshot=5 hard-errors), next-token letter-logit argmax, fp16, giving Qwen3-0.6B-Base = 0.328. The subset matches Sherkala's, but the 41.4/51.6 figures diverge on three axes: shots (0 vs 3), scoring (normalized full-string log-likelihood vs letter-logit), and base-vs-chat. A load-bearing KB CONFLICT is flagged: the 41.4 was mislabeled "5-shot avg" when the paper text says 0-shot. Two quantitative facts make cross-protocol mixing indefensible — shot count alone moves scores ~11pp (Qwen-2.5-7B-Instruct 47.8→58.9, 0→3-shot), larger than the whole 32.8→36 target delta, and instruction tuning costs -10.2pp (Sherkala base 51.6 vs chat 41.4), meaning the honest base-to-base ceiling reference is 51.6, not 41.4. Open question: the only clean comparison is base-to-base through the same runner, so any QymyzLM claim must be re-measured under the pinned protocol rather than cited against Sherkala's published numbers.

## Frontier highlights
- [[home-altairzhambyl-projects-slms-qymyzlm-evallab-results|/home/altairzhambyl/projects/SLMs/qymyzlm/evallab/results/2026-04-30__…]] — Canonical protocol pinned in code: 9,870-Q kk split, 3-shot (dev=3 hard max), letter-logit, Qwen3-0.6B=0.328
- [[sherkala-chat-building-a-state-of-the-art-llm-for-kazakh-in-a-moderately|Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resour…]] — Ceiling audit: 41.4/51.6 are 0-shot string-log-lik, mislabeled '5-shot'; cross-protocol on 3 axes vs lab's 32.8
- [[kazmmlu-evaluating-language-models-on-kazakh-russian-and-regional-knowledge-of|KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge o…]] — Shot count moves scores ~11pp (47.8→58.9); paper's own Table 4 is a third protocol (0-shot English, full 23K)

## Papers (2)
- [[kazmmlu-evaluating-language-models-on-kazakh-russian-and-regional-knowledge-of|KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan]] (2025) — sota-slm
- [[sherkala-chat-building-a-state-of-the-art-llm-for-kazakh-in-a-moderately|Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting]] (2025) — tokenizer-morphology

## Sources & findings (1)
- [[home-altairzhambyl-projects-slms-qymyzlm-evallab-results|/home/altairzhambyl/projects/SLMs/qymyzlm/evallab/results/2026-04-30__…]] — [tested-on-Kazakh] The lab's canonical protocol is fully pinned in code and a committed result record: KazMMLU Kazakh-la…

## Related topics
- [[kazakh-turkic-nlp]] — 2 shared nodes

[[Home]]
