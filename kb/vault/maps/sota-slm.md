---
type: "moc"
topic: "sota-slm"
nodes: 17
papers: 10
sources: 7
uncertain_claims: 5
tags: ["moc"]
---
# Topic: sota-slm

The sub-1B frontier is converged on a handful of architectural facts: DEPTH beats WIDTH (MobileLLM, adopted by SmolLM2-360M's 32L/d960 deep-thin GQA), tied input/output embeddings are near-universal, GQA head ratios cluster at 2:1-4:1 with head_dim=64, and extreme token/param overtraining is the dominant lever (Qwen3-0.6B ~60,000 tok/param; LFM2.5-350M claims 80,000:1 on 28T tokens). The hard, CONFIRMED constraint for this lab is that NO mainstream sub-1B SLM is trained for Kazakh/Turkic — Falcon-H1 and LFM2 exclude all Turkic, and the practical ≤1B KazMMLU ceiling is held by general Qwen3-0.6B at 32.8% (lab-measured, 3-shot), with Gemma-3-270M and Llama-3.2-1B at random (24-25%). The live architectural contest is attention/KV efficiency: Gemma 3's 5:1 sliding-window interleave (KV 60%→~15% at 32K), Falcon-H1's parallel attention+Mamba-2-per-layer, LFM2/Granite's conv-or-Mamba + few-global-attention hybrids, versus MLA's latent KV compression (70KB/tok vs GQA's 192-328KB). Contested/uncertain: whether extreme overtraining still pays (saturation results loom), Gemma-3-270M's exact d_model (embedding arithmetic implies ~640, not the reported 1024), and Qwen3.5-0.8B's undocumented sub-1B specs. The open question for QymyzLM: adapt the frozen Qwen3-0.6B backbone (QLoRA-CPT, KV pinned at 3.75GB@32K) or train Kazakh from scratch to exploit depth-over-width and a Turkic-native tokenizer.

## Frontier highlights
- [[qwen3-technical-report|Qwen3 Technical Report]] — Qwen3-0.6B: the 32.8% KazMMLU baseline and frozen CPT backbone — QK-Norm, GQA 2:1, 60k tok/param
- [[kazmmlu-evaluating-language-models-on-kazakh-russian-and-regional-knowledge-of|KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge o…]] — KazMMLU primary eval: no dedicated sub-1B model beats ~33%; sets the 32.8→36 target delta
- [[gemma-3-technical-report|Gemma 3 Technical Report]] — Gemma 3: 5:1 sliding-window KV template (60→15% @32K) + 270M fine-tuning substrate at random on Kazakh
- [[lfm2-technical-report|LFM2 Technical Report]] — LFM2-350M conv+GQA hybrid beats Qwen3-0.6B on multilingual MMLU at fewer params, 2x faster on CPU
- [[mobilellm-optimizing-sub-billion-parameter-language-models-for-on-device-use|MobileLLM: Optimizing Sub-billion Parameter Language Models for On-Device Use Ca…]] — MobileLLM founding result: depth>>width and embedding-sharing at sub-1B, adopted by all successors
- [[sebastian-raschka-mla-gallery|Sebastian Raschka MLA gallery]] — MLA compresses KV 2.7-4.7x vs GQA (70KB/tok) — the alternative to sliding-window/hybrid KV routes

## Papers (10)
- [[verchol-grammar-first-tokenization-for-agglutinative-languages|VerChol -- Grammar-First Tokenization for Agglutinative Languages]] (2026) — sota-slm
- [[qwen3-5-omni-technical-report|Qwen3.5-Omni Technical Report]] (2026) — sota-slm
- [[smollm2-when-smol-goes-big-data-centric-training-of-a-small-language-model|SmolLM2: When Smol Goes Big -- Data-Centric Training of a Small Language Model]] (2025) — sota-slm
- [[tumlu-a-unified-and-native-language-understanding-benchmark-for-turkic-languages|TUMLU: A Unified and Native Language Understanding Benchmark for Turkic Languages]] (2025) — sota-slm
- [[kazmmlu-evaluating-language-models-on-kazakh-russian-and-regional-knowledge-of|KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan]] (2025) — sota-slm
- [[gemma-3-technical-report|Gemma 3 Technical Report]] (2025) — sota-slm
- [[qwen3-technical-report|Qwen3 Technical Report]] (2025) — sota-slm
- [[falcon-h1-a-family-of-hybrid-head-language-models-redefining-efficiency-and|Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance]] (2025) — sota-slm
- [[lfm2-technical-report|LFM2 Technical Report]] (2025) — sota-slm
- [[mobilellm-optimizing-sub-billion-parameter-language-models-for-on-device-use|MobileLLM: Optimizing Sub-billion Parameter Language Models for On-Device Use Cases]] (2024) — sota-slm

## Sources & findings (7)
- [[huggingface-co-blog-smollm3|huggingface.co/blog/smollm3]] — SmolLM3-3B architecture innovations transferable downward: GQA with 4 KV groups, NoPE (remove RoPE from every 4th layer)…
- [[apxml-com-models-gemma-3-270m-conflicts-with-embedding|apxml.com/models/gemma-3-270m (conflicts with embedding-param arithmet…]] — Gemma 3 270M's exact layer count / d_model are inconsistently reported (apxml lists 12 layers, d_model 1024, but 256K×10…
- [[cross-model-synthesis-smollm2-qwen3-lfm2-falcon-h1|cross-model synthesis: SmolLM2/Qwen3/LFM2/Falcon-H1/MobileLLM cards &…]] — GQA head-group ratios cluster tightly across 2025-2026 sub-1B SOTA: SmolLM2-360M 15:5 (3:1), Qwen3-0.6B 16:8 (2:1), LFM2…
- [[ibm-announcement-marktechpost-2025-10-29|IBM announcement + MarkTechPost 2025-10-29]] — IBM Granite 4.0 Nano (Oct 2025) ships 350M and 1B models in hybrid Mamba-2/Transformer (H) and pure-transformer variants…
- [[marktechpost-2025-09-14|MarkTechPost 2025-09-14]] — MobileLLM-R1-950M (Sept 2025): deep-thin, 22 layers, 24 query / 6 KV heads (GQA 4:1), embedding dim 1536, FFN 6144, trai…
- [[marktechpost-2026-03-31|MarkTechPost 2026-03-31]] — LFM2.5-350M (March 2026) pushes the token-to-parameter ratio to 80,000:1 by training a 350M model on 28T tokens plus sca…
- [[sebastian-raschka-mla-gallery|Sebastian Raschka MLA gallery]] — MLA (DeepSeek multi-head latent attention) compresses the KV cache far more than GQA while preserving per-head expressiv…

## Related topics
- [[hybrid-efficiency-efficient-attention-se]] — 3 shared nodes
- [[training-recipes]] — 3 shared nodes
- [[attention-kv-sub1b-attention-kv-architec]] — 2 shared nodes
- [[kazakh-turkic-nlp]] — 2 shared nodes
- [[small-lm-training-recipes-qymyzlm-design]] — 2 shared nodes

[[Home]]
