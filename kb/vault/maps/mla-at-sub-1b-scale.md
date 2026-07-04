---
type: "moc"
topic: "mla-at-sub-1b-scale"
nodes: 6
papers: 5
sources: 1
uncertain_claims: 6
tags: ["moc"]
---
# Topic: mla-at-sub-1b-scale

The frontier splits cleanly into three evidence classes. FROM-SCRATCH MLA is proven small: the Latent-MHA-for-SLMs paper (30M-202M, arxiv:2506.09342) shows decoupled-RoPE MLA at r=d/2 costs only +0.3% val loss for a 45% KV cut, but collapses at r=d/4 (+4.4%) and needs the RoPE branch. CONVERSION at sub-1B is proven-but-lossy and teacher-free: MHA2MLA (arxiv:2502.14837) converts SmolLM-135M/360M on ~0.38% of pretraining tokens, but shows an inverse-scale law — smaller models lose more at equal KV compression (135M -3.28pp vs 7B -0.30pp at deep cuts). LOSSLESS deep conversion at ~1B exists only with a 3-8x-larger same-tokenizer teacher (X-EcoMLA, arxiv:2503.11132: 6.4-10.6x KV at parity via distillation), a path the lab cannot use with a bespoke tokenizer — leaving ~1.9x self-distill lossless or ~3.2x teacher-free at -1.7pp as the realistic ceiling. The dominant OPEN question is long-context: every sub-1B result is short-context; the only long-context retrieval evidence at ~1B is HyLo (arxiv:2604.24715, 4 MLA + 12 linear layers, RULER-64K 40.8) with no pure-MLA arm, and the smallest pure-MLA RULER-128K number (81.3) belongs to Kimi Linear's 3B-active MoE baseline. Even DeepSeek-V2-Lite, the smallest shipped pure-MLA config (kv_lora_rank=512 at d/4), has no published needle/RULER results. All six nodes are unverified (verdict null); the X-EcoMLA config-to-ratio mapping is internally contradictory and self-flagged uncertain.

## Frontier highlights
- [[long-context-aware-upcycling-a-new-frontier-for-hybrid-llm-scaling|Long-Context Aware Upcycling: A New Frontier for Hybrid LLM Scaling]] — Only long-context retrieval evidence for MLA at ~1B: 4-MLA+12-linear, RULER-64K 40.8; no pure-MLA arm
- [[towards-economical-inference-enabling-deepseek-s-multi-head-latent-attention-in|Towards Economical Inference: Enabling DeepSeek's Multi-Head Latent Attention in…]] — Teacher-free conversion at 135M/360M on 0.38% of tokens; inverse-scale law — small models lose more
- [[x-ecomla-upcycling-pre-trained-attention-into-mla-for-efficient-and-extreme-kv|X-EcoMLA: Upcycling Pre-Trained Attention into MLA for Efficient and Extreme KV…]] — 1.24B distillation upcycle: 1.9x lossless self-distill, 6.4-10.6x only with bigger same-tokenizer teacher
- [[latent-multi-head-attention-for-small-language-models|Latent Multi-Head Attention for Small Language Models]] — Only from-scratch MLA at 30M-202M: r=d/2 = 45% KV cut at +0.3% loss, needs decoupled RoPE
- [[kimi-linear-an-expressive-efficient-attention-architecture|Kimi Linear: An Expressive, Efficient Attention Architecture]] — Smallest pure-MLA with RULER-128K (81.3) — but 3B-active MoE, 5-6x lab scale, not dense
- [[huggingface-co-deepseek-ai-deepseek-v2-lite-config-json|huggingface.co/deepseek-ai/DeepSeek-V2-Lite config.json (fetched direc…]] — Smallest shipped pure-MLA config (kv_lora_rank=512 at d/4) — but zero long-context evals

## Papers (5)
- [[long-context-aware-upcycling-a-new-frontier-for-hybrid-llm-scaling|Long-Context Aware Upcycling: A New Frontier for Hybrid LLM Scaling]] (2026) — mla-at-sub-1b-scale
- [[towards-economical-inference-enabling-deepseek-s-multi-head-latent-attention-in|Towards Economical Inference: Enabling DeepSeek's Multi-Head Latent Attention in Any Transformer-bas…]] (2025) — mla-sub1b
- [[x-ecomla-upcycling-pre-trained-attention-into-mla-for-efficient-and-extreme-kv|X-EcoMLA: Upcycling Pre-Trained Attention into MLA for Efficient and Extreme KV Compression]] (2025) — mla-sub1b
- [[latent-multi-head-attention-for-small-language-models|Latent Multi-Head Attention for Small Language Models]] (2025) — hybrid-efficiency-efficient-attention-se
- [[kimi-linear-an-expressive-efficient-attention-architecture|Kimi Linear: An Expressive, Efficient Attention Architecture]] (2025) — mla-at-sub-1b-scale

## Sources & findings (1)
- [[huggingface-co-deepseek-ai-deepseek-v2-lite-config-json|huggingface.co/deepseek-ai/DeepSeek-V2-Lite config.json (fetched direc…]] — Smallest official DeepSeek MLA config (DeepSeek-V2-Lite, 15.7B total / 2.4B active, d_model=2048, 27 layers, 16 heads) d…

## Related topics
- [[mla-at-sub-1b]] — 3 shared nodes
- [[mla-sub1b]] — 3 shared nodes
- [[mla-upcycling-at-1b-under-a-bespoke-toke]] — 2 shared nodes
- [[mla-vs-gqa-pretraining-cost-and-converge]] — 2 shared nodes

[[Home]]
