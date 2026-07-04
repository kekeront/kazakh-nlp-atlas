---
kb_id: "hf:ai-forever/frida"
type: "source"
title: "huggingface.co/ai-forever/FRIDA"
doi: null
hf_repo: "ai-forever/FRIDA"
year: null
topics: ["embed-kazakh"]
claims: 1
uncertain_claims: 0
verdicts: []
aliases: ["hf:ai-forever/frida"]
tags: ["source", "topic/embed-kazakh"]
---
# huggingface.co/ai-forever/FRIDA

**Topics:** [[embed-kazakh]]

## Source URLs
- huggingface.co/ai-forever/FRIDA
- huggingface.co/ai-sage/Giga-Embeddings-instruct
- habr.com/ru/companies/sberdevices/articles/909924/

## Findings

> [!note] CLAIM — embed-kazakh
> Russian embedders do not cover Kazakh: FRIDA (ai-forever) and ru-en-RoSBERTa are ru/en models; Giga-Embeddings developers explicitly recommend it 'only for Russian'. None claims or benchmarks kk despite the shared Cyrillic script and heavy kk-ru code-switching — cross-script transfer from ru embedders to kk is unmeasured anywhere.
>
> **Numbers:** 0 kk claims across FRIDA / Giga-Embeddings / ru-en-RoSBERTa model cards
> **Relevance:** The kk-ru code-switching niche is completely unserved — a code-switch eval + training pairs is a differentiating milestone no competitor addresses.
> **Source:** huggingface.co/ai-forever/FRIDA; huggingface.co/ai-sage/Giga-Embeddings-instruct; habr.com/ru/companies/sberdevices/articles/909924/ · **Sweep:** `embeddings-2026-07`

## Related
- [[the-russian-focused-embedders-exploration-rumteb-benchmark-and-russian|The Russian-focused embedders' exploration: ruMTEB benchmark and Russian embedding model d…]] — FRIDA is a ruMTEB-lineage Russian embedder; node documents it excludes kk despite shared Cyrillic — cross-script ru→kk transfer is…

[[Home]]
