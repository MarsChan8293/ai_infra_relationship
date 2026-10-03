---
type: project
name: TIRx Harness
layer: compiler
status: active
repository: https://github.com/mlc-ai/TIRx-harness
docs: https://tirxharness.mlc.ai/docs/
areas:
  - "agentic-gpu-programming"
  - "kernel-authoring"
  - "compiler-analysis"
  - "correctness-analysis"
  - "remote-execution"
  - "benchmark-server"
  - "agent-skills"
hardware:
  - "nvidia"
integrations:
  - "TIRx Kernels"
last_verified: "2026-10"
---
# TIRx Harness
## 项目定位

TIRx Harness 是 MLC 新开源的 **compiler harness for agentic GPU programming**。它的重点不是单独提供一个 kernel DSL，而是把稳定编译器基础、知识库、工具、远程 GPU 执行和 benchmark server 组织成 Agent 可反复调用的工程闭环。

## 核心结构

- **TIRx-lite**：建立在 TIRx IR 之上的 kernel authoring DSL。
- **Compiler analysis**：检查 synchronization、memory race、numerical behavior，并暴露 compiler output / GPU instruction。
- **kcoral remote execution**：Agent 可留在控制机，将 GPU workload 发送到远端执行。
- **Skills + workload contracts**：把如何优化 kernel 与 correctness / performance 条件显式化。

因此它直接属于 [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]] 和 [[concept/kernel/programming/Kernel DSL|Kernel DSL]] 的交叉区域。

## 与现有 Agentic Kernel Infra 的关系

[[community/Ascend/CANNBot-DSL/CANNBot-DSL|CANNBot-DSL]] 面向 Ascend 的 Agent-friendly DSL/backend；[[community/LancerLab/Croqtile/Croqtile|Croqtile]] 强调 agent-native kernel DSL/compiler；TIRx Harness 则进一步把 compiler analysis、knowledge、remote execution 与 benchmark server 一体化。三者可以作为不同硬件/编译栈上的同类 Harness 路线进行比较。

配套实现库为 [[community/mlc-ai/TIRx-Kernels/TIRx-Kernels|TIRx Kernels]]。

## Sources

- https://github.com/mlc-ai/TIRx-harness
- https://tirxharness.mlc.ai/docs/
- https://blog.mlc.ai/2026/09/29/tirx-harness-an-open-compiler-harness-for-agentic-gpu-programming
