---
kb_id: "title:github com dao ailab flash attention readme issues 887 1608 github com farnghwai flash attention 2080ti"
type: "source"
title: "github.com/Dao-AILab/flash-attention README + issues #887, #1608"
doi: null
hf_repo: null
year: null
topics: ["attention-kv-sub1b-attention-kv-architec"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:github com dao ailab flash attention readme issues 887 1608 github com farnghwai flash attention 2080ti"]
tags: ["source", "topic/attention-kv-sub1b-attention-kv-architec"]
---
# github.com/Dao-AILab/flash-attention README + issues #887, #1608

**Topics:** [[attention-kv-sub1b-attention-kv-architec]]

## Source URLs
- github.com/Dao-AILab/flash-attention README + issues #887, #1608
- github.com/farnghwai/flash-attention-2080ti

## Findings

> [!note] CLAIM — attention-kv-sub1b-attention-kv-architec
> [hardware fact, verified] FlashAttention-2 does NOT support Turing (SM75 = Kaggle T4): the official Dao-AILab repo states FA2 supports Ampere/Ada/Hopper only and directs Turing users to FlashAttention 1.x; open issues #887/#1608 confirm no FA2 Turing kernel as of 2025-2026 (an unofficial community port exists for a feature subset). Practical consequence: on T4x2 use PyTorch SDPA's memory-efficient (xformers-style) backend or FA1; any recipe whose throughput claims assume FA2 (e.g., Transformer++ fastest-at-2K in the Gated DeltaNet paper's Fig.3, NSA custom kernels) does not transfer. Whether Triton FLA kernels (GatedDeltaNet/KDA) run acceptably on SM75 is unverified — a blocker for any hybrid-linear variant on free compute.
>
> **Numbers:** FA2 requires SM80+; T4 = SM75; fallback = FA1 or PyTorch SDPA mem-efficient backend
> **Relevance:** Directly constrains both the QLoRA-CPT training config (attn_implementation choice) and the from-scratch architecture menu: exotic-kernel attention (NSA, linear hybrids) carries unquantified T4 risk; plain SDPA-compatible designs (GQA/MLA/SWA/gated-SDPA) are safe.
> **Source:** github.com/Dao-AILab/flash-attention README + issues #887, #1608; github.com/farnghwai/flash-attention-2080ti · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[lab-probe-2026-07-04-torch-nn-attention-sdpa-kernel|Lab probe 2026-07-04 (torch.nn.attention.sdpa_kernel warnings verbatim…]] — independently confirm FlashAttention is unavailable on sm_75 Turing (T4/2080Ti class)

[[Home]]
