---
kb_id: "arxiv:2502.02732"
type: "paper"
title: "Peri-LN: Revisiting Normalization Layer in the Transformer Architecture"
arxiv_id: "2502.02732"
doi: null
hf_repo: null
year: 2025
topics: ["residual-stream-stability-qymyzlm-design"]
claims: 2
uncertain_claims: 0
verdicts: []
aliases: ["Peri-LN: Revisiting Normalization Layer in the Transformer Architecture", "arXiv:2502.02732", "arxiv:2502.02732"]
tags: ["paper", "topic/residual-stream-stability-qymyzlm-design"]
---
# Peri-LN: Revisiting Normalization Layer in the Transformer Architecture

[arXiv](https://arxiv.org/abs/2502.02732)
**Topics:** [[residual-stream-stability-qymyzlm-design]]

> [!abstract]
> Selecting a layer normalization (LN) strategy that stabilizes training and speeds convergence in Transformers remains difficult, even for today's large language models (LLM). We present a comprehensive analytical foundation for understanding how different LN strategies influence training dynamics in large-scale Transformers. Until recently, Pre-LN and Post-LN have long dominated practices despite …

## Claims

> [!note] CLAIM — residual-stream-stability-qymyzlm-design
> [transferable-untested] Peri-LN (LN->sublayer->LN->residual) is the single strongest fp16-relevant norm result: at 400M/30B-token scale it beats Pre-LN on final loss AND has direct fp16-overflow evidence — Pre-LN hidden-state magnitude exceeds the FP16 max (65504) as early as 0.5B training tokens, while Peri-LN stays below it throughout; benchmark std across seeds reduced by more than half. Gemma 3 and OLMo 2 use the same peri-norm family. On a T4 (fp16 only, no bf16) a from-scratch Pre-LN 500M run is at documented overflow risk that Peri-LN removes architecturally.
>
> **Numbers:** 400M: loss Pre-LN 3.43 -> Peri-LN 3.34; 1.5B: 3.29 -> 3.18; 3.2B: 3.20 -> 3.11; 30B tokens DCLM, seq 8192; Pre-LN exceeds FP16 max at 0.5B tokens (Fig 11); seed-variance reduced >2x; Pre-LN best LR 2e-3, Peri-LN stable across 1e-4..5e-3
> **Relevance:** Kaggle T4 has NO bf16; fp16 overflow of the residual stream is the concrete failure mode for a from-scratch 500M/10B-token Kazakh run. Peri-LN is ~zero-cost (extra RMSNorm per sublayer) and widens the usable LR range. Verdict: worth it at 500M/10B — default norm scheme for the from-scratch spec.
> **Source:** arXiv:2502.02732 (Peri-LN, HTML full text fetched 2026-07-04, Fig 11 + Table 1) · **Sweep:** `slm-arch-for-kazakh`

> [!note] CLAIM — residual-stream-stability-qymyzlm-design
> [transferable-untested] The variance-control field has NO published composition results: Peri-LN, LayerNorm Scaling, GPAS, value residual, and Canon layers have never been combined in any published run at any scale; the one measured interaction is negative (LNS + Scaled Init is worse than LNS alone, arXiv:2502.05795). A 500M spec that naively stacks all of them is outside every validated regime — same failure pattern the KB documents for Engram-on-dense.
>
> **Numbers:** 1 measured interaction, negative (LNS+Scaled-Init < LNS alone); 0 published multi-technique compositions
> **Relevance:** Design-panel guardrail: the from-scratch spec should adopt at most ONE variance-control mechanism (recommend Peri-LN for its direct fp16-overflow evidence) + value residual (orthogonal, value-stream not hidden-stream) and treat anything further as proxy-ablation candidates, not defaults.
> **Source:** Cross-source synthesis: arXiv:2502.02732, 2502.05795, 2506.22049, 2410.17897, 2512.17351 (no combination experiments found in any; LNS+ScaledInit negative result in 2502.05795) · **Sweep:** `slm-arch-for-kazakh`

**Cited KB notes:** [[the-curse-of-depth-in-large-language-models]]

## Related
- [[2-olmo-2-furious|2 OLMo 2 Furious]] — OLMo2 reordered-norm and Peri-LN are the same normalize-sublayer-outputs family for residual-stream stability
- [[defeating-the-training-inference-mismatch-via-fp16|Defeating the Training-Inference Mismatch via FP16]] — both target fp16 numerical stability; Peri-LN keeps hidden states below FP16 max architecturally
- [[qwen3-technical-report|Qwen3 Technical Report]] — Both target residual/attention stability at scale; Qwen3 uses QK-Norm, Peri-LN repositions the norm

[[Home]]
