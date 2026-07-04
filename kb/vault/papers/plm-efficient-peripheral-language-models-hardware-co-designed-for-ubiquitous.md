---
kb_id: "arxiv:2503.12167"
type: "paper"
title: "PLM: Efficient Peripheral Language Models Hardware-Co-Designed for Ubiquitous Computing"
arxiv_id: "2503.12167"
doi: null
hf_repo: "PLM-Team/PLM-1.8B-Instruct"
year: 2025
topics: ["mla-at-sub-1b-scale"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["PLM: Efficient Peripheral Language Models Hardware-Co-Designed for Ubiquitous Computing", "arXiv:2503.12167", "arxiv:2503.12167"]
tags: ["paper", "topic/mla-at-sub-1b-scale"]
---
# PLM: Efficient Peripheral Language Models Hardware-Co-Designed for Ubiquitous Computing

[arXiv](https://arxiv.org/abs/2503.12167)
**Topics:** [[mla-at-sub-1b-scale]]

> [!abstract]
> While scaling laws have been continuously validated in large language models (LLMs) with increasing model parameters, the inherent tension between the inference demands of LLMs and the limited resources of edge devices poses a critical challenge to the development of edge intelligence. Recently, numerous small language models have emerged, aiming to distill the capabilities of LLMs into smaller fo …

## Claims

> [!note] CLAIM — mla-at-sub-1b-scale
> PLM-1.8B (nearest production from-scratch MLA above the lab's scale) config verified: kv_lora_rank=512, q_lora_rank=null (no q compression), qk_rope_head_dim=64, qk_nope_head_dim=128, v_head_dim=128, hidden 2048, 16 heads, 32 layers. Confirms the pattern: every from-scratch dense MLA near 1-2B published with benchmarks uses shared rank 512, none 256.
>
> **Numbers:** rank 512 = d/4 at d=2048; cache (512+64)=576 elem/token/layer, same absolute latent as DeepSeek-V2/V3
> **Relevance:** Anchors the conservative option: at 1.8B the proven choice is 512 (=d/4). For the lab's d=1536, rank 512=d/3 (EG-MLA's proven sub-1B ratio) and rank 384=d/4 (PLM's ratio) are the ratio-matched picks.
> **Source:** https://huggingface.co/PLM-Team/PLM-1.8B-Instruct/raw/main/config.json (fetched 2026-07-03); arXiv:2503.12167 · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[deepseek-v3-technical-report|DeepSeek-V3 Technical Report]] — PLM-1.8B's rank-512 latent is the same absolute cache as DeepSeek-V3; confirms 1–2B from-scratch uses 512

[[Home]]
