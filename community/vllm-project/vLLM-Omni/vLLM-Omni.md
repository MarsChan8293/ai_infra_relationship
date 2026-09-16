---
type: project
name: vLLM-Omni
layer: multimodal-serving
open_source: true
repository: https://github.com/vllm-project/vllm-omni
areas: [multimodal-inference, disaggregated-inference, data-transfer, npu, serving]
people:
  - "community/vllm-project/vLLM/Roger Wang"
related_projects: ["vLLM", "YuanRong DataSystem", "YuanRong TransferEngine", "Mooncake"]
last_verified: "2026-09"
---
# vLLM-Omni

## 项目定位
vLLM-Omni 是 vLLM 生态面向多模态 / 多 stage inference pipeline 的 serving 项目。其 disaggregated inference connector 把跨 stage 数据移动抽象为统一接口，因此是观察各种数据传输 backend 如何进入 production inference 的重要节点。

## YuanRong 连接
当前代码和文档已经同时提供两条 YuanRong 路径：
- `YuanrongConnector`：使用 [[community/openEuler/openYuanRong/YuanRong DataSystem|YuanRong DataSystem]] 作为分布式 KV store。
- `YuanrongTransferEngineConnector`：使用 [[community/openEuler/openYuanRong/YuanRong TransferEngine|YuanRong TransferEngine]] 做 Ascend NPU P2P transfer，直接管理 NPU memory pool。

这不是早期 RFC 的占位关系；最新 connector factory 与 API 文档已注册并公开对应实现。

## 人物
- [[community/vllm-project/vLLM/Roger Wang|Roger Wang]]：现有仓库已记录其为 vLLM-Omni lead maintainer / vLLM 多模态方向核心人物，因此作为当前图谱的高价值入口。

## Sources
- https://github.com/vllm-project/vllm-omni
- https://docs.vllm.ai/projects/vllm-omni/en/latest/design/feature/disaggregated_inference/
- https://docs.vllm.ai/projects/vllm-omni/en/latest/design/feature/omni_connectors/yuanrong_transfer_engine_connector/
- https://github.com/vllm-project/vllm-omni/blob/main/vllm_omni/distributed/omni_connectors/__init__.py
