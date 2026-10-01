---
type: project
name: "CUDA-Agent"
linked_people: []
layer: optimization
status: active
repository: https://github.com/BytedTsinghua-SIA/CUDA-Agent
docs: https://cuda-agent.github.io/
areas: ["agentic-kernel-optimization", "agentic-rl", "cuda", "kernel-generation", "correctness-verification", "profiling"]
hardware: ["nvidia"]
companies: ["字节跳动"]
last_verified: "2026-10"
---

# CUDA-Agent

CUDA-Agent 是 ByteDance Seed × 清华 AIR 联合 SIA-Lab 公开的高性能 CUDA kernel generation 工作。项目把 agentic RL 与可执行 kernel 环境结合，并公开了训练数据、SKILL 和标准化 agent workspace。

## Agent Harness

`agent_workdir` 明确提供完整执行闭环：

`implement CUDA → compile → verify correctness → profile performance → iterate`

其中包含 baseline model、优化后的 custom CUDA extension、编译脚本、correctness verifier 与 profiler。

该项目同时连接了 **Agent Harness** 与 **Agentic RL / trajectory training** 两条路线，对长期把优化轨迹用于模型训练很有参考价值。

## Sources

- https://github.com/BytedTsinghua-SIA/CUDA-Agent
- https://cuda-agent.github.io/
