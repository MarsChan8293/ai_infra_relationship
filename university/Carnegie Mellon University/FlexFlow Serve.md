---
type: project
name: "FlexFlow Serve"
linked_people: []
layer: distributed-serving
status: unknown
repository: https://github.com/flexflow/flexflow-serve
areas: [llm-serving, speculative-decoding, distributed-inference, cpu-offload, quantization]
hardware: [nvidia, amd]
last_verified: "2026-09"
linked_companies: []
---
# FlexFlow Serve

FlexFlow Serve 是 CMU Catalyst 当前 Research 页面列出的 LLM serving 项目，也是一个开源 compiler + distributed multi-GPU runtime。其核心路线包括 tree-based speculative inference / token-tree verification、CPU offloading 与 INT4/INT8 quantization。

Catalyst 官方项目页把它作为本组的 LLM serving 工作展示；GitHub 仓库 `flexflow/flexflow-serve` 当前未归档，但本轮不把“未归档”单独解释成持续高频开发，因此 lifecycle 保守记录为 `unknown`。

## Catalyst

- [[university/Carnegie Mellon University/Catalyst Group|Catalyst Group]]：官方 Research 页面直接列出 FlexFlow Serve。
- 代表工作：SpecInfer。

## Sources
- https://catalyst.cs.cmu.edu/projects/flexflow%20serve.html
- https://github.com/flexflow/flexflow-serve
