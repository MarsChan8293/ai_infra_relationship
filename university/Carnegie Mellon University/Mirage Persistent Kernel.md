---
type: project
name: "Mirage Persistent Kernel"
linked_people: []
layer: compiler
status: active
repository: https://github.com/mirage-project/mirage
docs: https://mirage-project.readthedocs.io/
areas: [llm-inference, megakernel, compiler, runtime, kernel-fusion, multi-gpu]
hardware: [nvidia]
last_verified: "2026-09"
linked_companies: []
---
# Mirage Persistent Kernel

Mirage Persistent Kernel（MPK）是 CMU Catalyst Research 页面列出的 compiler/runtime 项目，把 LLM inference 转换为单个 mega-kernel，并在 SM 粒度表达 task dependencies，以支持 cross-operator pipelining、kernel overlap 与分布式调度。

截至 2026-09，`mirage-project/mirage` 的默认分支就是 `mpk`，仓库仍在活跃更新。

## Catalyst

- [[university/Carnegie Mellon University/Catalyst Group|Catalyst Group]]：官方 Research 页面直接列出 MPK。
- 代表工作：MPK / Mirage 系列。

## Sources
- https://catalyst.cs.cmu.edu/projects/mpk.html
- https://github.com/mirage-project/mirage
- https://mirage-project.readthedocs.io/
