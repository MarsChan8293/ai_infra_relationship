---
type: project
name: Seer
linked_people:
  - "university/清华大学/Mingxing Zhang"
  - "university/清华大学/Ruoyu Qin"
  - "university/清华大学/Yingdi Shan"
companies: ["月之暗面"]
company_relation: industry-academia-research-collaboration
layer: rl-rollout-serving
open_source: false
areas: [llm-serving, reinforcement-learning, rollout, scheduling, speculative-decoding]
last_verified: "2026-09"
linked_companies:
  - "company/月之暗面/月之暗面"
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

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[university/清华大学/Mingxing Zhang|章明星（Mingxing Zhang）]]：[[company/月之暗面/Seer|Seer]]：OSDI 2026 论文作者，与 Ruoyu Qin、[[university/清华大学/Yingdi Shan|闪英迪（Yingdi Shan）]]、[[company/趋境科技/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]]等共同把 MADSys 技术路线延伸到 synchronous LLM RL rollout 与 speculative decoding。
- [[university/清华大学/Ruoyu Qin|秦若愚（Ruoyu Qin）]]：[[company/月之暗面/Seer|Seer]]：OSDI 2026 第一作者，面向 synchronous LLM RL rollout，通过 divided rollout、context-aware scheduling 与 grouped speculative decoding 降低长尾并提高吞吐。
- [[university/清华大学/Yingdi Shan|闪英迪（Yingdi Shan）]]：[[company/月之暗面/Seer|Seer]]：OSDI 2026 论文作者，与 [[university/清华大学/Mingxing Zhang|章明星（Mingxing Zhang）]]、[[university/清华大学/Ruoyu Qin|Ruoyu Qin]]、[[company/趋境科技/武永卫 Yongwei Wu|武永卫（Yongwei Wu）]]共同参与 synchronous LLM RL rollout 系统研究。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/月之暗面/月之暗面|月之暗面]]：公司页与社区/项目页均有显式记录；关系：`industry-academia-research-collaboration`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
