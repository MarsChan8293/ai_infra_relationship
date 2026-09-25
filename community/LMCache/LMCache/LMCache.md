---
type: project
name: LMCache
linked_concepts:
  - "concept/memory/CXL Memory"
  - "concept/memory/Host Memory"
  - "concept/inference/kv-cache/KV Cache Management"
  - "concept/inference/kv-cache/KV Cache Offloading"
  - "concept/inference/kv-cache/KV Cache Sharing"
  - "concept/inference/kv-cache/KV Cache Transfer"
  - "concept/memory/Memory Hierarchy"
  - "concept/inference/serving/P-D Disaggregation"
  - "concept/inference/kv-cache/Tiered KV Cache"
status: active
docs: https://docs.lmcache.ai/
linked_people:
  - "community/LMCache/LMCache/Andy Luo"
  - "community/LMCache/LMCache/chloroethylene"
  - "community/LMCache/LMCache/deng451e"
  - "community/LMCache/LMCache/Dongjoo Seo"
  - "community/LMCache/LMCache/Hunter Zhang"
  - "community/LMCache/LMCache/Oasis-Git"
  - "community/LMCache/LMCache/Roy Huang"
  - "community/LMCache/LMCache/Rui Zhang"
  - "community/LMCache/LMCache/Samm Shen"
  - "community/LMCache/LMCache/Shaoting Feng"
  - "community/LMCache/LMCache/Tony Lin"
  - "community/LMCache/LMCache/Zhengfei He"
  - "company/IBM/Martin Hickey"
  - "company/TensorMesh/Jiayi Yao"
  - "company/TensorMesh/Junchen Jiang"
  - "company/TensorMesh/杜昆泰 Kuntai Du"
  - "company/TensorMesh/程翊华 Yihua Cheng"
  - "company/腾讯/Baolong Mao"
  - "company/腾讯/Chunxiao Zheng"
companies: ["TensorMesh"]
company_relation: research-to-startup-core-network
layer: kv-cache
repository: https://github.com/LMCache/LMCache
areas:
  - "kv-cache"
  - "distributed-kv-cache"
  - "offloading"
  - "storage-backend"
  - "p2p"
  - "disaggregated-serving"
  - "multiprocess"
  - "cacheblend"
  - "vllm-integration"
  - "sglang-integration"
  - "ascend"
  - "rocm"
  - "cxl"
  - "prefix-reuse"
  - "remote-kv-cache"
  - "kv-transfer"
  - "observability"
people:
  - "company/TensorMesh/Junchen Jiang"
  - "company/TensorMesh/杜昆泰 Kuntai Du"
  - "company/TensorMesh/程翊华 Yihua Cheng"
  - "company/TensorMesh/Jiayi Yao"
  - "community/LMCache/LMCache/Samm Shen"
  - "company/腾讯/Baolong Mao"
  - "company/腾讯/Chunxiao Zheng"
  - "community/LMCache/LMCache/Shaoting Feng"
  - "company/IBM/Martin Hickey"
hardware:
  - "nvidia"
integrations:
  - "vLLM"
  - "llm-d"
  - "NIXL"
last_verified: "2026-09"
linked_companies:
  - "company/TensorMesh/TensorMesh"
---
# LMCache

## 项目简介
LMCache 是 LLM KV cache 的分层存储、传输、共享与复用系统，把 KV 从单 GPU HBM 扩展到 CPU、远端存储和跨实例/跨节点数据路径，并通过 connector 接入主流 serving engine。到 2026 年，其技术重点已从单进程 offload 扩展到 multiprocess（MP）架构、distributed KV、P2P sharing、PD disaggregation、CacheBlend / sparse KV reuse、KV management interface 和多硬件/多存储后端。

## 当前治理 / 维护网络
官方 `MAINTAINERS.md` 当前列出 10 名 Committer，包括 Yihua Cheng、Jiayi Yao、Kuntai Du、Martin Hickey、Hunter Zhang、Baolong Mao、Chunxiao Zheng、Shaoting Feng、Samuel Shen、Dongjoo Seo。

当前 `CODEOWNERS` 进一步把责任细化到 core engine、cache controller、multiprocess、distributed/L2、GPU connector、platform、lookup client、storage backends、serving-engine integrations、C extensions、operator、ROCm、CI 等模块。这一层比 contributor list 更适合构建 maintainer / component-owner 强边。

## 2026 新增工程骨架
- [[community/LMCache/LMCache/Tony Lin|Tony Lin（hlin99）]]：Intel；distributed eviction、GPU connector、platform、storage backend、vLLM integration 等跨模块 CODEOWNER。
- [[community/LMCache/LMCache/Andy Luo|Andy Luo（andyluo7）]]：AMD；ROCm / AMD Instinct、GPU connector、MP、ATOM 与 packaging 路线。
- [[community/LMCache/LMCache/Dongjoo Seo|Dongjoo Seo（DongDongJu）]]：Samsung Committer；MP、distributed/L2、DAX/CXL、SGLang、C extensions、Rust / operator。
- [[community/LMCache/LMCache/Oasis-Git|Oasis-Git]]：MP observability、L1/L2 telemetry、fault tolerance 与 SGLang integration。
- [[community/LMCache/LMCache/Roy Huang|Roy Huang]]：isolated CUDA IPC、VMM IPC、MP observability、operator → vLLM deployment。
- [[community/LMCache/LMCache/Rui Zhang|Rui Zhang]]：MP coordinator / control plane、operator 与 CLI。
- [[community/LMCache/LMCache/Zhengfei He|Zhengfei He]]：distributed/L2、Valkey、NIXL、storage backend 与 transfer profiling。
- [[community/LMCache/LMCache/deng451e|deng451e]]：CacheBlend、sparse prefetch 与 vLLM integration；身份只保留公开 handle，不推断公司。
- [[community/LMCache/LMCache/chloroethylene|chloroethylene]]：LMCache ↔ vLLM-Ascend 的 Ascend MP / KV format / connector 桥节点。

## Serving Engine 关系
### vLLM
LMCache 与 vLLM 已是双向工程集成关系，而不是单纯外部插件。vLLM 自身保留 `LMCacheConnectorV1`；Jiayi Yao、Baolong Mao、Samuel Shen、Martin Hickey 等都有可核验的 vLLM 侧直接 commit 或 connector 维护证据。Tony Lin、deng451e 等当前也直接 ownership `lmcache/integration/vllm/` 路径。

### SGLang
LMCache 已有独立 `lmcache/integration/sglang/` 路径。当前最值得跟踪的是 Chunxiao Zheng 发起的 **UnifiedRadixCache ↔ LMCache MP** 双仓集成：LMCache PR #4828 与 SGLang PR #38652 截至 2026-09-16 均为 open。PR 中已给出 DeepSeek-V4-Flash 与 Qwen-3.5-27B 的 prefix reuse、filesystem-hit 与 accuracy 验证，但在合入前仍标记为 active integration，不写成稳定发布能力。

### TensorRT-LLM / ATOM
`lmcache/integration/tensorrt_llm/` 已有独立 adapter 与 ownership；2026 年 MP 架构又扩展到 ATOM。LMCache 正从“vLLM 的 KV offload 插件”逐步变成可跨多个 serving engine 的共享 cache runtime。

## Ascend / vLLM-Ascend
Ascend 路线已经从 roadmap 进入 upstream implementation：
- 2026-03，[[community/LMCache/LMCache/chloroethylene|chloroethylene]] 向 vLLM-Ascend 合入 `LMCacheAscendConnector`（vLLM-Ascend #6882）；
- LMCache #3968 于 2026-08-27 合入，将 Ascend NPU 纳入 MP platform，并识别 vLLM-Ascend per-layer `(K,V)` KV format；
- LMCache #4763 于 2026-09-01 合入，通过 AscendCL `aclrtHostRegister` 提供 NPU pinned-memory backend，让 MP gather/scatter 的 D2H/H2D 可真正异步；
- LMCache #5138 截至 2026-09-16 仍 open，继续处理 vLLM-Ascend MLA / DSA plane tuples，并报告 Ascend 910B roundtrip / detection 验证。

因此当前最合理的图谱语义是 **active upstream integration**，而不是“规划中”或“已全部成熟”。

## Storage / 数据路径关系
- **Mooncake Store**：LMCache 有 MooncakeStore L2 adapter、storage connector、lookup client；Baolong Mao / Chunxiao Zheng 在这些路径有明确 CODEOWNERS。这里表示 LMCache 侧技术集成，不等价于二人是 Mooncake maintainer。
- **Valkey / Redis / S3 / filesystem / native L2**：形成越来越清晰的 L2 adapter 层；Zhengfei He 直接推进 Valkey standalone / cluster adapter。
- **Device-DAX / CXL**：Dongjoo Seo 持续推进 DAX hotplug、DAX L2 batching 等路线。#4338 曾验证 coordinator-owned shared Device-DAX L1 与 SGLang → vLLM 跨节点 KV sharing，但该 PR 已于 2026-09-14 closed、未合入，因此只保留为实验性证据，不标记为当前稳定能力。
- **CacheBlend / sparse reuse**：`deng451e` 持续推进 fused-KV geometry、blend-rate correctness 与 sparse-prefetch 生命周期，是 LMCache 从 prefix-only reuse 向更细粒度 KV reuse 扩展的重要路线。

## 硬件生态
LMCache 当前已明显从 CUDA-only 向多平台展开：
- **AMD / ROCm**：[[community/LMCache/LMCache/Andy Luo|Andy Luo]] 已进入 ROCm 相关 CODEOWNERS；
- **Ascend NPU**：已有合入的 MP platform / pinned-memory 支持，并持续补 MLA/DSA KV format；
- **Intel**：[[community/LMCache/LMCache/Tony Lin|Tony Lin]] 横跨 platform / connector / distributed 路径；
- **Samsung / CXL-DAX**：[[community/LMCache/LMCache/Dongjoo Seo|Dongjoo Seo]] 推进存储级 KV cache 路线；
- Moore Threads / MUSA、MetaX MACA、AWS Trainium 等也有持续工程工作，但这里暂不因硬件支持本身推断公司级 LMCache 治理关系。

## TensorMesh 与公司关系原则
[[company/TensorMesh/TensorMesh|TensorMesh]] 由 LMCache 核心研究/工程网络产业化而来，并持续维护 LMCache，因此保留 `research-to-startup-core-network` 公司级边。Tencent、IBM、Intel、AMD、Samsung、ByteDance 等虽然都有明确人物贡献或职业邮箱证据，但**员工参与不会自动升级为公司治理/所有权关系**；公司级项目边仍要求独立组织证据。

## 下一轮 BFS
优先追踪：
1. UnifiedRadixCache 双仓 PR 的 reviewer / merge network，尤其 Chunxiao Zheng ↔ SGLang maintainers；
2. `chloroethylene` 的 LMCache-Ascend / vLLM-Ascend review network，以及 #5138 后续落地；
3. Dongjoo Seo / Rui Zhang / Zhengfei He 周围的 MP coordinator + DAX/CXL + L2 storage 子图；
4. CacheBlend / sparse prefetch 与 SGLang SparDA 等更细粒度 KV reuse 路线。

## Sources
- https://github.com/LMCache/LMCache
- https://github.com/LMCache/LMCache/blob/dev/MAINTAINERS.md
- https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS
- https://github.com/LMCache/LMCache/pull/4828
- https://github.com/sgl-project/sglang/pull/38652
- https://github.com/LMCache/LMCache/pull/3968
- https://github.com/LMCache/LMCache/pull/4763
- https://github.com/LMCache/LMCache/pull/5138
- https://github.com/LMCache/LMCache/pull/4338
- https://blog.lmcache.ai/en/2026/01/21/p2p-1/
- https://blog.lmcache.ai/en/2025/03/31/cacheblend-best-paper-acm-eurosys25-enabling-100-kv-cache-hit-rate-in-rag/

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/LMCache/LMCache/Andy Luo|Andy Luo]]：https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS
- [[community/LMCache/LMCache/chloroethylene|chloroethylene]]：#3968（已合入）：把 Ascend NPU 作为 LMCache MP first-class platform，并支持 vLLM-Ascend per-layer `(K,V)` tuple KV format；
- [[community/LMCache/LMCache/deng451e|deng451e]]：https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS
- [[community/LMCache/LMCache/Dongjoo Seo|Dongjoo Seo]]：https://github.com/LMCache/LMCache/blob/dev/MAINTAINERS.md
- [[community/LMCache/LMCache/Hunter Zhang|Hunter Zhang]]：https://github.com/LMCache/LMCache/blob/dev/MAINTAINERS.md
- [[community/LMCache/LMCache/Oasis-Git|Oasis-Git]]：[[community/LMCache/LMCache/Samm Shen|Samuel Shen]]：L2 performance / telemetry CI 多个 commit 有直接 co-author 证据，因此建立 `open-source-collaboration` / `technical-collaboration`。
- [[community/LMCache/LMCache/Roy Huang|Roy Huang]]：LMCache operator 向 vLLM pod 注入 payload。
- [[community/LMCache/LMCache/Rui Zhang|Rui Zhang]]：https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS
- [[community/LMCache/LMCache/Samm Shen|Samuel Shen]]：`lmcache/integration/vllm/`：CODEOWNER；
- [[community/LMCache/LMCache/Shaoting Feng|Shaoting Feng]]：https://github.com/LMCache/LMCache/blob/dev/MAINTAINERS.md
- [[community/LMCache/LMCache/Tony Lin|Tony Lin]]：https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS
- [[community/LMCache/LMCache/Zhengfei He|Zhengfei He]]：[[company/腾讯/Baolong Mao|Baolong Mao]]：#4621 的 LMCache build/CI commit 有直接 co-author 证据，记录为开源协作关系。
- [[company/IBM/Martin Hickey|Martin Hickey]]：2026-01 直接向 vLLM 提交 LMCache connector KV events 修复，因此这里将其记录为 `IBM → Martin Hickey → LMCache → vLLM KV Connector` 的可验证桥梁，而不是仅因为 IBM 同时参与 llm-d 就推断项目关系。
- [[company/TensorMesh/Jiayi Yao|Jiayi Yao]]：2025-03：为 LMCache connector 增加 chunked prefill 支持；
- [[company/TensorMesh/Junchen Jiang|Junchen Jiang]]：[[LMCache]]：共同创建者 / UChicago 研究网络核心节点。
- [[company/TensorMesh/杜昆泰 Kuntai Du|杜昆泰（Kuntai Du）]]：[[LMCache]]：核心维护、KV cache 系统设计、offloading / connector / 分层缓存
- [[company/TensorMesh/程翊华 Yihua Cheng|程翊华（Yihua Cheng）]]：[[LMCache]]：KV cache offloading、connector、分层缓存与传输
- [[company/腾讯/Baolong Mao|Baolong Mao]]：[[company/腾讯/Chunxiao Zheng|Chunxiao Zheng]]：腾讯同事 + LMCache P2P / distributed cache 直接工程协作者。2026-01 LMCache 官方文章明确记录两位 Tencent 作者参与 multi-node CPU P2P KV sharing 的 productionization。
- [[company/腾讯/Chunxiao Zheng|Chunxiao Zheng]]：LMCache #4828：为 MP 模式加入 Unified LMCache Radix Cache connector；

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/TensorMesh/TensorMesh|TensorMesh]]：公司页与社区/项目页均有显式记录；关系：`research-to-startup-core-network`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->

<!-- BEGIN AUTO PROJECT CONCEPTS -->
## 关联概念（自动汇总）

以下概念由 canonical Concept 节点的 `projects:` 反向汇总。它表示该 Concept 页面已有直接公开证据将本项目列为实现/支持者；本区块是派生视图，不应手工维护，也不会从 `areas` 或关键词自动推断。

- [[concept/memory/CXL Memory|CXL Memory]]
- [[concept/memory/Host Memory|Host Memory]]
- [[concept/inference/kv-cache/KV Cache Management|KV Cache Management]]
- [[concept/inference/kv-cache/KV Cache Offloading|KV Cache Offloading]]
- [[concept/inference/kv-cache/KV Cache Sharing|KV Cache Sharing]]
- [[concept/inference/kv-cache/KV Cache Transfer|KV Cache Transfer]]
- [[concept/memory/Memory Hierarchy|Memory Hierarchy]]
- [[concept/inference/serving/P-D Disaggregation|P-D Disaggregation]]
- [[concept/inference/kv-cache/Tiered KV Cache|Tiered KV Cache]]

<!-- END AUTO PROJECT CONCEPTS -->
