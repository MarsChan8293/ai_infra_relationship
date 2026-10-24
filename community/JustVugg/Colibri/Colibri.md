---
type: project
name: Colibri
layer: inference-engine
status: active
code_availability: public
repository: https://github.com/JustVugg/colibri
areas:
  - local-inference
  - moe-expert-offload
  - ssd-streaming
  - cpu-gpu-hybrid
  - dgx-spark
hardware:
  - nvidia
integrations: []
companies: []
company_relation: community-led
last_verified: "2026-10"
---

# Colibri

## 项目简介
纯 C 的本地 MoE/LLM 推理引擎，以小内存运行超大模型为目标，采用 CPU RAM / SSD Expert 流式加载，也提供 NVIDIA CUDA 与 Vulkan 加速路径。

## 硬件兼容性与证据层级
- **DGX Spark GB10 / SM121**：仓库包含 GB10 统一内存预算修复、ARM NEON 和 CUDA 路径；可视为明确适配/优化目标，实际每个模型和量化组合仍需分别验收。
- **RTX PRO 6000 / SM120**：通用 NVIDIA CUDA 路径具移植基础，但未在仓库证据中确认该具体 SKU 端到端性能验证。

## 核心技术与部署意义
- CPU RAM 与 SSD 是 MoE Expert 的容量层级，按模型路由需求加载；与全权重常驻显存的高吞吐 Serving 目标不同。
- 支持 CPU-only、Linux NVIDIA CUDA、Vulkan GPU；在 GB10 统一内存上须防止将共享 RAM 错当离散 VRAM 重复计算。

## 关系与对比
[[llama.cpp]]、[[community/antirez/ds4/ds4|ds4]]、[[community/jesdga95/Basalt/Basalt|Basalt]] 为技术路线对照，**不意味着直接依赖**。

## 来源
- https://github.com/JustVugg/colibri
- https://github.com/JustVugg/colibri/blob/HEAD/README.md
