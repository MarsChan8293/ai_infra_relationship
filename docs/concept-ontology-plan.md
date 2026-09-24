# Concept Ontology 分批实施计划

> 启动日期：2026-09-25  
> 目标：在 `ai_infra_relationship` 中增加第四类 canonical 图谱节点 `concept`，把“项目/组织关系图”扩展为“组织 ↔ 项目 ↔ 技术机制”的 AI Infra Knowledge Graph。

## 0. 决策与边界

本计划覆盖并替代 `docs/software-merge-plan.md` 中“Concept 永久留在 ai_infra_docs、不在 relationship 建 concept type”的旧边界。旧计划仍保留为 2026-09-19 Software Project 迁移的历史记录。

新的职责划分：

- `ai_infra_relationship/concept`：canonical、轻量、可计算、可建立关系的技术概念节点。
- Project 页面：某个软件如何实现/暴露这些机制。
- 长篇教程、实验笔记、芯片/模型专题：可以继续留在 `ai_infra_docs`，但若与这里存在同名 atomic concept，应链接到 relationship canonical concept，而不是维护两份互相漂移的定义。

核心原则：**Concept 描述 mechanism，Project 描述 implementation。**

## 1. Concept Schema

Canonical Concept 使用 `type: concept`，最小字段：

```yaml
---
type: concept
name: KV Cache Offloading
aliases:
  - KV Offloading
  - KV Cache 卸载
domain: inference
topic: kv-cache
parent_concepts:
  - KV Cache Management
related_concepts:
  - Tiered KV Cache
  - KV Cache Transfer
projects:
  - LMCache
  - vLLM
last_verified: 2026-09
---
```

治理规则：

- 一个机制只有一个 canonical 节点；TP / Tensor Parallelism、PD 分离 / P-D Disaggregation 等只通过 aliases 归一。
- hierarchy 保持浅层，`parent_concepts` 只表达真正的“属于/细分”。
- 非严格上下位关系放 `related_concepts`。
- `projects` 只记录有直接公开证据的实现/支持，不从关键词、areas 或相似性推断。
- 第一阶段图谱边以 Markdown 双链为主；等 taxonomy 稳定后再决定是否增加 typed Project ↔ Concept relation，避免过早固化错误本体。

## 2. Concept 页面模板

每个概念页固定回答六件事：

1. **一句话定义**：它是什么。
2. **解决的问题**：为什么需要它。
3. **核心机制**：关键数据流/控制流/算法。
4. **细分与相邻概念**：父概念、子概念、容易混淆的技术。
5. **代价与适用边界**：吞吐、延迟、显存、网络、复杂度等 trade-off。
6. **项目实现**：哪些 canonical project 有直接实现，以及连接到对应项目页。

正文不追求百科长度。Concept 应成为图谱枢纽，而不是把项目文档再抄一遍。

## 3. 分批实施

### Batch A：Ontology 基础设施

- [x] 新增 `schema/concept.yaml` 并注册到 schema catalog。
- [x] 新增第四个一级目录 `concept/` 与入口页。
- [x] `audit-graph.py` 扫描 concept root。
- [x] Graph Explorer 增加 Concept 类型显示。
- [x] 新增 `scripts/generate-concept-index.py`。
- [x] Quartz Pages 构建/发布 Concept 与 generated Concept Index。
- [x] Sync Node Schemas 监听、生成并回写 Concept 节点/索引。
- [x] 根索引写入 Concept 规则。
- [x] 明确旧 Software migration “不迁 Concept”边界已被本计划覆盖。

验收：PR #36 已通过 graph audit、node schema generation、Quartz build、Graph Explorer route reconciliation 和 internal-link audit，并于 2026-09-25 合入 main。

### Batch B1：KV Cache + Serving 核心概念

首批只建立骨干节点，目标 10–12 个：

- [x] KV Cache
- [x] KV Cache Management
- [x] KV Cache Offloading
- [x] Tiered KV Cache
- [x] KV Cache Transfer
- [x] KV Cache Sharing
- [x] Prefix Caching
- [x] P-D Disaggregation
- [x] Disaggregated Serving
- [x] Continuous Batching
- [x] Chunked Prefill

优先连接：LMCache、Mooncake、vLLM、SGLang、Dynamo、llm-d、MindIE-Motor、MemCache / MemFabric。

### Batch B2：Decoding + Parallelism

- [x] Speculative Decoding
- [x] Draft-Target Decoding
- [x] N-gram Speculation
- [x] Self-Speculative Decoding
- [x] Multi-token Prediction
- [x] Parallelism
- [x] Tensor Parallelism
- [x] Pipeline Parallelism
- [x] Data Parallelism
- [x] Expert Parallelism
- [x] Sequence Parallelism
- [x] Context Parallelism

### Batch C：Project ↔ Concept 系统化

#### Batch C1：单源关系 + 派生反向视图

- [x] 选择 Concept 侧 `projects:` 作为唯一人工事实源；Project 不新增人工 `concepts:` 字段。
- [x] Project schema 增加 derived `linked_concepts`，禁止手工维护或从 `areas` 自动推断。
- [x] 新增 `sync-project-concepts.py`，自动生成 Project frontmatter 反向链接和“关联概念”区块。
- [x] 新增 `audit-project-concept-coverage.py`，输出 Markdown / JSON coverage report。
- [x] Quartz 与 Sync Node Schemas workflow 接入 Project ↔ Concept 同步和审计。
- [x] 补齐 llm-d / MindIE-Motor 与 Disaggregated Serving / P-D Disaggregation 的 canonical 连接。
- [ ] 根据 coverage report 继续补高价值 project / concept 缺口。

#### Batch C2：关系语义升级

- [ ] taxonomy 和 C1 coverage 稳定后，再决定是否导出 typed Project ↔ Concept edge。
- [ ] 若升级 typed relation，优先从 Concept `projects:` 单源派生，不允许 Project 侧重复声明。
- [ ] 关系名需区分“直接实现/支持”与“仅相关/集成”，避免一个 `implements-concept` 覆盖所有语义。

### Batch D：扩展到更完整 AI Infra Ontology

候选域：

- kernel / operator：FlashAttention、PagedAttention、GEMM、Grouped GEMM、MoE dispatch/combine。
- communication：AllReduce、AllGather、All-to-All、RDMA、GPUDirect、collective communication。
- scheduling：request routing、load balancing、prefill/decode scheduling、gang scheduling。
- quantization：weight-only、W8A8、FP8、KV Cache Quantization。
- compiler：graph compiler、kernel DSL、operator fusion、AOT/JIT。
- hardware/memory：HBM、CXL、NUMA、memory pooling、hierarchical memory。

是否进入 P0/P1 由现有项目覆盖密度和用户研究频率决定，不为了“概念大全”机械扩张。

## 4. 自动索引设计

`generated/concept-index.md` 从 `concept/**/*.md` 中所有 `type: concept` 自动生成，按 `domain → topic` 聚合，展示：

- canonical concept
- aliases
- parent concepts
- related concepts 数量
- projects 数量
- Graph Explorer focus 深链

`concept/concept.md` 只作为稳定导航入口，不人工复制全量列表。

## 5. 与 Graph 的关系

Batch A/B 使用两种边：

- Markdown wikilink：Concept ↔ Concept、Concept ↔ Project。
- frontmatter metadata：用于索引、治理与后续派生。

暂不自动把 `parent_concepts / related_concepts / projects` 直接生成 typed edge，因为名称解析和方向语义需要先经过一轮真实内容验证。等 B1/B2 稳定后再升级。

## 6. Definition of Done

每个批次必须满足：

- 新节点 canonical basename 唯一，同义词只出现在 aliases。
- 所有显式双链可解析；不引入新的 ambiguous wikilink hard error。
- Concept 至少连接一个父/相关概念或一个真实 project，禁止孤立空壳。
- 项目实现关系在正文有直接公开证据，不能凭印象推断。
- `generated/concept-index.md` 可自动重建。
- Graph Explorer 可筛选并聚焦 `concept`。
- schema mirror 生成完整，Quartz 页面无 404。
- 每个批次单独 PR / commit group，便于回滚和审阅。

## 7. 当前状态

- Batch A：已完成并合入 main。
- Batch B1：已完成并合入 main（PR #37）。
- Batch B2：已完成并合入 main（PR #38）。
- Batch C1：Project ↔ Concept 单源同步、coverage 审计与第一轮 llm-d / MindIE-Motor 缺口修复正在独立分支实施。
- Batch C2 / D：待 C1 coverage 数据稳定后继续。
