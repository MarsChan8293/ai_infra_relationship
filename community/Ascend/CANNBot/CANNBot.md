---
type: project
name: "CANNBot"
linked_people: []
linked_concepts:
  - "concept/inference/optimization/Agentic Inference Optimization"
  - "concept/kernel/optimization/Agentic Kernel Optimization"
layer: optimization
status: active
repository: https://gitcode.com/cann/cannbot
docs: https://gitcode.com/cann/cannbot-skills
areas: ["agentic-inference-optimization", "agentic-kernel-optimization", "ascendc", "triton-ascend", "pytorch-npu", "model-infer-optimize", "multi-agent", "harness"]
hardware: ["ascend"]
companies: ["华为"]
last_verified: "2026-10"
linked_companies:
  - "company/华为/华为"
---

# CANNBot

CANNBot 是 CANN 社区面向 Ascend 的 Infra 智能体层，覆盖算子开发、模型迁移、推理优化、图模式与 runtime 等场景。其应用仓提供 plugin / harness，skills/knowledge/DSL/benchmark 等能力由配套仓库补充。其中 [[community/Ascend/CANNBot-DSL/CANNBot-DSL|CANNBot-DSL]] 是 Agent-friendly kernel DSL / compiler 层。

## model-infer-optimize

公开的 `model-infer-optimize` plugin 通过 analyzer、implementer、reviewer 等 SubAgent 编排 NPU 模型推理端到端优化，覆盖：

- 并行策略；
- KVCache / FlashAttention；
- 融合算子；
- 量化适配；
- 图模式；
- 多流并行；
- 权重预取；
- SuperKernel。

因此 CANNBot 是当前 Ascend 侧同时触达 **Framework/E2E + Kernel** 的关键 Agent/Harness 参考。

## Sources

- https://gitcode.com/cann/cannbot
- https://gitcode.com/cann/cannbot-skills
- https://gitcode.com/cann/cannbot-skills/blob/master/plugins-official/model-infer-optimize/quickstart.md

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/inference/optimization/Agentic Inference Optimization|Agentic Inference Optimization]]
- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]

<!-- END AUTO PROJECT CONCEPTS -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/华为/华为|华为]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
