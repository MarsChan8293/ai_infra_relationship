---
type: concept
name: FP4 Quantization
aliases:
  - Float4 Quantization
  - FP4
  - MXFP4
  - NVFP4
domain: quantization
topic: quantization
parent_concepts:
  - Quantization
related_concepts:
  - Weight-Activation Quantization
  - Weight-Only Quantization
  - FP8 Quantization
projects:
  - vLLM
  - msModelSlim
  - DeepGEMM
  - TileKernels
  - ggml
  - llama.cpp
last_verified: 2026-09
---

# FP4 Quantization

## 一句话定义

FP4 Quantization 使用 4bit 浮点或 microscaling 方案表示权重或 activation，把模型数据体积进一步压到 FP8 的约一半，同时依赖更细粒度 scale 来控制精度损失。

## 常见格式

- **MXFP4**：OCP microscaling FP4，通常以小 block 共享 E8M0 scale。
- **NVFP4**：NVIDIA FP4/microscaling 路径，具体 block/scale 规则与 MXFP4 不完全相同。

因此“FP4”不是一个单一 binary layout，模型 checkpoint 与 kernel backend 必须匹配。

## Weight-only 与 W-A

FP4 可以只用于权重，也可以让 activation 进入 FP4/MXFP4 compute。前者更接近 [[Weight-Only Quantization]]，后者属于 [[Weight-Activation Quantization]]。不能只看到“FP4 model”就假定 activation 也是 4bit。

## 为什么更难

4bit 的动态范围和精度都更紧张，outlier、scale granularity 和 block layout 对误差更敏感；同时硬件是否有原生 FP4 tensor-core 路径会决定它是真正的低精度计算，还是需要额外 unpack/dequant。

## 项目实现

[[community/vllm-project/vLLM/vLLM|vLLM]] 当前支持 MXFP4 等在线/预量化路径；[[community/Ascend/msModelSlim/msModelSlim|msModelSlim]] 提供 MXFP4/W4A8 等实践；[[community/deepseek-ai/DeepSeek-Infra/DeepGEMM|DeepGEMM]] 提供 FP4/Mega-MoE kernel；[[community/deepseek-ai/DeepSeek-Infra/TileKernels|TileKernels]] 提供 FP4 quantization kernel；[[community/ggml-org/ggml/ggml|ggml]] / [[community/ggml-org/llama.cpp/llama.cpp|llama.cpp]] 生态也支持 MXFP4 等低比特 tensor encoding。

## Sources

- https://docs.vllm.ai/en/latest/features/quantization/online/
- https://gitcode.com/Ascend/msmodelslim
- https://github.com/deepseek-ai/DeepGEMM
- https://github.com/deepseek-ai/TileKernels
- https://github.com/ggml-org/llama.cpp
