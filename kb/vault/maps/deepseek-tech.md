---
type: "moc"
topic: "deepseek-tech"
nodes: 7
papers: 7
sources: 0
uncertain_claims: 5
tags: ["moc"]
---
# Topic: deepseek-tech

The DeepSeek stack supplies QymyzLM's two efficiency levers, but the slice's own math repeatedly shows they were validated at scales the ≤600M-dense target does not inhabit. MLA is the strongest transferable win: DeepSeek-V2 cuts KV cache 93.3% vs MHA (cache = d_c+d_h_rope = 576 elem/tok/layer ≈ GQA-2.25) while beating MHA/GQA/MQA quality, and EG-MLA proves it survives from scratch at 120M (kv_lora_rank=256, cache 3.84K elem/tok; rank-64 with token-embedding gating scores +0.49) — the only located sub-1B DeepSeek-style run below rank 512. The Engram lookup axis beats a strictly iso-param/iso-FLOP MoE-27B (MMLU +3.0, BBH +5.0, NIAH 84.2→97.0) with a clean U-shaped ρ≈75-80% allocation law, but every Engram result sits on an MoE backbone (min 568M active) with the table offloaded off-GPU, ρ=0 pure-dense is never tested, and param-accounting is decisive: a 500M dense backbone + ~512M table = ~1B total, outside the ≤600M class the peer group (Qwen3-0.6B, SozKZ-600M, Gemma3-270M) is measured in. Other levers are gated by scale/hardware: MTP degrades below a 1-3B threshold, R1's smallest distill is 1.5B with no 500M release, and FP8 training needs Hopper (A100/T4 cannot). The open question is whether MLA's and Engram's scale-validated gains, plus the genuinely unoccupied morpheme-keyed memory/MTP novelty, transfer down to a dense sub-600M agglutinative-Kazakh model.

## Frontier highlights
- [[conditional-memory-via-scalable-lookup-a-new-axis-of-sparsity-for-large|Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Languag…]] — Engram conditional-memory axis: beats iso-param/iso-FLOP MoE-27B, but only on MoE backbones — ρ=0 dense untested
- [[deepseek-v2-a-strong-economical-and-efficient-mixture-of-experts-language-model|DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Mod…]] — MLA: 93.3% KV cut, beats MHA quality; the concrete cache win over the planned GQA-2
- [[eg-mla-embedding-gated-multi-head-latent-attention-for-scalable-and-efficient|EG-MLA: Embedding-Gated Multi-head Latent Attention for Scalable and Efficient L…]] — EG-MLA: only located from-scratch sub-1B DeepSeek-MLA (120M, rank 256/64), proves MLA transfers down
- [[deepseek-v3-technical-report|DeepSeek-V3 Technical Report]] — MTP threshold 1-3B (degrades below); FP8 needs Hopper — A100/T4 excluded
- [[deepseekmoe-towards-ultimate-expert-specialization-in-mixture-of-experts|DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Langua…]] — MoE premise collapses at ≤600M total; sparse budget better spent on the lookup axis
- [[deepseek-r1-incentivizing-reasoning-capability-in-llms-via-reinforcement|DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learni…]] — Reasoning distill floor: smallest R1 distill is 1.5B, needs domain-matched base + 800K CoT

## Papers (7)
- [[conditional-memory-via-scalable-lookup-a-new-axis-of-sparsity-for-large|Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models]] (2026) — deepseek-tech
- [[deepseek-r1-incentivizing-reasoning-capability-in-llms-via-reinforcement|DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning]] (2025) — deepseek-tech
- [[native-sparse-attention-hardware-aligned-and-natively-trainable-sparse-attention|Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention]] (2025) — deepseek-tech
- [[eg-mla-embedding-gated-multi-head-latent-attention-for-scalable-and-efficient|EG-MLA: Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs]] (2025) — deepseek-tech
- [[deepseekmoe-towards-ultimate-expert-specialization-in-mixture-of-experts|DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models]] (2024) — deepseek-tech
- [[deepseek-v2-a-strong-economical-and-efficient-mixture-of-experts-language-model|DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model]] (2024) — deepseek-tech
- [[deepseek-v3-technical-report|DeepSeek-V3 Technical Report]] (2024) — deepseek-tech

## Related topics
- [[novelty-check]] — 3 shared nodes
- [[inference-tts]] — 2 shared nodes
- [[kazakh-turkic-nlp]] — 2 shared nodes

[[Home]]
