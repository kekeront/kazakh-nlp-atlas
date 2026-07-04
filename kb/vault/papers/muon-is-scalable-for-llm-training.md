---
kb_id: "arxiv:2502.16982"
type: "paper"
title: "Muon is Scalable for LLM Training"
arxiv_id: "2502.16982"
doi: null
hf_repo: null
year: 2025
topics: ["small-lm-training-recipes-qymyzlm-design"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Muon is Scalable for LLM Training", "arXiv:2502.16982", "arxiv:2502.16982"]
tags: ["paper", "topic/small-lm-training-recipes-qymyzlm-design"]
---
# Muon is Scalable for LLM Training

[arXiv](https://arxiv.org/abs/2502.16982)
**Topics:** [[small-lm-training-recipes-qymyzlm-design]]

> [!abstract]
> Recently, the Muon optimizer based on matrix orthogonalization has demonstrated strong results in training small-scale language models, but the scalability to larger models has not been proven. We identify two crucial techniques for scaling up Muon: (1) adding weight decay and (2) carefully adjusting the per-parameter update scale. These techniques allow Muon to work out-of-the-box on large-scale …

## Claims

> [!note] CLAIM — small-lm-training-recipes-qymyzlm-design
> [transferable-untested] Muon (Moonlight paper) is validated down to 399M non-embedding params — inside the lab's scale: scaling-law fits give Muon loss 2.506*C^-0.052 vs AdamW 2.608*C^-0.054, i.e. ~52% of AdamW's training FLOPs to match performance. Required fixes to scale: (1) decoupled weight decay lambda=0.1 (W_t = W_{t-1} - eta*(O_t + lambda*W_{t-1})); (2) update-RMS matching: scale update by 0.2*sqrt(max(A,B)) to match AdamW's typical update RMS 0.2-0.4. Scaling-law runs: 399M-1.5B non-emb params, 8.92-38.91B tokens, LRs 9.5e-4..8.3e-4, batch 96-256 seqs @ 8K ctx. Muon stores ONE momentum buffer vs AdamW's two (half the optimizer memory). Caveat: paper runs Newton-Schulz iterations in bf16; fp16 NS on T4 (no bf16) is unvalidated anywhere.
>
> **Numbers:** ~52% FLOPs vs AdamW; smallest model 399M non-emb @ 8.92B tok; WD 0.1; RMS-match factor 0.2*sqrt(max(A,B)); 1 vs 2 momentum buffers
> **Relevance:** At QymyzLM scale Muon halves optimizer VRAM (critical on 2x16GB T4) and roughly halves compute-to-loss — but the fp16-only constraint makes NS-iteration numerics the open risk; needs a cheap pilot (NS in fp32 costs little since it runs per-step on weight matrices).
> **Source:** arXiv:2502.16982 (Muon is Scalable for LLM Training), Table 2 + Sec. 2 (HTML) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[predictable-scale-part-i-step-law-optimal-hyperparameter-scaling-law-in-large|Predictable Scale: Part I, Step Law -- Optimal Hyperparameter Scaling Law in Large Languag…]] — Both give sub-2B optimizer/LR scaling laws; Step-Law's AdamW HP transfer complements Muon's FLOPs-efficiency claim
- [[defeating-the-training-inference-mismatch-via-fp16|Defeating the Training-Inference Mismatch via FP16]] — Muon's fp16 Newton-Schulz is unvalidated on T4; this node argues fp16 training is viable, testing that gap
- [[empirical-tmp-claude-1000-home-altairzhambyl-projects-slms|Empirical: /tmp/claude-1000/-home-altairzhambyl-projects-SLMs-basic/98…]] — Empirical SM75 6.6x bf16 trap in KellerJordan Muon; this paper argues Muon scales but is silent on Turing/fp16 NS5 path

[[Home]]
