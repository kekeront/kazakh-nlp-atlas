---
kb_id: "arxiv:2401.04088"
type: "paper"
title: "Mixtral of Experts"
arxiv_id: "2401.04088"
doi: null
hf_repo: null
year: 2024
topics: ["parameter-counting-convention-and-iso-si"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["Mixtral of Experts", "arXiv:2401.04088", "arxiv:2401.04088"]
tags: ["paper", "topic/parameter-counting-convention-and-iso-si"]
---
# Mixtral of Experts

[arXiv](https://arxiv.org/abs/2401.04088)
**Topics:** [[parameter-counting-convention-and-iso-si]]

> [!abstract]
> We introduce Mixtral 8x7B, a Sparse Mixture of Experts (SMoE) language model. Mixtral has the same architecture as Mistral 7B, with the difference that each layer is composed of 8 feedforward blocks (i.e. experts). For every token, at each layer, a router network selects two experts to process the current state and combine their outputs. Even though each token only sees two experts, the selected e …

## Claims

> [!note] CLAIM — parameter-counting-convention-and-iso-si
> The field size-classes sparse (MoE) models by TOTAL params, not active — active is a secondary efficiency stat. Mixtral 8x7B is universally called a 47B model (13B active); DeepSeek-V3 is 'the 671B model' (37B active, 5.5% activation ratio). Capacity/knowledge is credited to total params, compute to active. This precedent cuts AGAINST the user: even the MoE convention the paper would invoke to report '500M active' still groups the model by its ~1B total. No major model claims membership in a smaller size class than its total param count.
>
> **Numbers:** Mixtral 8x7B: 47B total / 13B active. DeepSeek-V3: 671B total / 37B active (5.5%). Named/bracketed by total in both cases.
> **Relevance:** Reporting only '500M active' to claim the 500M class runs against community naming norms and will read as size-class gaming; the safe move is to report both and bracket by total.
> **Source:** arXiv 2401.04088 (Mixtral of Experts); arXiv 2412.19437 (DeepSeek-V3 Technical Report) · **Sweep:** `slm-architecture-2026-07`

**Cited KB notes:** [[deepseek-v3-technical-report]]

## Related
- [[deepseekmoe-towards-ultimate-expert-specialization-in-mixture-of-experts|DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models]] — DeepSeekMoE formalizes the expert-specialization sparsity Mixtral popularized; both report total as the size class
- [[deepseek-v3-technical-report|DeepSeek-V3 Technical Report]] — Co-cited precedent: DeepSeek-V3 is 'the 671B model' (37B active, 5.5%) — models bracketed by total, not active

[[Home]]
