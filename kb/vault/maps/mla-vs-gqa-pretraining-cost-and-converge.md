---
type: "moc"
topic: "mla-vs-gqa-pretraining-cost-and-converge"
nodes: 5
papers: 4
sources: 1
uncertain_claims: 3
tags: ["moc"]
---
# Topic: mla-vs-gqa-pretraining-cost-and-converge

The frontier question is whether MLA beats GQA enough to justify it when pretraining a sub-1B model from scratch. Three independent from-scratch head-to-heads now exist — TPA/T6 (353M/772M, FineWeb-Edu ~49B tok), the Dao-group GLA paper (183M-1.47B, 25-50B tok), and latent-MHA-for-SLMs (30-202M, ~3.3B tok TinyStories). Established: MLA quality sits within roughly ±1pp of GQA across 350M-1.5B — never the DeepSeek-V2 large-scale win, never catastrophic; the Dao group shows MLA (kv_lora_rank=4·d_h + rope 32) matching or beating GQA-4 while caching LESS (876M: MLA 11.363 vs GQA-4 11.340 ppl; MLA best at 433M), and their GLA-2 variant beats both. Contested: TPA claims MLA "trains more slowly, higher validation loss," but this is figure-only (no numeric table) and its own downstream tables show parity/better, so the convergence-penalty is weak evidence — and its GQA arm cached only 256 elem vs MLA's 544. Open: zero published wall-clock or training-memory MLA-vs-GQA numbers at sub-1B, zero long-context (RULER/LongBench) evidence for from-scratch sub-1B MLA, and production adoption is zero (SmolLM3, Qwen3-0.6B both shipped GQA-4). Escape hatch: MHA2MLA converts an existing GQA model to MLA with ~0.4% of pretraining data (-1.2/-1.7pp at -69% KV), decoupling the choice from the from-scratch run.

## Frontier highlights
- [[hardware-efficient-attention-for-fast-decoding|Hardware-Efficient Attention for Fast Decoding]] — Strongest from-scratch evidence: MLA matches/beats GQA-4 while caching less at 433M/876M (11.363 vs 11.340 ppl)
- [[tensor-product-attention-is-all-you-need|Tensor Product Attention Is All You Need]] — First MLA-vs-GQA head-to-head; parity@353M, +1pp@772M, but figure-only slower-convergence caveat, GQA under-cached
- [[towards-economical-inference-enabling-deepseek-s-multi-head-latent-attention-in|Towards Economical Inference: Enabling DeepSeek's Multi-Head Latent Attention in…]] — Escape hatch: GQA->MLA conversion with 0.4% pretrain data, -1.2/-1.7pp at -69% KV, decouples the decision
- [[latent-multi-head-attention-for-small-language-models|Latent Multi-Head Attention for Small Language Models]] — Smallest-scale MLA study (30-202M): decoupled-RoPE r=d/2 -> 45% KV cut at +0.3% loss, needs RoPE
- [[huggingface-smol-training-playbook-via-crawl-gist-github|HuggingFace Smol Training Playbook (via crawl: gist.github.com/uncleco…]] — Production sub-1B MLA adoption is zero: SmolLM3 and Qwen3-0.6B both shipped GQA-4

## Papers (4)
- [[tensor-product-attention-is-all-you-need|Tensor Product Attention Is All You Need]] (2025) — mla-sub1b
- [[towards-economical-inference-enabling-deepseek-s-multi-head-latent-attention-in|Towards Economical Inference: Enabling DeepSeek's Multi-Head Latent Attention in Any Transformer-bas…]] (2025) — mla-sub1b
- [[hardware-efficient-attention-for-fast-decoding|Hardware-Efficient Attention for Fast Decoding]] (2025) — mla-sub1b
- [[latent-multi-head-attention-for-small-language-models|Latent Multi-Head Attention for Small Language Models]] (2025) — hybrid-efficiency-efficient-attention-se

## Sources & findings (1)
- [[huggingface-smol-training-playbook-via-crawl-gist-github|HuggingFace Smol Training Playbook (via crawl: gist.github.com/uncleco…]] — Production adoption at sub-1B remains zero as of mid-2026: SmolLM3 (3B, 11T tokens) explicitly did not ablate MLA becaus…

## Related topics
- [[mla-sub1b]] — 3 shared nodes
- [[mla-at-sub-1b]] — 2 shared nodes
- [[mla-at-sub-1b-scale]] — 2 shared nodes

[[Home]]
