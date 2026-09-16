---
type: project
name: SGLang
linked_people:
  - "community/ai-dynamo/Dynamo/Ishan Dhanani"
  - "community/kvcache-ai/Mooncake/Shangming Cai"
  - "community/kvcache-ai/Mooncake/马腾 Teng Ma"
  - "community/sgl-project/SGLang/Shenggui Li"
  - "community/sgl-project/SGLang/Yineng Zhang"
  - "community/sgl-project/SGLang/尹良升 Liangsheng Yin"
  - "community/sgl-project/SGLang/谢志强 Zhiqiang Xie"
  - "community/sgl-project/SGLang/郑连民 Lianmin Zheng"
  - "company/Inferact/Ion Stoica"
  - "company/Inferact/Joseph Gonzalez"
  - "company/RadixArk/Baizhou Zhang"
  - "company/RadixArk/Cheng Wan"
  - "company/RadixArk/Qiaolin Yu"
  - "company/RadixArk/Xiaoyu Zhang"
  - "company/RadixArk/朱邦华 Banghua Zhu"
  - "company/RadixArk/盛颖 Ying Sheng"
  - "university/UC Berkeley/Shiyi Cao"
companies: ["RadixArk"]
company_relation: core-maintainer-network
layer: llm-serving-engine
open_source: true
linked_companies:
  - "company/RadixArk/RadixArk"
---
# SGLang

## 项目简介
SGLang 是面向大语言模型与多模态模型的高性能 serving framework，从 RadixAttention / prefix reuse 出发，逐步扩展到 continuous batching、speculative decoding、structured generation、distributed serving、MoE 与多模态执行。它与 vLLM 一起构成当前开源 LLM serving engine 的核心路线。

## GitHub
https://github.com/sgl-project/sglang

## 主要贡献公司
- [[company/RadixArk/RadixArk|RadixArk]]：公司人物网络与 SGLang core maintainer / runtime / kernel / release engineering 高度重叠，是当前最清晰的产业核心贡献节点。这里标记为 **core-maintainer network**，不把 SGLang 社区所有权归给 RadixArk。

## 主要维护者 / 组织
由 sgl-project 社区维护，起源与 UC Berkeley Sky Computing Lab 高度相关，并形成 [[RadixArk]] 等产业化节点。核心人物包括 [[郑连民 Lianmin Zheng]]、[[盛颖 Ying Sheng]]、[[尹良升 Liangsheng Yin]]、[[谢志强 Zhiqiang Xie]]，以及 RadixArk/SGLang 社区的 Cheng Wan、Qiaolin Yu、Baizhou Zhang 等。

历史核心维护者中，[[community/sgl-project/SGLang/Yineng Zhang|Yineng Zhang]] 在 2024–2025 担任 SGLang core maintainer，并参与 DeepSeek-V3 day-0 support 与性能优化；2025-07 后进入 [[Together AI]] inference 团队，2026-03 又共同创建 [[TokenSpeed]]。这里按时间写为“历史 core maintainer”，不把其 2024–2025 身份误写成当前治理角色。

## 跨项目人才桥
- [[community/sgl-project/SGLang/Shenggui Li|Shenggui Li]]：当前 SGLang Core Dev、SpecForge Project Lead；此前处于 [[Colossal-AI]] / HPC-AI 早期核心系统网络，形成 distributed training → serving / speculative decoding 的人才迁移桥。
- [[community/sgl-project/SGLang/Yineng Zhang|Yineng Zhang]]：2024–2025 SGLang core maintainer；同时是 [[FlashInfer]]、[[Mooncake]] 作者网络成员，2025-07 加入 [[Together AI]]，2026-03 co-create [[TokenSpeed]]。这是 SGLang → production inference → 新 serving engine 的直接人才迁移边。

## 生态关系
[[vLLM]] · [[FlashInfer]] · [[Mooncake]] · [[DeepSeek-Infra]] · [[Dynamo]] · [[TokenSpeed]] · [[RadixArk]] · [[Colossal-AI]] · [[UC Berkeley]]。项目社区协作不能自动推断为公司同事。

## Sources
- https://github.com/sgl-project/sglang
- https://zhyncs.com/

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/ai-dynamo/Dynamo/Ishan Dhanani|Ishan Dhanani]]：[[SGLang]]：NVIDIA/model-specific optimization 与 CI 方向贡献者
- [[community/kvcache-ai/Mooncake/Shangming Cai|Shangming Cai]]：[[SGLang]]：PD disaggregation / CI 相关核心贡献者
- [[community/kvcache-ai/Mooncake/马腾 Teng Ma|马腾（Teng Ma）]]：[[community/kvcache-ai/Mooncake/Shangming Cai|Shangming Cai]]：**Alibaba Cloud 同事 + Mooncake Codeowner**。截至 2026-09 两人均公开关联 Alibaba Cloud，并共同维护 Mooncake；马腾偏项目生态/社区与云侧协作，Shangming Cai 负责 SGLang Integration。首次在 Alibaba Cloud 共事的精确月份公开未确认。
- [[community/sgl-project/SGLang/Shenggui Li|Shenggui Li]]：[[SGLang]]：当前 Core Dev；进一步负责 SpecForge，聚焦 speculative decoding / serving systems。
- [[community/sgl-project/SGLang/Yineng Zhang|Yineng Zhang]]：[[SGLang]]：2024–2025 core maintainer，参与 DeepSeek-V3 day-0 support 与性能优化。
- [[community/sgl-project/SGLang/尹良升 Liangsheng Yin|尹良升（Liangsheng Yin）]]：LMSYS：2023 起 Research Intern / research collaborator，与郑连民、盛颖等共同开发 SGLang
- [[community/sgl-project/SGLang/谢志强 Zhiqiang Xie|谢志强（Zhiqiang Xie）]]：[[community/sgl-project/SGLang/郑连民 Lianmin Zheng|郑连民（Lianmin Zheng）]]：**SGLang 原始论文合著者 + 当前系统模块协作者**。两人共同署名 2023/2024 SGLang 原始工作；截至 2026-09 郑连民负责 scheduler，谢志强负责 KV Cache merge oncall，属于 scheduler ↔ cache 的持续开源协作，不等同于公司同事。
- [[community/sgl-project/SGLang/郑连民 Lianmin Zheng|郑连民（Lianmin Zheng）]]：Berkeley 期间参与 Alpa、TVM/Ansor、FastChat、Chatbot Arena、SGLang 等系统
- [[company/Inferact/Ion Stoica|Ion Stoica]]：[[community/sgl-project/SGLang/郑连民 Lianmin Zheng|郑连民（Lianmin Zheng）]]：**UC Berkeley 博士导师 / 学生**。郑连民 Berkeley 博士阶段由 Ion Stoica 与 Joseph Gonzalez 指导，其系统研究谱系连接 Alpa、FastChat 与 [[SGLang]]；这里已从泛化 `mentor-network` 升级为正式 `student` 强边。
- [[company/Inferact/Joseph Gonzalez|Joseph Gonzalez]]：[[community/sgl-project/SGLang/郑连民 Lianmin Zheng|郑连民（Lianmin Zheng）]]：**UC Berkeley 博士导师 / 学生**。郑连民 Berkeley 博士阶段由 Joseph Gonzalez 与 Ion Stoica 指导；其系统工作从 Alpa、FastChat 延伸到 [[SGLang]]。这里已从泛化 `mentor-network` 升级为正式 `student` 强边。
- [[company/RadixArk/Baizhou Zhang|Baizhou Zhang]]：SGLang NVIDIA / model-specific optimization
- [[company/RadixArk/Cheng Wan|Cheng Wan]]：SGLang parallelism、EPLB、DP Attention、distributed communication
- [[company/RadixArk/Qiaolin Yu|Qiaolin Yu]]：[[SGLang]] speculative decoding、模型优化与 GPU 性能
- [[company/RadixArk/Xiaoyu Zhang|Xiaoyu Zhang]]：SGLang kernel、diffusion、多模态生成与 DeepSeek 优化
- [[company/RadixArk/朱邦华 Banghua Zhu|朱邦华（Banghua Zhu）]]：[[SGLang]]：个人主页将 `sgl-project/sglang` 直接列在 Open Source 部分，并说明 RadixArk 团队由 SGLang creators / core developers 组成。
- [[company/RadixArk/盛颖 Ying Sheng|盛颖（Ying Sheng）]]：SGLang co-creator / original paper author
- [[university/UC Berkeley/Shiyi Cao|Shiyi Cao]]：[[SGLang]]：UC Berkeley Sky 官方项目页面把 Shiyi Cao 列为 SGLang collaborator，连接 Berkeley inference research 与开源 serving runtime。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/RadixArk/RadixArk|RadixArk]]：公司页与社区/项目页均有显式记录；关系：`core-maintainer-network`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
