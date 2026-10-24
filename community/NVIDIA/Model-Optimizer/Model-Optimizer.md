---
type: project
name: Model Optimizer
layer: optimization
status: active
code_availability: public
repository: https://github.com/NVIDIA/Model-Optimizer
docs: https://nvidia.github.io/Model-Optimizer/
areas:
  - nvfp4-quantization
  - fp8-quantization
  - ptq
  - qat
  - pruning
  - distillation
  - speculative-decoding
  - mixed-precision-kv
hardware:
  - nvidia
integrations:
  - "TensorRT-LLM"
  - "TensorRT"
  - "vLLM"
  - "SGLang"
companies:
  - NVIDIA
last_verified: "2026-10"
---

# Model Optimizer

## 项目简介
NVIDIA Model Optimizer（ModelOpt，早期名称 TensorRT Model Optimizer）为 PyTorch/Hugging Face/ONNX 模型提供量化、剪枝、蒸馏、稀疏化及推测解码相关模型优化工具，导出用于下游推理引擎的 Checkpoint。

## 技术能力
- PTQ、QAD/QAT、NVFP4/FP8、混合精度权重量化和模型优化。
- README 在 2026-10 公开介绍 **AutoQuant KV** 逐层混合精度 KV Cache 量化搜索方向；需要分清研究/工具功能与特定 vLLM/LLM 模型已可用的 Backend。
- 支持向 [[TensorRT-LLM]]、[[TensorRT]]、[[vLLM]]、[[SGLang]] 等下游执行引擎输出可适配的模型资产；实际支持依赖格式和版本。

## 在 AI Infra 中的层级
ModelOpt **不是 Runtime 或 Serving Engine**。它改变模型权重与执行所需的量化/结构表示，后续仍由 TensorRT-LLM、vLLM、SGLang 等执行。最适合纳入同模型、同精度对比实验中的模型准备链。

## Sources
- https://github.com/NVIDIA/Model-Optimizer
- https://nvidia.github.io/Model-Optimizer/
- https://github.com/NVIDIA/Model-Optimizer/blob/main/README.md
