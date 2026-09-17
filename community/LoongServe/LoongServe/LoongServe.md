---
type: project
name: LoongServe
organization: Peking University / Shanghai AI Laboratory
linked_people:
  - "community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu"
  - "company/深度求索/Yinmin Zhong"
  - "university/北京大学/Bingyang Wu"
  - "university/北京大学/Xin Jin"
layer: long-context-llm-serving
open_source: true
repository: https://github.com/LoongServe/LoongServe
areas: [llm-serving, long-context, sequence-parallelism, kv-cache, scheduling, distributed-inference]
last_verified: "2026-09"
linked_companies: []
---
# LoongServe

LoongServe 是面向长上下文 LLM serving 的系统，提出 Elastic Sequence Parallelism（ESP），根据请求与阶段实时调整 sequence parallelism，从计算、通信和 KV-cache memory 三侧提高长上下文推理效率。论文发表于 SOSP 2024。

## 刘胜与网络
- [[university/北京大学/Bingyang Wu|Bingyang Wu]]、[[community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu|刘胜与]]、[[company/深度求索/Yinmin Zhong|Yinmin Zhong]]、Peng Sun、Xuanzhe Liu、[[university/北京大学/Xin Jin|Xin Jin]] 构成论文作者网络。
- 对刘胜与而言，LoongServe 把其研究从 DistServe 的 prefill/decode disaggregation 推进到长上下文的动态并行、KV migration 和多实例显存管理。

## Sources
- https://arxiv.org/abs/2404.09526
- https://github.com/LoongServe/LoongServe
- https://interestinglsy.github.io/
- https://xinjin.github.io/publications.html

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu|刘胜与（Shengyu Liu）]]：[[community/LoongServe/LoongServe/LoongServe|LoongServe]]：SOSP 2024，Elastic Sequence Parallelism，面向 long-context serving 的动态并行与 KV-cache 管理。
- [[company/深度求索/Yinmin Zhong|Yinmin Zhong]]：[[community/LoongServe/LoongServe/LoongServe|LoongServe]]：共同作者，长上下文 serving。
- [[university/北京大学/Bingyang Wu|Bingyang Wu]]：项目关联；人物页已明确记录该项目。
- [[university/北京大学/Xin Jin|Xin Jin]]：[[community/LoongServe/LoongServe/LoongServe|LoongServe]]：elastic sequence parallelism for long-context serving。

<!-- END AUTO PROJECT PEOPLE -->
