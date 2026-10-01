---
type: community
name: Ascend
aliases: [Ascend, 昇腾, 昇腾开源生态]
linked_people: []
linked_companies: []
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
  - "community/deepseek-ai/DeepSeek-Infra/DeepGEMM-Ascend"
  - "community/deepseek-ai/DeepSeek-Infra/DeepEP-Ascend"
  - "community/deepseek-ai/DeepSeek-Infra/FlashMLA"
  - "community/deepseek-ai/DeepSeek-Infra/DeepJIT"
  - "community/deepseek-ai/DeepSeek-Infra/clangd-ascend"
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

## DeepSeek Ascend 推理基础设施
2026-09-30，DeepSeek 开源/扩展了一组面向 Ascend 的推理基础设施组件：
- [[community/deepseek-ai/DeepSeek-Infra/DeepGEMM-Ascend|DeepGEMM-Ascend]]：Ascend 950 上的 BF16/FP8/FP4 GEMM、MQA logits、MegaMoE kernel。
- [[community/deepseek-ai/DeepSeek-Infra/DeepEP-Ascend|DeepEP-Ascend]]：基于 HCCL/HCOMM、UBMEM、URMA 的 MoE EP dispatch/combine 通信。
- [[community/deepseek-ai/DeepSeek-Infra/FlashMLA|FlashMLA]]：新增 DeepSeek Sparse Attention 的 Ascend prefill / decode kernel。
- [[community/deepseek-ai/DeepSeek-Infra/DeepJIT|DeepJIT]]：提供 CUDA / Ascend 统一 JIT runtime。
- [[community/deepseek-ai/DeepSeek-Infra/clangd-ascend|clangd-ascend]]：为 AscendC `.asc` 文件提供 clangd 代码智能。

### 这组项目的分层位置
`clangd-ascend → DeepJIT → DeepGEMM-Ascend / FlashMLA → DeepEP-Ascend` 可以近似看成开发工具、JIT/compiler、compute/attention kernel、EP communication 四层。它们不是 MindIE 或 vLLM-Ascend 的替代品，而是更底层、可被上层 inference runtime 消费的能力。

性能解读需特别区分公开软件 baseline：DeepGEMM-Ascend 的首发验证是 Ascend 950 series + CANN 9.20；DeepEP-Ascend 的首发性能数据则依赖 950DT + CANN 9.2.0 与当时未公开的 PoC HDK 配置。
