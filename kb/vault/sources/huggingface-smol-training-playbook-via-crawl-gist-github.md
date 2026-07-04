---
kb_id: "title:huggingface smol training playbook via crawl gist github com unclecode e5da5fb6a1d37022b089e243e0d9e00e adoption absence from july 2026 searches"
type: "source"
title: "HuggingFace Smol Training Playbook (via crawl: gist.github.com/uncleco…"
doi: null
hf_repo: null
year: null
topics: ["mla-vs-gqa-pretraining-cost-and-converge"]
claims: 1
uncertain_claims: 1
verdicts: []
aliases: ["title:huggingface smol training playbook via crawl gist github com unclecode e5da5fb6a1d37022b089e243e0d9e00e adoption absence from july 2026 searches"]
tags: ["source", "topic/mla-vs-gqa-pretraining-cost-and-converge"]
---
# HuggingFace Smol Training Playbook (via crawl: gist.github.com/uncleco…

**Topics:** [[mla-vs-gqa-pretraining-cost-and-converge]]

## Source URLs
- HuggingFace Smol Training Playbook (via crawl: gist.github.com/unclecode/e5da5fb6a1d37022b089e243e0d9e00e)
- adoption-absence from July 2026 searches

## Findings

> [!warning] UNCERTAIN — mla-vs-gqa-pretraining-cost-and-converge
> Production adoption at sub-1B remains zero as of mid-2026: SmolLM3 (3B, 11T tokens) explicitly did not ablate MLA because 'it wasn't implemented in nanotron at the time of the ablations' and shipped GQA-4 after 1B-scale/45B-token ablations; Qwen3-0.6B uses GQA (KB-verified). No dense <1B released model with MLA was found (EG-MLA at 1B is research-only, per KB). Combined with KB's llama.cpp finding (MLA GGUF needs ik_llama.cpp fork), MLA at sub-1B is a research-proven but production-unshipped choice.
>
> **Numbers:** SmolLM3 ablation baseline: 1B params (Llama3.2-1B arch), 45B tokens, GQA-4 chosen; MLA arm: absent
> **Relevance:** The lab would be among the first to ship a sub-1B dense MLA model — novelty upside for the paper, but zero production precedent and known GGUF deployment friction; the deciding constraint is tooling, not quality.
> **Source:** HuggingFace Smol Training Playbook (via crawl: gist.github.com/unclecode/e5da5fb6a1d37022b089e243e0d9e00e); adoption-absence from July 2026 searches · **Sweep:** `mla-sub1b-2026-07`

## Related
- [[huggingface-co-qwen-qwen3-0-6b-base-config-json-fetched-raw|huggingface.co/Qwen/Qwen3-0.6B-Base config.json (fetched raw, 2026-07-…]] — Evidence that production sub-1B MLA adoption is zero: Qwen3-0.6B is a shipped GQA model, no MLA arm

[[Home]]
