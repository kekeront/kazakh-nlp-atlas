---
type: "moc"
topic: "post-hoc-attachment-of-engram-style-cond"
nodes: 6
papers: 6
sources: 0
uncertain_claims: 4
tags: ["moc"]
---
# Topic: post-hoc-attachment-of-engram-style-cond

The frontier question is whether QymyzLM can bolt a random-init, deterministic-hash Engram-style conditional memory onto a converged dense ~500M backbone (Qwen3-0.6B) during continual PT and have it form useful Kazakh knowledge without wrecking the kk/ru/en base. CONFIRMED at exactly lab scale: post-hoc attach works when the integration is ADDITIVE (keep the pretrained MLP, add alpha*mem with learnable alpha_init=0.01) and preceded by a memory-only "healing" recovery phase — on Qwen2.5-0.5B additive gives MedMCQA +2.5pp with PPL BELOW base and TriviaQA -0.4pp, while REPLACEMENT (discard MLP) is Pareto-dominated (PPL +26%); sparse memory FT is genuinely low-forgetting (NQ F1 -11% vs LoRA -71%, full FT -89%). The feared failure mode — gate suppression of a random module over a converged residual stream — is effectively REFUTED at 0.5-1.7B (Lngram Table 4 CONFIRMED: a frozen backbone + ~200M memory learns domain QA, gate does not suppress, +5.54pp over full FT). BUT every positive datapoint uses LEARNED keys (product-key memory, latent binary symbols), never Engram's deterministic token-ID hash, so none actually supports the plan as specified. The real, unanswered risk is COLLISION NOISE: vanilla Engram UNDERPERFORMS its MoE baseline at 0.92B (45.03 vs 45.62, 9-task avg) attributed to hash collisions in a table too small for the key space, and no Engram-lineage paper has ever attached hash-keyed memory post-hoc (Memory Grafting relegates it to future work with zero experiments) — so QymyzLM's ~3B-token kill-switch ablation is literally unanswerable from the literature. Compounding this, Engram's own convention counts the memory table in TOTAL params (500M dense + ~512M table ≈ 1B), pushing the model outside the ≤600M size class it competes in.

## Frontier highlights
- [[sparse-memory-finetuning-as-a-low-forgetting-alternative-to-lora-and-full|Sparse Memory Finetuning as a Low-Forgetting Alternative to LoRA and Full Finetu…]] — Decisive result at lab scale (Qwen2.5-0.5B): ADDITIVE attach (alpha=0.01) wins, REPLACEMENT Pareto-dominated
- [[memory-grafting-scaling-language-model-pre-training-via-offline-conditional|Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Mem…]] — GAP CONFIRMED: zero post-hoc hash-memory experiments; real risk is collision noise (45.03<45.62 at 0.92B), not gate suppression
- [[lngram-n-gram-conditional-memory-in-latent-space|Lngram: N-gram Conditional Memory in Latent Space]] — Strongest positive post-hoc datapoint (+5.54pp on frozen Qwen3-1.7B) but LEARNED latent keys — does NOT support the deterministic-hash plan
- [[improving-sparse-memory-finetuning|Improving Sparse Memory Finetuning]] — Documents the attach loss-spike and cheap memory-only healing: val loss 2.3->2.1 in ~1k steps before joint training
- [[continual-learning-via-sparse-memory-finetuning|Continual Learning via Sparse Memory Finetuning]] — Low-forgetting substrate: sparse memory FT drops NQ F1 -11% vs LoRA -71%, full FT -89% — but base had memory from scratch
- [[conditional-memory-via-scalable-lookup-a-new-axis-of-sparsity-for-large|Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Languag…]] — The Engram source: all results MoE-only, table counted in TOTAL params, plus zero-init-value safe-attach math

## Papers (6)
- [[conditional-memory-via-scalable-lookup-a-new-axis-of-sparsity-for-large|Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models]] (2026) — deepseek-tech
- [[improving-sparse-memory-finetuning|Improving Sparse Memory Finetuning]] (2026) — post-hoc-attachment-of-engram-style-cond
- [[sparse-memory-finetuning-as-a-low-forgetting-alternative-to-lora-and-full|Sparse Memory Finetuning as a Low-Forgetting Alternative to LoRA and Full Finetuning]] (2026) — post-hoc-attachment-of-engram-style-cond
- [[memory-grafting-scaling-language-model-pre-training-via-offline-conditional|Memory Grafting: Scaling Language Model Pre-training via Offline Conditional Memory]] (2026) — does-the-engram-conditional-memory-modul
- [[lngram-n-gram-conditional-memory-in-latent-space|Lngram: N-gram Conditional Memory in Latent Space]] (2026) — novelty-check-has-any-2026-preprint-impl
- [[continual-learning-via-sparse-memory-finetuning|Continual Learning via Sparse Memory Finetuning]] (2025) — post-hoc-attachment-of-engram-style-cond

## Related topics
- [[does-the-engram-conditional-memory-modul]] — 2 shared nodes
- [[novelty-check-has-any-2026-preprint-impl]] — 2 shared nodes

[[Home]]
