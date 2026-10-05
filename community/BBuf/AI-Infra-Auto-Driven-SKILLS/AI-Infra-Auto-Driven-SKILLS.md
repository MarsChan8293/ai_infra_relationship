---
type: project
name: AI-Infra-Auto-Driven-SKILLS
layer: optimization
status: active
repository: https://github.com/BBuf/AI-Infra-Auto-Driven-SKILLS
last_verified: "2026-10"
areas:
  - "agent-skills"
  - "llm-serving-benchmark"
  - "capacity-planning"
  - "profiling"
  - "pipeline-analysis"
  - "model-day0-support"
  - "code-review"
  - "incident-triage"
  - "model-pr-history"
code_availability: public
---

# AI-Infra-Auto-Driven-SKILLS

## 项目简介

AI-Infra-Auto-Driven-SKILLS 是 BBuf 维护的 AI Infra Agent Skill 集合，把 LLM serving 性能工程中的可复用操作知识封装为普通 `SKILL.md` 目录，供 Claude Code、Codex、Kimi 等 coding agent 直接消费。它不是新的推理引擎，也不是一个长期驻留的 Agent Harness；更准确的定位是 **AI Infra Domain Knowledge / Operational Skill Layer**。

## 当前能力

截至 2026-10，仓库 README 列出的主要能力包括：

- `llm-serving-auto-benchmark`：在 SGLang、vLLM、TensorRT-LLM、TokenSpeed 间做可比 serving benchmark，并输出满足 workload / GPU / SLA 约束的部署命令；
- `llm-serving-capacity-planner`：从 serving 日志解释启动显存、KV Cache budget、请求容量和 OOM 压力；
- `llm-torch-profiler-analysis`、`llm-pipeline-analysis`、`torch-profiler-layer-track`：把 profiler trace 下钻到 forward / layer / kernel，并识别 overlap / fusion 机会；
- `model-compute-simulation`：估算 operator shape、FLOPs、MFU，并把 kernel 映射回算子；
- `sglang-model-day0-support`：把新模型架构拆成 SGLang Day-0 支持的 PR DAG、验证矩阵和 release lock；
- `sglang-humanize-review` 与 `sglang-prod-incident-triage`：沉淀 maintainer review 经验和生产故障排障流程；
- `model-pr-optimization-history`：维护 SGLang、vLLM、TensorRT-LLM、TokenSpeed 的模型实现与优化 PR 历史知识库。

## 与 Agent Skill / Agent Harness 的关系

这个项目是 [[concept/inference/agent/Agent Skill|Agent Skill]] 的典型实现：Skill 给 coding agent 提供领域知识、证据规则、执行步骤和判断边界，但不负责 session lifecycle、权限、模型路由和 tool runtime。后者属于 [[concept/inference/agent/Agent Harness|Agent Harness]]。

因此它可以被 Harness 或 coding-agent CLI 装载，成为 [[concept/inference/optimization/Agentic Inference Optimization|Agentic Inference Optimization]] 的知识与操作层，但“提供优化 Skill”本身不等于已经实现自主 keep/revert 的闭环优化器。

## 与 Kernel Agent 的边界

仓库明确把 standalone kernel campaigns、kernel knowledge 与 NCU workflow 放到 sibling project `KDA-Pilot`。因此本图谱不把 AI-Infra-Auto-Driven-SKILLS 与 NVLabs 的 [[community/NVIDIA/KDA/KDA|KDA]] 混为同一项目，也不据此建立两者的强 integration edge。

## 生态连接

README 直接覆盖 SGLang、vLLM、TensorRT-LLM 与 TokenSpeed 的 benchmark、profiling、model support 或 PR-history 工作流。这些是 Skill 的目标框架/知识源关系，不自动等价为这些上游项目的治理或官方插件关系。

## 证据规则

项目强调 benchmark 行必须记录模型、framework revision、GPU、workload、并发/速率、SLA 与原始 artifacts；profiling 要区分 prefill / decode；性能结论必须限定到具体模型、硬件、精度、workload 与 framework revision。这使它适合作为 AI Infra Agent 的可复现 evidence layer。

## Sources

- https://github.com/BBuf/AI-Infra-Auto-Driven-SKILLS
- https://github.com/BBuf/AI-Infra-Auto-Driven-SKILLS/blob/main/README.md
