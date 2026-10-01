---
type: project
name: "CANNBot"
linked_people: []
layer: optimization
status: active
repository: https://gitcode.com/cann/cannbot
docs: https://gitcode.com/cann/cannbot-skills
areas: ["agentic-inference-optimization", "agentic-kernel-optimization", "ascendc", "triton-ascend", "pytorch-npu", "model-infer-optimize", "multi-agent", "harness"]
hardware: ["ascend"]
companies: ["华为"]
last_verified: "2026-10"
---

# CANNBot

CANNBot 是 CANN 社区面向 Ascend 的 Infra 智能体层，覆盖算子开发、模型迁移、推理优化、图模式与 runtime 等场景。其应用仓提供 plugin / harness，skills/knowledge/DSL/benchmark 等能力由配套仓库补充。

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
