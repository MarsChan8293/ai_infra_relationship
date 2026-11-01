---
type: project
name: "ForgeKernel"
linked_people: []
linked_concepts:
  - "concept/kernel/optimization/Agentic Kernel Optimization"
layer: optimization
status: active
maturity: early
repository: https://github.com/OpenBMB/ForgeKernel
docs: https://github.com/OpenBMB/ForgeKernel/blob/main/README_zh.md
areas: ["agentic-kernel-optimization", "self-evolving-kernels", "architecture-first-curriculum", "gpu-profiling", "correctness-gate", "hardware-knowledge-base", "cutedsl", "cuda", "sparse-attention", "deepseek-v4.1"]
hardware: ["nvidia"]
last_verified: "2026-11"
code_availability: public
---

# ForgeKernel

ForgeKernel 是 [[company/面壁智能/ForgeTrain|ForgeTrain]] 同属的 OpenBMB **Forge 系列**中的自进化 GPU Kernel Agent / Harness。它从已有 reference kernel 出发，测量与 profile 硬件行为，由架构 Agent 将优化分解为可验证的里程碑，再由代码 Agent 实现；通过正确性、性能和机制证据的 gate 决定是否提升候选为新 reference。这里的“同属 Forge 系列”来自官方 README，不代表两个项目存在直接运行时依赖。

- 开源地址：https://github.com/OpenBMB/ForgeKernel
- 开源许可：Apache-2.0。
- 技术论文：JustGoal（https://arxiv.org/abs/2610.36434）。
- 核心定位：**Agentic Kernel Optimization / 自进化算子优化**，不是完整 LLM inference engine。

## 架构与实现

1. **Architecture-first milestone curriculum**：M0 先确定 kernel 分拆、tile shape、warp role、寄存器与 shared memory 预算，以及 orchestration；后续 M1–Mk 在该架构内优化。遇到结构性瓶颈时由架构 Agent 返回修订 M0。
2. **双层 Agent 闭环**：teacher / arch agent 负责里程碑与验证逻辑，student / coding agent 负责代码实现；每轮由 GPU job 做 correctness、benchmark 和可选 profiling，错误候选回退。
3. **Self-evolution**：`scripts/self_evolve.py` 将每轮经确认的 best kernel 晋升为下一代 reference，直至改进落入同一测量任务的噪声地板或无有效新候选。
4. **Hardware knowledge base**：`hw_kb/cutedsl/` 与 `hw_kb/cuda/` 保存由硬件 probe 验证的优化机制，可跨 operator 复用；`meta_milestone.md` 定义里程碑提炼策略。
5. **可复现任务约束**：`task.toml`、`description.md`、`shapes.json` 分别规定模型/硬件/预算/参考实现、算子语义及评测 shapes。支持 source、blackbox、generate 与 leaderboard 等任务模式。

公开源码包含 `src/forgekernel/` Harness、`skills/`、`meta/`、`hw_kb/`、`scripts/`、`tests/` 和 `kernels/`；并非仅发布论文或预生成 kernel。

## 算子覆盖与项目方成绩

- `kernels/` 提供论文中的 **24 个 CuTe DSL kernels**（H100 / B200），以及之后生成的 **DeepSeek-V4.1 sparse-attention fused prefill CUDA C++ kernel**。
- 覆盖 attention forward/backward、GQA/MLA paged decode/prefill、DeepSeek sparse attention、Gated DeltaNet、Kimi Delta Attention、FP8/FP4 GEMM 与部分 convolution。
- 官方报告在 27 个 Hopper / Blackwell 算子实验中，表现达到或超过 22 个专家库 kernel 中的 18 个，以及 3 类 kernel-generation 系统公布的全部 7 个 kernel；这些为项目方 benchmark，实际工作负载仍需独立验证。
- 官方称 DeepSeek-V4.1 fused sparse-attention prefill 在 B200 上相对 FlashMLA 为 **1.10×**。

## 硬件与开源边界（2026-11）

| 硬件 | 开源实现 / 官方说明 |
| --- | --- |
| NVIDIA H100 / Hopper SM90 | 官方 Quick Start 与论文实验覆盖 |
| NVIDIA B200 / Blackwell SM100 | 官方 Quick Start 与论文实验覆盖 |
| RTX Pro 5000/6000 Blackwell SM120 | **未列为已验证支持**；不能由 Blackwell 名称推断直接适配 |
| Ascend A3 / 910C | 官方宣布取得 CANN-Bench 榜单成绩；**当前公开 Quick Start 未提供 Ascend 后端部署路径** |
| Ascend 950DT / 950PR | 官方宣布 950DT 榜单成绩；**不能据此断言仓库已开放 Ascend 950 的实现或 950PR 适配** |

运行 Harness 所需主机环境为 Linux/macOS、Python ≥3.11、git 和配置好的 Claude Code CLI（或 agent backend）；GPU 机侧需要 NVIDIA SM90/SM100、CUDA PyTorch，CuTe DSL 任务需 `nvidia-cutlass-dsl`。Nsight Compute 推荐但不是必需。项目允许本地或 SSH GPU execution；迭代可能耗时数小时并消耗前沿模型调用费用。

## 与 AI Infra 自优化的关系

- 与 [[concept/kernel/optimization/Agentic Kernel Optimization|Agentic Kernel Optimization]] 直接关联：它提供 reference → architecture diagnosis → code generation → correctness/perf gate → promotion → hardware knowledge memory 的可运行闭环。
- 与 [[community/Ascend/CANNBot/CANNBot|CANNBot]] 是**技术路线对照**：ForgeKernel 当前开源执行路径针对 NVIDIA；CANNBot 面向 Ascend。两者并非官方已实现的直接插件集成。
- 与 [[community/NVIDIA/KernelBlaster/KernelBlaster|KernelBlaster]] 可对照优化记忆机制；与 [[community/alibaba/Atrex Kernel Agent/Atrex Kernel Agent|Atrex Kernel Agent]] 可对照 supervisor / recovery / correctness gate 的工程实现。
- 用于 vLLM / vLLM-Ascend 推理内核自进化时，仍需额外验证算子数值容差、跨 shape 正确性，以及端到端 TTFT/TPOT/吞吐；**微基准提升不自动等价于生产推理提升**。

## Sources

- https://github.com/OpenBMB/ForgeKernel
- https://github.com/OpenBMB/ForgeKernel/blob/main/README.md
- https://github.com/OpenBMB/ForgeKernel/blob/main/kernels/README.md
- https://arxiv.org/abs/2610.36434
