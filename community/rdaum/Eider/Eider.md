---
type: project
name: Eider
layer: inference-engine
status: active
code_availability: public
repository: https://github.com/rdaum/eider
areas:
  - dgx-spark
  - rust-runtime
  - cuda-kernel
  - nvfp4
  - low-footprint
  - decision-inference
hardware:
  - nvidia
integrations: []
companies: []
company_relation: community-led
last_verified: "2026-10"
---

# Eider

## 项目简介
Eider 是为 DGX Spark 构建的 Rust + CUDA/cuBLASLt 原生推理服务器，不依赖 PyTorch、vLLM 或 llama.cpp 的在线运行时。

## 硬件兼容性与证据层级
- **DGX Spark（GB10 / SM121）：明确目标及作者实测平台**，支持 NVFP4/混合精度模型。
- **RTX PRO 6000 / SM120**：无对应编译/部署支持的证据，不标记为支持。

## 核心技术与部署意义
- GB10 NVFP4 Kernel 试验，强调启动轻量和专用模型路径。
- 本地决策/路由模型支持；Qwen3.8 Flash Next 等实测数字以作者条件为准。

## 关系与对比
[[community/Avarok-Cybersecurity/Atlas/Atlas|Atlas]]、[[community/Metrale/Metrale-Engine/Metrale-Engine|Metrale Engine]] 为 Rust 原生 Runtime 对照。

## 来源
- https://github.com/rdaum/eider
- https://github.com/rdaum/eider/blob/HEAD/README.md
