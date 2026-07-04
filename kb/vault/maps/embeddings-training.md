---
type: "moc"
topic: "embeddings-training"
nodes: 7
papers: 7
sources: 0
uncertain_claims: 0
tags: ["moc"]
---
# Topic: embeddings-training

The frontier converges on one recipe for sub-1B embedders: multi-stage training (weakly-supervised contrastive pretrain on ~150-470M synthetic/weak pairs → supervised fine-tune on ~6-7M pairs with hard negatives), InfoNCE + in-batch negatives with false-negative removal, Matryoshka (near-free, standard at 32-1024 dims), checkpoint souping/slerp as a free robustness gain, instruction prefixes, and distillation from a larger teacher (KaLM-V2 distills Qwen3-Embedding-8B). The concrete hard-negative protocol is NV-Retriever's TopK-PercPos (mine top-k with a teacher, discard candidates scoring >95% of the positive). The load-bearing open contest is pooling/attention at 0.5B: Qwen3-Embedding-0.6B keeps causal attention + last-token [EOS] and calls it "on par," but KaLM-V2 and LLM2Vec REMOVE the causal mask (bidirectional + mean pooling) and reach higher MTEB (KaLM-V2 67.81 vs Qwen3-Emb 64.33) — not iso-controlled, so it must be a design-spec ablation. For Kazakh specifically the decoder-to-embedder path is REFUTED on the only public signal: Qwen3-Emb-0.6B (a Qwen3-0.6B-Base specialization, the lab's exact CPT base) scores Belebele kaz nDCG@10 0.7545, losing badly to encoders BGE-M3 (0.9017) and mE5-large-instruct (0.8949), traced to synthetic contrastive data skewed to high-resource languages. Turkic evidence (TurkEmbed/TR-MTEB, 34.2M pairs) and AfriE5/Less-is-More/kazembed-v5 all agree the realistic gain from adapting mE5 is small (+1.1 to +2.1), so beating mE5 on KazQAD is hard but achievable via cross-lingual contrastive distillation on a few tens of thousands of quality-filtered pairs.

## Frontier highlights
- [[qwen3-embedding-advancing-text-embedding-and-reranking-through-foundation-models|Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Model…]] — The sub-1B target to beat: full reproducible 3-stage recipe, causal+EOS, but REFUTED on Kazakh (Belebele 0.7545)
- [[kalm-embedding-v2-superior-training-techniques-and-data-inspire-a-versatile|KaLM-Embedding-V2: Superior Training Techniques and Data Inspire A Versatile Emb…]] — Closest architectural template (Qwen2-0.5B, mask removed, mean+MRL, distills Qwen3-Emb-8B); 67.81 refutes causal parity
- [[afrimteb-and-afrie5-benchmarking-and-adapting-text-embedding-models-for-african|AfriMTEB and AfriE5: Benchmarking and Adapting Text Embedding Models for African…]] — Closest task analogue: adapt mE5 to LRL via cross-lingual contrastive distillation, +1.1/+1.7, ~60k COMET-filtered pairs
- [[turkembed-turkish-embedding-model-on-nli-sts-tasks|TurkEmbed: Turkish Embedding Model on NLI & STS Tasks]] — Turkic warning: 34.2M Turkish pairs still fail to surpass mE5 — beating mE5 on a Kazakh sibling is hard
- [[nv-retriever-improving-text-embedding-models-with-effective-hard-negative-mining|NV-Retriever: Improving text embedding models with effective hard-negative minin…]] — The concrete hard-negative protocol evallab pins: TopK-PercPos, discard candidates >95% of positive score
- [[mmbert-a-modern-multilingual-encoder-with-annealed-language-learning|mmBERT: A Modern Multilingual Encoder with Annealed Language Learning]] — Only fresh encoder backbone with confirmed Kazakh pretraining (annealed language learning, 1833 langs)

## Papers (7)
- [[qwen3-embedding-advancing-text-embedding-and-reranking-through-foundation-models|Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models]] (2025) — embed-sota
- [[kalm-embedding-v2-superior-training-techniques-and-data-inspire-a-versatile|KaLM-Embedding-V2: Superior Training Techniques and Data Inspire A Versatile Embedding Model]] (2025) — embed-sota
- [[mmbert-a-modern-multilingual-encoder-with-annealed-language-learning|mmBERT: A Modern Multilingual Encoder with Annealed Language Learning]] (2025) — embed-sota
- [[afrimteb-and-afrie5-benchmarking-and-adapting-text-embedding-models-for-african|AfriMTEB and AfriE5: Benchmarking and Adapting Text Embedding Models for African Languages]] (2025) — decoder-to-embedder
- [[turkembed-turkish-embedding-model-on-nli-sts-tasks|TurkEmbed: Turkish Embedding Model on NLI & STS Tasks]] (2025) — embeddings-training
- [[nv-retriever-improving-text-embedding-models-with-effective-hard-negative-mining|NV-Retriever: Improving text embedding models with effective hard-negative mining]] (2024) — embeddings-training
- [[mgte-generalized-long-context-text-representation-and-reranking-models-for|mGTE: Generalized Long-Context Text Representation and Reranking Models for Multilingual Text Retrie…]] (2024) — embeddings-training

## Related topics
- [[embed-sota]] — 3 shared nodes
- [[decoder-to-embedder]] — 2 shared nodes

[[Home]]
