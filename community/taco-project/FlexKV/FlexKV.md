---
type: project
name: FlexKV
companies: ["腾讯"]
company_relation: company-led
linked_companies:
  - "company/腾讯/腾讯"
linked_people:
  - "company/腾讯/Stary"
repository: https://github.com/taco-project/FlexKV
open_source: true
layer: distributed-kv-cache
areas: [kv-cache, distributed-storage, multi-level-cache, rdma, data-movement, llm-inference]
last_verified: "2026-09"
---
# FlexKV

## 项目简介
FlexKV 是腾讯云 TACO 团队与社区共同开发的分布式 KV store / 多级 KVCache 管理系统，面向大规模 LLM inference。其缓存层覆盖 CPU memory、local SSD 与 scalable remote storage，并通过异步 transfer / prefetch 降低 KV 重算与数据移动开销。

## 与 Mooncake 的直接关系
FlexKV 不是 Mooncake 的简单竞品关系，而已经形成两层直接技术连接：

1. **Mooncake Transfer Engine**：FlexKV distributed KVCache reuse 官方文档明确使用 Mooncake Transfer Engine 做跨节点 RDMA KVCache 传输。
2. **Mooncake Store**：2026-07 起 FlexKV 支持把 Mooncake Store 作为 key-addressed remote cache tier，用于 cluster-wide KV reuse。

因此这条边应建模为 `integration / data-plane dependency`，而不是笼统的“同类项目”。

## 生态
- **vLLM**：FlexKVConnectorV1 已于 2026-03 合入 vLLM mainline。
- **SGLang**：提供 HiCacheStorage / distributed cache 相关集成。
- **TensorRT-LLM**：提供适配方案。
- **NVIDIA Dynamo**：提供 FlexKV + KV Router 的部署与集成文档。
- [[community/kvcache-ai/Mooncake/Mooncake|Mooncake]]：Transfer Engine + Store 两条集成路径。

## 人物桥
- [[company/腾讯/Stary|Stary（@staryxchen）]]：腾讯员工；Mooncake Transfer Engine codeowner，同时是 FlexKV Collaborator，是当前已公开核验的 Mooncake ↔ FlexKV 强人物桥之一。

## Sources
- https://github.com/taco-project/FlexKV
- https://github.com/taco-project/FlexKV/blob/main/docs/dist_reuse/README_en.md
- https://github.com/taco-project/FlexKV/blob/main/docs/vllm_adapter/README_en.md
- https://github.com/taco-project/FlexKV/blob/main/docs/dynamo_integration/README_en.md
