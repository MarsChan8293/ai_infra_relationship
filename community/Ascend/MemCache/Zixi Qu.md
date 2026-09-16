---
type: person
name: Zixi Qu
aliases: ["huawei_zixiqu", "zixiqu", "ZixiQu"]
current_affiliations: ["华为"]
public_email: quzixi@huawei.com
email_affiliations:
  - "华为"
linked_companies:
  - "company/华为/华为"
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

公开职业邮箱：`quzixi@huawei.com`。

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

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/华为/华为|华为]]：当前 affiliation + 公开职业邮箱域名双重证据。

<!-- END AUTO PERSON COMPANIES -->
