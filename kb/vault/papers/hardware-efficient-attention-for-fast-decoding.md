---
kb_id: "arxiv:2505.21487"
type: "paper"
title: "Hardware-Efficient Attention for Fast Decoding"
arxiv_id: "2505.21487"
doi: null
hf_repo: null
year: 2025
topics: ["mla-sub1b", "mla-vs-gqa-pretraining-cost-and-converge", "gla-2-gta-arxiv-2505-21487-zadouri-strau", "attention-kv-sub1b-attention-kv-architec"]
claims: 5
uncertain_claims: 0
verdicts: []
aliases: ["Hardware-Efficient Attention for Fast Decoding", "arXiv:2505.21487", "arxiv:2505.21487"]
tags: ["paper", "topic/mla-sub1b", "topic/mla-vs-gqa-pretraining-cost-and-converge", "topic/gla-2-gta-arxiv-2505-21487-zadouri-strau", "topic/attention-kv-sub1b-attention-kv-architec"]
---
# Hardware-Efficient Attention for Fast Decoding

[arXiv](https://arxiv.org/abs/2505.21487)
**Topics:** [[mla-sub1b]], [[mla-vs-gqa-pretraining-cost-and-converge]], [[gla-2-gta-arxiv-2505-21487-zadouri-strau]], [[attention-kv-sub1b-attention-kv-architec]]

> [!abstract]
> LLM decoding is bottlenecked for large batches and long contexts by loading the key-value (KV) cache from high-bandwidth memory, which inflates per-token latency, while the sequential nature of decoding limits parallelism. We analyze the interplay among arithmetic intensity, parallelization, and model quality and question whether current architectures fully exploit modern hardware. This work redes …

## Claims

> [!note] CLAIM — mla-sub1b
> Second independent from-scratch head-to-head (Tri Dao group): models at 433M, 876M, 1.471B on FineWeb-Edu 50B tokens (Llama-3-style). At 876M: GQA-4 ppl 11.340 / 56.9% avg downstream vs MLA 11.363 / 56.7% (parity within 0.2pp); at 433M MLA 54.9% > GQA-4 54.5%; at 1.47B MLA 59.1% < GQA-4 60.2% (MLA loses 1.1pp). Their GLA-2 (2 latent heads, d_c=2*d_h per head, rope dim 32) beats BOTH at 433M (55.4%) and 876M (57.5%, ppl 11.293) with MLA-class cache and better tensor-parallel sharding; GTA-4 (tied KV) gets 57.6% at 876M with ~half of GQA-4 cache. MLA config: single latent of dim 512, rope dim d_R=32, q NOT compressed.
>
> **Numbers:** 876M: GQA-4 11.340/56.9 vs MLA 11.363/56.7 vs GLA-2 11.293/57.5 vs GTA-4 11.232/57.6; 433M: MLA 54.9 vs GQA-4 54.5 vs GLA-2 55.4; 1.47B: MLA 59.1 vs GQA-4 60.2; MLA latent 512, rope 32, no q compression; 50B tokens
> **Relevance:** Closest published run to a 600M Kazakh model (433M/876M bracket the target). Result pattern = parity, not superiority; and GLA-2/GTA-4 are strictly better-performing drop-in alternatives at this scale with the same cache budget.
> **Source:** arXiv 2505.21487 (Hardware-Efficient Attention for Fast Decoding), Tables 3-5, HTML v1 · **Sweep:** `mla-sub1b-2026-07`

> [!note] CLAIM — mla-vs-gqa-pretraining-cost-and-converge
> Strongest direct evidence MLA converges to GQA-or-better quality within 25-50B tokens at sub-1B: 'Hardware-Efficient Attention for Fast Decoding' (Dao-AILab) pretrained param-matched MHA/MQA/GQA-4/GTA-4/MLA/GLA-2 from scratch on FineWeb-Edu at 183M (25B tokens), 433M/876M/1.47B (50B tokens each), GPT-3 config + Llama-3 arch, param-matched by widening FFN (not by changing heads). MLA beats GQA-4 at both sub-1B checkpoints where MLA also caches LESS.
>
> **Numbers:** FineWeb-Edu val ppl — 183M@25B: MLA 16.318 vs GQA-4 16.578 vs MHA 16.715; 433M@50B: MLA 12.561 vs GQA-4 12.922; 876M@50B: MLA 11.363 vs GQA-4 11.340 (5-dataset avg ppl: MLA 24.929 vs GQA-4 25.286); 1.47B@50B: MLA 10.256 vs GQA-4 10.202, downstream 7-bench avg MLA 59.1% vs GQA-4 60.2%. Downstream 433M: MLA 54.9% vs GQA-4 54.5% vs GLA-2 55.4%. Configs: LR 2.6e-4/1.45e-4/1.2e-4/1.0e-4 (S/M/L/XL), batch 512 (XL 256), AdamW b=(0.9,0.95), wd 0.1, Llama-3 128K tokenizer.
> **Relevance:** Exactly the lab's scale (433M ~ target 500-600M) and closest published token budget (25-50B vs lab's 9-30B kk). MLA wins on ppl AND downstream at 183M/433M while caching 288 vs GQA-4's 512 elem/tok/layer — the pro-MLA half of the verdict.
> **Source:** arXiv 2505.21487 (Zadouri, Strauss, Dao), PDF Tables 2-6 read directly; extracted text /tmp/claude-1000/-home-altairzhambyl-projects-SLMs-basic/98053e10-7c62-465c-acd3-b6c763138a63/scratchpad/gla.txt · **Sweep:** `mla-sub1b-2026-07`

> [!note] CLAIM — mla-vs-gqa-pretraining-cost-and-converge
> Exact sub-1B MLA configs that worked (fills KB gap on kv_lora_rank/rope_dim below 1B): the GLA paper uses a single latent head with d_c = 4*d_h and decoupled RoPE dim 32 (48 ablated at 876M). Per scale: 183M (d=768, 12 heads, d_h=64) -> kv_lora_rank=256, rope_dim=32; 433M (d=1024, 16h, d_h=64) -> 256/32; 876M (d=1536, 16h, d_h=96) -> 384/32; 1.47B (d=2048, 16h, d_h=128) -> 512/32. No q_lora (queries not compressed, unlike DeepSeek-V2).
>
> **Numbers:** kv_lora_rank = 4*d_h (256 at d_model 768-1024; 384 at 1536; 512 at 2048); rope_dim = 32 default; MLA cache = 4*d_h + 32 elem/tok/layer; GLA-2 alternative: 2 latent heads x 2*d_h, same total cache, ppl 12.456 at 433M (beats both MLA 12.561 and GQA-4 12.922)
> **Relevance:** Directly reusable recipe for the lab's ~500M model (d_model~1536 -> d_c=384, rope 32), replacing the KB's DeepSeek-V2-derived guess (d_c=512, rope 64) which is tuned for d=5120, not sub-1B.
> **Source:** arXiv 2505.21487 Appendix B.1-B.2 (Tables 6-9) + Section 4 ('GLA... d_c = 2*d_h, half of MLA's 4*d_h'; 'by default we use a RoPE dimension d_R = 32') · **Sweep:** `mla-sub1b-2026-07`

> [!note] CLAIM — gla-2-gta-arxiv-2505-21487-zadouri-strau
> The original GLA/GTA evidence base is single-seed and workshop-level. Models trained: 183M / 433M / 876M / 1.471B on FineWeb-Edu (25B tokens for small, 50B for the rest); the paper contains NO mention of multiple seeds, variance, or error bars anywhere in the experimental methodology. Venue is the ICML 2025 ES-FoMo III workshop (oral), not a main conference; arXiv is still v1 (2025-05-27); Semantic Scholar shows 14 citations, 1 influential, venue 'arXiv.org'.
>
> **Numbers:** Scales 183M/433M/876M/1.47B; 25-50B tokens; 0 seed/variance statements; 14 citations (1 influential) by 2026-07; arXiv v1 only
> **Relevance:** The lab's Recommendation 5 rests on single-seed runs from the method authors; the seed-noise floor for the 0.6-0.9pp GLA-2 advantages is unestablished in the primary source itself.
> **Source:** arxiv.org/html/2505.21487v1 (experiments section); icml.cc/virtual/2025/51861 (ES-FoMo III oral); api.semanticscholar.org/graph/v1/paper/arXiv:2505.21487 · **Sweep:** `mla-sub1b-2026-07`

> [!note] CLAIM — attention-kv-sub1b-attention-kv-architec
> [derived, design-spec arithmetic] KV-cache-per-token menu at the lab's from-scratch shape (d_model=1024, 28 layers, fp16): GQA-8×128 (Qwen3-0.6B clone) = 57,344 elem = 112 KiB/token; GQA-4×128 = 28,672 elem = 56 KiB; GQA-2×128 = 28 KiB; MLA kv_lora_rank=256 + rope_dim=32 (the KB-validated 4×d_h recipe at d≈1024 from arXiv:2505.21487) = 288×28 = 8,064 elem = 15.75 KiB/token (3.6x below GQA-4, 7.1x below Qwen3-0.6B); Gemma-style 5:1 SWA-512 + MQA amortizes to near-constant ~8 MiB + full-attn-share growth. At 8K context per sequence: 0.94 GB / 470 MB / 235 MB / 132 MB respectively — on 16GB T4s this is the difference between eval batch 8 and batch 64.
>
> **Numbers:** 112 / 56 / 28 / 15.75 KiB per token fp16 for GQA-8 / GQA-4 / GQA-2 / MLA-256+32 at d1024×28L
> **Relevance:** The single table the design panel needs to trade attention variants against T4 memory; combine with KB's quality envelope (MLA within ±1pp of GQA at 350M-1.5B; Mellum2: GQA-2 quality-insufficient).
> **Source:** derived from verified configs (Qwen/Qwen3-0.6B-Base config.json; arXiv:2505.21487 KB node; unsloth/gemma-3-270m-it config.json) · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[eg-mla-embedding-gated-multi-head-latent-attention-for-scalable-and-efficient|EG-MLA: Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs]] — EG-MLA gates MLA with embeddings; builds on the sub-1B MLA config this paper pins (kv_lora, decoupled rope)
- [[kitty-accurate-and-efficient-2-bit-kv-cache-quantization-with-dynamic-channel|Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precis…]] — Competing KV-cache reduction axes: MLA latent compression vs Kitty 2-bit KV quantization
- [[huggingface-co-blog-smollm3|huggingface.co/blog/smollm3]] — GLA paper shows MLA beats GQA-4 sub-1B, yet SmolLM3 shipped GQA-4 without ablating MLA (not in nanotron at the time)
- [[huggingface-co-qwen-qwen3-0-6b-base-config-json-fetched-raw|huggingface.co/Qwen/Qwen3-0.6B-Base config.json (fetched raw, 2026-07-…]] — Lab's GQA-8x128 baseline; 2505 shows GQA-4 approx MLA at sub-1B, motivating MLA over Qwen3-0.6B's GQA-8
- [[github-com-dao-ailab-flash-attention-readme-fetched-2026-07|github.com/Dao-AILab/flash-attention README (fetched 2026-07-04) + emp…]] — Both weigh hardware-fit of attention; node measures SDPA fp16 as fastest SM75 kernel while FA2 needs Ampere+

[[Home]]
