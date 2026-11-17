---
type: project
name: VibeSys
aliases: ["VibeServe"]
layer: optimization
status: active
maturity: research-prototype
code_availability: public
repository: https://github.com/uw-syfi/vibesys
docs: https://github.com/uw-syfi/vibesys/tree/main/skills
areas:
  - llm-inference
  - dedicated-inference-engine
  - inference-framework-generation
  - agentic-inference-optimization
  - inference-rsi
  - agentic-code-evolution
  - workload-aware-serving
  - hardware-aware-optimization
hardware:
  - nvidia
  - amd
  - aws-trainium
integrations: []
companies: []
company_relation: community-led
linked_concepts:
  - "concept/inference/optimization/Agentic Inference Optimization"
last_verified: "2026-11"
---

# VibeSys

## 项目定位

[VibeSys](https://github.com/uw-syfi/vibesys) 是 University of Washington 的 [[university/University of Washington/SyFI Lab|SyFI Lab]] 公开的 AI Agent **bespoke systems generation** 框架。`VibeServe` 是它针对 LLM Serving 的研究实例：根据模型、应用需求、真实 workload 和硬件拓扑，**由 Agent 编写或重构完整服务系统**，而不是仅自动调节现有引擎的几个参数。

仓库提供 Claude Code / Codex 方向的插件和 domain skills；可从空项目或已有 serving 代码出发，围绕调度、KV/内存管理、kernel 和专用解码算法生成候选系统。

## 自主优化机制

1. 用户定义需求、不可破坏的正确性约束与基准任务；
2. Outer-loop Designer 从历史 git commits、profiler 与实验记忆中提出可证伪的优化假设；
3. Inner-loop Implementer 编码、实验并提名候选；
4. Independent Judge 检查正确性不变量、激活证据与 reward hacking 风险；
5. 框架独立运行正式 Accuracy / Performance Benchmark，并将实验结果留存到下一轮。

上游公开的部署案例覆盖 NVIDIA、AMD MI300A、AWS Trainium2；这些是针对各自模型与测评设置的项目方结果，不代表所有芯片、模型都已支持。**暂无已核验的 Ascend/CANN 原生执行适配**。

## 与其他引擎生成工具对照

- [[community/pegainfer-project/kern/kern|Kern]]：Kern 通过 Manifest + 通用 Runtime 缩小优化范围；VibeSys 能直接改变更广的 Serving Stack 代码与架构。
- [[community/MetaInfer/MetaInfer|MetaInfer]]：两者都使用 Agent 生成专用引擎；MetaInfer 还突出模型移植、kernel 及异构软硬件协同适配。
- [[community/NVIDIA/Flare/Flare|Flare / Hyperflare]]：Flare 是模型准备与 Rust Serving 分层实现，**并不原生提供 VibeSys 式独立 Judge + 多轮系统合成闭环**。
- [[community/smth-fun/SEIS/SEIS|SEIS]]：同样属于端到端推理系统 RSI；SEIS 公开实验重点是对 mini-SGLang 代码持续修改。

这些边仅表示技术互补/对照，**不代表仓库间存在代码级依赖或正式集成**。

## 值得迁移的设计

适合用于面向 vLLM-Ascend / MindIE 的 RSI Harness：将真实 workload、不可变 Accuracy / Benchmark 命令、每轮实验 Git 快照、只读 Judge 与领域技能分离。将 Ascend Profiler、CANN 构建与 NPU 评测作为新 backend 集成需要独立开发和验收。

## Sources

- https://github.com/uw-syfi/vibesys
- https://arxiv.org/abs/2605.06068
- https://syfi.cs.washington.edu/blog/2026-05-12-introducing-vibeserve/
- https://syfi.cs.washington.edu/blog/2026-10-08-qwen35-mi300a/
- https://syfi.cs.washington.edu/blog/2026-11-04-vibesys-trainium/
