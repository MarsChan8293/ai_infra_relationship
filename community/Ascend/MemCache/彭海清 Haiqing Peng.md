---
type: person
name: 彭海清
english_name: Haiqing Peng
aliases: ["p3rry", "@p3rry", "Peng Haiqing"]
current_affiliations: ["华为"]
public_email: penghaiqing1@huawei.com
email_affiliations:
  - "华为"
linked_companies:
  - "company/华为/华为"
projects: [MemCache, MemFabric]
roles: [Cross-project Contributor, MemFabric Integration Contributor]
areas: [memory-pooling, kv-cache, rdma, 56bit-gva, integration, kv-event, ascend]
confidence: high
last_verified: "2026-09"
---
# 彭海清（Haiqing Peng）

项目：[[MemCache]] · [[MemFabric]]

## 身份核验
MemCache / MemFabric 提交 metadata 使用 `p3rry`，并出现 `penghaiqing1@huawei.com`；MemCache 的 KV Event 集成 MR 还直接提到“基于 @彭海清 工作”，因此可把 handle、拼音邮箱与中文名交叉到同一人物。当前不推断具体职级。

公开职业邮箱：`penghaiqing1@huawei.com`。

## MemCache
- 负责或参与 MemFabric C API / 动态加载解耦、ABI 对齐、stream 字段适配等底层接口工作。
- 在 KV Event / PyMotor affinity 路线上提供了前置框架，后续由 [[Zixi Qu]] 继续完成广播事件与 kv-conductor 对接。

## MemFabric
- 参与 host RDMA / hcom 依赖更新、56-bit GVA 大容量池化整改、release 版本更新等工作。
- 其贡献同时触及 MemFabric 自身和 MemCache 对 MemFabric 的接口边界，是这条数据面链路中很值得继续追的核心工程人物。

## 人物关系
- [[Zixi Qu]]：MemCache KV Event 的后续实现明确说明建立在彭海清前期工作之上，属于有 pair-specific 证据的开源技术协作。
- [[yrewzjsx]]、[[chenyz6]]：其多个 MemCache / MemFabric PR 由两者合入。

## Sources
- https://gitcode.com/Ascend/memcache/tree/develop
- https://gitcode.com/Ascend/memfabric_hybrid/tree/release/1.1

<!-- BEGIN AUTO PERSON COMPANIES -->
## 关联公司（自动汇总）

以下公司由 `current_affiliations:` 与/或 `public_email` 企业域名规则生成。邮箱域名只证明公开上下文中的组织关联，不单独证明当前任职或职级。

- [[company/华为/华为|华为]]：当前 affiliation + 公开职业邮箱域名双重证据。

<!-- END AUTO PERSON COMPANIES -->
