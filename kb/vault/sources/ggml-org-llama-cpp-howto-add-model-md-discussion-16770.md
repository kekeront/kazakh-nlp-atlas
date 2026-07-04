---
kb_id: "title:ggml org llama cpp howto add model md discussion 16770 ubergarm deepseek v3 gguf card ik llama cpp requirement"
type: "source"
title: "ggml-org/llama.cpp HOWTO-add-model.md + Discussion #16770"
doi: null
hf_repo: null
year: null
topics: ["inference-tts"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:ggml org llama cpp howto add model md discussion 16770 ubergarm deepseek v3 gguf card ik llama cpp requirement"]
tags: ["source", "topic/inference-tts"]
---
# ggml-org/llama.cpp HOWTO-add-model.md + Discussion #16770

**Topics:** [[inference-tts]]

## Source URLs
- ggml-org/llama.cpp HOWTO-add-model.md + Discussion #16770
- ubergarm/DeepSeek-V3-GGUF card (ik_llama.cpp requirement)

## Findings

> [!note] CLAIM — inference-tts
> MLA breaks mainline GGUF export: DeepSeek-style MLA GGUF requires the ik_llama.cpp fork and will not run on vanilla llama.cpp, ollama, LM Studio, or KoboldCpp. Any novel module (Engram conditional n-gram memory, mHC hyper-connections, MLA) requires a full custom C++ integration: new llm_arch enum, LLM_TENSOR_NAMES/INFOS, a build_arch_graph implementation, plus a gguf-py conversion subclass with tensor mappings.
>
> **Numbers:** MLA -> ik_llama.cpp fork only; each custom module = 1 new llm_arch + build_arch_graph + gguf-py class
> **Relevance:** Engram + mHC + MLA together = three custom C++ integrations before any edge/GGUF deploy. For a shippable product, either budget that engineering or keep a GGUF-clean GQA+RoPE inference variant.
> **Source:** ggml-org/llama.cpp HOWTO-add-model.md + Discussion #16770; ubergarm/DeepSeek-V3-GGUF card (ik_llama.cpp requirement) · **Sweep:** `slm-architecture-2026-07`

## Related
- [[x-ecomla-upcycling-pre-trained-attention-into-mla-for-efficient-and-extreme-kv|X-EcoMLA: Upcycling Pre-Trained Attention into MLA for Efficient and Extreme KV Compressio…]] — MLA export breaks mainline GGUF (ik_llama.cpp fork only); X-EcoMLA's upcycled MLA inherits this deployment penalty
- [[conditional-memory-via-scalable-lookup-a-new-axis-of-sparsity-for-large|Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models]] — Deployment tax: Engram conditional-lookup memory needs a full custom llm_arch + gguf-py C++ integration, not a drop-in

[[Home]]
