---
type: concept
name: Weight-Activation Quantization
aliases:
  - Weight and Activation Quantization
  - W-A Quantization
  - 权重激活量化
domain: quantization
topic: quantization
parent_concepts:
  - Quantization
related_concepts:
  - Weight-Only Quantization
  - W8A8
  - FP8 Quantization
  - FP4 Quantization
projects:
  - vLLM
  - msModelSlim
  - DeepGEMM
  - TileKernels
last_verified: 2026-09
---

# Weight-Activation Quantization

## 一句话定义

Weight-Activation Quantization 同时降低权重和 activation 的表示精度，使低精度数据直接进入 GEMM / MoE kernel。

## 解决的问题

Weight-only 只能降低权重读取量；activation 仍然占用原始带宽和 tensor-core 输入精度。若硬件原生支持 INT8、FP8、FP4 等低精度计算，同时量化 W/A 可以进一步提升 GEMM throughput 并降低内存流量。

## 核心机制

除了量化权重，还要为运行时 activation 生成 scale。常见策略包括：

- static activation scale：离线 calibration。
- dynamic per-tensor / per-token scale：forward 时统计范围。
- per-block / microscaling：为局部 block 保存更细粒度 scale。

kernel 需要同时理解 weight format、activation format 和 scale layout，才能避免额外 dequant/requant 开销。

## 子概念

- [[W8A8]]：W/A 都是 8bit 的常见部署形态。
- [[FP8 Quantization]]：使用 E4M3/E5M2/MXFP8 等浮点 8bit format。
- [[FP4 Quantization]]：进一步降低到 4bit floating/microscaling 路径。

## 项目实现

[[community/vllm-project/vLLM/vLLM|vLLM]] 支持 FP8/INT8 W8A8 以及在线量化；[[community/Ascend/msModelSlim/msModelSlim|msModelSlim]] 提供 W8A8、W4A8、MXFP8/MXFP4 等量化；[[community/deepseek-ai/DeepSeek-Infra/DeepGEMM|DeepGEMM]] 提供 FP8/FP4 GEMM；[[community/deepseek-ai/DeepSeek-Infra/TileKernels|TileKernels]] 提供 FP8/FP4、per-token/per-block 等量化 kernel。

## Sources

- https://docs.vllm.ai/en/latest/features/quantization/online/
- https://gitcode.com/Ascend/msmodelslim
- https://github.com/deepseek-ai/DeepGEMM
- https://github.com/deepseek-ai/TileKernels
