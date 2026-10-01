---
type: project
name: "GEAK"
linked_people: []
layer: optimization
status: active
repository: https://github.com/AMD-AGI/GEAK
docs: https://rocm.docs.amd.com/projects/geak/
areas: ["agentic-inference-optimization", "agentic-kernel-optimization", "multi-agent", "deterministic-workflow", "vllm", "sglang", "profiling", "benchmarking"]
hardware: ["amd"]
companies: ["AMD"]
last_verified: "2026-10"
---

# GEAK

GEAK（Generating Efficient AI-Centric Kernels）是 AMD-AGI 公开的自主性能优化 Agent。它既可以针对单个 GPU kernel 做生成、profiling、benchmark 与迭代，也可以针对 vLLM / SGLang 的完整 serving workload 做端到端吞吐优化。

## 与本图谱的关系

GEAK 最有参考价值的是“双层闭环”：

- **e2e_workflow**：定位 serving stack 热点，先做框架/配置侧优化，再把值得深入的热点递归下钻到 kernel workflow。
- **kernel_workflow**：围绕单个 kernel 的正确性、性能和真实硬件测量持续优化。

它把控制流放在 deterministic workflow 中，而把分析、策略与代码修改交给 Agent，符合“Agent 提案，Harness 判定”的性能工程边界。

## Sources

- https://github.com/AMD-AGI/GEAK
