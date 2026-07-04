---
kb_id: "hf:api/models"
type: "source"
title: "GitHub search API over vllm-project/vllm, ggml-org/llama.cpp, NVIDIA/T…"
doi: null
hf_repo: "api/models"
year: null
topics: ["gla-2-gta-arxiv-2505-21487-zadouri-strau"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["hf:api/models"]
tags: ["source", "topic/gla-2-gta-arxiv-2505-21487-zadouri-strau"]
---
# GitHub search API over vllm-project/vllm, ggml-org/llama.cpp, NVIDIA/T…

**Topics:** [[gla-2-gta-arxiv-2505-21487-zadouri-strau]]

## Source URLs
- GitHub search API over vllm-project/vllm, ggml-org/llama.cpp, NVIDIA/TensorRT-LLM, sgl-project/sglang, Dao-AILab repos
- huggingface.co/api/models?search=grouped-tied and grouped latent
- github.com/Dao-AILab/grouped-latent-attention

## Findings

> [!note] CLAIM — gla-2-gta-arxiv-2505-21487-zadouri-strau
> Zero adoption in any serving stack or released model as of 2026-07-03: vLLM has 0 code hits for grouped_latent/GroupedLatentAttention (only tangential issue mentions in Helix-parallelism discussions); llama.cpp has 0 issues/PRs mentioning grouped-tied/grouped-latent/2505.21487 (no GGUF path); TensorRT-LLM 0 code hits; SGLang 0 (2 apparent hits are multimodal latent-pipeline false positives); Hugging Face hosts 0 models matching 'grouped-tied' or 'grouped latent'. The official repo (Dao-AILab/grouped-latent-attention) has 135 stars, 4 forks, ships only modeling files (no training code), and its modeling_llama_GLA.py is reused by 0 real downstream projects (3 GitHub-wide hits, all index/doc files).
>
> **Numbers:** vLLM 0, llama.cpp 0, TRT-LLM 0, SGLang 0, HF models 0; repo 135 stars / 4 forks / 5 open issues; 0 downstream code reuse
> **Relevance:** Negates the shipping story outright: a ≤600M Kazakh model using GLA-2/GTA could not be served by any mainstream stack or distributed as GGUF, unlike MLA (DeepSeek format), which is natively supported in vLLM/SGLang/llama.cpp.
> **Source:** GitHub search API over vllm-project/vllm, ggml-org/llama.cpp, NVIDIA/TensorRT-LLM, sgl-project/sglang, Dao-AILab repos; huggingface.co/api/models?search=grouped-tied and grouped latent; github.com/Dao-AILab/grouped-latent-attention · **Sweep:** `mla-sub1b-2026-07`

[[Home]]
