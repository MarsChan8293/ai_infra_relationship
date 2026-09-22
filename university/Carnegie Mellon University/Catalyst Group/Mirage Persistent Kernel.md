---
type: project
name: "Mirage Persistent Kernel"
linked_people: []
layer: "kernel-compiler-runtime"
status: active
repository: https://github.com/mirage-project/mirage
docs: https://mirage-project.readthedocs.io/
areas:
  - "llm-inference"
  - "persistent-kernel"
  - "megakernel"
  - "compiler"
  - "gpu-runtime"
last_verified: "2026-09"
---
# Mirage Persistent Kernel

Mirage Persistent Kernel 是 Catalyst 的 compiler + runtime 研究路线，用于把 LLM inference tensor programs mega-kernelize。

## AI Infra 位置
- 目标是减少多 kernel launch / synchronization 带来的 inference latency。
- 把 tensor program search / compilation 与 persistent-kernel runtime 连接起来。

## Sources
- https://catalyst.cs.cmu.edu/
- https://github.com/mirage-project/mirage
- https://mirage-project.readthedocs.io/
