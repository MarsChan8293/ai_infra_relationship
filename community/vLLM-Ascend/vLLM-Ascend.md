---
type: project
name: vLLM-Ascend
layer: hardware-backend
open_source: true
---
# vLLM-Ascend

## 项目简介
vLLM-Ascend 是 vLLM 面向 Huawei Ascend NPU 的硬件插件/backend 社区，把 vLLM 的 scheduler、API 与模型 serving 能力适配到 Ascend/CANN 生态。它是观察开源 LLM engine 如何跨 CUDA 之外硬件平台扩展的重要节点。

## GitHub
https://github.com/vllm-project/vllm-ascend

## 主要维护者 / 组织
由 vLLM Project / vLLM-Ascend 社区维护。当前图谱按 roadmap、release、社区组织等公开职责记录 [[Wang Xiyuan]]、[[yiz-liu]]、[[zzzzwwjj]]、[[weijinqian0]]、[[ningjingbengxiaohai]] 等节点。

## 生态关系
[[vLLM]] · Huawei Ascend/CANN · [[LMCache]] · [[Mooncake]] · [[DeepJIT]]。它是 hardware backend，不应与独立 serving engine 视为平级替代关系。
