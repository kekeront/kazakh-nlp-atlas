---
kb_id: "arxiv:2601.21579"
type: "paper"
title: "KromHC: Manifold-Constrained Hyper-Connections with Kronecker-Product Residual Matrices"
arxiv_id: "2601.21579"
doi: null
hf_repo: null
year: 2026
topics: ["residual-stream-stability-qymyzlm-design"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["KromHC: Manifold-Constrained Hyper-Connections with Kronecker-Product Residual Matrices", "arXiv:2601.21579", "arxiv:2601.21579"]
tags: ["paper", "topic/residual-stream-stability-qymyzlm-design"]
---
# KromHC: Manifold-Constrained Hyper-Connections with Kronecker-Product Residual Matrices

[arXiv](https://arxiv.org/abs/2601.21579)
**Topics:** [[residual-stream-stability-qymyzlm-design]]

> [!abstract]
> The success of Hyper-Connections (HC) in neural networks (NN) has also highlighted issues related to training instability and restricted scalability. The Manifold-Constrained Hyper-Connections (mHC) mitigate these challenges by projecting the residual connection space onto a Birkhoff polytope, however, it faces two issues: 1) its iterative Sinkhorn-Knopp (SK) algorithm does not always yield exactl …

## Claims

> [!note] CLAIM — residual-stream-stability-qymyzlm-design
> [transferable-untested] mHC follow-ups add ZERO meaningful sub-1B dense evidence — the only sub-1B dense datapoints in the whole HC/mHC lineage show near-nil gains: KromHC (Kronecker-factored doubly-stochastic HC) at 60M and 186M dense, ~20 tok/param: validation BPB residual 0.864 vs mHC 0.861 vs KromHC 0.862 (delta ~0.002-0.003 BPB), though KromHC gets best CORE score 16.872 and lowest gradient norms; it cuts HC parameter overhead 48% (959K vs mHC 1,844K at n=4/12 blocks, O(n^2 C) vs O(n^3 C)). go-mHC validates only on a 30M GPT + synthetic stream-mixing tasks (10x faster convergence to theoretical minimum — synthetic only). This extends the KB entry 'mHC has no sub-3B/dense validation': the gap has since been probed and the effect at our scale looks marginal.
>
> **Numbers:** KromHC: 60M/186M dense, ~20 tok/param; BPB 0.864 (residual) / 0.861 (mHC) / 0.862 (KromHC); CORE 16.872; params +959K (KromHC) vs +1,844K (mHC) vs +2,433K (mHC-lite) at n=4, D=12; go-mHC: 30M GPT, O(d^3) parameterization
> **Relevance:** Design panel must decide on the residual stack; the mHC lineage's own smallest-scale evidence (186M dense) shows ~0.002 BPB — noise-level for a 6.7-25% overhead technique on T4 without fused kernels (KB). Verdict: reject entire HC/mHC family at 500M; value residual + Peri-LN/LNS deliver more at zero cost.
> **Source:** arXiv:2601.21579 (KromHC, HTML v2 full text fetched 2026-07-04); arXiv:2604.02309 (go-mHC, abstract fetched); KB mHC entries (2512.24880) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[mhc-manifold-constrained-hyper-connections|mHC: Manifold-Constrained Hyper-Connections]] — KromHC extends mHC with Kronecker-product mixing — evidence mHC is a fast-moving mainstream subfield, indefensible as a novel contribution

[[Home]]
