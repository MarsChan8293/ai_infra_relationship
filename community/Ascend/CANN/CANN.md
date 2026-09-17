---
type: project
name: CANN
organization: Ascend
companies: ["华为"]
company_relation: company-led
layer: ai-compute-software-stack
open_source: true
linked_companies:
  - "company/华为/华为"
linked_people:
  - "community/Ascend/ops-transformer/wangchao661"
  - "community/Ascend/ops-transformer/Konstantin Berestizshevsky"
---
# CANN

CANN（Compute Architecture for Neural Networks）是华为昇腾 AI 计算软件栈的核心层，连接 Ascend NPU 与上层框架、算子、编译、通信和推理运行时。

## 开源位置
- 2025 年华为宣布 CANN 全面开源开放，并成立技术指导委员会。
- 开源范围逐步覆盖算子库、领域加速库、图计算、Ascend C 与相关工具链。
- 与 PyTorch、Triton、TileLang、vLLM、verl 等上游社区形成硬件后端与软件栈协作。

## 图谱关系
[[ops-transformer]] 是 CANN 面向 Transformer / LLM 的算子与 kernel 线；[[vLLM-Ascend]]、MindIE、MemCache 等处于更上层的 serving / cache / runtime 生态。

## Sources
- https://www.huawei.com/cn/news/2025/8/ascend-summit-CANN-open-source
- https://www.huawei.com/cn/news/2025/9/hc-shengten-opensource
- https://www.huawei.com/cn/news/2026/3/mwc-superpod-computing
