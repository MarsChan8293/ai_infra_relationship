---
type: project
name: TensorRT Edge-LLM
layer: inference-engine
status: active
code_availability: public
repository: https://github.com/NVIDIA/TensorRT-Edge-LLM
docs: https://nvidia.github.io/TensorRT-Edge-LLM/
areas:
  - edge-inference
  - llm-inference
  - multimodal-inference
  - cpp-runtime
  - nvfp4
  - speculative-decoding
hardware:
  - nvidia
integrations:
  - "TensorRT"
  - "Model Optimizer"
companies:
  - NVIDIA
last_verified: "2026-10"
---

# TensorRT Edge-LLM

## 项目简介
TensorRT Edge-LLM 是 NVIDIA 针对 Jetson、DRIVE 和 DGX Spark 的端侧 LLM/VLM/音视频等模型推理框架，采用导出/构建流程加 **C++ Runtime**。README 说明主流路径是将 Hugging Face Checkpoint 导出到 ONNX 后构建 TensorRT 引擎，也提供不经 ONNX 的实验性 Direct Engine Builder。

## 核心技术
- C++ 推理执行，强调有限设备显存、低延迟和本地多模态应用。
- 支持 KV Cache 复用、量化、推测解码；实验性 In-flight Batching、OpenAI 兼容服务由版本/配置决定。
- 以官方 Support Matrix 校验 JetPack/DriveOS/CUDA/TensorRT、设备和具体 Model Checkpoint，不应由 Blackwell 代际推断任意 RTX PRO 5000 SKU 已经在矩阵内。
- 官方 2026-09 版本说明提供 **双 DGX Spark 实验性 TP2**，并不意味着同机 TP8 适配。

## 研究价值
与 [[community/NVIDIA/Flare/Flare|Flare]] 的“Python 准备+Rust 原生 Serving”相比，Edge-LLM 侧重 TensorRT Engine Builder 与 C++ Runtime；与 [[TensorRT-LLM]] 相比，更聚焦边缘平台的资源与软件版本约束。适合在 DGX Spark 上做 TTFT/TPOT、显存峰值、模型导出与冷启动成本对比。

## 关联
- [[TensorRT]]：直接引擎构建/执行依赖。
- [[community/NVIDIA/Model-Optimizer/Model-Optimizer|Model Optimizer]]：量化与导出链路参考，实际 Checkpoint 需具体验证。
- [[TensorRT-LLM]]、[[community/NVIDIA/Flare/Flare|Flare]]：技术路线对照，**不是直接依赖或互换运行时**。

## Sources
- https://github.com/NVIDIA/TensorRT-Edge-LLM
- https://nvidia.github.io/TensorRT-Edge-LLM/latest/user_guide/getting_started/support-matrix.html
- https://nvidia.github.io/TensorRT-Edge-LLM/latest/developer_guide/software-design/cpp-runtime-overview.html
