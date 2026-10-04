---
type: project
name: NaiveRT
status: active
docs: https://naive.ai/en/research/
linked_people: []
companies: ["Naive AI"]
layer: runtime
areas:
  - "single-stream-decode"
  - "long-context-rl"
  - "speculative-decoding"
  - "mega-kernel-fusion"
  - "programmatic-dependent-launch"
  - "gpu-driven-scheduling"
  - "deterministic-sampling"
  - "w8a8-kernels"
hardware:
  - "nvidia"
last_verified: "2026-09"
linked_companies:
  - "company/Naive AI/Naive AI"
code_availability: unconfirmed
---
# NaiveRT

## 项目简介

NaiveRT 是 Naive AI 为 [[company/Naive AI/Naive-N0.5-Flash|Naive-N0.5-Flash]] 构建的 inference runtime，目标不是最大化多请求 batching throughput，而是缩短百万 Token 长上下文 RL rollout 中单条 trajectory 的 wall-clock decode 时间。

官方技术报告称 NaiveRT 在 8 GPU single-stream 场景下达到峰值 2,122 tokens/s，并在同一系统上把一次完整 speculative decoding round（draft + verify + sampling + commit）从 [[community/sgl-project/SGLang/SGLang|SGLang]] 路径的 12.3 ms 降至 3.4 ms，即 round latency 下降 72.4%。

这里不把“50 tok/s Standard → 2,000 tok/s Ultrafast”直接写成 NaiveRT 相对 SGLang 的 40× 加速；这两个数字来自不同产品模式。对 SGLang 的同机、同类 full-round 对照是 12.3 ms → 3.4 ms。

## 执行模型

### Mega-kernel

官方 profile 中，一个 DSA layer 在被测 SGLang 配置下每 GPU / 每 decode step 需要 29 次 kernel executions。NaiveRT 将其重组为单个 cooperative mega-kernel，覆盖 RMSNorm、Q/K/V 与 index projections、RoPE、KV cache write、index scoring/top-k、sparse attention、combine、O projection 与 TP tail。

### Programmatic Dependent Launch

未被融合的 kernel boundary 使用 NVIDIA Programmatic Dependent Launch（PDL）连接，使 downstream kernel 可以在 upstream work 尚未完全结束时提前 launch。speculative loop 进一步采用 GPU-driven scheduling，减少 CPU 介入。

### Selective fusion

NaiveRT 没有追求“所有 kernel 都融合”。官方记录显示 MoE fusion 连续做了 7 轮实现仍然导致端到端回退，因此保留 router / up-gate / down projections 三类 kernel，并通过 PDL overlap。这是典型的 whole-model latency engineering，而非只看 isolated microbenchmark。

### Correctness constraint

官方将 deterministic sampling 与 bitwise comparison 作为硬约束：优化在进入性能路径前，需要通过 full-model logits / KV cache 的一致性检查。

## 开源状态

截至 **2026-09-29**：

- Naive AI 官方研究页称 NaiveRT “open source”，并给出了 NaiveRT GitHub / Hugging Face 入口。
- 同一页面明确注明 runtime、fused kernels、benchmark scripts 等内容 **will be available by Oct, 12th**。
- 因此本节点当前不填写 `repository:`，避免把尚未公开可访问的源码仓库误记为已发布代码；待官方仓库可访问后再补。

## 与 SGLang 的关系

[[community/sgl-project/SGLang/SGLang|SGLang]] 在这里同时是：

1. Naive-N0.5-Flash 官方 acknowledgments 中明确感谢的 open-source inference infrastructure；
2. NaiveRT 技术报告中的同机 latency benchmark baseline。

这些证据不足以声明 NaiveRT fork 自 SGLang 或与其存在正式 project integration，因此不在 frontmatter 的 `integrations:` 中建立强边。

## Sources

- https://naive.ai/en/research/
- https://github.com/NaiveAI-Labs/Naive-N0.5-Flash
- https://docs.nvidia.com/cuda/cuda-programming-guide/04-special-topics/programmatic-dependent-launch.html

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/Naive AI/Naive AI|Naive AI]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
