---
type: project
name: Edge0
linked_people: []
linked_concepts:
  - "concept/memory/SSD-NVMe Tier"
layer: inference-engine
status: active
repository: https://github.com/Edge0-AI/Edge0
docs: https://github.com/Edge0-AI/Edge0
areas:
  - "moe-inference"
  - "ssd-expert-offload"
  - "expert-streaming"
  - "routing-prediction"
  - "int4"
  - "lora"
  - "edge-inference"
  - "local-inference"
hardware:
  - "apple-silicon"
last_verified: "2026-10"
linked_companies: []
---
# Edge0
## 项目定位

Edge0 是面向 consumer / edge hardware 的 streaming MoE inference framework。其核心不是把完整 MoE 权重常驻内存，而是把 expert weight 放在 SSD 上按需 streaming，并用训练得到的 prerouter 提前预测下一步 expert，从而把 I/O 与 forward overlap。

## 核心机制

- **SSD expert offload**：只让 active expert set 占用峰值内存，完整 expert 权重保留在存储层。
- **Prerouter**：提前一步预测 expert routing，用于隐藏 storage latency。
- **Recover-LoRA**：冻结 int4 base，用 distillation 训练 LoRA adapter 恢复量化质量；base 不 merge，可共享多个 adapter。
- Python/MLX 路径当前明确支持 Apple Silicon；仓库还在 2026-09-30 开源 macOS、iOS、Android、Windows 平台 engine，统一 access layer 仍在 roadmap。

## 与内存层次的关系

Edge0 是 [[concept/memory/SSD-NVMe Tier|SSD/NVMe Tier]] 不只服务 KV cache、也服务 model/expert state 的典型例子。它与 [[university/UC Berkeley/MoE-Lightning|MoE-Lightning]] 等 CPU/GPU offload 路线关注点不同：Edge0 把 SSD I/O 和 routing prediction 直接纳入 sparse-MoE decode critical path。

## 当前边界

README 的 CUDA backend 仍是 reserved slot；不能因为 Windows/Vulkan 或多平台源码已开放，就推断所有 GPU vendor 均有等价优化能力。当前最明确、性能数据最完整的是 Apple Silicon / MLX 路径。

## Sources

- https://github.com/Edge0-AI/Edge0
- https://arxiv.org/abs/2609.18063

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/memory/SSD-NVMe Tier|SSD/NVMe Tier]]

<!-- END AUTO PROJECT CONCEPTS -->
