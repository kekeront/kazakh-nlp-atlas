---
type: "moc"
topic: "mla-at-sub-1b-scale"
nodes: 19
papers: 13
sources: 6
uncertain_claims: 8
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

## Papers (13)
- [[long-context-aware-upcycling-a-new-frontier-for-hybrid-llm-scaling|Long-Context Aware Upcycling: A New Frontier for Hybrid LLM Scaling]] (2026) — mla-at-sub-1b-scale
- [[tensor-product-attention-is-all-you-need|Tensor Product Attention Is All You Need]] (2025) — mla-at-sub-1b-scale
- [[towards-economical-inference-enabling-deepseek-s-multi-head-latent-attention-in|Towards Economical Inference: Enabling DeepSeek's Multi-Head Latent Attention in Any Transformer-bas…]] (2025) — mla-at-sub-1b-scale
- [[x-ecomla-upcycling-pre-trained-attention-into-mla-for-efficient-and-extreme-kv|X-EcoMLA: Upcycling Pre-Trained Attention into MLA for Efficient and Extreme KV Compression]] (2025) — mla-at-sub-1b-scale
- [[plm-efficient-peripheral-language-models-hardware-co-designed-for-ubiquitous|PLM: Efficient Peripheral Language Models Hardware-Co-Designed for Ubiquitous Computing]] (2025) — mla-at-sub-1b-scale
- [[hardware-efficient-attention-for-fast-decoding|Hardware-Efficient Attention for Fast Decoding]] (2025) — mla-at-sub-1b-scale
- [[latent-multi-head-attention-for-small-language-models|Latent Multi-Head Attention for Small Language Models]] (2025) — hybrid-efficient-attention-architectures
- [[decoder-hybrid-decoder-architecture-for-efficient-reasoning-with-long-generation|Decoder-Hybrid-Decoder Architecture for Efficient Reasoning with Long Generation]] (2025) — mla-at-sub-1b-scale
- [[eg-mla-embedding-gated-multi-head-latent-attention-for-scalable-and-efficient|EG-MLA: Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs]] (2025) — deepseek-tech
- [[kimi-linear-an-expressive-efficient-attention-architecture|Kimi Linear: An Expressive, Efficient Attention Architecture]] (2025) — mla-at-sub-1b-scale
- [[youtu-llm-unlocking-the-native-agentic-potential-for-lightweight-large-language|Youtu-LLM: Unlocking the Native Agentic Potential for Lightweight Large Language Models]] (2025) — mla-at-sub-1b-scale
- [[you-only-cache-once-decoder-decoder-architectures-for-language-models|You Only Cache Once: Decoder-Decoder Architectures for Language Models]] (2024) — hybrid-efficient-attention-architectures
- [[reducing-transformer-key-value-cache-size-with-cross-layer-attention|Reducing Transformer Key-Value Cache Size with Cross-Layer Attention]] (2024) — hybrid-efficient-attention-architectures

## Sources & findings (6)
- [[huggingface-co-deepseek-ai-deepseek-ocr-config-json-fetched|huggingface.co/deepseek-ai/DeepSeek-OCR config.json (fetched directly)]] — Counter-datapoint from DeepSeek themselves: the DeepSeek-OCR decoder (DeepSeek-3B-MoE, ~570M ACTIVE params — the closest…
- [[huggingface-co-deepseek-ai-deepseek-v2-lite-config-json|huggingface.co/deepseek-ai/DeepSeek-V2-Lite config.json (fetched direc…]] — Smallest official DeepSeek MLA config (DeepSeek-V2-Lite, 15.7B total / 2.4B active, d_model=2048, 27 layers, 16 heads) d…
- [[huggingface-co-openbmb-minicpm3-4b-config-json-fetched|huggingface.co/openbmb/MiniCPM3-4B config.json (fetched directly)]] — Smallest production kv_lora_rank shipped: MiniCPM3-4B (d_model=2560, 62 layers, 40 heads) uses kv_lora_rank=256, q_lora_…
- [[huggingface-co-qwen-qwen3-5-0-8b-config-json-fetched|huggingface.co/Qwen/Qwen3.5-0.8B config.json (fetched directly)]] — Resolves KB [UNVERIFIED] on Qwen3.5 sub-1B: Qwen/Qwen3.5-0.8B config.json shows NO MLA — it is a hybrid: 24 layers, hidd…
- [[arithmetic-from-verified-configs-deepseek-v2-lite-minicpm3|Arithmetic from verified configs (DeepSeek-V2-Lite, MiniCPM3, Qwen3-0.…]] — Cache-accounting nuance the design spec must not miss: MLA's cache advantage depends on the GQA baseline it replaces. Pe…
- [[cfgs-qwen3-0-6b-4gpu-yml-src-mha2mla-patching-model-load-py|cfgs/Qwen3-0_6B-4GPU.yml + src/mha2mla/patching_model_load.py (from-sc…]] — MHA2MLA repo (2025-2026 updates) contains a Qwen3-0.6B config with is_mla_from_scratch=true: attention projections rando…

## Related topics
- [[mla-vs-gqa-convergence-cost]] — 4 shared nodes
- [[hybrid-efficient-attention-architectures]] — 3 shared nodes
- [[attention-kv-architecture-sub-1b]] — 2 shared nodes
- [[mla-upcycling-bespoke-tokenizer]] — 2 shared nodes

[[Home]]
