---
type: company
name: Naive AI
aliases: ["NaiveAI", "naive.ai"]
linked_people: []
areas:
  - "ai-centered-rd"
  - "long-context-models"
  - "inference-optimization"
  - "reinforcement-learning-infrastructure"
  - "sparse-attention"
  - "speculative-decoding"
projects:
  - "Naive-N0.5-Flash"
  - "NaiveRT"
people:
  - "company/Naive AI/代季峰 Jifeng Dai"
  - "company/Naive AI/Zhe Chen"
  - "company/Naive AI/Weiyun Wang"
last_verified: "2026-09"
linked_projects:
  - "company/Naive AI/Naive-N0.5-Flash"
  - "company/Naive AI/NaiveRT"
---
# Naive AI

## 组织定位

Naive AI（公开品牌亦写作 NaiveAI / naive.ai）是 2026 年公开进入大模型与 AI R&D 基础设施视野的团队。官方研究页面将自身方法描述为 **AI-centered R&D**：人类研究者定义方向、约束和验收标准，模型参与代码实现、实验、性能分析、验证与迭代。

2026-09 的 The Information 报道将 Naive AI 描述为由清华大学教授 [[company/Naive AI/代季峰 Jifeng Dai|代季峰（Jifeng Dai）]] 领导的 AI startup。由于公司官网目前没有公开完整团队名册，本图谱只把有直接公开证据的人物关系写成强边；模型发布贡献不自动推断为雇佣或汇报关系。

## AI Infra 主线

- [[company/Naive AI/Naive-N0.5-Flash|Naive-N0.5-Flash]]：309B MoE、15.5B active、原生 1M context；由 MiMo-V2.5 开放权重继续训练而来，将原有 global-attention 层替换为轻量化 DeepSeek Sparse Attention。
- [[company/Naive AI/NaiveRT|NaiveRT]]：面向超长上下文 RL rollout 的单流低延迟 inference runtime，核心技术包括 speculative decoding、mega-kernel fusion、Programmatic Dependent Launch（PDL）与 GPU-driven scheduling。
- [[community/sgl-project/SGLang/SGLang|SGLang]]：Naive-N0.5-Flash 官方 acknowledgments 明确感谢 SGLang 的开源 inference infrastructure；NaiveRT 技术报告也以同机 SGLang 路径作为 full speculative round 的对照基线。这里记录技术影响 / benchmark 关系，不标记为 fork、治理或正式 integration。

## 人物

- [[company/Naive AI/代季峰 Jifeng Dai|代季峰（Jifeng Dai）]]：The Information 报道称 Naive AI 由其领导；清华官方页面确认其现为电子工程系副教授。
- [[company/Naive AI/Zhe Chen|Zhe Chen]]（HF: `czczup`）：直接发布 Naive-N0.5-Flash、FP8 与 Draft 模型；这是明确的项目贡献证据，不单独推断公司雇佣关系。
- [[company/Naive AI/Weiyun Wang|Weiyun Wang]]（HF: `Weiyun1025`）：直接上传和更新 Naive-N0.5-Flash 模型配置与权重；同样按项目贡献记录。

## 与 MiroMind 的研究网络连续性

代季峰个人主页记录其在 2025-05 至 2026-01 担任 MiroMind Leader；MiroFlow 作者网络中又包含代季峰与 Zhe Chen 等人。该事实支持“前后存在研究协作网络连续性”，但不足以把所有 MiroMind 成员批量升级为 Naive AI 员工，因此不建立未经逐人验证的 coworker / employment 边。

## Sources

- https://naive.ai/en/research/
- https://github.com/NaiveAI-Labs/Naive-N0.5-Flash
- https://huggingface.co/NaiveAI
- https://www.theinformation.com/articles/tsinghua-professors-stealth-llm-startup-hits-1-4-billion-valuation/
- https://jifengdai.org/

<!-- BEGIN AUTO COMPANY COMMUNITY LINKS -->
## 社区 / 开源项目关联（自动汇总）

以下关系由公司页与社区/项目页的显式元数据双向汇总。员工个人参与不会自动升级为公司官方关系。

- [[company/Naive AI/Naive-N0.5-Flash|Naive-N0.5-Flash]]：公司页与社区/项目页均有显式记录。
- [[company/Naive AI/NaiveRT|NaiveRT]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMPANY COMMUNITY LINKS -->
