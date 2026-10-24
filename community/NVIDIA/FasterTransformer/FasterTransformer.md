---
type: project
name: FasterTransformer
layer: inference-engine
status: deprecated
code_availability: public
repository: https://github.com/NVIDIA/FasterTransformer
docs: https://github.com/NVIDIA/FasterTransformer
areas:
  - transformer-inference
  - cuda-kernels
  - legacy-inference-engine
hardware:
  - nvidia
companies:
  - NVIDIA
last_verified: "2026-10"
---

# FasterTransformer

## 项目简介
FasterTransformer 是 NVIDIA 早期基于 CUDA/cuBLAS 等实现的高性能 Transformer Encoder/Decoder 推理方案，是 NVIDIA LLM Runtime 的历史技术路线。

## 生命周期
官方 README 明确提示 **后续开发已转向 [[TensorRT-LLM]]，FasterTransformer 将不再继续开发**。这里的 `status: deprecated` 表示它作为新系统选型已被上游后继方案取代，仓库仍保留公开代码，不等于源码被删除。

## 研究价值
用于回顾 Transformer 层融合、早期 Decoder Kernel 和 C++/CUDA Runtime 设计；对于 RTX PRO 5000/Blackwell、NVFP4 和长上下文服务，不推荐以其作为新部署基座。

## 关联
- [[TensorRT-LLM]]：官方指定的后续发展项目。
- [[TensorRT]]：同属 NVIDIA CUDA 推理生态，但职责/版本演进各异。

## Sources
- https://github.com/NVIDIA/FasterTransformer
- https://github.com/NVIDIA/FasterTransformer/blob/main/README.md
