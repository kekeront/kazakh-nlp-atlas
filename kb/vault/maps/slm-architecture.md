---
type: "moc"
topic: "slm-architecture"
nodes: 2
papers: 2
sources: 0
uncertain_claims: 3
tags: ["moc"]
---
# Topic: slm-architecture

This slice frames sub-1B SLM architecture around two competing KV-efficiency mechanisms. (1) Sliding-window hybrid attention: Gemma 3 interleaves local SWA and global layers 5:1 (window 1024, RoPE 10K local / 1M global), cutting KV overhead from ~60% to <15% at 32K with minimal perplexity cost; the 270M config (18L, d640, MQA 4Q/1KV, 15:3 window-512:global) yields a constant ~108 MB KV@32K vs Qwen3-0.6B's ~3.75 GB (~35x smaller) — the strongest ≤300M long-context attention template, though that KV derivation is still uncertain-tagged. (2) MLA conversion/upcycling: X-EcoMLA upcycles Llama3.2-1B-Instruct to MLA via SVD init + distillation, reaching 6.4x KV compression at score parity (52.94 vs 52.85) with an 8B teacher on ~3.6B tokens/70 MI300-h. The load-bearing contest: X-EcoMLA's own node carries a CONFIRMED internal config conflict (kv_lora_rank 128 vs 512, r_q 1344/864/854, baseline 52.85 vs 52.77), so every specific config→ratio mapping is unverified — only "up to 6.4x via post-hoc MLA conversion" stands. Two open questions dominate: deep lossless compression (6.4–10.6x) is published ONLY with a 3–8x-larger same-tokenizer teacher (impossible under a bespoke Kazakh tokenizer; cross-tokenizer rescue = zero published results), and NO MLA-conversion paper evaluates long context (no LongBench/RULER/needle), so rank-512-at-1B is unmeasured beyond short tasks. As a base LM Gemma3-270M is near-random (24.4% KazMMLU, lab measurement), positioned as a fine-tuning substrate not a generative target.

## Frontier highlights
- [[x-ecomla-upcycling-pre-trained-attention-into-mla-for-efficient-and-extreme-kv|X-EcoMLA: Upcycling Pre-Trained Attention into MLA for Efficient and Extreme KV…]] — MLA-conversion precedent at 1.24B: 6.4x KV at parity w/ 8B teacher, but config conflict + zero long-context eval
- [[gemma-3-technical-report|Gemma 3 Technical Report]] — Sliding-window 5:1 template: ~108MB KV@32K at 270M (~35x < Qwen3-0.6B), the ≤300M long-context attention baseline

## Papers (2)
- [[x-ecomla-upcycling-pre-trained-attention-into-mla-for-efficient-and-extreme-kv|X-EcoMLA: Upcycling Pre-Trained Attention into MLA for Efficient and Extreme KV Compression]] (2025) — mla-sub1b
- [[gemma-3-technical-report|Gemma 3 Technical Report]] (2025) — sota-slm

[[Home]]
