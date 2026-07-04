---
kb_id: "hf:deepseek-ai/deepseek-ocr"
type: "source"
title: "huggingface.co/deepseek-ai/DeepSeek-OCR config.json (fetched directly)"
doi: null
hf_repo: "deepseek-ai/DeepSeek-OCR"
year: null
topics: ["mla-at-sub-1b-scale"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["hf:deepseek-ai/deepseek-ocr"]
tags: ["source", "topic/mla-at-sub-1b-scale"]
---
# huggingface.co/deepseek-ai/DeepSeek-OCR config.json (fetched directly)

**Topics:** [[mla-at-sub-1b-scale]]

## Source URLs
- huggingface.co/deepseek-ai/DeepSeek-OCR config.json (fetched directly)

## Findings

> [!note] CLAIM — mla-at-sub-1b-scale
> Counter-datapoint from DeepSeek themselves: the DeepSeek-OCR decoder (DeepSeek-3B-MoE, ~570M ACTIVE params — the closest DeepSeek model to the lab's active-param class) ships with MLA DISABLED: config.json has kv_lora_rank=null, q_lora_rank=null, 12 layers, hidden 1280, 10 attention heads = 10 KV heads (plain MHA), 64 routed + 2 shared experts, vocab 129,280, ctx 8,192.
>
> **Numbers:** d=1280, 12L, 10 heads MHA, kv_lora_rank=null; 64+2 experts, 6 active/token; ~570M active
> **Relevance:** The inventors of MLA chose plain MHA for their own ~0.6B-active decoder (short 8K context) — supports the view that MLA's payoff at this scale is context-length-dependent, not automatic.
> **Source:** huggingface.co/deepseek-ai/DeepSeek-OCR config.json (fetched directly) · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[youtu-llm-unlocking-the-native-agentic-potential-for-lightweight-large-language|Youtu-LLM: Unlocking the Native Agentic Potential for Lightweight Large Language Models]] — Opposite production choices near sub-2B: DeepSeek-OCR ships MLA DISABLED (~570M active MoE) while Youtu-LLM ships dense MLA at 1.96B…

[[Home]]
