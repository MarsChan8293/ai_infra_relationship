---
type: project
name: "AVO"
linked_people: []
linked_concepts:
  - "concept/kernel/optimization/Agentic Kernel Optimization"
layer: optimization
status: research
docs: https://arxiv.org/abs/2603.24517
areas: ["agentic-kernel-optimization", "evolutionary-search", "agentic-variation-operators", "attention", "cuda", "ptx", "execution-feedback"]
hardware: ["nvidia"]
companies: ["NVIDIA"]
last_verified: "2026-10"
linked_companies:
  - "company/NVIDIA/NVIDIA"
---

# AVO

AVO（Agentic Variation Operators）把传统 evolutionary search 中固定的 mutation / crossover 替换为自主 coding agent。Agent 可以读取 lineage、domain knowledge 和 execution feedback，自主提出、修复、批评并验证 kernel edit。

公开论文在 NVIDIA Blackwell B200 attention kernel 上评估该机制。这里把 AVO 记录为 research system，不把论文作者网络自动等价为某一组织的单独所有权。

## Sources

- https://arxiv.org/abs/2603.24517

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]

<!-- END AUTO PROJECT CONCEPTS -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/NVIDIA/NVIDIA|NVIDIA]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
