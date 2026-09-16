---
type: project
name: MemCache
companies: ["华为"]
company_relation: company-led
layer: kv-cache
hardware: [Ascend]
open_source: true
repository: https://gitcode.com/Ascend/memcache
areas: [kv-cache, distributed-storage, prefix-cache, memory-pooling, disaggregated-serving, ascend]
linked_people: []
last_verified: "2026-09"
---
# MemCache

## 项目简介
MemCache 是 Ascend 生态面向 AI / LLM 推理的高性能分布式 KV Cache 存储引擎。它把 HBM、DDR、SSD 等多级介质组织成缓存池，并通过 [[MemFabric]] 提供的跨机、跨介质直接访问能力降低 KV 数据搬运开销。

它对本图谱的重要性在于：这是昇腾侧少数直接落在 **KV Cache 池化 / Prefix Cache / 分离式推理数据面** 的开源项目，位置介于 serving engine 与硬件数据传输层之间。

## GitCode
https://gitcode.com/Ascend/memcache

## GitHub 镜像
https://github.com/Ascend/memcache

## 推理优化主线
- **多级 KV Cache 池**：支持 HBM / DDR / SSD 等多层缓存池，以及冷热数据淘汰、预取。
- **OneCopy 数据路径**：底层依赖 [[MemFabric]]，在不同 Ascend 硬件上利用 device RDMA / SDMA、host RDMA、URMA、UBOE 等路径完成跨节点与跨介质访问。
- **Prefix Cache**：官方 2026-06 动态明确给出 MemCache 使能推理 PrefixCache 的案例。
- **高可用与解耦部署**：仓库持续出现 MetaService HA、分离部署、地址导出、KV offload 等工程改动。

## Serving / KV 生态关系
- [[MemFabric]]：**强依赖 / 数据传输底座**。MemCache 官方安装与 README 均明确依赖 MemFabric。
- [[vLLM-Ascend]]：**已验证 KV Pool backend**。vLLM-Ascend 官方 KV Pool 文档提供以 MemCache 作为 backend 的部署流程。
- [[SGLang]]：MemCache 官方 README 明确列为已对接的开源推理框架之一；后续 BFS 继续核验具体 connector / adapter 路径与负责人。
- [[MindIE-LLM]]：MemCache 官方 README 明确列为已对接的昇腾推理框架之一；后续继续追具体集成边。
- [[Mooncake]]：属于同一 KV cache / data movement 邻域。MemCache 2026 年提交中出现与 Mooncake API 对齐的改动，但这里暂不写成直接治理或共同维护关系。

## 第一轮人物探索候选
当前仓库 merge metadata 中反复出现 `yrewzjsx`、`chenyz6`、`shilinlee_com` / `shilinlee`、`p3rry`、`j00808874` 等 handle，分别覆盖 merge、核心 API、MemFabric 解耦、HA / REST、构建与性能路径。

这些信号足以进入下一轮人物调查，但**本轮不直接把它们标成 maintainer**：目前尚未找到稳定的 MAINTAINERS / CODEOWNERS / governance 文件来证明正式治理角色，也不根据邮箱或 handle 猜实名与职级。

## BFS 下一跳
1. `MemCache -> maintainers / core reviewers`：优先找 governance、长期 merge 权限与 release 责任人。
2. `MemCache -> MemFabric -> maintainers`：识别 KV 存储层与数据移动层是否由同一批核心工程师连接。
3. `MemCache -> vLLM-Ascend`：追具体 KV connector / backend PR 与两侧直接协作者。
4. `MemCache -> SGLang / MindIE-LLM`：确认实际 adapter、接口 owner 和性能优化贡献者。
5. `MemCache -> Mooncake / LMCache`：只比较工程边界、API 对齐和竞争/互补关系，不因功能相似自动建立人物关系。

## Sources
- https://gitcode.com/Ascend/memcache/tree/develop
- https://gitcode.com/Ascend/memcache/blob/develop/README.md
- https://github.com/Ascend/memcache
- https://docs.vllm.ai/projects/ascend/en/main/user_guide/feature_guide/kv_pool.html
