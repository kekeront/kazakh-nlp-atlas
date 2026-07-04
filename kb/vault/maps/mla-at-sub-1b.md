---
type: "moc"
topic: "mla-at-sub-1b"
nodes: 7
papers: 5
sources: 2
uncertain_claims: 5
tags: ["moc"]
---
# Topic: mla-at-sub-1b

MLA is CONFIRMED viable below 1B along three distinct paths, and this slice pins the tradeoffs. From-scratch: 2506.09342 (30–202M, decoupled-RoPE MLA at r=d/2 gives 45% KV cut for +0.3% val loss) and EG-MLA (120M, shared kv_lora_rank=256, and 64 with token-embedding gating) prove shared ranks well below the DeepSeek-V2/PLM-1.8B default of 512; MiniCPM3-4B ships rank 256 (=d/10). Teacher-free conversion (MHA2MLA) converts SmolLM-135M/360M GQA→MLA with only ~2.25B tokens (0.38% of pretrain) but is lossy and shows inverse-scale degradation — smaller models lose MORE at equal compression (360M: −1.72pp at −68.75% KV, −4.59pp at −87.5%). Distillation upcycling (X-EcoMLA) reaches ~1.9x lossless via self-distillation, but 6.4–10.6x lossless is published ONLY with a 3–8x-larger SAME-tokenizer teacher — unreachable for a bespoke Kazakh vocab. The load-bearing open question: cross-tokenizer lossless deep conversion at sub-1B has ZERO published results, and every sub-1B MLA study (from-scratch or converted) evaluated short-context only — no LongBench/RULER/needle evidence exists below 7B. Two internal conflicts are flagged uncertain: X-EcoMLA's config-to-ratio mapping (kv_lora_rank 128 vs 512) and 2506.09342's KV-reduction figure (87.5% vs 72%).

## Frontier highlights
- [[towards-economical-inference-enabling-deepseek-s-multi-head-latent-attention-in|Towards Economical Inference: Enabling DeepSeek's Multi-Head Latent Attention in…]] — Teacher-free GQA→MLA conversion at 135M/360M on 0.38% of pretrain; lossy with inverse-scale degradation
- [[x-ecomla-upcycling-pre-trained-attention-into-mla-for-efficient-and-extreme-kv|X-EcoMLA: Upcycling Pre-Trained Attention into MLA for Efficient and Extreme KV…]] — Distillation upcycling Llama3.2-1B: 1.9x lossless self-distill; deep lossless needs larger same-tokenizer teacher
- [[eg-mla-embedding-gated-multi-head-latent-attention-for-scalable-and-efficient|EG-MLA: Embedding-Gated Multi-head Latent Attention for Scalable and Efficient L…]] — Only from-scratch sub-1B run with shared rank below 512: kv256 and kv64-gated at 120M
- [[latent-multi-head-attention-for-small-language-models|Latent Multi-Head Attention for Small Language Models]] — Dedicated 30–202M MLA study: r=d/2 → 45% KV cut, +0.3% loss; decoupled RoPE mandatory
- [[plm-efficient-peripheral-language-models-hardware-co-designed-for-ubiquitous|PLM: Efficient Peripheral Language Models Hardware-Co-Designed for Ubiquitous Co…]] — Production from-scratch dense MLA at 1.8B pins the rank-512 (=d/4) precedent, never 256
- [[huggingface-co-openbmb-minicpm3-4b-config-json-fetched|huggingface.co/openbmb/MiniCPM3-4B config.json (fetched directly)]] — Smallest shipped kv_lora_rank=256 (=d/10 + rope32), same ratio class as DeepSeek-V2/V3

## Papers (5)
- [[towards-economical-inference-enabling-deepseek-s-multi-head-latent-attention-in|Towards Economical Inference: Enabling DeepSeek's Multi-Head Latent Attention in Any Transformer-bas…]] (2025) — mla-sub1b
- [[x-ecomla-upcycling-pre-trained-attention-into-mla-for-efficient-and-extreme-kv|X-EcoMLA: Upcycling Pre-Trained Attention into MLA for Efficient and Extreme KV Compression]] (2025) — mla-sub1b
- [[plm-efficient-peripheral-language-models-hardware-co-designed-for-ubiquitous|PLM: Efficient Peripheral Language Models Hardware-Co-Designed for Ubiquitous Computing]] (2025) — mla-at-sub-1b
- [[latent-multi-head-attention-for-small-language-models|Latent Multi-Head Attention for Small Language Models]] (2025) — hybrid-efficiency-efficient-attention-se
- [[eg-mla-embedding-gated-multi-head-latent-attention-for-scalable-and-efficient|EG-MLA: Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs]] (2025) — deepseek-tech

## Sources & findings (2)
- [[huggingface-co-openbmb-minicpm3-4b-config-json-fetched|huggingface.co/openbmb/MiniCPM3-4B config.json (fetched directly)]] — Smallest production kv_lora_rank shipped: MiniCPM3-4B (d_model=2560, 62 layers, 40 heads) uses kv_lora_rank=256, q_lora_…
- [[cfgs-qwen3-0-6b-4gpu-yml-src-mha2mla-patching-model-load-py|cfgs/Qwen3-0_6B-4GPU.yml + src/mha2mla/patching_model_load.py (from-sc…]] — MHA2MLA repo (2025-2026 updates) contains a Qwen3-0.6B config with is_mla_from_scratch=true: attention projections rando…

## Related topics
- [[mla-at-sub-1b-scale]] — 3 shared nodes
- [[mla-sub1b]] — 3 shared nodes
- [[mla-upcycling-at-1b-under-a-bespoke-toke]] — 2 shared nodes
- [[mla-vs-gqa-pretraining-cost-and-converge]] — 2 shared nodes

[[Home]]
