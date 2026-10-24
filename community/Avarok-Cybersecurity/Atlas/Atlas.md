---
type: project
name: Atlas
layer: inference-engine
status: active
code_availability: public
repository: https://github.com/Avarok-Cybersecurity/atlas
areas:
  - rust-runtime
  - dedicated-inference-engine
  - dgx-spark
  - nvfp4
  - fp8
  - agent-serving
  - prefix-cache
  - expert-parallel
hardware:
  - nvidia
integrations: []
companies: []
company_relation: community-led
last_verified: "2026-10"
---

# Atlas

## 项目简介
Atlas 是 Rust + CUDA 原生推理 Runtime，采用 `(hardware, model, quant)` 元组组织专用编译和 Kernel，支持 KV/状态管理、MTP/DFlash 与前缀缓存。

## 硬件兼容性与证据层级
- **DGX Spark GB10 / SM121：官方验证平台**，提供镜像、模型配置与并发测试。
- 另有 **H100/H200 SM90a、B200/GB200 SM100a** 等目标；AMD Strix Halo/Metal 路线以对应实现或构建能力为准。
- **RTX PRO 6000 / SM120：并非现成目标**；上游 `docs/HARDWARE.md` 明确说明新增 `sm_120` 需要新的 hardware target 和 Kernel 验证。

## 核心技术与部署意义
- Kernel/Model/Quant 静态映射、精确分配优化工作到硬件模型组合。
- Rust Serving、推测解码、prefix-cache 和多节点 Expert Parallel；上游 Benchmark 为作者实验，仍需外部复测。

## 关系与对比
[[community/Metrale/Metrale-Engine/Metrale-Engine|Metrale Engine]]、[[community/NVIDIA/Flare/Flare|Flare]] 提供专用 Runtime 架构对比。

## 来源
- https://github.com/Avarok-Cybersecurity/atlas
- https://github.com/Avarok-Cybersecurity/atlas/blob/HEAD/README.md
