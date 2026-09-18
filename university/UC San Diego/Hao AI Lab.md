---
type: research-institution
name: "Hao AI Lab"
aliases: ["HaoAI Lab"]
organization: "UC San Diego"
linked_people: []
areas: [machine-learning-systems, llm-serving, distributed-systems, speculative-decoding, model-parallelism]
projects:
  - vLLM
  - DistServe
  - "Lookahead Decoding"
  - FastChat
website: https://cseweb.ucsd.edu/~haozhang/
country: "USA"
city: "San Diego, CA"
last_verified: "2026-09"
---
# Hao AI Lab

Hao AI Lab 由 UC San Diego 的 Hao Zhang 领导。官方主页将 **LLM inference and serving systems** 单列为当前研究方向，并把 vLLM、DistServe、Dynasor、DeepConf 放在同一条系统主线上。

## AI Infra 主线

- [[vLLM]]：高吞吐、memory-efficient LLM inference engine；Hao Zhang 的官方主页列为长期维护的开源系统之一。
- [[community/LLMServe/DistServe/DistServe|DistServe]]：OSDI 2024 prefill/decode disaggregation serving system。
- [[community/lmsys-org/Lookahead-Decoding/Lookahead-Decoding|Lookahead Decoding]]：无需 draft model 的 parallel decoding 研究路线。
- [[community/lmsys-org/FastChat/FastChat|FastChat]]：Hao Zhang 主页列出的 previous project，连接 UCSD 与 LMSYS 早期 serving / evaluation 历史。
- 当前研究还包括 Dynasor、DeepConf，以及 model-parallel ML systems。

## 图谱价值

这个节点把仓库已有的 **vLLM → DistServe → LMSYS/Lookahead** 多条边收束到一个明确的学术系统研究源头，并提供 UCSD 人才扩散的起点。

项目出现在 Hao Zhang / Hao AI Lab 官方主页中表示直接研究或维护关系，不表示这些开源项目由该实验室单独治理。

## Sources
- https://cseweb.ucsd.edu/~haozhang/
