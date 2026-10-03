---
type: project
name: TIRx Kernels
layer: kernel
status: active
repository: https://github.com/mlc-ai/TIRx-kernels
docs: https://github.com/mlc-ai/TIRx-kernels
areas:
  - "gpu-kernels"
  - "gemm"
  - "grouped-gemm"
  - "sparse-attention"
  - "flash-attention"
  - "linear-attention"
  - "moe"
  - "distributed-kernel-fusion"
  - "fp4"
  - "fp8"
hardware:
  - "nvidia"
integrations:
  - "TIRx Harness"
  - "FlashInfer"
last_verified: "2026-10"
---
# TIRx Kernels
## 项目定位

TIRx Kernels 是 MLC 面向 TIRx 的高性能 GPU kernel 组合库，也是 [[community/mlc-ai/TIRx-Harness/TIRx-Harness|TIRx Harness]] 的直接配套实现集合。它既包含 native TIRx kernel，也包含从 cuDNN Frontend、FlashAttention、[[community/flashinfer-ai/FlashInfer/FlashInfer|FlashInfer]] 等生态移植的实现。

## 当前 kernel 覆盖

官方目录已公开：

- FP16/BF16 GEMM、NVFP4 GEMM；
- all-gather + GEMM、GEMM + reduce-scatter；
- Qwen3-Next Alpha-MoE FP8；
- KDA / GDN / MSA / VSA 等 linear/recurrent attention 路径；
- DeepSeek V4 sparse MLA；
- grouped GEMM、fused MoE；
- FlashAttention forward/backward；
- block sparse / DSA sparse attention；
- FP4 / FP8 quantization 与多个 FlashInfer entry point port。

这些能力把它直接连接到 [[concept/kernel/gemm/GEMM|GEMM]] 和 [[concept/kernel/attention/Sparse Attention|Sparse Attention]]。

## 硬件边界

README 当前默认 kernel 面向 NVIDIA 新架构，明确列出 sm_100a、sm_103a、sm_107a，并有部分 +sm_110a；性能调优基准主要在 sm_100a。不能把源级 TIRx 可移植性直接等价成当前已验证的跨厂商硬件支持。

## Sources

- https://github.com/mlc-ai/TIRx-kernels
