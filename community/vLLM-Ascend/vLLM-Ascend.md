---
type: project
name: vLLM-Ascend
companies: [华为]
company_relation: hardware-ecosystem-core-contributor
layer: hardware-backend
open_source: true
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

## 生态关系
[[vLLM]] · [[LMCache]] · [[Mooncake]] · [[DeepJIT]] · [[ops-transformer]] · [[MindIE-LLM]] · [[MindIE-Motor]] · [[msModelSlim]]。它是 hardware backend，不应与独立 serving engine 视为平级替代关系。
