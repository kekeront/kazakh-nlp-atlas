---
kb_id: "arxiv:2412.07633"
type: "paper"
title: "ChocoLlama: Lessons Learned From Teaching Llamas Dutch"
arxiv_id: "2412.07633"
doi: null
hf_repo: null
year: 2024
topics: ["qymyzlm-architecture-fork"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["ChocoLlama: Lessons Learned From Teaching Llamas Dutch", "arXiv:2412.07633", "arxiv:2412.07633"]
tags: ["paper", "topic/qymyzlm-architecture-fork"]
---
# ChocoLlama: Lessons Learned From Teaching Llamas Dutch

[arXiv](https://arxiv.org/abs/2412.07633)
**Topics:** [[qymyzlm-architecture-fork]]

> [!abstract]
> While Large Language Models (LLMs) have shown remarkable capabilities in natural language understanding and generation, their performance often lags in lower-resource, non-English languages due to biases in the training data. In this work, we explore strategies for adapting the primarily English LLMs (Llama-2 and Llama-3) to Dutch, a language spoken by 30 million people worldwide yet often underre …

## Claims

> [!note] CLAIM — qymyzlm-architecture-fork
> [transferable-untested (Dutch); flag] Full tokenizer swap + CPT DOES retain the base model's advantage and even beats keeping the original tokenizer, given ~32B CPT tokens: ChocoLlama-2-7B-tokentrans-base (Dutch tokenizer swapped via trans-tokenization, embedding reinit) outperforms ChocoLlama-2-7B-base (original Llama-2 tokenizer, same 32B Dutch tokens, same LoRA r=8/alpha=32, 544M trainable = 7.75%) on Dutch benchmarks. Caveat directly relevant to Qwen3: on the stronger multilingual Llama-3-8B the same CPT recipe gave ~zero gain (0.50 -> 0.49 avg), suggesting strong 2024+ multilingual bases (Qwen3 class) gain little from LoRA-CPT without tokenizer/vocab surgery — the swap is where the win is.
>
> **Numbers:** Swapped vs kept tokenizer @32B Dutch tokens: avg 0.45 vs 0.41 (ARC 0.42 vs 0.35, HellaSwag 0.61 vs 0.56, MMLU 0.32 vs 0.31, TruthfulQA 0.43 = 0.43); swapped tokenizer −29.4% tokens; Llama-3-8B: 0.50 -> 0.49 after CPT
> **Relevance:** Central fork evidence: at 7B, swap-CPT > keep-CPT > (implicitly) from-scratch when B-scale target tokens exist. Our ~10B kk budget is 1/3 of ChocoLlama's; and Qwen3-0.6B is a 'Llama-3-like' strong base, so the CPT gain must come from the fertility fix (4.7->~2.0), not from generic continued training.
> **Source:** ChocoLlama, arXiv:2412.07633 (Table 2) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[estllm-enhancing-estonian-capabilities-in-multilingual-llms-via-continued|EstLLM: Enhancing Estonian Capabilities in Multilingual LLMs via Continued Pretraining and…]] — Both continual-pretrain a base into a new EU language; ChocoLlama swaps the tokenizer at 32B tokens, EstLLM adapts Estonian — comparable…

[[Home]]
