---
type: project
name: TensorRT
layer: runtime
status: active
code_availability: public
repository: https://github.com/NVIDIA/TensorRT
docs: https://docs.nvidia.com/deeplearning/tensorrt/latest/
areas:
  - inference-compiler
  - engine-builder
  - onnx-parser
  - plugin-runtime
  - quantization
hardware:
  - nvidia
companies:
  - NVIDIA
last_verified: "2026-10"
---

# TensorRT

## 项目简介
TensorRT 是 NVIDIA 通用神经网络推理优化和执行平台，提供 Engine 构建/执行、层融合、图优化、算子插件及低精度推理能力，面向视觉、语音、Transformer 等模型。

## 开源边界
GitHub 仓库为 **TensorRT-OSS**，包括插件、ONNX Parser、示例等公开源代码，官方明确写明这只是 TensorRT GA SDK 的**部分开源组件**，不能将此 GitHub 仓库误当作完整开源 Runtime。SDK 版本、CUDA/Driver、Plugin ABI 需要匹配。

## 技术定位
- [[TensorRT-LLM]]：基于 NVIDIA 推理栈的 LLM 专用能力，独立项目。
- [[TensorRT-RTX]]：面向 RTX 设备的小型 TensorRT SDK，提供运行时 JIT 优化。
- [[TensorRT Edge-LLM]]：利用 TensorRT Builder 和 Runtime 面向 Jetson/DRIVE/DGX Spark。
- [[Torch-TensorRT]]：从 PyTorch 进入 TensorRT 编译/部署的路径。
与 vLLM/SGLang 的 Token Scheduling、KV Cache 和多租户服务抽象不是同一层。

## Sources
- https://github.com/NVIDIA/TensorRT
- https://github.com/NVIDIA/TensorRT/blob/main/README.md
- https://docs.nvidia.com/deeplearning/tensorrt/latest/
