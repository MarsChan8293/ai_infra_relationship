---
type: person
name: gcw_qYJeyWK4
aliases: ["@gcw_qYJeyWK4"]
current_affiliations: ["华为"]
projects: [MemCache]
roles: [Storage-tier Contributor]
areas: [kv-cache, eviction, prefetch, ssd-tiering, ubsio, reliability, ascend]
confidence: project-credit
last_verified: "2026-09"
---
# gcw_qYJeyWK4

项目：[[MemCache]]

## 公开身份
公开提交 metadata 使用 `gcw_qYJeyWK4`，并出现 `jiangbo97@huawei.com`，因此记录华为 affiliation；当前不根据邮箱猜中文实名。

## MemCache
- 2026 年持续推进配置加载、UBS IO、Python 动态加载等工程路径。
- 与 [[Zixi Qu]] 共同实现 key eviction / prefetch，把 key 从 DRAM 下放到 SSD、再从 SSD 拉回 DRAM，直接落在多级 KV cache 的冷热迁移核心路径。
- 还涉及 async flush、rewarm 等 storage tier / reliability 工作，是当前 MemCache 分层存储方向非常值得继续追的人物。

## 人物关系
- [[Zixi Qu]]：共同提交 key eviction / prefetch 特性，属于明确的开源技术协作。
- [[yrewzjsx]]：其近期多个存储与配置 PR 由 yrewzjsx 合入。

## Sources
- https://gitcode.com/Ascend/memcache/tree/develop
- https://gitcode.com/Ascend/memcache/tree/master/config
