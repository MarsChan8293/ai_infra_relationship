---
type: project
name: vLLM-Ascend
linked_people:
  - "community/Ascend/MemCache/ader47"
  - "community/Ascend/MemCache/DreamerLeader"
  - "community/Ascend/MemCache/Pz1116"
  - "community/Ascend/MemCache/tyy0829"
  - "community/vllm-project/vLLM-Ascend/chengruiqi"
  - "community/vllm-project/vLLM-Ascend/leolee"
  - "community/vllm-project/vLLM-Ascend/Levi-JQ"
  - "community/vllm-project/vLLM-Ascend/ningjingbengxiaohai"
  - "community/vllm-project/vLLM-Ascend/QiuChunshuo"
  - "community/vllm-project/vLLM-Ascend/Wang Xiyuan"
  - "community/vllm-project/vLLM-Ascend/weiguihua2"
  - "community/vllm-project/vLLM-Ascend/weijinqian0"
  - "community/vllm-project/vLLM-Ascend/yiz-liu"
  - "community/vllm-project/vLLM-Ascend/zzzzwwjj"
  - "community/vllm-project/vLLM-Ascend/管文宇 Guan Wenyu"
  - "community/vllm-project/vLLM-Omni/Canlin Guo"
companies: ["华为"]
company_relation: hardware-ecosystem-core-contributor
layer: hardware-backend
open_source: true
linked_companies:
  - "company/华为/华为"
---
# vLLM-Ascend

## 项目简介
vLLM-Ascend 是 vLLM 面向 Huawei Ascend NPU 的硬件插件/backend 社区，把 vLLM 的 scheduler、API 与模型 serving 能力适配到 Ascend/CANN 生态。它是观察开源 LLM engine 如何跨 CUDA 之外硬件平台扩展的重要节点。

## GitHub
https://github.com/vllm-project/vllm-ascend

## 主要贡献公司
- [[company/华为/华为|华为]]：Ascend/CANN 硬件与软件生态的核心公司贡献方。vLLM-Ascend 仍由 vLLM Project / vLLM-Ascend 社区治理，因此这里表示 **hardware ecosystem core contributor**，不是公司私有项目。

## 主要维护者 / 组织
由 vLLM Project / vLLM-Ascend 社区维护。当前图谱按 roadmap、release、社区组织等公开职责记录 [[Wang Xiyuan]]、[[yiz-liu]]、[[zzzzwwjj]]、[[weijinqian0]]、[[ningjingbengxiaohai]] 等节点。

## 推理优化扩展线
- [[ops-transformer]]：Ascend/CANN kernel 层，连接 sparse attention、BlockSparseAttention、量化 attention 与 AscendC 自定义 kernel。
- [[MindIE-LLM]]：昇腾 inference runtime，连接 SplitFuse、Prefix Cache、MTP 与 PD 混部。
- [[MindIE-Motor]]：分布式 serving / Coordinator，连接 KV cache affinity、PD 调度与容量规划。
- [[msModelSlim]]：量化工具链，连接 W8A8 / W4A8 / MXFP 系低比特部署。
- [[管文宇 Guan Wenyu]]：2026 年贡献 MiniMax-M2.5 在 Ascend A3 + vLLM-Ascend 上的 MXFP4/W4A4 推理适配。

## openYuanRong 数据平面
- [[community/openEuler/openYuanRong/YuanRong DataSystem|YuanRong DataSystem]]：当前官方 KV Pool 文档支持它作为 `AscendStoreConnector` 的 storage backend，提供 distributed KV pool 路径。
- [[community/openEuler/openYuanRong/YuanRong TransferEngine|YuanRong TransferEngine]]：RFork 官方指南直接要求安装 `openyuanrong-transfer-engine`，用于 Ascend 推理实例的模型权重传输。
- [[community/openEuler/openYuanRong/openYuanRong|openYuanRong]]：因此与 vLLM-Ascend 的关系已从“潜在国产分布式底座”升级成明确的 KV storage + weight-transfer 软件集成。

## 生态关系
[[vLLM]] · [[LMCache]] · [[Mooncake]] · [[DeepJIT]] · [[ops-transformer]] · [[MindIE-LLM]] · [[MindIE-Motor]] · [[msModelSlim]] · [[community/openEuler/openYuanRong/openYuanRong|openYuanRong]]。它是 hardware backend，不应与独立 serving engine 视为平级替代关系。

## Sources
- https://github.com/vllm-project/vllm-ascend
- https://docs.vllm.ai/projects/ascend/en/main/user_guide/feature_guide/kv_pool.html
- https://docs.vllm.ai/projects/ascend/en/main/user_guide/feature_guide/rfork.html

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/华为/华为|华为]]：公司页与社区/项目页均有显式记录；关系：`hardware-ecosystem-core-contributor`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/Ascend/MemCache/ader47|ader47（Feng Liu）]]：https://github.com/vllm-project/vllm-ascend/pull/11444
- [[community/Ascend/MemCache/DreamerLeader|DreamerLeader]]：2026-01 发起 vLLM-Ascend RFC #6410，明确提出把 MemCache 纳入 KV Pool storage backend，并将原有 MooncakeStoreConnector 抽象为统一的 AscendStoreConnector + Backend 接口。
- [[community/Ascend/MemCache/Pz1116|Pz1116]]：https://github.com/vllm-project/vllm-ascend/issues/9057
- [[community/Ascend/MemCache/tyy0829|tyy0829]]：2026 年直接推进 vLLM-Ascend 的 **layerwise KV Pool + MemCache backend**：减少 per-layer key / MetaServer lookup 开销，把 GVA 分配移动到 worker，并使用 MemCache `batch_copy` / lease 生命周期管理完成按层 KV save/load。
- [[community/vllm-project/vLLM-Ascend/chengruiqi|chengruiqi]]：该实现明确使用 `AscendStoreConnector` + **MemCache backend**，并验证 MTP、prefix caching 与多前缀 pooled prefill workload，是 MemCache 与 vLLM-Ascend 当前非常直接的工程桥。
- [[community/vllm-project/vLLM-Ascend/leolee|leolee]]：https://github.com/vllm-project/vllm-ascend/commit/92995fbbf30301b6f4b702fdb375a888608c1e20
- [[community/vllm-project/vLLM-Ascend/Levi-JQ|Levi-JQ]]：https://github.com/vllm-project/vllm-ascend/commit/ce9e24a28131b59c6df27470ac42aee742a711ad
- [[community/vllm-project/vLLM-Ascend/ningjingbengxiaohai|ningjingbengxiaohai]]：2026 vLLM-Ascend 技术周会多次担任 Chair。
- [[community/vllm-project/vLLM-Ascend/QiuChunshuo|QiuChunshuo]]：https://github.com/vllm-project/vllm-ascend/commit/81e75f893b7ce98f1633cb66a5408687db6e039b
- [[community/vllm-project/vLLM-Ascend/Wang Xiyuan|Wang Xiyuan]]：vLLM-Ascend 主要维护与社区组织者之一。
- [[community/vllm-project/vLLM-Ascend/weiguihua2|weiguihua2]]：https://github.com/vllm-project/vllm-ascend/commit/3d84be3ce62206223b39204722649b66c21033dd
- [[community/vllm-project/vLLM-Ascend/weijinqian0|Jinqian Wei]]：[[community/vllm-project/vLLM-Ascend/Wang Xiyuan|Wang Xiyuan]]：社区治理/Attention 工程邻接关系；缺 pair-specific 证据时不自动生成 typed edge。
- [[community/vllm-project/vLLM-Ascend/yiz-liu|yiz-liu]]：vLLM-Ascend 活跃维护者。
- [[community/vllm-project/vLLM-Ascend/zzzzwwjj|zzzzwwjj]]：vLLM-Ascend roadmap 主要推动者之一。
- [[community/vllm-project/vLLM-Ascend/管文宇 Guan Wenyu|管文宇（Guan Wenyu）]]：https://github.com/vllm-project/vllm-ascend
- [[community/vllm-project/vLLM-Omni/Canlin Guo|Canlin Guo]]：2026 Q1 / Q2 NPU roadmap 的主要推动者，公开路线明确写出 vLLM-Omni NPU 支持依赖 [[community/vllm-project/vLLM-Ascend/vLLM-Ascend|vLLM-Ascend]]，并把 [[MindIE-SD]] 作为 Ascend-optimized diffusion operator library 接入 FlashAttentionBackend / CustomOp 路径。

<!-- END AUTO PROJECT PEOPLE -->
