---
kb_id: "title:own measurement transformers 5 5 2 autotokenizer qwen qwen3 0 6b base 66 word kazakh paragraph"
type: "source"
title: "Own measurement, transformers 5.5.2, AutoTokenizer Qwen/Qwen3-0.6B-Bas…"
doi: null
hf_repo: null
year: null
topics: ["tokenizer-agglutinative"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["title:own measurement transformers 5 5 2 autotokenizer qwen qwen3 0 6b base 66 word kazakh paragraph"]
tags: ["source", "topic/tokenizer-agglutinative"]
---
# Own measurement, transformers 5.5.2, AutoTokenizer Qwen/Qwen3-0.6B-Bas…

**Topics:** [[tokenizer-agglutinative]]

## Source URLs
- Own measurement, transformers 5.5.2, AutoTokenizer Qwen/Qwen3-0.6B-Base, 66-word Kazakh paragraph

## Findings

> [!note] CLAIM — tokenizer-agglutinative
> Qwen3-0.6B-Base's own tokenizer (the planned CPT backbone) tokenizes real Kazakh Cyrillic prose at fertility ~5.3 tok/word — WORSE than Llama-3.1's 4.73 — because Kazakh Cyrillic has essentially no dedicated merges and falls back to UTF-8 byte pieces. Individual agglutinative words explode: 'үйлерімізден' -> 8 tokens, 'қалаларымыздағы' -> 10, 'оқушыларымыздың' -> 11. Vocab is 151,643/151,936. CPT without vocabulary expansion inherits this ~5.3 fertility.
>
> **Numbers:** 66 words -> 350 tokens = 5.303 tok/word; per-word: 8/10/11 tokens for үйлерімізден/қалаларымыздағы/оқушыларымыздың; vocab 151,643
> **Relevance:** tested-on-Kazakh. Directly kills the option of CPT-on-Qwen3 with the stock tokenizer: at 5.3 fertility a 10B-token Kazakh corpus becomes ~5.3B words of usable text vs ~2.0 target = 2.6x waste on context, KV, throughput. Mandates Sherkala-style vocab expansion (+~31.5K, WECHSEL init -> 2.04) before/at CPT.
> **Source:** Own measurement, transformers 5.5.2, AutoTokenizer Qwen/Qwen3-0.6B-Base, 66-word Kazakh paragraph · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[the-tokenizer-tax-across-25-european-languages-domain-invariance-cross-lingual|The Tokenizer Tax Across 25 European Languages: Domain Invariance, Cross-Lingual Few-Shot…]] — Tax study: Qwen3 fragments Cyrillic 8-9 subw/word; own Kazakh measurement corroborates at 5.3 tok/word via byte fallback
- [[kazbyte-adapting-qwen-models-to-kazakh-via-byte-level-adapter|KazByte: Adapting Qwen models to Kazakh via Byte-level Adapter]] — measured ~5.3 tok/word Qwen-Kazakh explosion is exactly the fertility problem KazByte's byte-adapter targets

[[Home]]
