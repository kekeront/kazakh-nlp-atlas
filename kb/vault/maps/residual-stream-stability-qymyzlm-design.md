---
type: "moc"
topic: "residual-stream-stability-qymyzlm-design"
nodes: 12
papers: 12
sources: 0
uncertain_claims: 7
tags: ["moc"]
---
# Topic: residual-stream-stability-qymyzlm-design

This topic maps residual-stream/normalization stability tricks for the from-scratch ~500M QymyzLM path, which must train in fp16-only on a T4 (no bf16). The best-established fp16-relevant result is Peri-LN (arxiv:2502.02732): Pre-LN hidden-state magnitude exceeds the FP16 max (65504) by ~0.5B tokens while Peri-LN stays below it and cuts seed variance >2x (400M loss 3.43->3.34). LayerNorm Scaling (arxiv:2502.05795) is the largest zero-parameter perplexity win (1B/8.9B tok 17.02->15.71 ppl) but is explicitly INCOMPATIBLE with scaled init, conflicting with YuLan-Mini's 1.4/sqrt(n_layers) residual scaling — pick one. Value Residual/ResFormer (arxiv:2410.17897) is the cheapest zero-overhead win at exactly our scale (468M: iso-loss at -16.1% params), and OLMo 2's reordered-norm+QK-norm kit tames spikes only jointly. The contested frontier: the Hyper-Connections lineage delivers only marginal gains at sub-1B (KromHC BPB delta ~0.002-0.003) while raw HC costs +26% training memory — effectively dead on T4; plain muP diverges in fp16 (u-µP) and its LR-transfer benefit is itself disputed (weight decay, not muP). The open question is composition: no published run combines Peri-LN, LNS, GPAS, value residual and Canon at any scale (the one measured interaction, LNS+scaled-init, is negative), and SozKZ proves the entire technique set is untested on Kazakh — a plain-Llama 600M baseline reaches only 30.3% cultural QA.

## Frontier highlights
- [[peri-ln-revisiting-normalization-layer-in-the-transformer-architecture|Peri-LN: Revisiting Normalization Layer in the Transformer Architecture]] — Direct fp16 evidence: Pre-LN overflows FP16 max at 0.5B tok, Peri-LN stays below + halves seed variance
- [[the-curse-of-depth-in-large-language-models|The Curse of Depth in Large Language Models]] — Largest zero-param ppl win (17.02->15.71 @1B) but incompatible with scaled init — can't stack
- [[value-residual-learning|Value Residual Learning]] — Cheapest win at 468M scale: iso-loss with -16% params, zero FLOP/memory overhead
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] — Kazakh baseline: plain-Llama 600M, none of these techniques used — whole ablation space unclaimed
- [[2-olmo-2-furious|2 OLMo 2 Furious]] — Stability kit: reordered-norm + QK-norm reduce spikes only jointly; spikes traced to repeated n-grams
- [[kromhc-manifold-constrained-hyper-connections-with-kronecker-product-residual|KromHC: Manifold-Constrained Hyper-Connections with Kronecker-Product Residual M…]] — Settles HC-at-sub-1B: marginal (~0.002 BPB), extends 'mHC has no sub-3B dense validation' gap

## Papers (12)
- [[kromhc-manifold-constrained-hyper-connections-with-kronecker-product-residual|KromHC: Manifold-Constrained Hyper-Connections with Kronecker-Product Residual Matrices]] (2026) — residual-stream-stability-qymyzlm-design
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] (2026) — tokenizer-morphology
- [[peri-ln-revisiting-normalization-layer-in-the-transformer-architecture|Peri-LN: Revisiting Normalization Layer in the Transformer Architecture]] (2025) — residual-stream-stability-qymyzlm-design
- [[the-curse-of-depth-in-large-language-models|The Curse of Depth in Large Language Models]] (2025) — residual-stream-stability-qymyzlm-design
- [[don-t-be-lazy-completep-enables-compute-efficient-deep-transformers|Don't be lazy: CompleteP enables compute-efficient deep transformers]] (2025) — residual-stream-stability-qymyzlm-design
- [[qwen3-technical-report|Qwen3 Technical Report]] (2025) — sota-slm
- [[gpas-accelerating-convergence-of-llm-pretraining-via-gradient-preserving|GPAS: Accelerating Convergence of LLM Pretraining via Gradient-Preserving Activation Scaling]] (2025) — residual-stream-stability-qymyzlm-design
- [[physics-of-language-models-part-4-1-architecture-design-and-the-magic-of-canon|Physics of Language Models: Part 4.1, Architecture Design and the Magic of Canon Layers]] (2025) — residual-stream-stability-qymyzlm-design
- [[u-p-the-unit-scaled-maximal-update-parametrization|u-$μ$P: The Unit-Scaled Maximal Update Parametrization]] (2024) — residual-stream-stability-qymyzlm-design
- [[hyper-connections|Hyper-Connections]] (2024) — residual-stream-stability-qymyzlm-design
- [[value-residual-learning|Value Residual Learning]] (2024) — residual-stream-stability-qymyzlm-design
- [[2-olmo-2-furious|2 OLMo 2 Furious]] (2024) — residual-stream-stability-qymyzlm-design

## Related topics
- [[small-lm-training-recipes-qymyzlm-design]] — 3 shared nodes
- [[attention-kv-architecture-sub-1b]] — 2 shared nodes

[[Home]]
