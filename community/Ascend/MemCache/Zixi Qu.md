---
type: person
name: Zixi Qu
aliases: ["huawei_zixiqu", "zixiqu", "ZixiQu"]
current_affiliations: ["华为"]
projects: [MemCache, MemFabric]
roles: [KV Event Contributor, Cross-project Contributor]
areas: [kv-cache, kv-event, prefill-affinity, distributed-serving, security, memory-pooling, ascend]
confidence: high
last_verified: "2026-09"
---
# Zixi Qu

项目：[[MemCache]] · [[MemFabric]]

## 身份核验
2026 年 MemCache / MemFabric 提交 metadata 同时出现 `huawei_zixiqu`、`zixiqu`、`Zixi Qu` 与 `quzixi@huawei.com`，因此这些 handle 可可靠归并到同一项目人物。这里仅依据当前项目提交记录确认华为 affiliation，不与外部同名个人自动合并。

## MemCache
- 推进 KV Event：增加 key store/remove/clear 广播，使 PyMotor 的 kv-conductor 能做 prefill 节点亲和性计算。
- 该 MR 明确说明工作基于 [[彭海清 Haiqing Peng|彭海清]] 的前期框架，形成一条可核验的人物技术协作边。
- 后续继续推进 KV Event 的 ZMQ 通道、安全加密、IPv6，以及 key eviction / prefetch 等相关路径。

## MemFabric
- 在 memfabric_hybrid 中参与 examples / naming 等改动，说明其活动跨越存储上层与内存池化底座。

## 人物关系
- [[彭海清 Haiqing Peng|彭海清]]：KV Event / PyMotor affinity 路线存在直接继承式工程协作证据。
- [[chenyz6]]：KV Event 主体与安全相关 MR 多次由 chenyz6 合入。
- [[gcw_qYJeyWK4]]：共同推进 key eviction / prefetch，直接落在分层 KV cache 数据管理路径。

## Sources
- https://gitcode.com/Ascend/memcache/tree/develop/3rdparty
- https://gitcode.com/Ascend/memcache/tree/develop/test
- https://gitcode.com/Ascend/memfabric_hybrid/tree/master/examples
