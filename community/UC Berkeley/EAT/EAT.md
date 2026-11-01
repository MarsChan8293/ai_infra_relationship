---
type: project
name: "EAT"
aliases: ["Evolving Agent Teams"]
layer: optimization
status: active
maturity: research-prototype
repository: https://github.com/caoshiyi/EAT
docs: https://arxiv.org/abs/2610.36848
areas: ["multi-agent", "agent-team-evolution", "supervisor-agent", "agentic-kernel-optimization", "agentic-inference-optimization", "benchmark-driven-optimization", "claude-code", "code-optimization"]
hardware: ["nvidia", "amd", "apple-silicon"]
last_verified: "2026-11"
code_availability: public
---

# EAT（Evolving Agent Teams）

EAT 是 UC Berkeley 研究团队提出并开源的 **自演化 Agent Team Harness**。它不是固定角色的多 Agent 工作流：由 Supervisor Agent 根据评测和执行轨迹判断团队为什么停滞，重新设计 coding agents 的角色、提示词、阶段、代码文件所有权和 GPU 资源分配，再由 Harness 执行任务和统一评测。Supervisor 不直接提交被优化程序的解决方案。

## 研究团队

论文 *Evolving Agent Teams*（NeurIPS 2026）作者为 Shiyi Cao、Ziming Mao、Dacheng Li、Joseph E. Gonzalez 和 Ion Stoica。

- [[university/UC Berkeley/Shiyi Cao|Shiyi Cao（曹诗怡）]]：第一作者。
- [[company/Inferact/Joseph Gonzalez|Joseph E. Gonzalez]]：共同作者。
- [[company/Inferact/Ion Stoica|Ion Stoica]]：共同作者。

这里只将作者与研究项目建立学术关联，不据此推断 Inferact、Anyscale 或 Databricks 对项目拥有治理权。

## 自演化机制

1. 以固定的 correctness / performance evaluation 和资源预算定义优化任务。
2. Supervisor 分析前一轮 agent team 的运行日志、团队协作和性能平台期。
3. Supervisor 更新团队配置：角色、prompt、阶段、工作文件及 GPU 分配。
4. Coding agents 修改目标代码；Harness 执行客观评测，保存得分、成本、轨迹及最佳产物。
5. 将经验及失败记录持久化，进入下一轮迭代，直到预算耗尽或停止。

与 [[community/UC Berkeley/K-Search/K-Search|K-Search]] 偏向 kernel 候选及性能知识搜索不同，EAT 的核心优化对象首先是 **完成任务的 Agent 团队本身**。

## 已公开验证任务

- **GPU kernels**：FlashInfer MLA paged decode、AMD MI350X 上的 KDA、NVIDIA B200 上的 KDA 等，作者发布了可查看的 kernel 及运行轨迹。
- **本地模型推理引擎**：在 Apple M4 Pro（48GB）上，Agent 通过修改 SSD expert offload 路径优化 Qwen3.8-Flash-Next serving；公开报告包含与基线引擎的 prefill / decode 对比。
- **其他代码任务**：RoboDojo robot policy，证明演化对象并不限于 kernel。

这些结果依赖特定测例、硬件、评测定义和 agent 成本预算，不代表通用或跨平台性能保证。

## 开源与适配边界

- 主框架（Apache-2.0）：https://github.com/caoshiyi/EAT
- 输出 kernel：https://github.com/caoshiyi/eat-kernels
- 实验任务：https://huggingface.co/datasets/eva98/eat-gym
- 迭代配置、日志和轨迹：https://huggingface.co/datasets/eva98/eat-evolution-traces
- 官方主要入口：Claude Code Plugin / Skill（见主仓库 README）。
- **昇腾 AscendC / Triton-Ascend：未见主项目明确宣称原生支持或经过实测。** 可以借鉴 Supervisor 与 eval 闭环，但需要单独适配 NPU 工具链、correctness 与性能评测。

## AI Infra 图谱关系

- [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]]：Kernel 优化任务的可验证、自演化 agent 工作流。
- [[concept/inference/agent/Agent Harness|Agent Harness]]：多 agent 生命周期、角色演化、实验记录和评测控制。
- [[concept/inference/optimization/Agentic Inference Optimization|Agentic Inference Optimization]]：优化对象延伸到推理引擎实现，不只限于 microkernel。
- [[community/UC Berkeley/K-Search/K-Search|K-Search]]：同属 Berkeley Sky 系统优化研究谱系；两者机制不同。

## Sources

- https://github.com/caoshiyi/EAT
- https://arxiv.org/abs/2610.36848
- https://github.com/caoshiyi/eat-kernels
- https://huggingface.co/datasets/eva98/eat-gym
- https://huggingface.co/datasets/eva98/eat-evolution-traces
