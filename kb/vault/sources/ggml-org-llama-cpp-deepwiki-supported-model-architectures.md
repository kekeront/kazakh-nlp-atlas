---
kb_id: "title:ggml org llama cpp deepwiki supported model architectures devingulliver mamba gguf"
type: "source"
title: "ggml-org/llama.cpp DeepWiki 'Supported Model Architectures'"
doi: null
hf_repo: null
year: null
topics: ["inference-tts"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:ggml org llama cpp deepwiki supported model architectures devingulliver mamba gguf"]
tags: ["source", "topic/inference-tts"]
---
# ggml-org/llama.cpp DeepWiki 'Supported Model Architectures'

**Topics:** [[inference-tts]]

## Source URLs
- ggml-org/llama.cpp DeepWiki 'Supported Model Architectures'
- devingulliver/mamba-gguf

## Findings

> [!note] CLAIM — inference-tts
> llama.cpp does support recurrent/hybrid backbones (Mamba, RWKV, Qwen3-Next Gated DeltaNet SSM layers) and 100+ architectures, and llama-server handles SSM prefix-caching for multiple users — but each still requires the per-architecture C++ graph and gguf-py conversion class described above.
>
> **Numbers:** 100+ architectures; Mamba GGUF at 2/3/4/5/6/8/16/32-bit; Qwen3-Next hybrid SSM supported
> **Relevance:** If the Kazakh design explores a hybrid SSM/attention backbone for cheaper KV, it is deployable in llama.cpp — but budget the same custom-arch integration cost as MLA/Engram; there is no free export.
> **Source:** ggml-org/llama.cpp DeepWiki 'Supported Model Architectures'; devingulliver/mamba-gguf · **Sweep:** `slm-architecture-2026-07`

## Related
- [[github-com-state-spaces-mamba-setup-py-raw-main-branch|github.com/state-spaces/mamba setup.py (raw, main branch, fetched 2026…]] — Both track Mamba deployability; node confirms mamba-ssm CUDA builds for sm_75, complementing llama.cpp Mamba GGUF support

[[Home]]
