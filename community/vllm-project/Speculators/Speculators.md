---
type: project
name: Speculators
linked_people: []
linked_concepts:
  - "concept/inference/decoding/Speculative Decoding"
layer: training
open_source: true
repository: https://github.com/vllm-project/speculators
areas: ["speculative-decoding", "online-training", "hidden-state-transfer", "vllm", "distributed-training", "speculative-decoding-training"]
governance: vLLM Project ecosystem
last_verified: "2026-09"
linked_companies: []
code_availability: public
---
# Speculators

## 项目简介
Speculators 是 vLLM Project 生态中的 speculative decoding draft-model training framework，覆盖 hidden-state 生成、draft model 训练与直接部署到 vLLM 的端到端路径。

## Mooncake 关系
2026 年 Speculators 引入 `hs_connectors` 多节点在线训练插件。官方 README 明确说明 Mooncake backend 用 distributed store 在 vLLM inference workers 与 trainer 之间跨节点传输 hidden states，使在线 speculative-model training 不依赖共享文件系统。

这条边把 [[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] 从 KV cache / serving data plane 延伸到了 speculative decoding 的训练数据平面。

## Sources
- https://github.com/vllm-project/speculators
- https://github.com/kvcache-ai/Mooncake

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/inference/decoding/Speculative Decoding|Speculative Decoding]]

<!-- END AUTO PROJECT CONCEPTS -->
