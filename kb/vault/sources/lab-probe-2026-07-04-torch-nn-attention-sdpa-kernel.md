---
kb_id: "title:lab probe 2026 07 04 torch nn attention sdpa kernel warnings verbatim reproduced oom vs 2 73 gib with patch in t4bench2 py"
type: "source"
title: "Lab probe 2026-07-04 (torch.nn.attention.sdpa_kernel warnings verbatim…"
doi: null
hf_repo: null
year: null
topics: ["kaggle-t4x2-compute-vram-budget-for-the"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:lab probe 2026 07 04 torch nn attention sdpa kernel warnings verbatim reproduced oom vs 2 73 gib with patch in t4bench2 py"]
tags: ["source", "topic/kaggle-t4x2-compute-vram-budget-for-the"]
---
# Lab probe 2026-07-04 (torch.nn.attention.sdpa_kernel warnings verbatim…

**Topics:** [[kaggle-t4x2-compute-vram-budget-for-the]]

## Source URLs
- Lab probe 2026-07-04 (torch.nn.attention.sdpa_kernel warnings verbatim)
- reproduced OOM vs 2.73 GiB with patch in t4bench2.py

## Findings

> [!note] CLAIM — kaggle-t4x2-compute-vram-budget-for-the
> [measured; engineering landmine] On sm_75 (Kaggle T4 and lab 2070), PyTorch 2.11 has NO FlashAttention (kernel explicitly 'only supports gpu architectures in the range [sm80, sm121]'), and the fused memory-efficient SDPA kernel rejects GQA head-count mismatch (Q=16 vs KV=8 heads). transformers 5.5.2's SDPA path (enable_gqa) therefore silently falls back to the MATH backend, materializing O(s^2) score tensors (16x4096x4096 fp16 ≈ 512MiB-1GiB allocations) — we reproduced OOM at 4K ctx without the fix. Workaround (measured working): repeat_interleave KV heads to 16 before SDPA => EFFICIENT_ATTENTION kernel engages, peak drops to 2.73 GiB. Any Kaggle CPT script must include this repeat_kv patch or pin an attention implementation verified to expand KV heads.
>
> **Numbers:** FLASH: fails sm7.5; MEM_EFF: fails 16-vs-8 heads, OK after KV expansion; math-backend spike ~512MiB-1GiB per attention op @ 4K
> **Relevance:** Without this patch the 4K-ctx run OOMs or crawls on T4; it is the single most likely 'works-on-A100, dies-on-Kaggle' failure of the recipe.
> **Source:** Lab probe 2026-07-04 (torch.nn.attention.sdpa_kernel warnings verbatim); reproduced OOM vs 2.73 GiB with patch in t4bench2.py · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[native-sparse-attention-hardware-aligned-and-natively-trainable-sparse-attention|Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention]] — NSA's hardware-aligned kernels assume Ampere+; on sm_75 with no FlashAttention such sparse-attention wins do not port to Kaggle T4
- [[github-com-dao-ailab-flash-attention-readme-issues-887-1608|github.com/Dao-AILab/flash-attention README + issues #887, #1608]] — independently confirm FlashAttention is unavailable on sm_75 Turing (T4/2080Ti class)

[[Home]]
