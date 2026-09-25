---
type: concept
name: Kernel Fusion
aliases:
  - Operator Fusion
  - Fused Kernel
  - 算子融合
domain: kernel
topic: optimization
related_concepts:
  - Attention Kernel
  - GEMM
  - Grouped GEMM
  - Kernel DSL
projects:
  - DeepGEMM
  - FlashInfer
  - TileKernels
  - FlagGems
last_verified: 2026-09
---

# Kernel Fusion

## 一句话定义

Kernel Fusion 把原本需要多个 kernel 依次执行的算子组合进一个更大的 kernel，减少中间结果写回显存、kernel launch 和同步开销。

## 解决的问题

LLM 推理里很多热点不是单个大 GEMM，而是“GEMM + bias + activation + quantization”“attention + mask + softmax”“MoE routing + expand/reduce”等连续数据流。若每一步都单独 launch kernel，中间 tensor 会反复经过 HBM，Decode 小 batch 时 launch overhead 也会更加明显。

## 核心机制

融合后的 kernel 让中间值尽可能停留在 register / shared memory / SRAM，只在真正需要时写回 HBM。常见融合位置包括：

- GEMM epilogue：bias、scale、activation、quant/dequant。
- Attention：mask、scale、softmax、RoPE 或其他轻量变换。
- MoE：routing、token expand/reduce、activation、quantization。
- Norm / activation：RMSNorm、SwiGLU、residual 等组合路径。

## 收益与代价

收益来自更少的 memory traffic、launch 和同步；代价是 kernel 更复杂、寄存器/共享内存压力更高，并可能降低 shape / backend 复用性。过度融合会导致 occupancy 下降或编译搜索空间爆炸。

## 与编译器的关系

[[Kernel DSL]] 和 [[JIT Kernel Compilation]] 让融合 kernel 更容易针对具体 shape、dtype 和硬件动态生成。Fusion 是优化目标，DSL/JIT 是实现手段之一，两者不应混成同一个概念。

## 项目实现

[[community/deepseek-ai/DeepSeek-Infra/DeepGEMM|DeepGEMM]] 覆盖 fused MoE / epilogue 等路径；[[community/flashinfer-ai/FlashInfer/FlashInfer|FlashInfer]] 提供多类 fused serving kernels；[[community/deepseek-ai/DeepSeek-Infra/TileKernels|TileKernels]] 明确包含 fused expansion/reduction、SwiGLU + quantization 等 kernel；[[community/flagos-ai/FlagGems/FlagGems|FlagGems]] 提供面向多后端的大量融合/高性能算子实现。

## Sources

- https://github.com/deepseek-ai/DeepGEMM
- https://docs.flashinfer.ai/
- https://github.com/deepseek-ai/TileKernels
- https://github.com/flagos-ai/FlagGems
