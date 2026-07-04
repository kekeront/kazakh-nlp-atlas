---
kb_id: "title:github com dao ailab flash attention readme fetched 2026 07 04 empirical sdpa measurement this session turing port performance details from search snippets only"
type: "source"
title: "github.com/Dao-AILab/flash-attention README (fetched 2026-07-04) + emp…"
doi: null
hf_repo: null
year: null
topics: ["hardware-gate"]
claims: 1
uncertain_claims: 1
verdicts: []
aliases: ["title:github com dao ailab flash attention readme fetched 2026 07 04 empirical sdpa measurement this session turing port performance details from search snippets only"]
tags: ["source", "topic/hardware-gate"]
---
# github.com/Dao-AILab/flash-attention README (fetched 2026-07-04) + emp…

**Topics:** [[hardware-gate]]

## Source URLs
- github.com/Dao-AILab/flash-attention README (fetched 2026-07-04) + empirical SDPA measurement this session
- Turing-port performance details from search snippets only

## Findings

> [!warning] UNCERTAIN — hardware-gate
> Softmax attention on SM75 is NOT blocked by FA2's Ampere-only requirement: (a) torch SDPA fp16 runs fast on SM75 out of the box (fastest kernel we measured, via cuDNN/memory-efficient backends); (b) the official Dao-AILab/flash-attention README now points Turing users to a separate 'flash-attention-turing' repo supporting 'a core subset of FlashAttention features on Turing' (fp16-only, since 'bf16 requires Ampere, Ada, or Hopper'). Search snippets attribute head dims up to 256 and 1.2-2.4x fwd speedups on RTX 2080 Ti to the Turing port — repo-level details not independently read. Flag: transferable-untested.
>
> **Numbers:** SDPA fp16, B=2/T=1024/d=768: 5.2 ms fwd+bwd, 397,144 tok/s/layer on SM75; FA2 requirement quote: 'Ampere, Ada, or Hopper GPUs'; Turing port claims fwd 1.2-2.4x, bwd up to 15-20x vs naive at long seq [snippet-level]
> **Relevance:** v1 QLoRA-CPT on Qwen3-0.6B (pure softmax attention) trains fine on T4 via SDPA — no FA2 needed; the Turing FA port is an optional upgrade worth one further verification pass.
> **Source:** github.com/Dao-AILab/flash-attention README (fetched 2026-07-04) + empirical SDPA measurement this session; Turing-port performance details from search snippets only · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[hardware-efficient-attention-for-fast-decoding|Hardware-Efficient Attention for Fast Decoding]] — Both weigh hardware-fit of attention; node measures SDPA fp16 as fastest SM75 kernel while FA2 needs Ampere+

[[Home]]
