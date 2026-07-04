---
kb_id: "arxiv:2405.14591"
type: "paper"
title: "Base of RoPE Bounds Context Length"
arxiv_id: "2405.14591"
doi: null
hf_repo: null
year: 2024
topics: ["attention-kv-architecture-sub-1b"]
claims: 1
uncertain_claims: 1
verdicts: []
aliases: ["Base of RoPE Bounds Context Length", "arXiv:2405.14591", "arxiv:2405.14591"]
tags: ["paper", "topic/attention-kv-architecture-sub-1b"]
---
# Base of RoPE Bounds Context Length

[arXiv](https://arxiv.org/abs/2405.14591)
**Topics:** [[attention-kv-architecture-sub-1b]]

> [!abstract]
> Position embedding is a core component of current Large Language Models (LLMs). Rotary position embedding (RoPE), a technique that encodes the position information with a rotation matrix, has been the de facto choice for position embedding in many LLMs, such as the Llama series. RoPE has been further utilized to extend long context capability, which is roughly based on adjusting the \textit{base} …

## Claims

> [!warning] UNCERTAIN — attention-kv-architecture-sub-1b
> [transferable-untested] RoPE base has an absolute lower bound per target context (NeurIPS 2024 'Base of RoPE Bounds Context Length'); below it the model gains only 'superficial' long-context ability. Reported bound table: 1K→4.3e3, 2K→1.6e4, 4K→2.7e4, 8K→8.4e4, 16K→3.1e5, 32K→6.4e5, 128K→7.8e6, 1M→5.1e8. For QymyzLM's realistic 4-8K native context, theta ≈1e5-5e5 satisfies the bound with margin; classic theta=1e4 is BELOW the 8K bound; Qwen3's 1e6 (32K) and Gemma3's 1e6-global/1e4-local(512-window) are both consistent with the theory. Exact table values taken from search-indexed paper text, not re-read in the primary PDF.
>
> **Numbers:** theta lower bounds: 4K→2.7e4, 8K→8.4e4, 16K→3.1e5, 32K→6.4e5
> **Relevance:** Directly sets the from-scratch rope_theta choice: theta=1e5 (or copy Gemma's 1e4-local/1e6-global split under SWA) for a 4-8K model; avoids both superficial-long-context (too small) and needless decay-flattening (1e6 at 4K).
> **Source:** arXiv:2405.14591 (NeurIPS 2024) — abstract read; bound table via search snippet of paper HTML · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[lab-measurement-t4bench2-py-t4bench3-py|Lab measurement t4bench2.py/t4bench3.py]] — proposed 2048-ctx CPT with late 4K annealing interacts with RoPE base, which bounds usable context length

[[Home]]
