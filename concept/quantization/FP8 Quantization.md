---
type: concept
name: FP8 Quantization
aliases:
  - Float8 Quantization
  - FP8
  - E4M3
  - E5M2
  - MXFP8
domain: quantization
topic: quantization
parent_concepts:
  - Quantization
related_concepts:
  - W8A8
  - Weight-Activation Quantization
  - Weight-Only Quantization
  - KV Cache Quantization
projects:
  - vLLM
  - msModelSlim
  - DeepGEMM
  - TileKernels
last_verified: 2026-09
---

# FP8 Quantization

## 一句话定义

FP8 Quantization 使用 8bit 浮点格式表示权重、activation 或 KV Cache，在保留浮点动态范围特性的同时降低存储和计算成本。

## 常见格式

- **E4M3**：指数位较少、尾数更多，精度更高但动态范围较小。
- **E5M2**：动态范围更大，但有效精度更低。
- **MXFP8**：使用 microscaling，把一小组数值与共享 scale 组合起来。

“FP8”本身不说明是 weight-only、W8A8 还是 KV cache，因此部署时必须同时说明作用对象和 scale granularity。

## 典型路径

- FP8 W8A8：权重 + activation 都是 FP8，见 [[W8A8]]。
- FP8 W8A16：只把权重降为 FP8，属于 [[Weight-Only Quantization]]。
- FP8 KV：把 K/V cache 存储为 FP8，属于 [[KV Cache Quantization]]。

## scale 粒度

常见有 per-tensor、per-token、per-channel、per-block 和 per-attention-head。粒度越细通常越容易保住精度，但 scale metadata、kernel complexity 和 conversion overhead 也会增加。

## 项目实现

[[community/vllm-project/vLLM/vLLM|vLLM]] 支持 FP8 W8A8、W8A16、online quantization 和 FP8 KV Cache；[[community/Ascend/msModelSlim/msModelSlim|msModelSlim]] 提供 W8A8/MXFP8 等量化；[[community/deepseek-ai/DeepSeek-Infra/DeepGEMM|DeepGEMM]] 提供 FP8 GEMM/MoE kernel；[[community/deepseek-ai/DeepSeek-Infra/TileKernels|TileKernels]] 覆盖 per-token/per-block FP8 quantization kernel。

## Sources

- https://docs.vllm.ai/en/latest/features/quantization/llm_compressor/fp8/
- https://docs.vllm.ai/en/latest/features/quantization/online/
- https://gitcode.com/Ascend/msmodelslim
- https://github.com/deepseek-ai/DeepGEMM
- https://github.com/deepseek-ai/TileKernels
