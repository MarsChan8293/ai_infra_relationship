---
type: project
name: "Hyperloom"
linked_people: []
layer: optimization
status: active
repository: https://github.com/AMD-AGI/Hyperloom
docs: https://rocm.docs.amd.com/projects/hyperloom/
areas: ["agentic-inference-optimization", "agentic-kernel-optimization", "multi-agent", "e2e-validation", "recipe-memory", "vllm", "sglang", "xdit"]
hardware: ["amd"]
companies: ["AMD"]
last_verified: "2026-10"
---

# Hyperloom

ROCm Hyperloom 是 AMD-AGI 的多 Agent 推理优化 Harness，目标是自动优化 AMD Instinct 上的推理 workload。公开实现覆盖 vLLM、SGLang 与 xDiT，并把 framework optimization、kernel optimization、sweep、端到端 validation 与跨 session Recipe Knowledge Base 组织成闭环。

## 核心机制

典型阶段为：

`PRELUDE → ENABLEMENT → FRAMEWORK_AGENT → KERNEL_AGENT → SWEEP → CLOSE`

Hyperloom 强调局部 kernel speedup 不能直接视为成功；候选必须重新回到真实 workload 做端到端验证。KEEP / REVERT、baseline anchor 和 Recipe KB 使优化过程可审计、可复用。

## Sources

- https://github.com/AMD-AGI/Hyperloom
- https://rocm.docs.amd.com/projects/hyperloom/
