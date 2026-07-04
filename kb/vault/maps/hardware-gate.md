---
type: "moc"
topic: "hardware-gate"
nodes: 8
papers: 0
sources: 8
uncertain_claims: 2
tags: ["moc"]
---
# Topic: hardware-gate

This topic is the lab's own SM75 (Kaggle T4 / RTX 2070 proxy, cc 7.5, 64KB shared-mem, no bf16 tensor cores) execution gate for QymyzLM architecture choices, all first-hand measurements under torch 2.11.0+cu130 / triton 3.6.0 / fla 0.5.1. GATE OPEN is CONFIRMED: GatedDeltaNet, KimiDeltaAttention (KDA), and fla-Triton Mamba2 all run fwd+bwd in fp16 with finite outputs/grads, and mamba-ssm's CUDA path builds for sm_75. The load-bearing REFUTATION is a throughput inversion — the classic linear-attention speed premise is inverted on SM75: torch SDPA fp16 is the fastest kernel measured and beats every linear kernel up to T=8192 (KDA break-even only extrapolated to T~12-16K), so at CPT ctx 1024-4096 a KDA layer costs 2.7-4.8x SDPA and GDN/Mamba2 layers cost 28-47x (fla fallback under the 64KB limit); KDA is the only fla linear kernel with acceptable SM75 throughput. Two silent traps are established: bf16 (torch.cuda.is_bf16_supported() lies — returns True but runs 7.3x slower than fp16 GEMM), forcing fp16+GradScaler pins everywhere, and KellerJordan Muon's hard-cast to bf16 (6.6x trap, fixed by a one-line .bfloat16()->.half() patch, with its single momentum buffer confirming ~50% optimizer-VRAM saving vs AdamW). All numbers sit against a T4 = ~21% of one A100 (both axes) ceiling. Open question: none of these are yet run on the actual Kaggle T4 or on a Kazakh model — every claim carries flag transferable-untested, and the mamba-ssm/Turing-FA2 runtime behavior is inferred from build targets, not observed.

## Frontier highlights
- [[empirical-this-session-tmp-claude-1000-home-altairzhambyl-69058ff0|Empirical, this session: /tmp/claude-1000/-home-altairzhambyl-projects…]] — GATE OPEN: GDN, KDA, fla-Mamba2 all PASS fwd+bwd in fp16 on real SM75 hardware — the foundational go/no-go
- [[empirical-this-session-tmp-claude-1000-home-altairzhambyl-8a3008cc|Empirical, this session: /tmp/claude-1000/-home-altairzhambyl-projects…]] — Throughput inversion refutes linear-attn motivation: SDPA beats all linear kernels to T=8192; KDA 2.7-4.8x, GDN/Mamba2 28-47x
- [[empirical-muon-ns-py-and-smoke2-py-this-session-torch-2-11|Empirical: muon_ns.py and smoke2.py this session (torch 2.11.0+cu130,…]] — bf16 is a silent trap on SM75: capability flag lies, 7.3x slower GEMM — every T4 config must pin fp16+GradScaler
- [[empirical-tmp-claude-1000-home-altairzhambyl-projects-slms|Empirical: /tmp/claude-1000/-home-altairzhambyl-projects-SLMs-basic/98…]] — Muon usable on T4 after a 1-line fp16 patch (6.6x bf16 trap); single momentum buffer = ~50% optimizer VRAM vs AdamW
- [[nvidia-com-en-us-data-center-tesla-t4-official-spec-page|nvidia.com/en-us/data-center/tesla-t4/ (official spec page, fetched 20…]] — Grounds every number: T4 = ~21% of one A100 on compute and bandwidth; 2xT4 aggregate ~41.7%
- [[empirical-smoke-one-py-smoke2-py-timings-this-session|Empirical: smoke_one.py / smoke2.py timings this session]] — Triton first-call compile tax is 7-9 min/session on Kaggle unless TRITON_CACHE_DIR points at /kaggle/working

## Sources & findings (8)
- [[empirical-muon-ns-py-and-smoke2-py-this-session-torch-2-11|Empirical: muon_ns.py and smoke2.py this session (torch 2.11.0+cu130,…]] — bf16 on SM75 is a silent trap across the stack: torch.cuda.is_bf16_supported() returns True on SM75 (torch 2.11), and bf…
- [[empirical-smoke-one-py-smoke2-py-timings-this-session|Empirical: smoke_one.py / smoke2.py timings this session]] — First-call Triton compile/autotune cost on SM75 is large and per-session on Kaggle: KDA's first fwd+bwd took 439 s (fp16…
- [[empirical-this-session-tmp-claude-1000-home-altairzhambyl-8a3008cc|Empirical, this session: /tmp/claude-1000/-home-altairzhambyl-projects…]] — THROUGHPUT INVERSION at training-relevant context lengths: on SM75 the classic linear-attention speed motivation is inve…
- [[empirical-this-session-tmp-claude-1000-home-altairzhambyl-69058ff0|Empirical, this session: /tmp/claude-1000/-home-altairzhambyl-projects…]] — GATE OPEN: all three kernel families RUN on SM75 in fp16 with finite outputs and gradients. We executed the actual ~30-m…
- [[empirical-tmp-claude-1000-home-altairzhambyl-projects-slms|Empirical: /tmp/claude-1000/-home-altairzhambyl-projects-SLMs-basic/98…]] — Muon IS usable on T4, but the official implementation contains a 6.6x SM75 performance trap: KellerJordan/Muon's zeropow…
- [[github-com-dao-ailab-flash-attention-readme-fetched-2026-07|github.com/Dao-AILab/flash-attention README (fetched 2026-07-04) + emp…]] — Softmax attention on SM75 is NOT blocked by FA2's Ampere-only requirement: (a) torch SDPA fp16 runs fast on SM75 out of…
- [[github-com-state-spaces-mamba-setup-py-raw-main-branch|github.com/state-spaces/mamba setup.py (raw, main branch, fetched 2026…]] — state-spaces/mamba (mamba-ssm CUDA kernels) explicitly compiles for SM75: setup.py always emits gencode 'arch=compute_75…
- [[nvidia-com-en-us-data-center-tesla-t4-official-spec-page|nvidia.com/en-us/data-center/tesla-t4/ (official spec page, fetched 20…]] — Fraction-of-A100 context for all measured numbers: T4 peak is ~21% of one A100 on both axes, and Kaggle gives two of the…

[[Home]]
