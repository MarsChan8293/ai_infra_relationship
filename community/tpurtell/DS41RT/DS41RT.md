---
type: project
name: "DS41RT"
layer: inference-engine
status: active
code_availability: public
repository: https://github.com/tpurtell/ds41rt
areas:
  - heterogeneous-inference
  - attention-ffn-disaggregation
  - dgx-spark
  - rtx-pro-6000
  - roce
  - speculative-decoding
  - moe-inference
hardware:
  - nvidia
integrations: []
companies: []
company_relation: community-led
last_verified: "2026-10"
---

# DS41RT

## 项目简介
DS41RT 是针对 DeepSeek V4.1 Flash 的原生异构推理 Runtime：RTX PRO 6000 Coordinator 维护 Attention、KV、Router 和采样，DGX Spark 负责 MoE Expert；支持推测解码与 OpenAI API。

## 硬件兼容性与证据层级
- **RTX PRO 6000 Blackwell 96GB（SM120）+ DGX Spark（GB10/SM121）**：官方主配置为 1–2 张 PRO 6000 + 4 台 Spark，提供多个版本的容器、拓扑、硬件和性能记录。
- 还有双 RTX PRO 6000 无 Spark 配置及其他实验性 TP 配置，但不同 Release/量化/验证等级不可合并概括。
- **RTX PRO 5000 72GB** 不是官方已验证目标；硬件/显存和性能不得直接类推。
- README 的 5090+Spark 内存预算模拟 **并不等于物理 RTX 5090 经过实测**。

## 核心技术与部署意义
- Attention–FFN Disaggregation（AFD），跨服务器 RoCE 发送 Expert Activation，和传统完整层 TP/P-D 解耦不同。
- 提供 Prefix Reuse、dSpark 推测解码、性能记录；需区分可复现正式结果与 informational/candidate 测试。

## 关系与对比
[[community/gpillon/Ignis/Ignis|Ignis]]、[[community/HawkBearPig/DGPP/DGPP|DGPP]]、[[community/NVIDIA/Flare/Flare|Flare]] 是性能/架构比较，不代表代码直接依赖。

## 来源
- https://github.com/tpurtell/ds41rt
- https://github.com/tpurtell/ds41rt/blob/HEAD/README.md
