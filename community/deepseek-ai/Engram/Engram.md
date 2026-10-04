---
type: project
name: Engram
linked_concepts:
  - "concept/memory/Conditional Memory"
  - "concept/memory/Host Memory"
status: active
linked_people: []
repository: https://github.com/deepseek-ai/Engram
docs: https://github.com/deepseek-ai/Engram
last_verified: "2026-10"
companies: ["深度求索"]
layer: other
areas:
  - "conditional-memory"
  - "ngram-lookup"
  - "static-memory"
  - "host-memory-offload"
  - "model-system-codesign"
integrations: []
linked_companies:
  - "company/深度求索/深度求索"
code_availability: public
---
# Engram

## 项目简介
Engram 是 DeepSeek 2026 年公开的 Conditional Memory 研究/实现，提出以 scalable static lookup 作为 MoE conditional computation 之外的另一条 sparsity 轴。核心模块把现代化 N-gram embedding lookup 与动态 hidden state 融合，让“知识查找”从纯 Transformer 计算中部分剥离出来。

## AI Infra 意义
Engram 的系统侧特征是 **deterministic addressing**：官方论文/README 明确指出，大规模 embedding table 可以 offload 到 host memory，并以较低 inference overhead 进行 lookup。这使其同时是模型结构创新和 memory hierarchy / data movement 问题。

## 与 DeepEP-Ascend 的连接
[[community/deepseek-ai/DeepSeek-Infra/DeepEP-Ascend|DeepEP-Ascend]] 暴露 `EngramBuffer`，支持 NPU-backed BF16/FP8 tables 与 per-layer fetch hooks，并把 Engram remote-memory access 列为通信原语之一。这里记录的是明确的接口/系统支撑关系；由于 DeepEP-Ascend README 同时把该能力标为 experimental，不把它写成已完成的端到端生产部署。

## 代码边界
Engram 仓库当前提供的是用于展示核心 data flow 的 standalone demonstration implementation，并明确 mock Attention/MoE/mHC 等标准组件；因此它不能被当作完整 production serving runtime。

## Sources
- https://github.com/deepseek-ai/Engram
- https://github.com/deepseek-ai/DeepEP-Ascend

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/memory/Conditional Memory|Conditional Memory]]
- [[concept/memory/Host Memory|Host Memory]]

<!-- END AUTO PROJECT CONCEPTS -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/深度求索/深度求索|深度求索]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
