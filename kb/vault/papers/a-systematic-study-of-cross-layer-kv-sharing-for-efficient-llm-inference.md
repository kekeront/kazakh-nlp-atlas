---
kb_id: "arxiv:2410.14442"
type: "paper"
title: "A Systematic Study of Cross-Layer KV Sharing for Efficient LLM Inference"
arxiv_id: "2410.14442"
doi: null
hf_repo: null
year: 2024
topics: ["kv-cache-architecture"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["A Systematic Study of Cross-Layer KV Sharing for Efficient LLM Inference", "arXiv:2410.14442", "arxiv:2410.14442"]
tags: ["paper", "topic/kv-cache-architecture"]
---
# A Systematic Study of Cross-Layer KV Sharing for Efficient LLM Inference

[arXiv](https://arxiv.org/abs/2410.14442)
**Topics:** [[kv-cache-architecture]]

> [!abstract]
> Recently, sharing key-value (KV) cache across layers has been found effective in efficient inference of large language models (LLMs). To systematically investigate different techniques of cross-layer KV sharing, we propose a unified framework that covers several recent methods and their novel variants. We conduct comprehensive experiments on all the configurations of the framework, evaluating thei …

## Claims

> [!note] CLAIM — kv-cache-architecture
> Independent 2025 reproduction of cross-layer KV sharing ON GQA at ~1B exists: NAACL 2025 systematic study trains a 1.1B Llama (22 layers, 32 Q heads, 4 KV heads = GQA) from scratch on 100B SlimPajama tokens with 5 configs. At 2x KV-layer cut (11/22), the CLA2-equivalent (lasagna-bottom) loses 0.95 avg downstream points, while Gemma-3n-style trailing reuse (pizza-bottom) loses only 0.55 and sandwich-top only 0.12. Paper conclusion: at 2x reduction 'most configurations can achieve competitive performance to and higher throughput than standard transformers'. Also tests 110M GQA models (12 heads/6 KV) on Minipile 1.7B tokens — the smallest published cross-layer-KV-on-GQA datapoint.
>
> **Numbers:** 8-task zero-shot avg (Hellaswag/OBQA/WinoGrande/ARC-c/ARC-e/BoolQ/PIQA/SciQ) at 11 KV layers: baseline 50.17, sandwich-top 50.05 (-0.12), pizza-bottom 49.62 (-0.55), sandwich-middle 49.29 (-0.88), lasagna-bottom (=CLA2) 49.22 (-0.95). 1.1B: hidden 2048, 22 layers, lr 4e-4, batch 2M tok. Exact ppl values only in Figure 1(c) (image)
> **Relevance:** This is the answer to the assigned question: CLA2-on-GQA at ~1B IS published and reproduced — it works but is the WORST of the 2x-sharing layouts on downstream tasks; trailing-layer (Gemma-3n-style) and sandwich-top layouts dominate it at equal cache. Directly reorders the lab's plan-B design choice at ~600M.
> **Source:** arXiv:2410.14442 (Wu, Wu & Tu, NAACL 2025 short), Table 2 (configs), Table 4 (downstream), Sec 4.3; verified from arxiv.org/html/2410.14442v1; averages computed from quoted Table 4 rows · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[reducing-transformer-key-value-cache-size-with-cross-layer-attention|Reducing Transformer Key-Value Cache Size with Cross-Layer Attention]] — The Systematic Study of Cross-Layer KV Sharing generalizes and stress-tests CLA's adjacent-layer KV-reuse scheme
- [[kitty-accurate-and-efficient-2-bit-kv-cache-quantization-with-dynamic-channel|Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precis…]] — Orthogonal, composable KV-cut axis: layer-sharing vs 2-bit KV quantization
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] — Both train Kazakh/small LMs from scratch; cross-layer KV sharing is a candidate cut for SozKZ-scale from-scratch models
- [[config-json-via-huggingface-co-unsloth-gemma-3n-e2b-mirror|config.json via huggingface.co/unsloth/gemma-3n-E2B (mirror]] — Gemma-3n's trailing-layer reuse = study's pizza-bottom layout (-0.55), which it finds strictly better than CLA2
- [[value-residual-learning|Value Residual Learning]] — ResFormer's SVFormer shares layer-1 values across layers ~halving KV — same family as cross-layer KV sharing

[[Home]]
