---
type: person
name: DreamerLeader
aliases: ["@DreamerLeader"]
projects: [MemCache, vLLM-Ascend]
roles: [KV Pool RFC Author, Connector Architecture Contributor]
areas: [kv-cache, pooling, connector-abstraction, pcp, dcp, ascend]
confidence: project-credit
last_verified: "2026-09"
---
# DreamerLeader

项目：[[MemCache]] · [[vLLM-Ascend]]

## vLLM-Ascend × MemCache
- 2026-01 发起 vLLM-Ascend RFC #6410，明确提出把 MemCache 纳入 KV Pool storage backend，并将原有 MooncakeStoreConnector 抽象为统一的 AscendStoreConnector + Backend 接口。
- 更早的 RFC #4312 讨论 KV pooling 与 PCP / DCP 的组合，属于 AscendStore / KV Pool 架构演进的重要公开设计线索。
- 后续还持续跟踪 DeepSeek V4 pooling 问题，说明其活动不止一次性提案。

这里把 DreamerLeader 记录为 **RFC / connector architecture contributor**，不据 RFC 作者身份推断 maintainer 或正式项目治理角色。

## Sources
- https://github.com/vllm-project/vllm-ascend/issues/6410
- https://github.com/vllm-project/vllm-ascend/issues/4312
- https://github.com/vllm-project/vllm-ascend/issues/9960
