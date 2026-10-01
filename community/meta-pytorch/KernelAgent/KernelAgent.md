---
type: project
name: "KernelAgent"
linked_people: []
layer: optimization
status: active
repository: https://github.com/meta-pytorch/KernelAgent
areas: ["agentic-kernel-optimization", "triton", "multi-agent", "ncu", "roofline", "correctness-verification", "benchmarking"]
hardware: ["nvidia", "intel-xpu"]
companies: ["Meta"]
last_verified: "2026-10"
---

# KernelAgent

KernelAgent 是 Meta / PyTorch 生态公开的 autonomous GPU kernel generation & optimization 系统。它将 PyTorch 程序拆解为可融合子图，并行生成 Triton kernel，执行严格 correctness verification，再使用硬件 profiling 驱动多轮优化。

## 优化闭环

公开 pipeline 包含：

1. NCU profiling；
2. roofline / bottleneck diagnosis；
3. LLM 生成优化候选；
4. numerical correctness verification；
5. CUDA event benchmark；
6. best-so-far 与 divergence-based revert。

因此它是很直接的 **NVIDIA KernelOptimizer runtime** 参考实现。

## Sources

- https://github.com/meta-pytorch/KernelAgent
- https://pytorch.org/blog/kernelfalcon-autonomous-gpu-kernel-generation-via-deep-agents/
