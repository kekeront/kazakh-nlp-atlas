---
kb_id: "arxiv:2309.14322"
type: "paper"
title: "Small-scale proxies for large-scale Transformer training instabilities"
arxiv_id: "2309.14322"
doi: null
hf_repo: null
year: 2023
topics: ["attention-kv-architecture-sub-1b", "small-lm-training-recipes-qymyzlm-design"]
claims: 2
uncertain_claims: 1
verdicts: []
aliases: ["Small-scale proxies for large-scale Transformer training instabilities", "arXiv:2309.14322", "arxiv:2309.14322"]
tags: ["paper", "topic/attention-kv-architecture-sub-1b", "topic/small-lm-training-recipes-qymyzlm-design"]
---
# Small-scale proxies for large-scale Transformer training instabilities

[arXiv](https://arxiv.org/abs/2309.14322)
**Topics:** [[attention-kv-architecture-sub-1b]], [[small-lm-training-recipes-qymyzlm-design]]

> [!abstract]
> Teams that have trained large Transformer-based models have reported training instabilities at large scale that did not appear when training with the same hyperparameters at smaller scales. Although the causes of such instabilities are of scientific interest, the amount of resources required to reproduce them has made investigation difficult. In this work, we seek ways to reproduce and study train …

## Claims

> [!note] CLAIM — attention-kv-architecture-sub-1b
> [transferable-untested] QK-norm is the consensus fp16-stability mechanism and is already inside the lab's CPT base: attention-logit-growth instability reproduces at small scale at high LR, and QK-layernorm lets models reach similar loss across orders of magnitude of learning-rate variation (small-scale proxies paper); Qwen3 explicitly added QK-Norm and removed QKV-bias 'to stabilize small-scale training' (KB); Mellum-2 (2026, ablation-driven production report) also ships QK-Norm (RMSNorm on Q and K projections). No paper ablates QK-norm on pure-fp16 (non-bf16) pretraining at sub-1B — the exact regime Kaggle T4 forces.
>
> **Numbers:** LR robustness across ~orders of magnitude with QK-layernorm (2309.14322); adopted by Qwen3, OLMo2, Gemma3, Mellum2
> **Relevance:** For from-scratch on T4 fp16 (no bf16), QK-Norm is mandatory, not optional: fp16's narrow range makes attention-logit growth the most likely divergence mode; CPT track inherits it for free from Qwen3-0.6B.
> **Source:** arXiv:2309.14322 (abstract read) + arXiv:2505.09388 (KB) + arXiv:2605.31268 (Mellum 2, fetched) · **Sweep:** `slm-arch-for-kazakh`

**Cited KB notes:** [[qwen3-technical-report]], [[mellum2-technical-report]]

> [!warning] UNCERTAIN — small-lm-training-recipes-qymyzlm-design
> [transferable-untested] The Wortsman et al. small-scale-proxies paper — the cited foundation of DCLM's stability setup — shows the two dominant instabilities (attention-logit growth, output-logit divergence) reproduce in small models at high LR and are mitigated by qk-layernorm and z-loss respectively, flattening LR sensitivity across orders of magnitude of learning rate. Exact model sizes and sensitivity ranges not re-verified from the PDF this sweep.
>
> **Numbers:** qk-layernorm -> attention-logit growth; z-loss -> output-logit divergence; 'orders of magnitude of learning rate variation' (abstract)
> **Relevance:** Primary justification that stability interventions validated at small scale transfer to the lab's 500M fp16 regime; details flagged for one follow-up read before the design spec cites numbers.
> **Source:** arXiv:2309.14322 (Small-scale proxies for large-scale Transformer training instabilities); cited as setup basis in arXiv:2406.11794 Appendix · **Sweep:** `slm-arch-for-kazakh`

**Cited KB notes:** [[datacomp-lm-in-search-of-the-next-generation-of-training-sets-for-language]]

## Related
- [[2-olmo-2-furious|2 OLMo 2 Furious]] — OLMo2 adopts this paper's qk-layernorm + z-loss stability pair as its production recipe
- [[defeating-the-training-inference-mismatch-via-fp16|Defeating the Training-Inference Mismatch via FP16]] — Both target fp16 numerical stability; relevant to the T4's forced fp16 regime this claim flags as never ablated at sub-1B
- [[yulan-mini-an-open-data-efficient-language-model|YuLan-Mini: An Open Data-efficient Language Model]] — YuLan-Mini's stability kit (muP init, z-loss, residual scaling) operationalizes the small-scale training-instability diagnostics of this…

[[Home]]
