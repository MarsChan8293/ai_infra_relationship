---
type: person
name: Stary
aliases: ["staryxchen", "@staryxchen"]
current_affiliations: ["腾讯"]
linked_companies:
  - "company/腾讯/腾讯"
communities: [Mooncake, FlexKV]
projects: [Mooncake, FlexKV]
roles: [Mooncake Transfer Engine Codeowner, FlexKV Collaborator]
areas: [kv-cache, data-movement, rdma, distributed-storage, llm-inference, gpu-communication]
confidence: verified
last_verified: "2026-09"
---
# Stary（@staryxchen）

公开 GitHub 资料目前只稳定确认昵称 / 公开名 **Stary** 与账号 `@staryxchen`，未找到足够可靠的完整法定姓名，因此本图谱不做实名猜测。

## 当前身份
- [[company/腾讯/腾讯|腾讯（Tencent）]]：GitHub 个人主页公开 affiliation 为 Tencent，所在地深圳。
- [[community/kvcache-ai/Mooncake/Mooncake|Mooncake]]：当前 `CODEOWNERS` 将 `@staryxchen` 列为 `mooncake-transfer-engine` 与 TENT 路径 codeowner 之一。
- [[community/taco-project/FlexKV/FlexKV|FlexKV]]：公开 PR 页面显示其为 Collaborator，并持续参与多 GPU backend、KV transfer 等工作。

## Mooncake ↔ FlexKV 桥
这是一个高价值跨项目工程节点。FlexKV 的 distributed KVCache reuse 官方文档明确使用 Mooncake Transfer Engine 完成跨节点高性能 KVCache 数据传输，而 Stary 同时出现在两边的核心工程网络中。

因此可以建立一条非常直接的推理数据面路径：

`Tencent / TACO → FlexKV → Mooncake Transfer Engine → RDMA / distributed KV reuse`

## 人物 / 项目关系
- [[community/kvcache-ai/Mooncake/任峰 Feng Ren|任峰（Feng Ren）]]、[[university/清华大学/Ruoyu Qin|秦若愚（Ruoyu Qin）]]：共同处于 Mooncake Transfer Engine codeowner / engineering network；不因同一模块自动标记为同事。
- [[community/taco-project/FlexKV/FlexKV|FlexKV]]：活跃 Collaborator；2026-04 的 multi-GPU backend abstraction PR 是公开可核验贡献之一。

## Sources
- https://github.com/staryxchen
- https://github.com/kvcache-ai/Mooncake/blob/main/.github/CODEOWNERS
- https://github.com/taco-project/FlexKV/pulls
- https://github.com/taco-project/FlexKV
