---
type: project
name: "Ignis"
layer: inference-engine
status: active
code_availability: public
repository: https://github.com/gpillon/ignis
areas:
  - rtx-pro-6000
  - blackwell-sm120
  - agent-serving
  - rust-runtime
  - nvfp4
  - moe-expert-offload
  - low-latency
hardware:
  - nvidia
integrations: []
companies: []
company_relation: community-led
last_verified: "2026-10"
---

# Ignis

## 项目简介
Ignis 是 Rust Core + C++/CUDA GPU Execution 的单卡、模型专用、面向 Agent 负载的推理服务，支持 Qwen3.8 Dense/Flash-Next 等目标及 OpenAI API。

## 硬件兼容性与证据层级
- **RTX PRO 6000 Blackwell 96GB（SM120a）**：官方支持，并提供 `rtxpro6000` 配置与实测报告。
- **RTX 5090（SM120a）**：主要作者实验平台。
- **DGX Spark / GB10（SM121）**：上游明确不以 Spark 作为当前执行目标，不能认为 Blackwell 全家族通用。
- **RTX PRO 5000 72GB（SM120）**：同架构系列但无本轮证实的具体 SKU 验证。

## 核心技术与部署意义
- 以少量 Resident Decode Lanes、Paged KV、Speculation 及低比特 Expert Cache 适应单机 Agent 请求。
- 性能表的 RTX 5090 测试与 6000 Profile 需分别记录，不能推定 PCIe/DRAM/显存容量改变不会影响性能。

## 关系与对比
[[community/Neroued/NInfer/NInfer|NInfer]]、[[community/jesdga95/Basalt/Basalt|Basalt]] 和 [[community/NVIDIA/Flare/Flare|Flare]] 为专用引擎技术对照。

## 来源
- https://github.com/gpillon/ignis
- https://github.com/gpillon/ignis/blob/HEAD/README.md
