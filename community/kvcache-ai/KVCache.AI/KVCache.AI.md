---
type: community
name: KVCache.AI
aliases: ["KVCache.AI", "KVCache.ai", "kvcache-ai"]
category: llm-inference-optimization-community
repository: https://github.com/kvcache-ai
companies: ["趋境科技","月之暗面"]
company_relation: industry-academia-co-development
linked_companies:
  - "company/趋境科技/趋境科技"
  - "company/月之暗面/月之暗面"
linked_projects:
  - "community/kvcache-ai/Mooncake/Mooncake"
  - "community/kvcache-ai/KTransformers/KTransformers"
linked_people:
  - "university/清华大学/Mingxing Zhang"
  - "company/趋境科技/武永卫 Yongwei Wu"
  - "university/清华大学/Ruoyu Qin"
areas: [llm-inference, kv-cache, caching, scheduling, compression, offloading, disaggregated-serving, heterogeneous-inference]
governance: MADSys and industry collaborators open-source organization
last_verified: "2026-09"
---
# KVCache.AI

KVCache.AI 是围绕 LLM inference optimization 建设的开源组织。官方定位把 KVCache 视为 decoder-only Transformer serving 的核心系统资源，重点覆盖 caching、scheduling、compression、offloading 与 disaggregated serving。

## 与 MADSys 的关系
[[university/清华大学/MADSys|MADSys]] 官方主页把 KVCache.AI 列为核心项目，并明确称其与 Approaching.AI、Moonshot AI 等产业伙伴协作。KVCache.AI 的 GitHub organization 也将自身描述为 MADSys 与产业协作者之间、面向高效 Agent / LLM serving 的开源组织。

[[university/清华大学/Mingxing Zhang|章明星（Mingxing Zhang）]] 的 MADSys 主页进一步将其列为 [[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] 与 [[community/kvcache-ai/KTransformers/KTransformers|KTransformers]] 的发起者，因此这里把 MADSys → KVCache.AI → 两个核心项目作为组织层主干，而不把所有项目作者自动视为社区负责人。

## 核心项目
- [[community/kvcache-ai/Mooncake/Mooncake|Mooncake]]：KVCache-centric disaggregated LLM serving，起源于清华 / Moonshot AI 产学合作，后扩展为独立开源社区与数据移动、缓存存储生态。
- [[community/kvcache-ai/KTransformers/KTransformers|KTransformers]]：CPU/GPU heterogeneous inference / fine-tuning，面向超大 MoE 模型的低成本本地执行与异构优化。

## 产业连接
- [[company/月之暗面/月之暗面|月之暗面（Moonshot AI）]]：Mooncake 的 production workload 与共同研发来源之一。
- [[company/趋境科技/趋境科技|趋境科技（Approaching.AI）]]：KTransformers 核心研发网络，同时在 Mooncake 与大规模 Token Factory 场景持续贡献。

## 图谱意义
KVCache.AI 是 MADSys 从传统 memory / storage / distributed systems 转向 LLM serving 的关键组织桥。它把清华 systems faculty、学生、Moonshot production workload 与 Approaching.AI 的产业化工程汇聚到同一开源治理层，使 `storage-for-compute`、KV cache、异构执行和 disaggregated serving 成为一条连续技术路线。

## Sources
- https://kvcache.ai/
- https://github.com/kvcache-ai
- https://madsys.cs.tsinghua.edu.cn/
- https://madsys.cs.tsinghua.edu.cn/~zhangmx/
