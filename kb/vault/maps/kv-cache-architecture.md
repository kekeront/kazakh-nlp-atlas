---
type: "moc"
topic: "kv-cache-architecture"
nodes: 5
papers: 3
sources: 2
uncertain_claims: 1
tags: ["moc"]
---
# Topic: kv-cache-architecture

The frontier here is cross-layer KV sharing on top of GQA/MQA — reusing K/V across layers so only a subset compute it. CONFIRMED: sharing across 2 layers (2x KV cut) is the only factor worth taking — CLA (arxiv:2405.12981) shows CLA3/CLA4 degrade monotonically (1B ppl 13.60→13.77→13.95), and at equal cache CLA2 is Pareto-better than halving head dim (13.60 vs 13.81). The load-bearing correction is that the lab's assumed "+0.04-0.06 ppl" cost is from the LR-tuned MQA-CLA2 rows (optimal lr 2.25e-3 vs 1.5e-3); the paper's actual untuned GQA+CLA2 ablation costs +0.07 (GQA2) to +0.12 (GQA4), and its prose/table even contradict each other on which GQA config wins (uncertain claim, likely a naming typo). CONTESTED: the independent NAACL-2025 from-scratch 1.1B reproduction (arxiv:2410.14442) finds CLA2's layout (lasagna-bottom, -0.95 avg) is the WORST of five layouts — trailing-reuse (pizza-bottom, -0.55) and sandwich-top (-0.12) are strictly better, which is exactly the trailing scheme Gemma-3n and Gemma 4 ship in production (num_kv_shared_layers) — yet Google publishes only "minimal impact on quality" with zero ablation numbers across two generations. The one sub-1B GQA datapoint with numbers is Hymba (arxiv:2411.13676): +0.60 commonsense but -0.75 recall at 300M. Open question for QymyzLM: at ≤600M from scratch, is trailing-layer reuse (not CLA2) the right layout, and does the recall hit matter for a retrieval-adjacent target.

## Frontier highlights
- [[a-systematic-study-of-cross-layer-kv-sharing-for-efficient-llm-inference|A Systematic Study of Cross-Layer KV Sharing for Efficient LLM Inference]] — Only from-scratch 1.1B GQA reproduction: CLA2 layout is WORST (-0.95); trailing/sandwich beat it — refutes CLA2-best
- [[reducing-transformer-key-value-cache-size-with-cross-layer-attention|Reducing Transformer Key-Value Cache Size with Cross-Layer Attention]] — Foundational CLA; real GQA+CLA2 cost is +0.07/+0.12 ppl (untuned), not the lab's +0.04; only factor-2 pays off
- [[hymba-a-hybrid-head-architecture-for-small-language-models|Hymba: A Hybrid-head Architecture for Small Language Models]] — Only sub-1B GQA ablation with numbers: +0.60 commonsense but -0.75 recall at 300M, 1.15x throughput
- [[config-json-via-huggingface-co-unsloth-gemma-3n-e2b-mirror|config.json via huggingface.co/unsloth/gemma-3n-E2B (mirror]] — Production trailing KV sharing at 2B-eff (num_kv_shared_layers=10) with NO quality ablation — only 2x prefill
- [[huggingface-co-blog-gemma4-fetched-2026-07-03|huggingface.co/blog/gemma4 (fetched 2026-07-03)]] — Second Google generation shipping trailing KV sharing with zero published quality cost

## Papers (3)
- [[reducing-transformer-key-value-cache-size-with-cross-layer-attention|Reducing Transformer Key-Value Cache Size with Cross-Layer Attention]] (2024) — hybrid-efficiency-efficient-attention-se
- [[a-systematic-study-of-cross-layer-kv-sharing-for-efficient-llm-inference|A Systematic Study of Cross-Layer KV Sharing for Efficient LLM Inference]] (2024) — kv-cache-architecture
- [[hymba-a-hybrid-head-architecture-for-small-language-models|Hymba: A Hybrid-head Architecture for Small Language Models]] (2024) — kv-cache-architecture

## Sources & findings (2)
- [[huggingface-co-blog-gemma4-fetched-2026-07-03|huggingface.co/blog/gemma4 (fetched 2026-07-03)]] — Gemma 4 (released April 2, 2026) carries the same num_kv_shared_layers mechanism forward across its lineup (smallest tie…
- [[config-json-via-huggingface-co-unsloth-gemma-3n-e2b-mirror|config.json via huggingface.co/unsloth/gemma-3n-E2B (mirror]] — Gemma 3n ships trailing-layer KV sharing ON GQA in production at effective-2B scale with NO public quality ablation: E2B…

[[Home]]
