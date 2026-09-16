---
type: person
name: chloroethylene
aliases: ["@chloroethylene"]
communities: [LMCache, vLLM-Ascend]
roles: [Ascend Integration Contributor, LMCache-Ascend Connector Author]
areas: [kv-cache, ascend, npu, multiprocess, vllm-ascend, kv-connector, mla, dsa, pin-memory]
confidence: high
last_verified: "2026-09"
---
# chloroethylene

`chloroethylene` 是当前 **LMCache ↔ vLLM-Ascend ↔ Ascend NPU** 路线中非常直接的工程桥节点。公开提交使用个人 Gmail，因此不据此推断公司或真实姓名。

## vLLM-Ascend
2026-03，其直接向 vLLM-Ascend 合入 `LMCacheAscendConnector`（#6882），将 LMCache-Ascend 注册为 vLLM-Ascend 可选择的 KV connector / KV cache pooling 路径。

## LMCache
2026 年继续在 LMCache 上推进 Ascend MP：
- #3968（已合入）：把 Ascend NPU 作为 LMCache MP first-class platform，并支持 vLLM-Ascend per-layer `(K,V)` tuple KV format；
- #4763（已合入）：通过 AscendCL `aclrtHostRegister` 增加 NPU pinned-memory backend，使 MP D2H/H2D 真正异步；
- #5138（截至 2026-09-16 open）：继续支持 vLLM-Ascend MLA / DSA plane tuples，并在 Ascend 910B 上验证 roundtrip / detection。

这条贡献链说明 LMCache 的 Ascend 支持已经从外部插件邻接进入 upstream MP/KV-format/platform 适配阶段。

## Sources
- https://github.com/vllm-project/vllm-ascend/commit/6852a2e267e1ad6eafd4399b0b2d134a8f9dbe93
- https://github.com/LMCache/LMCache/pull/3968
- https://github.com/LMCache/LMCache/pull/4763
- https://github.com/LMCache/LMCache/pull/5138
