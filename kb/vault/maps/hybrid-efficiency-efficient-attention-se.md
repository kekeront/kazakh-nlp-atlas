---
type: "moc"
topic: "hybrid-efficiency-efficient-attention-se"
nodes: 14
papers: 13
sources: 1
uncertain_claims: 6
tags: ["moc"]
---
# Topic: hybrid-efficiency-efficient-attention-se

The frontier splits into three efficiency levers for a ≤600M Kazakh SLM, all measured but none carrying novelty alone. (1) Latent/low-rank attention: DeepSeek-V2 MLA cuts KV cache 93.3% (~576 elem/tok/layer ≈ GQA-2.25) while beating MHA perplexity, but the only from-scratch sub-1B evidence (arxiv:2506.09342, 30M–202M) shows decoupled-RoPE MLA at r=d/2 gives just 45% KV cut at +0.3% loss, and r=d/4 costs +4.4%—and it was never benchmarked vs GQA, all at ctx≤512. (2) Cross-layer/global KV sharing: CLA2 gives 2x cut at +0.04–0.06 ppl for MQA, but the slice flags an internal contradiction—the paper's prose credits GQA2-CLA2 while Table 1 only supports GQA4-CLA2, and untuned GQA-CLA2 rows actually cost +0.07/+0.12 ppl (uncertain), so plan-B's "+0.04" is optimistic; YOCO caches one global KV layer for ~L-fold savings. (3) SSM/conv hybrids: pure Mamba trails Transformers ~15pt on 5-shot MMLU until ~7-8% attention layers are added; the shipped sub-1B winners (LFM2-350M conv+6-GQA beating Qwen3-0.6B on multilingual MMLU 37.99 vs 30.84; Falcon-H1-0.5B parallel attn+Mamba) prove hybrids compete. Gemma3-270M's 5:1 sliding-window recipe (window 512, KV ≈108MB@32K vs Qwen3-0.6B's 3.75GB) is the strongest ≤300M long-context template. Open question: which lever (MLA vs sliding-window vs conv-hybrid) survives at ≤600M ACTIVE params on Kazakh with only free T4 compute, given no from-scratch MLA-vs-GQA head-to-head exists at this scale.

## Frontier highlights
- [[deepseek-v2-a-strong-economical-and-efficient-mixture-of-experts-language-model|DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Mod…]] — DeepSeek-V2 MLA reference: 93.3% KV cut, beats MHA, ≈GQA-2.25 cache—the efficient-attention anchor
- [[latent-multi-head-attention-for-small-language-models|Latent Multi-Head Attention for Small Language Models]] — Only from-scratch sub-1B MLA study: r=d/2 = 45% cut/+0.3% loss, no GQA arm, ctx≤512
- [[gemma-3-technical-report|Gemma 3 Technical Report]] — Gemma3-270M 5:1 sliding-window: KV ≈108MB@32K vs 3.75GB—strongest ≤300M long-context template
- [[lfm2-technical-report|LFM2 Technical Report]] — LFM2-350M conv+6-GQA hybrid beats Qwen3-0.6B multilingual MMLU (37.99 vs 30.84), 2x faster on CPU
- [[reducing-transformer-key-value-cache-size-with-cross-layer-attention|Reducing Transformer Key-Value Cache Size with Cross-Layer Attention]] — CLA2 = 2x KV cut; slice flags prose/table contradiction, untuned GQA-CLA2 costs +0.07-0.12 ppl
- [[falcon-h1-a-family-of-hybrid-head-language-models-redefining-efficiency-and|Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Per…]] — Falcon-H1-0.5B parallel attn+Mamba block leads sub-1B math/code but covers no Turkic language

## Papers (13)
- [[gemma-3-technical-report|Gemma 3 Technical Report]] (2025) — sota-slm
- [[nemotron-h-a-family-of-accurate-and-efficient-hybrid-mamba-transformer-models|Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models]] (2025) — hybrid-efficiency-efficient-attention-se
- [[bitnet-b1-58-2b4t-technical-report|BitNet b1.58 2B4T Technical Report]] (2025) — hybrid-efficiency-efficient-attention-se
- [[minicpm4-ultra-efficient-llms-on-end-devices|MiniCPM4: Ultra-Efficient LLMs on End Devices]] (2025) — hybrid-efficiency-efficient-attention-se
- [[latent-multi-head-attention-for-small-language-models|Latent Multi-Head Attention for Small Language Models]] (2025) — hybrid-efficiency-efficient-attention-se
- [[falcon-h1-a-family-of-hybrid-head-language-models-redefining-efficiency-and|Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance]] (2025) — sota-slm
- [[kitty-accurate-and-efficient-2-bit-kv-cache-quantization-with-dynamic-channel|Kitty: Accurate and Efficient 2-bit KV Cache Quantization with Dynamic Channel-wise Precision Boost]] (2025) — hybrid-efficiency-efficient-attention-se
- [[lfm2-technical-report|LFM2 Technical Report]] (2025) — sota-slm
- [[deepseek-v2-a-strong-economical-and-efficient-mixture-of-experts-language-model|DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model]] (2024) — deepseek-tech
- [[you-only-cache-once-decoder-decoder-architectures-for-language-models|You Only Cache Once: Decoder-Decoder Architectures for Language Models]] (2024) — hybrid-efficiency-efficient-attention-se
- [[reducing-transformer-key-value-cache-size-with-cross-layer-attention|Reducing Transformer Key-Value Cache Size with Cross-Layer Attention]] (2024) — hybrid-efficiency-efficient-attention-se
- [[an-empirical-study-of-mamba-based-language-models|An Empirical Study of Mamba-based Language Models]] (2024) — hybrid-efficiency-efficient-attention-se
- [[the-zamba2-suite-technical-report|The Zamba2 Suite: Technical Report]] (2024) — hybrid-efficiency-efficient-attention-se

## Sources & findings (1)
- [[hf-qwen-qwen3-0-6b-config|HF Qwen/Qwen3-0.6B config]] — Baseline architecture to beat - Qwen3-0.6B: 28 layers, hidden 1024, 16 query heads / 8 KV heads (GQA-2), head_dim 128, F…

## Related topics
- [[sota-slm]] — 3 shared nodes
- [[mla-sub1b]] — 2 shared nodes

[[Home]]
