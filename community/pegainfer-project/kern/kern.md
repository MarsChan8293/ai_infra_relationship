---
type: project
name: Kern
aliases: ["kern", "pegainfer kern"]
layer: inference-engine
status: active
maturity: research-prototype
code_availability: public
repository: https://github.com/pegainfer-project/kern
docs: https://github.com/pegainfer-project/kern/tree/master/docs
areas:
  - llm-inference
  - dedicated-inference-engine
  - inference-framework-generation
  - agentic-inference-optimization
  - inference-rsi
  - manifest-driven-execution
  - cuda-graph
  - kv-cache
  - parallelism
hardware:
  - nvidia
integrations: []
companies: []
company_relation: community-led
linked_concepts:
  - "concept/inference/optimization/Agentic Inference Optimization"
last_verified: "2026-11"
---

# Kern

## 项目定位

[Kern](https://github.com/pegainfer-project/kern) 是面向 **model × workload × GPU** 专用推理引擎的 Runtime 与 Agent 优化基础设施。它把具体模型的执行逻辑从通用 serving 引擎里抽出，作为独立可修改、可验证、可交付的 model package；**不是仅生成一个 CUDA kernel**。

上游介绍将每个模型包拆为 `manifest.json`、`kernels/`、模型权重；模型无关 Runtime 加载 Manifest、分配 Buffer/State、绑定权重、执行 Kernel，适用时捕获/回放 CUDA Graph。Manifest 声明 buffers、state、ops、programs、parallel topology、collective launches 与 serving contract，Agent 可以对这些目标做局部修改而不需要修改整个通用引擎。

## Agent / RSI 闭环

- `kern verify` 检查 Manifest 的类型、边界与执行声明。
- `kern test` 对参考实现和候选实现进行差异、正确性和性能门禁。
- Agent 可替换 kernel、修改 fusion 与执行次序、调整模型特定并行部署，再用真实 trace / benchmark 决定保留或回退。
- 项目公开了 vLLM/SGLang 工作负载与 DeepSeek-V4.1-Flash（GB300 / HGX B300 专用 Manifest、EP4）示例；特定模型组合的可用性必须以对应 package / GPU 实测为准。

## 与专用引擎生成项目的关系

- [[community/NVIDIA/Flare/Flare|Flare / Hyperflare]]：两者都把模型专用执行逻辑与通用运行时隔离；Flare 偏 **Ignition 构建期准备 → Helios Rust Serving**，Kern 偏 **声明式 Manifest + model-agnostic Runtime + Agent 可修改执行程序**。这是架构对照，不代表直接集成。
- [[community/MetaInfer/MetaInfer|MetaInfer]]：后者让 Agent 生成紧凑的推理框架代码，Kern 更强调统一 Runtime 上的专用可验证模型包。
- [[community/uw-syfi/vibesys/VibeSys|VibeSys]]：后者的 Agent 可以从既有代码或零开始重构完整 serving stack；Kern 则约束模型执行界面以缩小优化和验收空间。
- [[concept/inference/optimization/Agentic Inference Optimization|Agentic Inference Optimization]]：该领域的端到端推理执行优化实现。

## 硬件与验证边界

当前公开 Runtime 主要绑定 NVIDIA CUDA 驱动和 GPU；**不将 Ascend/CANN 标为原生支持**。移植 910C / 950PR 时可借鉴 typed manifest、state ownership、正确性门禁和 GPU/模型特定 package，但需要重建 backend、collective、graph capture 以及异构数值测试。浮点容差或 KL 一致性与 logits / KV 逐位一致验收不等价。

## Sources

- https://github.com/pegainfer-project/kern
- https://github.com/pegainfer-project/kern/blob/master/docs/vllm-rsi-example.md
- https://github.com/pegainfer-project/kern/blob/master/docs/sglang.md
- https://github.com/pegainfer-project/kern/blob/master/docs/serve.md
- https://github.com/pegainfer-project/kern/blob/master/docs/registry.md
