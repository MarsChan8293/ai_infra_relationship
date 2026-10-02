---
type: project
name: 3FS
parent: DeepSeek-Infra
linked_concepts:
  - "concept/storage/Distributed Storage"
  - "concept/storage/NVMe SSD"
status: active
linked_people: []
repository: https://github.com/deepseek-ai/3FS
last_verified: "2026-09"
companies: ["深度求索"]
company_relation: company-led
layer: storage
areas:
  - "distributed-file-system"
  - "high-throughput-storage"
  - "linux"
integrations: []
linked_companies:
  - "company/深度求索/深度求索"
---
# 3FS

## 项目简介
3FS 是 DeepSeek 开源的高性能分布式文件系统，面向训练/推理数据访问、checkpoint 与大规模 AI workload 的高吞吐存储路径，重点使用 RDMA、NVMe SSD 与现代网络/存储能力降低 GPU 数据等待。

## GitHub
https://github.com/deepseek-ai/3FS

## 主要贡献公司
- [[company/深度求索/深度求索|深度求索]]：发起并通过 deepseek-ai 维护。

## 主要维护者 / 组织
由 [[深度求索]] / deepseek-ai 维护。人物关系应以仓库公开作者和长期贡献为准，不从公司归属反推具体模块负责人。

## 生态关系
[[DeepSeek-Infra]] · [[Mooncake]] · [[NIXL]] · distributed storage。3FS 位于持久化/分布式存储层，而 Mooncake 更专注 serving KV cache，NIXL 更专注数据移动抽象。

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/深度求索/深度求索|深度求索]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/storage/Distributed Storage|Distributed Storage]]
- [[concept/storage/NVMe SSD|NVMe SSD]]

<!-- END AUTO PROJECT CONCEPTS -->
