---
type: project
name: "GEAK"
linked_people: []
linked_concepts:
  - "concept/inference/optimization/Agentic Inference Optimization"
  - "concept/kernel/optimization/Agentic Kernel Optimization"
layer: optimization
status: active
repository: https://github.com/AMD-AGI/GEAK
docs: https://rocm.docs.amd.com/projects/geak/
areas: ["agentic-inference-optimization", "agentic-kernel-optimization", "multi-agent", "deterministic-workflow", "vllm", "sglang", "profiling", "benchmarking"]
hardware: ["amd"]
companies: ["AMD"]
last_verified: "2026-10"
linked_companies:
  - "company/AMD/AMD"
code_availability: public
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

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/inference/optimization/Agentic Inference Optimization|Agentic Inference Optimization]]
- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]

<!-- END AUTO PROJECT CONCEPTS -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/AMD/AMD|AMD]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
