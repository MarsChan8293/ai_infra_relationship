---
type: project
name: LMCache
linked_people:
  - "community/LMCache/LMCache/Baolong Ma"
  - "community/LMCache/LMCache/Samm Shen"
  - "company/TensorMesh/Junchen Jiang"
  - "company/TensorMesh/杜昆泰 Kuntai Du"
  - "company/TensorMesh/程翊华 Yihua Cheng"
companies: ["TensorMesh"]
company_relation: research-to-startup-core-network
layer: kv-cache-management
open_source: true
linked_companies:
  - "company/TensorMesh/TensorMesh"
---
# LMCache

## 项目简介
LMCache 是 LLM KV cache 的分层存储、传输与复用系统，把 KV 从单 GPU 显存扩展到 CPU、远端存储和跨实例数据路径，并通过 connector 接入 serving engine。它重点解决长上下文、prefill/decode 解耦与跨请求复用下的 KV 数据生命周期问题。

## GitHub
https://github.com/LMCache/LMCache

## 主要贡献公司
- [[company/TensorMesh/TensorMesh|TensorMesh]]：LMCache 核心研究/工程人物进入产业化后的主要公司节点，持续连接 KV cache、disaggregated serving 与 vLLM KV Connector。LMCache 本身起源于学术/开源社区，因此这里是 **core network / commercialization**，不是公司所有权。
- IBM、NVIDIA、Red Hat、Microsoft、AMD、Tencent、ByteDance 等公司人员也曾被 LMCache 社区公开列为产业贡献网络；本图谱暂不把一次性/非核心贡献全部升级为主公司边。

## 主要维护者 / 组织
由 LMCache 社区维护，核心网络与 [[TensorMesh]]、University of Chicago systems 研究及 vLLM KV Connector 生态重叠。已记录人物包括 [[程翊华 Yihua Cheng]]、[[杜昆泰 Kuntai Du]]、[[Baolong Ma]]、[[Samm Shen]]。

## 生态关系
[[vLLM]] · [[TensorMesh]] · [[vLLM-Ascend]] · [[Mooncake]] · [[NIXL]]。LMCache 更偏 engine 外部 KV 管理与复用，Mooncake 更强调分布式 KVCache-centric serving/storage，两者有交叉但并非同一项目。

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/LMCache/LMCache/Baolong Ma|Baolong Ma]]：[[TensorMesh/程翊华 Yihua Cheng|程翊华（Yihua Cheng）]]：**LMCache 社区协作者**。截至 2026-09，两人均持续参与 LMCache；程翊华负责 KV cache offloading / connector / 分层缓存等核心技术，Baolong Ma 更偏 contributor onboarding、issue 与社区协作。公开资料不足以确认二人在同一公司共事，因此不标记为“同事”；首次共同参与 LMCache...
- [[community/LMCache/LMCache/Samm Shen|Samm Shen]]：活跃于 LMCache 核心功能规划与社区协作
- [[company/TensorMesh/Junchen Jiang|Junchen Jiang]]：[[LMCache]]：共同创建者 / UChicago 研究网络核心节点。
- [[company/TensorMesh/杜昆泰 Kuntai Du|杜昆泰（Kuntai Du）]]：[[LMCache]]：核心维护、KV cache 系统设计、offloading / connector / 分层缓存
- [[company/TensorMesh/程翊华 Yihua Cheng|程翊华（Yihua Cheng）]]：[[LMCache]]：KV cache offloading、connector、分层缓存与传输

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/TensorMesh/TensorMesh|TensorMesh]]：公司页与社区/项目页均有显式记录；关系：`research-to-startup-core-network`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
