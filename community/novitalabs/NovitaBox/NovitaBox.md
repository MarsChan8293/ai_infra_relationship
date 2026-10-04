---
type: project
name: NovitaBox
status: active
repository: https://github.com/novitalabs/NovitaBox
docs: https://github.com/novitalabs/NovitaBox/tree/main/docs
last_verified: "2026-10"
companies: ["Novita AI"]
company_relation: company-led
layer: runtime
areas: [agent-sandbox, microvm, container-sandbox, gpu-sandbox, isolation, local-runtime]
hardware: [nvidia]
integrations: [Firecracker, gVisor, Cloud Hypervisor, E2B]
linked_companies:
  - "company/Novita AI/Novita AI"
linked_concepts:
  - "concept/inference/agent/Agent Harness"
---
# NovitaBox

NovitaBox 是 Novita Sandbox 的本地开源版，是面向 AI Agent 的 sandbox runtime。它把 agent code execution 放进受隔离的 MicroVM / userspace-kernel runtime，并提供模板、snapshot、network、filesystem 与 sandbox lifecycle 管理。

## Runtime

当前公开后端包括：

- Firecracker：MicroVM 与 snapshot 路径。
- gVisor：container-style sandbox；可通过 runsc nvproxy + NVIDIA CDI 暴露 NVIDIA GPU。
- Cloud Hypervisor：另一条 MicroVM backend。

同时提供 E2B SDK compatibility，因此现有 E2B 客户端可以通过切换 endpoint 接入 NovitaBox。

## 在 AI Infra 图谱中的位置

NovitaBox 不属于 LLM inference engine，而属于 agent execution / isolation 基础设施。它与 [[concept/inference/agent/Agent Harness|Agent Harness]] 的关系在于：harness 负责编排模型、工具和任务状态，而 NovitaBox 提供可隔离执行工具代码的 runtime boundary。

当 agent workload 需要 GPU code execution、kernel 编译、benchmark 或不可信代码运行时，sandbox runtime 会成为 AI infra 的实际资源与安全边界，因此值得单独建节点。

## Sources

- https://github.com/novitalabs/NovitaBox
- https://novita.ai/
