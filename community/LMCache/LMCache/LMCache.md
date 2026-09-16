---
type: project
name: LMCache
linked_people:
  - "community/LMCache/LMCache/Samm Shen"
  - "community/LMCache/LMCache/Shaoting Feng"
  - "company/IBM/Martin Hickey"
  - "company/TensorMesh/Jiayi Yao"
  - "company/TensorMesh/Junchen Jiang"
  - "company/TensorMesh/杜昆泰 Kuntai Du"
  - "company/TensorMesh/程翊华 Yihua Cheng"
  - "company/腾讯/Baolong Mao"
  - "company/腾讯/Chunxiao Zheng"
companies: ["TensorMesh"]
company_relation: research-to-startup-core-network
layer: kv-cache-management
open_source: true
repository: https://github.com/LMCache/LMCache
areas: [kv-cache, distributed-kv-cache, offloading, storage-backend, p2p, disaggregated-serving, vllm-integration, sglang-integration]
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
last_verified: "2026-09"
linked_companies:
  - "company/TensorMesh/TensorMesh"
---
# LMCache

## 项目简介
LMCache 是 LLM KV cache 的分层存储、传输、共享与复用系统，把 KV 从单 GPU HBM 扩展到 CPU、远端存储和跨实例/跨节点数据路径，并通过 connector 接入主流 serving engine。到 2026 年，其技术重点已从单进程 offload 扩展到 multiprocess（MP）架构、distributed KV、P2P sharing、PD disaggregation、KV management interface 和多硬件/多存储后端。

## 当前治理 / 维护网络
官方 `MAINTAINERS.md` 当前列出 10 名 Committer，包括 Yihua Cheng、Jiayi Yao、Kuntai Du、Martin Hickey、Hunter Zhang、Baolong Mao、Chunxiao Zheng、Shaoting Feng、Samuel Shen、Dongjoo Seo。

当前 `CODEOWNERS` 进一步把责任细化到 core engine、cache controller、multiprocess、distributed/L2、GPU connector、platform、lookup client、storage backends、serving-engine integrations、C extensions、operator、ROCm、CI 等模块。这比单纯 contributor list 更适合构建本图谱的 maintainer / component-owner 强边。

## 关键人物
- [[company/TensorMesh/程翊华 Yihua Cheng|程翊华（Yihua Cheng）]]、[[company/TensorMesh/杜昆泰 Kuntai Du|杜昆泰（Kuntai Du）]]、[[company/TensorMesh/Jiayi Yao|Jiayi Yao]]：UChicago / TensorMesh / LMCache 核心研究与工程网络。
- [[community/LMCache/LMCache/Samm Shen|Samuel Shen]]：TensorMesh Software Engineer；横跨 LMCache 的 vLLM、SGLang、TensorRT-LLM integration ownership。
- [[company/腾讯/Baolong Mao|Baolong Mao]]、[[company/腾讯/Chunxiao Zheng|Chunxiao Zheng]]：Tencent Committer；distributed/L2、storage、platform 与 P2P 路径核心工程网络。
- [[community/LMCache/LMCache/Shaoting Feng|Shaoting Feng]]：UChicago Committer；GPU/GDS、SGLang integration 与 vLLM multimodal KV caching 桥梁。
- [[company/IBM/Martin Hickey|Martin Hickey]]：IBM Committer；non-CUDA、KV events、tests/CI/packaging，并直接向 vLLM 修复 LMCache connector。

## Serving Engine 关系
### vLLM
LMCache 与 vLLM 已是双向工程集成关系，而不是单纯外部插件。vLLM 自身保留 `LMCacheConnectorV1`；Jiayi Yao、Baolong Mao、Samuel Shen、Martin Hickey 等都有可核验的 vLLM 侧直接 commit 或 connector 维护证据。

### SGLang
LMCache 当前仓库有独立 `lmcache/integration/sglang/` 路径，CODEOWNERS 包括 Samuel Shen、Shaoting Feng 等。2026 Q3 roadmap 继续推进 SGLang MP async store/retrieve 与 HiCache integration。

### TensorRT-LLM
当前 `lmcache/integration/tensorrt_llm/` 由 Samuel Shen ownership，形成第三条主 serving-engine 集成线。

## Storage / 数据路径关系
- **Mooncake Store**：LMCache 当前有 MooncakeStore L2 adapter、storage connector、lookup client；Baolong Mao / Chunxiao Zheng 在这些路径有明确 CODEOWNERS。这里表示 LMCache 侧技术集成，不等价于二人是 Mooncake maintainer。
- **Redis / S3 / filesystem / native L2**：当前均有独立 connector / adapter ownership。
- **3FS**：进入 2026 Q3 roadmap 的新 storage support，当前仍是 roadmap 状态，不标记为成熟 integration。

## 硬件生态
2026 Q3 roadmap 明确列出新 accelerator/platform 支持方向：Ascend、Moore Threads、MACA、AWS Trainium。当前应建“planned / in-progress integration”语义，不能提前写成成熟支持。

## TensorMesh 关系
[[company/TensorMesh/TensorMesh|TensorMesh]] 由 LMCache 核心研究/工程网络产业化而来，并持续维护 LMCache。这里保留 `research-to-startup-core-network` 的公司级边；相反，Tencent / IBM 等当前只因为具体员工有维护贡献，因此不自动升级成公司级 LMCache 治理边。

## Sources
- https://github.com/LMCache/LMCache
- https://github.com/LMCache/LMCache/blob/dev/MAINTAINERS.md
- https://github.com/LMCache/LMCache/blob/dev/.github/CODEOWNERS
- https://github.com/LMCache/LMCache/issues/4025
- https://blog.lmcache.ai/en/2026/01/21/p2p-1/
- https://blog.lmcache.ai/en/2025/03/31/cacheblend-best-paper-acm-eurosys25-enabling-100-kv-cache-hit-rate-in-rag/

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/LMCache/LMCache/Samm Shen|Samuel Shen]]：`lmcache/integration/vllm/`：CODEOWNER；
- [[community/LMCache/LMCache/Shaoting Feng|Shaoting Feng]]：https://github.com/LMCache/LMCache/blob/dev/MAINTAINERS.md
- [[company/IBM/Martin Hickey|Martin Hickey]]：2026-01 直接向 vLLM 提交 LMCache connector KV events 修复，因此这里将其记录为 `IBM → Martin Hickey → LMCache → vLLM KV Connector` 的可验证桥梁，而不是仅因为 IBM 同时参与 llm-d 就推断项目关系。
- [[company/TensorMesh/Jiayi Yao|Jiayi Yao]]：2025-03：为 LMCache connector 增加 chunked prefill 支持；
- [[company/TensorMesh/Junchen Jiang|Junchen Jiang]]：[[LMCache]]：共同创建者 / UChicago 研究网络核心节点。
- [[company/TensorMesh/杜昆泰 Kuntai Du|杜昆泰（Kuntai Du）]]：[[LMCache]]：核心维护、KV cache 系统设计、offloading / connector / 分层缓存
- [[company/TensorMesh/程翊华 Yihua Cheng|程翊华（Yihua Cheng）]]：[[LMCache]]：KV cache offloading、connector、分层缓存与传输
- [[company/腾讯/Baolong Mao|Baolong Mao]]：[[company/腾讯/Chunxiao Zheng|Chunxiao Zheng]]：腾讯同事 + LMCache P2P / distributed cache 直接工程协作者。2026-01 LMCache 官方文章明确记录两位 Tencent 作者参与 multi-node CPU P2P KV sharing 的 productionization。
- [[company/腾讯/Chunxiao Zheng|Chunxiao Zheng]]：[[company/腾讯/Baolong Mao|Baolong Mao]]：腾讯同事 + LMCache P2P / distributed cache 直接工程协作者，关系由官方 maintainer、CODEOWNERS 和 P2P 技术文章共同支撑。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/TensorMesh/TensorMesh|TensorMesh]]：公司页与社区/项目页均有显式记录；关系：`research-to-startup-core-network`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
