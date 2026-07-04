---
type: "moc"
topic: "inference-tts"
nodes: 14
papers: 11
sources: 3
uncertain_claims: 6
tags: ["moc"]
---
# Topic: inference-tts

The headline result is that compute-optimal test-time scaling lets sub-1B models beat 405B on MATH-500 (Can-1B: Llama-3.2-1B 66.2%, Qwen2.5-0.5B 76.4% vs Llama-3.1-405B 71.4%), but the win is method/PRM-dependent — beam search for ≤7B policies, and the PRM must match the policy's output distribution or gains collapse. Kinetics is the load-bearing refutation: once KV memory is counted, small-model TTS is overestimated (Qwen3-0.6B needs 3.5GB KV @32K vs 1.2GB weights), only ≥14B benefit from CoT beyond 10K tokens, and block-top-k sparse attention (+45pts, 8.58x cheaper) is the actual enabler because TTS at small scale is memory-access-bound, not FLOP-bound. Two failure modes are CONFIRMED at small scale: budget forcing collapses (s1: R1-distill-1.5B accuracy declines as tokens go 17K→25K, with content loops), and external-draft speculative decoding is non-viable for a 500M target (needs 10-20x size ratio and ≥60% acceptance), forcing self-speculative MTP heads instead (V3 MTP ~1.8x, EAGLE-3 3.0-6.5x). Deployment carries a concrete tax: MLA breaks mainline GGUF export (needs the ik_llama.cpp fork) and any Engram/custom module needs full C++ integration; edge throughput for 0.5-1.5B is 30-60 tok/s but perceived words/s scales ~2.4x with tokenizer fertility. The open question is whether TTS gains transfer to Kazakh knowledge — SozKZ-600M sits at ~30% MC-QA (below Qwen2.5-0.5B), no morphology-aware MTP or Kazakh PRM exists yet, and cross-lingual reward transfer (Best-of-L) remains the untested pragmatic path.

## Frontier highlights
- [[kinetics-rethinking-test-time-scaling-laws|Kinetics: Rethinking Test-Time Scaling Laws]] — Memory-aware refutation: sub-1B TTS overestimated; sparse attention (+45pts, 8.58x) is the real enabler
- [[can-1b-llm-surpass-405b-llm-rethinking-compute-optimal-test-time-scaling|Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling]] — Headline compute-optimal TTS: 0.5B hits 76.4% MATH-500 > 405B 71.4%, but PRM/policy-dependent
- [[deepseek-v3-technical-report|DeepSeek-V3 Technical Report]] — Core inference tech: MTP self-speculative 1.8x, MLA KV-cache math, FP8 (A100 can't use it)
- [[s1-simple-test-time-scaling|s1: Simple test-time scaling]] — Budget forcing FAILS at small scale: R1-distill-1.5B accuracy drops 17K→25K tokens
- [[flatter-tokens-are-more-valuable-for-speculative-draft-model-training|Flatter Tokens are More Valuable for Speculative Draft Model Training]] — 500M target has no viable external draft (needs 10-20x ratio, ≥60% accept) → self-speculative only
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] — Kazakh from-scratch baseline: fertility→throughput axis, ~30% MC-QA below Qwen2.5-0.5B

## Papers (11)
- [[flatter-tokens-are-more-valuable-for-speculative-draft-model-training|Flatter Tokens are More Valuable for Speculative Draft Model Training]] (2026) — inference-tts
- [[sozkz-training-efficient-small-language-models-for-kazakh-from-scratch|SozKZ: Training Efficient Small Language Models for Kazakh from Scratch]] (2026) — tokenizer-morphology
- [[kazbyte-adapting-qwen-models-to-kazakh-via-byte-level-adapter|KazByte: Adapting Qwen models to Kazakh via Byte-level Adapter]] (2026) — tokenizer-morphology
- [[deepseek-r1-incentivizing-reasoning-capability-in-llms-via-reinforcement|DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning]] (2025) — deepseek-tech
- [[s1-simple-test-time-scaling|s1: Simple test-time scaling]] (2025) — inference-tts
- [[can-1b-llm-surpass-405b-llm-rethinking-compute-optimal-test-time-scaling|Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling]] (2025) — inference-tts
- [[kazmmlu-evaluating-language-models-on-kazakh-russian-and-regional-knowledge-of|KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan]] (2025) — sota-slm
- [[ranked-voting-based-self-consistency-of-large-language-models|Ranked Voting based Self-Consistency of Large Language Models]] (2025) — inference-tts
- [[kinetics-rethinking-test-time-scaling-laws|Kinetics: Rethinking Test-Time Scaling Laws]] (2025) — inference-tts
- [[best-of-l-cross-lingual-reward-modeling-for-mathematical-reasoning|Best-of-L: Cross-Lingual Reward Modeling for Mathematical Reasoning]] (2025) — inference-tts
- [[deepseek-v3-technical-report|DeepSeek-V3 Technical Report]] (2024) — deepseek-tech

## Sources & findings (3)
- [[ggml-org-llama-cpp-deepwiki-supported-model-architectures|ggml-org/llama.cpp DeepWiki 'Supported Model Architectures']] — llama.cpp does support recurrent/hybrid backbones (Mamba, RWKV, Qwen3-Next Gated DeltaNet SSM layers) and 100+ architect…
- [[ggml-org-llama-cpp-discussions-3167-4167-8273|ggml-org/llama.cpp Discussions #3167/#4167/#8273]] — Realistic edge throughput for 0.5-1.5B models: ~30-60 tok/s at Q4 on M1/8GB-class GPU; 20-100 tok/s on CPU (memory-bandw…
- [[ggml-org-llama-cpp-howto-add-model-md-discussion-16770|ggml-org/llama.cpp HOWTO-add-model.md + Discussion #16770]] — MLA breaks mainline GGUF export: DeepSeek-style MLA GGUF requires the ik_llama.cpp fork and will not run on vanilla llam…

## Related topics
- [[kazakh-turkic-nlp]] — 3 shared nodes
- [[novelty-check]] — 3 shared nodes
- [[deepseek-tech]] — 2 shared nodes
- [[kazakh-tokenizer-fertility-vs-byte-premi]] — 2 shared nodes
- [[tokenizer-morphology]] — 2 shared nodes

[[Home]]
