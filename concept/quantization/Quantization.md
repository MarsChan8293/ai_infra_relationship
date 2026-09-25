---
type: concept
name: Quantization
aliases:
  - Model Quantization
  - LLM Quantization
  - 模型量化
domain: quantization
topic: quantization
related_concepts:
  - Weight-Only Quantization
  - Weight-Activation Quantization
  - KV Cache Quantization
projects:
  - vLLM
  - msModelSlim
  - QFactory
  - ggml
  - llama.cpp
  - LMDeploy
  - DeepGEMM
  - TileKernels
last_verified: 2026-09
---

# Quantization

## 一句话定义

Quantization 用更低精度的数据类型或编码表示模型权重、激活、KV Cache 等状态，以降低内存占用、带宽压力和计算成本。

## 解决的问题

LLM 推理通常同时受显存容量、HBM 带宽和矩阵乘吞吐约束。把 FP16/BF16 降到 INT8、INT4、FP8、FP4 等格式可以减少数据体积，并在支持低精度 tensor core / vector instruction 的硬件上提升吞吐。

## 三条主要量化路径

- [[Weight-Only Quantization]]：只压缩权重，activation 保持较高精度。
- [[Weight-Activation Quantization]]：权重和 activation 都进入低精度计算。
- [[KV Cache Quantization]]：只改变 attention KV 状态的存储/计算精度。

这三者可以组合，但优化目标不同，不能简单用“4bit/8bit”一词替代。

## 核心设计维度

量化方案通常还需要选择：

- 数据格式：INT / FP / microscaling。
- scale 粒度：per-tensor、per-channel、per-token、per-group、per-block。
- symmetric / asymmetric。
- static calibration / dynamic quantization。
- 哪些层保留高精度。
- kernel 是否能直接消费该格式，还是必须先 dequant。

## 项目实现

[[community/Ascend/msModelSlim/msModelSlim|msModelSlim]] 提供昇腾模型量化工具链；[[community/thu-pacman/QFactory/QFactory|QFactory]] 研究 quantized serving kernel generation；[[community/ggml-org/ggml/ggml|ggml]] / [[community/ggml-org/llama.cpp/llama.cpp|llama.cpp]] 提供多种低比特 tensor encoding；[[community/InternLM/LMDeploy/LMDeploy|LMDeploy]] 覆盖 weight-only / KV 等量化；[[community/vllm-project/vLLM/vLLM|vLLM]] 支持 FP8、INT8/INT4、AWQ/GPTQ、KV quantization 等运行时；[[community/deepseek-ai/DeepSeek-Infra/DeepGEMM|DeepGEMM]] 与 [[community/deepseek-ai/DeepSeek-Infra/TileKernels|TileKernels]] 提供低精度 kernel。

## Sources

- https://docs.vllm.ai/en/stable/features/quantization/
- https://gitcode.com/Ascend/msmodelslim
- https://github.com/ggml-org/llama.cpp
- https://github.com/InternLM/lmdeploy
- https://github.com/deepseek-ai/DeepGEMM
- https://github.com/deepseek-ai/TileKernels
