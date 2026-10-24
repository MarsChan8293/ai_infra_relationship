---
type: project
name: TensorRT-RTX
layer: runtime
status: active
code_availability: public
repository: https://github.com/NVIDIA/TensorRT-RTX
docs: https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/index.html
areas:
  - rtx-inference
  - jit-optimization
  - engine-portability
  - model-deployment
hardware:
  - nvidia
integrations:
  - "TensorRT"
companies:
  - NVIDIA
last_verified: "2026-10"
---

# TensorRT-RTX

## 项目简介
TensorRT-RTX（TensorRT for RTX）针对 RTX 台式机、笔记本和工作站提供更紧凑的 TensorRT 推理 SDK，侧重模型 Engine 在终端用户 RTX 设备上的 **JIT 优化和快速部署**。

## 核心设计
- README 描述支持 Turing 到 Blackwell 代的 RTX GPU，利用 Runtime JIT 优化减少预编译和跨设备部署负担。
- 官方介绍重点覆盖图像、语音、生成式模型等，不等于专为大模型 KV/Scheduler 构建的完整 LLM Serving。
- 当前仓库主要开源 SDK 配套组件和 samples/demos；不能将其视作完整 Runtime 开源。
- 对 RTX PRO 5000 可关注设备兼容、JIT 编译成本、单模型算子效果和推理模型交付，而不是直接作为 TP8 的替换方案。

## 关联
- [[TensorRT]]：同源 TensorRT SDK 生态，侧重不同部署端。
- [[TensorRT-LLM]]、[[community/NVIDIA/Flare/Flare|Flare]]：可对比不同运行时的 Engine 准备与执行边界，但不是直接集成。

## Sources
- https://github.com/NVIDIA/TensorRT-RTX
- https://docs.nvidia.com/deeplearning/tensorrt-rtx/latest/index.html
