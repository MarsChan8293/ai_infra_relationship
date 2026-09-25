---
type: project
name: FlashAttention
linked_people: []
linked_concepts:
  - "concept/kernel/attention/Attention Kernel"
  - "concept/kernel/attention/FlashAttention"
layer: runtime
status: active
repository: https://github.com/Dao-AILab/flash-attention
docs: https://github.com/Dao-AILab/flash-attention
areas:
  - "exact-attention"
  - "io-aware-attention"
  - "memory-efficient-attention"
hardware:
  - "nvidia"
  - "amd"
integrations:
last_verified: "2026-09"
linked_companies: []
---
# FlashAttention

> 面向 Transformer 的 IO-aware、内存高效 exact attention kernel 实现。

## 核心能力

| 能力 | 说明 |
|---|---|
| IO-aware Attention | 减少 HBM 与片上存储之间的数据搬运 |
| Exact Attention | 保持精确 attention 语义而非近似算法 |
| GPU Kernel | 围绕不同 GPU 架构持续优化 |
| 生态基准 | 成为推理与训练框架 attention 优化的重要参照 |

## 边界

FlashAttention 是 attention kernel 项目，不是完整 inference engine；KV 管理、请求调度和 serving API 由上层系统承担。

## 集成与后端

本页将上层框架使用关系记录为“关联”，不自动视作稳定项目级集成。

## 关联项目

- 上层推理：vLLM、SGLang。
- Attention 对照：FlashInfer、FlashMLA、FlagAttention。
- Kernel 编译：Triton。

## 版本快照

本页不绑定单一 release 或 commit；能力判断以 2026-09-15 前官方仓库为快照。

## 直接来源

- https://github.com/Dao-AILab/flash-attention

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/kernel/attention/Attention Kernel|Attention Kernel]]
- [[concept/kernel/attention/FlashAttention|FlashAttention]]

<!-- END AUTO PROJECT CONCEPTS -->
