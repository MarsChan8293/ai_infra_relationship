---
type: community
name: Ascend
aliases: [Ascend, 昇腾, 昇腾开源生态]
linked_people:
  - "community/Ascend/ops-transformer/wangchao661"
  - "community/Ascend/ops-transformer/Konstantin Berestizshevsky"
  - "community/Ascend/MemCache/吕有辉"
  - "community/vllm-project/vLLM-Omni/Gao Han"
  - "community/vllm-project/vLLM-Omni/Hongsheng Liu"
linked_companies:
  - "company/华为/华为"
linked_projects:
  - "community/Ascend/CANN/CANN"
  - "community/Ascend/MemCache/MemCache"
  - "community/Ascend/MemFabric/MemFabric"
  - "community/Ascend/MindIE-LLM/MindIE-LLM"
  - "community/Ascend/MindIE-Motor/MindIE-Motor"
  - "community/Ascend/MindIE-SD/MindIE-SD"
  - "community/Ascend/msModelSlim/msModelSlim"
  - "community/Ascend/ops-transformer/ops-transformer"
  - "community/vllm-project/vLLM-Ascend/vLLM-Ascend"
---
# Ascend / 昇腾开源生态

Ascend 是围绕华为昇腾 NPU、[[CANN]]、MindIE 与上游 AI Infra 社区形成的开放计算生态。仓库原有 MemCache、MemFabric、MindIE、ops-transformer、vLLM-Ascend 等节点已经较完整，本页作为统一上层入口，不复制已有项目和人物。

## 推理 Infra 主线
`Ascend NPU → CANN → kernels / communication / runtime → MindIE / vLLM-Ascend → MemCache / MemFabric`

2025 年华为宣布 CANN 全面开源开放，并成立 CANN 技术指导委员会；到 2026 年官方继续明确 CANN 已覆盖算子库、加速库、图计算与编程语言等开源组件，并支持 Triton、TileLang、PyTorch、vLLM、verl 等主流生态。

## Sources
- https://www.huawei.com/cn/news/2025/9/hc-shengten-opensource
- https://www.huawei.com/cn/news/2026/3/mwc-superpod-computing
- https://gitcode.com/Ascend
