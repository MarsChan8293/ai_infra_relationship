---
type: project
name: YuanRong TransferEngine
aliases: [openYuanRong TransferEngine, openyuanrong-transfer-engine]
linked_people: []
layer: npu-data-transfer
open_source: true
areas: [data-transfer, rdma, roce, npu, kv-transfer, weight-transfer, disaggregated-inference]
related_projects: ["openYuanRong", "YuanRong DataSystem", "vLLM-Ascend", "vLLM-Omni"]
last_verified: "2026-09"
linked_companies: []
---
# YuanRong TransferEngine

## 项目简介
YuanRong TransferEngine 是 openYuanRong 面向高性能数据传输的能力组件，并通过 `openyuanrong-transfer-engine` Python package 暴露运行时接口。在本图谱中单独实体化，是因为它已经进入多个大模型推理系统的关键数据路径，而不只是 DataSystem 的内部实现细节。

## 推理系统连接
- [[community/vllm-project/vLLM-Ascend/vLLM-Ascend|vLLM-Ascend]]：RFork 官方指南要求安装 `openyuanrong-transfer-engine`，用于 Ascend 推理实例间的权重传输。
- [[community/vllm-project/vLLM-Omni/vLLM-Omni|vLLM-Omni]]：当前代码实际注册 `YuanrongTransferEngineConnector`，在 Ascend NPU 上以 NPU memory pool 做跨 stage P2P transfer；它和 DataSystem-backed `YuanrongConnector` 是两条不同路径。

`YuanRong TransferEngine` 与 [[community/openEuler/openYuanRong/YuanRong DataSystem|YuanRong DataSystem]] 相关，但这里不把二者简单合并：前者在 vLLM-Omni / RFork 中承担直接 transport，后者更多承担 distributed KV / pooled storage backend。

## 治理发现
openEuler 社区的 YuanRong 分仓治理材料提供了 **parent repository 级** 的明确角色：2025 年社区 PR #6952 将 `yuanrong-datasystem` 的管理员记录为 **车煜林**，并新增 **姚昊林** 看护 Object / KV 语义。这说明 DataSystem 层已经有可核验的 administrator / committer ownership。

但 TransferEngine 当前作为 `yuanrong-datasystem` 内的独立能力目录 / package，现有一手材料还没有把上述 repo-level ownership 精确映射成 `transfer_engine` 目录的 maintainer。因此本轮只把它记成治理线索，不直接把车煜林或姚昊林写入 `linked_people`。后续 VERIFY 应读取当前 OWNERS / SIG 配置或目录级 reviewer/committer 规则后再升级强边。

## Sources
- https://pypi.org/project/openyuanrong-transfer-engine/
- https://docs.vllm.ai/projects/ascend/en/main/user_guide/feature_guide/rfork.html
- https://docs.vllm.ai/projects/vllm-omni/en/latest/design/feature/omni_connectors/yuanrong_transfer_engine_connector/
- https://github.com/vllm-project/vllm-omni/blob/main/vllm_omni/distributed/omni_connectors/__init__.py
- https://gitee.com/openeuler/community/pulls/6952
- https://gitee.com/openeuler/yuanrong-datasystem
