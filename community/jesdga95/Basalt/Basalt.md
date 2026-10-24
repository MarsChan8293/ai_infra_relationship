---
type: project
name: "Basalt"
layer: inference-engine
status: active
code_availability: public
repository: https://github.com/jesdga95/basalt
areas:
  - blackwell-sm120
  - moe-expert-offload
  - nvidia-cuda
  - low-vram-inference
  - cpu-gpu-hybrid
hardware:
  - nvidia
integrations: []
companies: []
company_relation: community-led
last_verified: "2026-10"
---

# Basalt

## 项目简介
Basalt 是针对 Qwen3.8 Flash-Next 等目标的 SM120 本地推理 Runtime，支持 GPU 显存不足时从主机 RAM 流式访问 MoE Expert，Linux 下可使用第二 GPU 作为 Expert 层。

## 硬件兼容性与证据层级
- **NVIDIA Blackwell SM120**：官方系统矩阵明确要求 SM120 + CUDA 13，Linux x86-64/Windows x64 均提供构建路径。
- **RTX PRO 6000（SM120）**：硬件架构满足官方目标，但尚未发现针对该具体 96GB SKU 的独立实测；标记为「架构兼容、待实测」，**不标记已验证**。
- **DGX Spark（SM121 / ARM64）**：不在现有 x86-64 / SM120 支持矩阵中。
- Windows 目前仅单 GPU，Linux 可选第二张 GPU 作 Expert Tier。

## 核心技术与部署意义
- 将 Expert 作为显存/主存/可选第二 GPU 的分层对象，与显存常驻策略形成对照。
- 主要运行效能取决于实际 PCIe 带宽、Host RAM、请求路由热度与上下文配置。

## 关系与对比
[[community/JustVugg/Colibri/Colibri|Colibri]]、[[community/gpillon/Ignis/Ignis|Ignis]] 为 Expert Streaming 和低显存运行技术路线对照。

## 来源
- https://github.com/jesdga95/basalt
- https://github.com/jesdga95/basalt/blob/HEAD/README.md
