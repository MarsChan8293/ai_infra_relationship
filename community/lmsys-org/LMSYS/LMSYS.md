---
type: community
name: LMSYS
aliases: ["LMSYS Org", "lmsys.org", "Large Model Systems"]
repository: https://github.com/lm-sys
people:
  - "community/sgl-project/SGLang/郑连民 Lianmin Zheng"
  - "company/RadixArk/盛颖 Ying Sheng"
  - "company/RadixArk/朱邦华 Banghua Zhu"
  - "company/RadixArk/Mingyi Lu"
  - "company/RadixArk/Richard Chen"
  - "company/Inferact/Joseph Gonzalez"
  - "company/Inferact/Ion Stoica"
  - "university/清华大学/Mingxing Zhang"
linked_people:
  - "community/sgl-project/SGLang/郑连民 Lianmin Zheng"
  - "company/RadixArk/盛颖 Ying Sheng"
category: ai-systems-community
areas: [llm-serving, evaluation, open-source-ai, ai-infrastructure, speculative-decoding, model-routing, adapter-serving]
governance: "501(c)(3) nonprofit; officer/advisor-governed open-source and research incubator"
website: https://www.lmsys.org/
last_verified: "2026-09"
linked_companies: []
---
# LMSYS

## 社区定位
LMSYS（Large Model Systems）是围绕大语言模型系统、评测与开源 AI 基础设施形成的非营利研究与开源组织。官方资料显示其源于 2023 年 UC Berkeley、Stanford、UCSD、CMU、MBZUAI 等多校协作，并于 2024 年 9 月注册为 501(c)(3) nonprofit。当前图谱中，它最重要的作用是连接 Berkeley systems 人才网络、[[SGLang]]、高效推理系统与后续 AI Infra 创业/工程组织。

## 与 AI Infra 的关系
- [[SGLang]]：LMSYS 体系中最重要的高性能 LLM serving 项目之一，连接 scheduler、RadixAttention、speculative decoding 与 production inference。
- [[community/sgl-project/SpecForge/SpecForge|SpecForge]]：SGLang 生态的 speculative decoding 训练框架，并被 LMSYS 持续作为 systems 项目推广。
- [[community/lmsys-org/FastChat/FastChat|FastChat]]：LMSYS 早期模型服务与 OpenAI-compatible serving 栈，是 Vicuna / Chatbot Arena 时代的重要运行底座。
- [[community/lmsys-org/S-LoRA/S-LoRA|S-LoRA]]：面向大规模 LoRA adapter 并发 serving 的研究系统，重点是 Unified Paging、heterogeneous batching 与 adapter/KV memory orchestration。
- [[community/lmsys-org/RouteLLM/RouteLLM|RouteLLM]]：从 preference data 学习模型路由，在质量约束下优化强弱模型组合的调用成本。
- [[community/lmsys-org/Lookahead-Decoding/Lookahead-Decoding|Lookahead Decoding]]：无需训练 draft model 的 exact parallel decoding 路线，以 Jacobi iteration 和 n-gram verification 加速自回归解码。

## 当前治理快照（2026-09）
LMSYS 官网当前将 Ying Sheng、Lianmin Zheng、Mingyi Lu、Jerry Zhou、Banghua Zhu、Richard Chen、Tiancheng Xie、Benhui He 列为 officers；将 Joseph E. Gonzalez、Ion Stoica、Eric P. Xing、Hao Zhang、Jun Qian、Mingxing Zhang 列为 advisors。本轮只为与推理优化图谱有高价值连接、且身份可稳定落点的人建立 canonical 节点或强社区关系，不把整个名单机械铺平。

其中最重要的跨组织桥包括：
- [[company/RadixArk/盛颖 Ying Sheng|Ying Sheng]]、[[company/RadixArk/朱邦华 Banghua Zhu|Banghua Zhu]]、[[company/RadixArk/Mingyi Lu|Mingyi Lu]]、[[company/RadixArk/Richard Chen|Richard Chen]]：把 LMSYS / SGLang 延伸到 RadixArk 的 production inference 与 post-training 工程网络。
- [[company/Inferact/Ion Stoica|Ion Stoica]]、[[company/Inferact/Joseph Gonzalez|Joseph Gonzalez]]：Berkeley Sky / vLLM / SGLang 的导师与 systems 研究桥。
- [[university/清华大学/Mingxing Zhang|Mingxing Zhang]]：当前 advisor 身份把 LMSYS 正式治理层连接到清华 MADSys、Mooncake、KTransformers、Seer、DualPath 等推理基础设施研究网络。

## 边界说明
LMSYS 社区关联只表示公开的研究、社区、项目参与或官网治理角色，不自动推出雇佣、导师、同事或公司关系。具体强关系仍由人物页的 typed relations 与公开来源决定。

本轮 EXPAND 有意把重点放在 inference / systems 主线上。Chatbot Arena / LMSYS-Chat、MT-Bench、Vicuna、数据集与评测作者网络只在形成 AI Infra 桥接时继续扩张，避免把图谱稀释成泛 LLM 作者名单。

## Sources
- https://www.lmsys.org/
- https://www.lmsys.org/contact/
- https://www.lmsys.org/blog/2026-03-25-gtc2026
- https://www.lmsys.org/about/
- https://www.lmsys.org/projects/


<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/sgl-project/SGLang/郑连民 Lianmin Zheng|郑连民（Lianmin Zheng）]]：[[community/sgl-project/SGLang/尹良升 Liangsheng Yin|尹良升（Liangsheng Yin）]]：**LMSYS/SGLang 研究与开源合作者**。尹良升从 2023 年起在 LMSYS/SGLang 网络中与郑连民、盛颖工作；2024 年夏天三人有明确的共同 debug 记录。当前郑连民负责 Scheduler merge oncall，尹良升负责 Scheduler + speculative decoding，属于持...
- [[company/RadixArk/盛颖 Ying Sheng|盛颖（Ying Sheng）]]：[[community/sgl-project/SGLang/尹良升 Liangsheng Yin|尹良升（Liangsheng Yin）]]：**LMSYS/SGLang 研究与开源合作者**。自 2023 年起进入同一 SGLang 核心开发网络；2024 年夏天有明确共同 debug 记录。尹良升目前负责 scheduler / speculative decoding，盛颖更多承担项目创建、社区与公司建设。

<!-- END AUTO PROJECT PEOPLE -->
