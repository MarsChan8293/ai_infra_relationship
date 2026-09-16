---
type: person
name: yrewzjsx
aliases: ["@yrewzjsx"]
current_affiliations: ["华为"]
projects: [MemCache, MemFabric]
roles: [Frequent Merge Gatekeeper, Core Contributor]
areas: [kv-cache, memory-pooling, performance, reliability, ascend]
confidence: project-credit
last_verified: "2026-09"
---
# yrewzjsx

项目：[[MemCache]] · [[MemFabric]]

## 公开身份
公开仓库 merge metadata 长期使用 `yrewzjsx` handle；提交记录中的协作者字段出现 `zhangjinshi2@huawei.com`，足以确认华为项目 affiliation，但当前不据邮箱猜中文实名或职级。

## MemCache
- 在 MemCache 的大量 MR 中持续出现 `Merged-by: yrewzjsx`，覆盖配置、存储层、KV Event、CI、文档、可靠性等多个子系统，是当前最明显的代码入口 / 合并把关者之一。
- 同时存在直接工程贡献，例如 benchmark 优化、聚合参数调优等，不只是机械 merge 账号。

## MemFabric
- 在 MemFabric / memfabric_hybrid 的 develop、release 分支同样持续参与 merge，并与 [[chenyz6]] 形成跨仓库重复 review / merge 邻接。
- 这种同时覆盖 MemCache 与 MemFabric 的模式，使其成为 KV 存储层与数据搬运层之间的重要人物桥梁。

## 人物关系
- [[chenyz6]]：MemCache 与 MemFabric 中存在大量交叉 merge / review 记录；可以确认长期开源工程协作，但当前不从仓库权限进一步推断正式组织职级。
- [[j00808874]]、[[shilinlee]]、[[彭海清 Haiqing Peng|彭海清]]、[[Zixi Qu]]：多次作为其合入 PR 的作者或共同贡献者，形成 MemCache / MemFabric 核心工程邻接网络。

## Sources
- https://gitcode.com/Ascend/memcache/tree/develop
- https://gitcode.com/Ascend/memfabric_hybrid/tree/master
