---
kb_id: "title:github com state spaces mamba setup py raw main branch fetched 2026 07 04 local build attempt blocked by nvcc 11 5 11 6"
type: "source"
title: "github.com/state-spaces/mamba setup.py (raw, main branch, fetched 2026…"
doi: null
hf_repo: null
year: null
topics: ["hardware-gate"]
claims: 1
uncertain_claims: 1
verdicts: []
aliases: ["title:github com state spaces mamba setup py raw main branch fetched 2026 07 04 local build attempt blocked by nvcc 11 5 11 6"]
tags: ["source", "topic/hardware-gate"]
---
# github.com/state-spaces/mamba setup.py (raw, main branch, fetched 2026…

**Topics:** [[hardware-gate]]

## Source URLs
- github.com/state-spaces/mamba setup.py (raw, main branch, fetched 2026-07-04)
- local build attempt blocked by nvcc 11.5 < 11.6

## Findings

> [!warning] UNCERTAIN — hardware-gate
> state-spaces/mamba (mamba-ssm CUDA kernels) explicitly compiles for SM75: setup.py always emits gencode 'arch=compute_75,code=sm_75' (lowest targeted arch), minimum CUDA 11.6. So it installs/builds for T4; we could NOT execute its CUDA selective-scan locally (local nvcc is 11.5, no prebuilt wheel for torch 2.11+cu130), so runtime behavior of the mamba-ssm CUDA path on SM75 is inferred from build targets plus our passing fla-Triton Mamba2, not directly observed. Flag: transferable-untested.
>
> **Numbers:** gencode targets: sm_75 (always), sm_80, sm_87; +sm_90 (CUDA>=11.8), +sm_100/sm_120 (CUDA>=12.8), +sm_103/sm_110/sm_121 (CUDA>=13.0); min CUDA 11.6
> **Relevance:** If the panel picks a Falcon-H1/Zamba2-style Mamba-2 component, the reference CUDA kernels are installable on Kaggle (nvcc 12.x present); but a 10-40 min source build or a matching prebuilt wheel must be planned, and the fla Triton path is the tested fallback.
> **Source:** github.com/state-spaces/mamba setup.py (raw, main branch, fetched 2026-07-04); local build attempt blocked by nvcc 11.5 < 11.6 · **Sweep:** `slm-arch-for-kazakh`

## Related
- [[ggml-org-llama-cpp-deepwiki-supported-model-architectures|ggml-org/llama.cpp DeepWiki 'Supported Model Architectures']] — Both track Mamba deployability; node confirms mamba-ssm CUDA builds for sm_75, complementing llama.cpp Mamba GGUF support

[[Home]]
