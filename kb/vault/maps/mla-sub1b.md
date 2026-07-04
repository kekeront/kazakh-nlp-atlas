---
type: "moc"
topic: "mla-sub1b"
nodes: 13
papers: 8
sources: 5
uncertain_claims: 3
tags: ["moc"]
---
# Topic: mla-sub1b

The frontier question — does MLA earn its place at sub-1B ACTIVE params — resolves to "rough parity, not a clear win." Two independent from-scratch head-to-heads bound it: the Dao group (2505.21487, 183M-1.47B FineWeb-Edu) finds MLA (single latent kv_lora_rank=4*d_h + rope32, queries NOT compressed) beats GQA-4 at 433M/876M while caching LESS, whereas TPA (2501.06425) reports MLA "trains more slowly and yields higher validation losses" — but that claim is figure-only with no numeric table, and TPA's own downstream tables show MLA at parity/better (772M: MLA 53.32 > GQA 52.30). Synthesis envelope: MLA sits within about ±1pp of GQA across 350M-1.5B, never catastrophic, never the DeepSeek-scale win. Conversion paths are de-risked but tiered: MHA2MLA (2502.14837) is teacher-free on ~0.4% of pretrain data but lossy (-1.2 to -4.6pp for 3.2-8x KV cut, and smaller models degrade MORE at equal d_kv); X-EcoMLA (2503.11132) reaches 6.4-10.6x lossless only with a 3-8x-larger same-tokenizer teacher — unreachable under a bespoke Kazakh tokenizer, leaving ~1.9x self-distill lossless or ~3.2x@-1.7pp as the realistic hedge. Production signal is genuinely split: MiniCPM3-4B (kv_lora_rank=256=d/10) and DeepSeek-V2-Lite (512, q-compression dropped sub-2B) ship MLA and Youtu-LLM ships dense MLA at 1.96B claiming MLA beats GQA in its own 1B ablation, yet DeepSeek-OCR ships MLA DISABLED at ~570M active and Qwen3.5-0.8B chose hybrid-linear (Gated DeltaNet) + GQA-2 over MLA. Open questions: lossless DEEP MLA conversion under a bespoke tokenizer, and long-context (RULER/needle/LongBench) MLA quality at sub-1B — the latter unmeasured everywhere (X-EcoMLA and DeepSeek-V2-Lite both publish short-context evals only).

## Frontier highlights
- [[hardware-efficient-attention-for-fast-decoding|Hardware-Efficient Attention for Fast Decoding]] — Strongest from-scratch evidence: MLA beats GQA-4 at 433M/876M while caching less; pins kv_lora_rank=4*d_h, rope32
- [[tensor-product-attention-is-all-you-need|Tensor Product Attention Is All You Need]] — First from-scratch MLA-vs-GQA in the d_model window; source of the ±1pp-vs-GQA envelope and the 'MLA slower' caveat
- [[towards-economical-inference-enabling-deepseek-s-multi-head-latent-attention-in|Towards Economical Inference: Enabling DeepSeek's Multi-Head Latent Attention in…]] — Teacher-free GQA→MLA conversion on 0.4% pretrain data — tokenizer-agnostic escape hatch, but lossy sub-1B
- [[x-ecomla-upcycling-pre-trained-attention-into-mla-for-efficient-and-extreme-kv|X-EcoMLA: Upcycling Pre-Trained Attention into MLA for Efficient and Extreme KV…]] — Lossless 6.4-10.6x MLA upcycling — but only with a larger same-tokenizer teacher, no long-context eval
- [[huggingface-co-deepseek-ai-deepseek-ocr-config-json-fetched|huggingface.co/deepseek-ai/DeepSeek-OCR config.json (fetched directly)]] — Counter-datapoint: DeepSeek ships MLA DISABLED at ~570M active (kv_lora_rank=null, plain MHA)
- [[youtu-llm-unlocking-the-native-agentic-potential-for-lightweight-large-language|Youtu-LLM: Unlocking the Native Agentic Potential for Lightweight Large Language…]] — Dense-MLA production at 1.96B; own 1B ablation has MLA beating GQA on ppl and MC across the board

## Papers (8)
- [[tensor-product-attention-is-all-you-need|Tensor Product Attention Is All You Need]] (2025) — mla-sub1b
- [[towards-economical-inference-enabling-deepseek-s-multi-head-latent-attention-in|Towards Economical Inference: Enabling DeepSeek's Multi-Head Latent Attention in Any Transformer-bas…]] (2025) — mla-sub1b
- [[x-ecomla-upcycling-pre-trained-attention-into-mla-for-efficient-and-extreme-kv|X-EcoMLA: Upcycling Pre-Trained Attention into MLA for Efficient and Extreme KV Compression]] (2025) — mla-sub1b
- [[hardware-efficient-attention-for-fast-decoding|Hardware-Efficient Attention for Fast Decoding]] (2025) — mla-sub1b
- [[decoder-hybrid-decoder-architecture-for-efficient-reasoning-with-long-generation|Decoder-Hybrid-Decoder Architecture for Efficient Reasoning with Long Generation]] (2025) — mla-sub1b
- [[youtu-llm-unlocking-the-native-agentic-potential-for-lightweight-large-language|Youtu-LLM: Unlocking the Native Agentic Potential for Lightweight Large Language Models]] (2025) — mla-sub1b
- [[you-only-cache-once-decoder-decoder-architectures-for-language-models|You Only Cache Once: Decoder-Decoder Architectures for Language Models]] (2024) — hybrid-efficiency-efficient-attention-se
- [[reducing-transformer-key-value-cache-size-with-cross-layer-attention|Reducing Transformer Key-Value Cache Size with Cross-Layer Attention]] (2024) — hybrid-efficiency-efficient-attention-se

## Sources & findings (5)
- [[huggingface-co-deepseek-ai-deepseek-ocr-config-json-fetched|huggingface.co/deepseek-ai/DeepSeek-OCR config.json (fetched directly)]] — Counter-datapoint from DeepSeek themselves: the DeepSeek-OCR decoder (DeepSeek-3B-MoE, ~570M ACTIVE params — the closest…
- [[huggingface-co-deepseek-ai-deepseek-v2-lite-config-json|huggingface.co/deepseek-ai/DeepSeek-V2-Lite config.json (fetched direc…]] — Smallest official DeepSeek MLA config (DeepSeek-V2-Lite, 15.7B total / 2.4B active, d_model=2048, 27 layers, 16 heads) d…
- [[huggingface-co-openbmb-minicpm3-4b-config-json-fetched|huggingface.co/openbmb/MiniCPM3-4B config.json (fetched directly)]] — Smallest production kv_lora_rank shipped: MiniCPM3-4B (d_model=2560, 62 layers, 40 heads) uses kv_lora_rank=256, q_lora_…
- [[huggingface-co-qwen-qwen3-5-0-8b-config-json-fetched|huggingface.co/Qwen/Qwen3.5-0.8B config.json (fetched directly)]] — Resolves KB [UNVERIFIED] on Qwen3.5 sub-1B: Qwen/Qwen3.5-0.8B config.json shows NO MLA — it is a hybrid: 24 layers, hidd…
- [[arithmetic-from-verified-configs-deepseek-v2-lite-minicpm3|Arithmetic from verified configs (DeepSeek-V2-Lite, MiniCPM3, Qwen3-0.…]] — Cache-accounting nuance the design spec must not miss: MLA's cache advantage depends on the GQA baseline it replaces. Pe…

## Related topics
- [[mla-at-sub-1b]] — 3 shared nodes
- [[mla-at-sub-1b-scale]] — 3 shared nodes
- [[mla-vs-gqa-pretraining-cost-and-converge]] — 3 shared nodes
- [[hybrid-efficiency-efficient-attention-se]] — 2 shared nodes
- [[mla-upcycling-at-1b-under-a-bespoke-toke]] — 2 shared nodes

[[Home]]
