---
type: "moc"
topic: "architecture-fork"
nodes: 5
papers: 5
sources: 0
uncertain_claims: 5
tags: ["moc"]
---
# Topic: architecture-fork

The core decision — adapt a strong base (continual pretraining / tokenizer transplant) vs build from scratch — is settled toward adaptation by the evidence that matters most for QymyzLM. The single most on-point datapoint is CONFIRMED and damning to from-scratch: SozKZ-600M (from-scratch, ~9B Kazakh tokens, dedicated 50K BPE with a 2-3x fertility edge) scores MC-QA 30.3 / Belebele 27.0, BELOW an un-adapted, smaller Qwen2.5-0.5B (31.5 / 30.0) that had zero Kazakh training — best tokenizer, no knowledge win. The only same-data head-to-head (NorMistral, Norwegian) favors continual on every metric including knowledge-QA (NorQuAD +21.1 F1, NRK-Quiz +9.7). The chief from-scratch justification — a native tokenizer — is largely capturable: training-free OMP transplant retains 99.1% of MMLU and recovers to 101.4% after only 2B CPT tokens (vs FOCUS 73.4%, WECHSEL 63.0%). Two live caveats bound this: (1) cross-scheme transplants catastrophically break numeric reasoning (GSM8K -78.7%) unless digit tokenization is preserved — a direct threat to STEM-heavy KazMMLU; (2) continual's Pareto FLOP edge (~26-40% savings) decays logarithmically with base pretraining, and Qwen3-0.6B is heavily overtrained, so the transfer benefit is real but saturating. Open question: whether the from-scratch architecture-ablation space (entirely unclaimed on Kazakh — SozKZ is vanilla Llama, no morphology/memory) is worth a first-on-Kazakh result, or whether adapting Qwen3-0.6B-Base within a 9-10B-token budget dominates given saturation plus the digit-tokenization risk.

## Frontier highlights
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] — On-point datapoint: from-scratch SozKZ-600M under-knows a smaller un-adapted Qwen despite a 2-3x better tokenizer
- [[small-languages-big-models-a-study-of-continual-training-on-languages-of-norway|Small Languages, Big Models: A Study of Continual Training on Languages of Norwa…]] — Only same-data continual-vs-from-scratch head-to-head; continual wins every metric incl. knowledge-QA (+21.1 F1)
- [[training-free-tokenizer-transplantation-via-orthogonal-matching-pursuit|Training-Free Tokenizer Transplantation via Orthogonal Matching Pursuit]] — Dissolves the tokenizer case for from-scratch (OMP 99.1% MMLU) but flags GSM8K -78.7% cross-scheme numeric break
- [[reusing-overtrained-language-models-saturates-scaling|Reusing Overtrained Language Models Saturates Scaling]] — Bounds the win: continual's FLOP edge decays log with base pretraining; Qwen3-0.6B is overtrained
- [[sherkala-chat-building-a-state-of-the-art-llm-for-kazakh-in-a-moderately|Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resour…]] — Field prior: every Kazakh SOTA is an adaptation (Sherkala continual Llama-3.1 -> 41.4 KazMMLU), none from-scratch

## Papers (5)
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] (2026) — tokenizer-morphology
- [[sherkala-chat-building-a-state-of-the-art-llm-for-kazakh-in-a-moderately|Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting]] (2025) — tokenizer-morphology
- [[training-free-tokenizer-transplantation-via-orthogonal-matching-pursuit|Training-Free Tokenizer Transplantation via Orthogonal Matching Pursuit]] (2025) — architecture-fork
- [[reusing-overtrained-language-models-saturates-scaling|Reusing Overtrained Language Models Saturates Scaling]] (2025) — architecture-fork
- [[small-languages-big-models-a-study-of-continual-training-on-languages-of-norway|Small Languages, Big Models: A Study of Continual Training on Languages of Norway]] (2024) — architecture-fork

## Related topics
- [[data-efficiency-10b-kazakh-10b-token-pre]] — 2 shared nodes
- [[kazakh-turkic-nlp]] — 2 shared nodes
- [[novelty-check]] — 2 shared nodes
- [[tokenizer-morphology]] — 2 shared nodes

[[Home]]
