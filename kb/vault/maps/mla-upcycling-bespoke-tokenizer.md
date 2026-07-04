---
type: "moc"
topic: "mla-upcycling-bespoke-tokenizer"
nodes: 5
papers: 5
sources: 0
uncertain_claims: 3
tags: ["moc"]
---
# Topic: mla-upcycling-bespoke-tokenizer

The question — can a ≤1B GQA model be upcycled to MLA when it uses a bespoke Kazakh tokenizer that no larger teacher shares — resolves into a three-tier frontier. Teacher-free conversion is CONFIRMED at sub-1B: MHA2MLA (arxiv:2502.14837) converts SmolLM-135M/360M via joint-SVD init + partial-RoPE on only 2.25B FT tokens (0.375% of pretrain), tokenizer-irrelevant because no teacher is involved, but it is LOSSY — 3.2x KV cut costs -1.2/-1.7pp and 8x costs -3.3/-4.6pp, with smaller models degrading more at equal d_kv. Lossless deep compression (6.4-10.6x) is published only via distillation from a 3-8x-larger SAME-tokenizer teacher (X-EcoMLA arxiv:2503.11132), which cannot exist for the lab; its only tokenizer-safe option is ~1.9x lossless self-distillation. The decisive open gap: zero published work combines cross-tokenizer KD (ALM arxiv:2503.20083 and peers) with MLA upcycling, so a Sherkala-8B→bespoke-Kazakh-SLM MLA conversion is unclaimed. Contested/caveats: X-EcoMLA's internal config-to-ratio mapping is self-conflicting (uncertain), Zebra-Llama shows deep hybrid compression still drops MMLU -8.2pp even with an 8B teacher (uncertain), and 2026 teacher-free advances (CARE) bottom out at 4B with no sub-1B evidence.

## Frontier highlights
- [[towards-economical-inference-enabling-deepseek-s-multi-head-latent-attention-in|Towards Economical Inference: Enabling DeepSeek's Multi-Head Latent Attention in…]] — Teacher-free GQA→MLA proven at 135M/360M on 0.375% FT data — tokenizer-irrelevant but lossy (3.2x@-1.7pp)
- [[x-ecomla-upcycling-pre-trained-attention-into-mla-for-efficient-and-extreme-kv|X-EcoMLA: Upcycling Pre-Trained Attention into MLA for Efficient and Extreme KV…]] — Verdict node: 1.9x lossless self-distill is the only tokenizer-safe path; 6.4-10.6x needs an unreachable same-tokenizer teacher
- [[universal-cross-tokenizer-distillation-via-approximate-likelihood-matching|Universal Cross-Tokenizer Distillation via Approximate Likelihood Matching]] — The open gap: zero papers combine cross-tokenizer KD with MLA upcycling — Sherkala-teacher route is unclaimed
- [[zebra-llama-towards-extremely-efficient-hybrid-models|Zebra-Llama: Towards Extremely Efficient Hybrid Models]] — Deep hybrid compression still lossy on knowledge: MMLU -8.2pp with 8B same-tokenizer teacher — what KazMMLU measures
- [[care-covariance-aware-and-rank-enhanced-decomposition-for-enabling-multi-head|CARE: Covariance-Aware and Rank-Enhanced Decomposition for Enabling Multi-Head L…]] — 2026 teacher-free conversion improves (215x ppl, 1.70x acc at matched KV) but smallest tested model is 4B — no sub-1B evidence

## Papers (5)
- [[care-covariance-aware-and-rank-enhanced-decomposition-for-enabling-multi-head|CARE: Covariance-Aware and Rank-Enhanced Decomposition for Enabling Multi-Head Latent Attention]] (2026) — mla-upcycling-bespoke-tokenizer
- [[towards-economical-inference-enabling-deepseek-s-multi-head-latent-attention-in|Towards Economical Inference: Enabling DeepSeek's Multi-Head Latent Attention in Any Transformer-bas…]] (2025) — mla-at-sub-1b-scale
- [[x-ecomla-upcycling-pre-trained-attention-into-mla-for-efficient-and-extreme-kv|X-EcoMLA: Upcycling Pre-Trained Attention into MLA for Efficient and Extreme KV Compression]] (2025) — mla-at-sub-1b-scale
- [[universal-cross-tokenizer-distillation-via-approximate-likelihood-matching|Universal Cross-Tokenizer Distillation via Approximate Likelihood Matching]] (2025) — mla-upcycling-bespoke-tokenizer
- [[zebra-llama-towards-extremely-efficient-hybrid-models|Zebra-Llama: Towards Extremely Efficient Hybrid Models]] (2025) — mla-upcycling-bespoke-tokenizer

## Related topics
- [[mla-at-sub-1b-scale]] — 2 shared nodes

[[Home]]
