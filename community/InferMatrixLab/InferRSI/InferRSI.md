---
type: project
name: "InferRSI"
layer: optimization
status: active
maturity: research-prototype
code_availability: public
repository: https://github.com/InferMatrixLab/InferRSI
docs: https://github.com/InferMatrixLab/InferRSI/blob/main/docs/quickstart.md
areas:
  - agentic-inference-optimization
  - controlled-benchmark
  - correctness-gate
  - performance-evidence
  - optimization-campaign
  - skill-library
last_verified: "2026-11"
---

# InferRSI

## 项目简介

推理优化 CLI 工作台，面向 Coding Agent 提供可控 baseline/candidate 实验、独立正确性与性能验收、实验记录和优化知识检索；不是新的 Serving Engine。

## 核心机制

依赖用户或外部 Agent 提供候选源码、Benchmark 与质量检查脚本；保留固定协议 A/B 或 AB/BA 测试、迭代 Campaign、结果证据及历史经验。Skill Library 按硬件/框架/推理引擎/方法/工作流组织，包含 Ascend Profiling、模型适配及 vLLM KV 生命周期等专题。

## 昇腾适配与限制

拥有昇腾相关 Skill 与案例，不等于已完成所有 NPU 设备适配；910B/910C/950 需要独立提供远端执行、数值门禁与性能脚本，区分真实测量收益和候选方法论。

## 技术关系

[[concept/inference/optimization/Agentic Inference Optimization|Agentic Inference Optimization]]、[[concept/inference/agent/Agent Harness|Agent Harness]]、[[concept/inference/agent/Agent Skill|Agent Skill]]；与 [[community/OpenRSI-Foundation/RSI-Harness/RSI-Harness|RSI-Harness]] 的 Work/Judge 隔离和 [[community/smth-fun/SEIS/SEIS|SEIS]] 的源码进化为互补思路，不能推断已有集成。

## openJiuwen / AgentInfer 源码快照（2026-11 核验）

openJiuwen 的 `agent-infer` 项目在仓库根目录以外的 **`inferrsi/` 子目录**收录 InferRSI **完整源码快照**，这是同一个上游推理调优与实验管理工作台的集成/分发形式，**不应另建同名 InferRSI 项目节点**。

- GitCode 访问入口：https://gitcode.com/openJiuwen/agent-infer/tree/main/inferrsi
- 可核实的 GitHub 对应路径：https://github.com/openJiuwen-ai/agent-infer/tree/main/inferrsi
- openJiuwen 官方快照来源说明：https://github.com/openJiuwen-ai/agent-infer/blob/main/docs/zh/reference/inferrsi.md
- 快照来源提交：`InferMatrixLab/InferRSI@76384cfb2c2af08eaa90753a18a45557ceed7ce0`，官方记录 **2026-10-21 同步，共 536 个受 Git 跟踪的文件**。
- `inferrsi/pyproject.toml` 声明发行包 `inferrsi==0.1.0`、项目主页仍指向 `InferMatrixLab/InferRSI`；主仓根目录的 `agentinfer` 为单独的发行包。
- **版本边界**：该子目录是某时点的源码快照；上游独立 GitHub 仓库已继续发展，不能把 GitCode 的旧快照视为上游最新特性或宣称持续自动同步。
- **功能边界**：openJiuwen `agent-infer` 主体围绕 Agent 负载下的 vLLM 调度/缓存，`inferrsi/` 则负责推理调优实验。两者同仓托管不等于已验证存在调用接口或自动优化联动。

对于昇腾推理 RSI，可借鉴 openJiuwen 的社区分发形式，将 InferRSI 作为验收和调优实验组件；但是否可直接部署至当前 vLLM-Ascend/910C 环境，仍需按版本分别验证。

## 维护组织与来源

上游组织：`InferMatrixLab`（以公开仓库治理与贡献证据为准，未确认个人维护者身份）。

- https://github.com/InferMatrixLab/InferRSI
- https://gitcode.com/openJiuwen/agent-infer/tree/main/inferrsi
- https://github.com/openJiuwen-ai/agent-infer/blob/main/docs/zh/reference/inferrsi.md
- https://github.com/InferMatrixLab/InferRSI/blob/main/docs/quickstart.md
- https://github.com/InferMatrixLab/InferRSI/blob/main/src/inferrsi/knowledge/data/skill_library/README.md
