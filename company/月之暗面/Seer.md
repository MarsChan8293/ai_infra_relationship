---
type: project
name: Seer
companies: ["月之暗面"]
company_relation: industry-academia-research-collaboration
layer: rl-rollout-serving
open_source: false
areas: [llm-serving, reinforcement-learning, rollout, scheduling, speculative-decoding]
last_verified: "2026-09"
---
# Seer

## 项目简介
Seer 是面向 synchronous LLM reinforcement learning 的 rollout 系统，发表于 OSDI 2026。它针对 rollout 阶段的长尾延迟与资源利用率问题，引入 divided rollout、context-aware scheduling 与 adaptive grouped speculative decoding。

USENIX 公布的 production-grade RL workload 实验中，Seer 的端到端 rollout throughput 最高提升 2.04×，同时显著降低长尾延迟。

## 研究 / 产业协作网络
作者网络横跨 [[company/月之暗面/月之暗面|月之暗面（Moonshot AI）]] 与 [[university/清华大学/清华大学|清华大学]]：
- [[university/清华大学/Ruoyu Qin|Ruoyu Qin]]：第一作者；作者单位同时列出 Moonshot AI 与 Tsinghua University。
- [[university/清华大学/Yingdi Shan|闪英迪（Yingdi Shan）]]：清华作者，连接 storage/distributed systems 与 RL serving。
- [[company/趋境科技/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]]、[[university/清华大学/Mingxing Zhang|章明星（Mingxing Zhang）]]：清华作者与 MADSys systems 网络。
- Moonshot AI 侧还包括 Weiran He、Weixiao Huang、Yangkun Zhang、Yikai Zhao、Bo Pang、Xinran Xu。

## 图谱意义
Seer 把章明星 / MADSys 的系统研究从 `KV cache / heterogeneous inference` 推进一步，进入 `RL rollout scheduling + speculative decoding`。它也是 Ruoyu Qin 从 Mooncake serving 路线向 RL infra 延伸的强项目证据。

## Sources
- https://www.usenix.org/conference/osdi26/presentation/qin
- https://www.usenix.org/conference/osdi26/technical-sessions
