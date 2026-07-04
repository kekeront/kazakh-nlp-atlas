---
kb_id: "hf:gen2b/irbis-7b-instruct_lora"
type: "source"
title: "huggingface.co/Gen2B/Irbis-7b-Instruct_lora (card fetched)"
doi: null
hf_repo: "Gen2B/Irbis-7b-Instruct_lora"
year: null
topics: ["continual-pt-lowres-qlora-vs-full-cpt-re"]
claims: 1
uncertain_claims: 1
verdicts: []
aliases: ["hf:gen2b/irbis-7b-instruct_lora"]
tags: ["source", "topic/continual-pt-lowres-qlora-vs-full-cpt-re"]
---
# huggingface.co/Gen2B/Irbis-7b-Instruct_lora (card fetched)

**Topics:** [[continual-pt-lowres-qlora-vs-full-cpt-re]]

## Source URLs
- huggingface.co/Gen2B/Irbis-7b-Instruct_lora (card fetched)
- huggingface.co/astanahub/alemllm via search + skywork summary

## Findings

> [!warning] UNCERTAIN — continual-pt-lowres-qlora-vs-full-cpt-re
> [tested-on-Kazakh] Irbis-7b (Gen2B, 2024): community Kazakh adaptation; the Instruct variant is a LoRA fine-tune of their own Irbis-7b-v0.1 base on 200K Kazakh (question, context, answer) examples; MIT license; NO published benchmarks (card admits it only 'handles simple questions well'); LoRA rank undisclosed. AlemLLM (astanahub, 2025): 247B-total/22B-active MoE, 56 layers, vocab 100,352, SentencePiece, kk/ru/en/tr; training token count undisclosed.
>
> **Numbers:** Irbis: 200K SFT pairs, MIT, 0 benchmarks; AlemLLM: 247B/22B MoE, vocab 100,352
> **Relevance:** Kazakh CPT landscape check: no ≤1.5B open Kazakh CPT model with published recipe+numbers exists (SozKZ is from-scratch) — QymyzLM's niche is uncontested; benchmark-less community LoRA efforts are the cautionary baseline.
> **Source:** huggingface.co/Gen2B/Irbis-7b-Instruct_lora (card fetched); huggingface.co/astanahub/alemllm via search + skywork summary · **Sweep:** `slm-arch-for-kazakh`

[[Home]]
