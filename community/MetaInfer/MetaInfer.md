---
type: project
name: MetaInfer
linked_people: []
layer: optimization
status: active
repository: https://github.com/MetaInfer/MetaInfer
areas: [llm-inference, inference-framework-generation, ai-infra-agent, kernel-optimization, model-porting, performance-optimization]
hardware: [nvidia]
last_verified: 2026-09
linked_companies: []
---
# MetaInfer

MetaInfer 是一个由 LLM 驱动的 AI Infra 优化工具箱，目标是根据模型、硬件、并行、量化以及吞吐/时延目标，自动生成紧凑、面向特定部署条件的高性能 LLM inference framework，而不是持续扩张一个覆盖所有组合的通用推理框架。

## 推理优化方向

- **Inference framework generation**：内置 `gen-infer-framework` 任务，可生成带 OpenAI-compatible HTTP API 的模型特定推理服务，并通过固定 prompt 与 LLM judge 做正确性验证。
- **AI-assisted kernel optimization**：围绕目标 kernel 运行自动化的 optimize → benchmark 循环。
- **Model porting**：将上游框架中的新模型能力移植到较老 GPU / 较低版本目标环境。
- **Performance modeling**：`calc-theoretical-value` 可计算单次 LLM forward 的理论 FLOPs 与 memory traffic。
- **Agent-driven infra engineering**：通过 `SubAgentManager` 调度 coding agent；README 当前列出 Claude/ccb、Codex 与 pi backend。

## 论文

MetaInfer 的初始思想和实验数据对应论文 **“MetaInfer: A Knowledge Only LLM Inference Engine Generator SKILL Toolbox”**：

- arXiv: https://arxiv.org/abs/2607.12875
- Authors: Zhenwen Miao, Honglin Wang, Mingheng Mi
- Year: 2026
- Primary class: cs.MA
- 论文相关代码由项目维护在 `arxiv-paper` branch。

这里把“论文作者”作为论文事实记录，不自动等价为当前项目 maintainer / owner；人物节点应在有进一步可核验身份与 AI Infra 关系后再建立。

## Repository identity

用户最初发现入口为 `HuangPuStar/MetaInfer`。截至 2026-09 核验，该仓库 README 中给出的 clone / canonical project URL 为 `MetaInfer/MetaInfer`，因此本图谱只建立一个 canonical **MetaInfer** 项目节点，以避免因 namespace 变化产生重复项目。

## 图谱价值

MetaInfer 位于 **AI-for-AI-Infra / inference optimization automation** 这一新方向：它不是单纯 serving runtime，而是尝试让 coding agent / LLM 直接生成或优化 inference engine、kernel 和模型移植代码。对本仓库关注的推理优化人才与软件生态而言，它可以作为后续连接作者、agentic systems、kernel optimization 与 inference-engine 项目的入口节点。

## Sources

- https://github.com/MetaInfer/MetaInfer
- https://github.com/HuangPuStar/MetaInfer
- https://arxiv.org/abs/2607.12875
