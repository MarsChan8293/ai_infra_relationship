---
type: project
name: HPC-Ops
companies: ["腾讯"]
company_relation: company-led
layer: kernel
open_source: true
repository: https://github.com/Tencent/hpc-ops
areas: [llm-inference, kernels, attention, moe, gemm, communication, sampling, quantization]
hardware: [NVIDIA H20, SM90]
last_verified: "2026-09"
---
# HPC-Ops

## 项目简介
HPC-Ops 是腾讯混元 AI Infra 团队开发的高性能 LLM 推理算子库，官方 README 明确将其定位为 production-grade operator library，覆盖 Attention、MoE、GEMM、sampling、normalization 与通信计算融合等在线推理热点路径。

## AI Infra 位置
- dynamic decode attention 与 paged KV cache
- FP8 block-sparse prefill attention
- FP8 grouped GEMM / fused MoE
- AllReduce + Residual + RMSNorm 融合
- fused sampler
- 面向 vLLM、SGLang、FlashInfer、TensorRT-LLM 等框架的对比与集成

## 组织关系
[[company/腾讯/腾讯|腾讯]]：官方 README 直接写明项目由 Tencent Hunyuan AI Infra team 开发，并用于腾讯大规模生产推理场景，因此这里可以建立公司级直接项目关系，而不是从单个员工贡献反推。

## Sources
- https://github.com/Tencent/hpc-ops
- https://github.com/Tencent/hpc-ops/blob/main/README.md
