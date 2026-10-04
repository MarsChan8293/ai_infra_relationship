---
type: project
name: Naive-N0.5-Flash
status: active
linked_people:
  - "company/Naive AI/Weiyun Wang"
  - "company/Naive AI/Zhe Chen"
repository: https://github.com/NaiveAI-Labs/Naive-N0.5-Flash
docs: https://naive.ai/en/research/
companies: ["Naive AI"]
layer: other
areas:
  - "mixture-of-experts"
  - "million-token-context"
  - "sliding-window-attention"
  - "deepseek-sparse-attention"
  - "continued-pretraining"
  - "ai-rd"
  - "speculative-decoding"
hardware:
  - "nvidia"
last_verified: "2026-09"
linked_companies:
  - "company/Naive AI/Naive AI"
code_availability: public
---
# Naive-N0.5-Flash

## 项目简介

Naive-N0.5-Flash 是 Naive AI 于 2026-09-27 发布的开放权重模型：309B MoE、15.5B active parameters、48 层，原生支持 1M-token context。官方 GitHub / Hugging Face 权重采用 MIT License。

该节点被纳入 AI Infra 图谱的原因不是“模型发布”本身，而是它和训练系统、稀疏注意力、超长上下文 RL 与专用 inference runtime [[company/Naive AI/NaiveRT|NaiveRT]] 形成了明确的 algorithm-system co-design 链路。

## 架构血缘

官方说明 Naive-N0.5-Flash 建立在 Xiaomi MiMo-V2.5 开放权重基础模型之上，并将原有 global-attention 层替换为 DeepSeek Sparse Attention（DSA）。最终网络以 Sliding-Window Attention（SWA）和 DSA 混合组成，主体约为 5:1 的 SWA–DSA 布局。

- SWA window：128 tokens。
- DSA：backbone attention 选择 top-2048 tokens。
- DSA 使用 GQA4，并采用 16 query heads 的轻量 indexer。
- 官方报告称轻量 indexer 相比原始 DSA index selection 路径减少约 44% wall time。
- 架构变更后进行了 3.25T tokens 的多阶段训练，始终围绕 1M context 适配。

## AI Infra 关系

- [[company/Naive AI/NaiveRT|NaiveRT]]：为该模型构建的专用 inference runtime，重点优化 RL rollout 中的 single-stream decode latency。
- [[community/sgl-project/SGLang/SGLang|SGLang]]：官方 acknowledgments 明确感谢 SGLang team/community 的开源 inference infrastructure。该关系记为技术影响 / 生态参考，不推断为直接 integration。
- MiMo-V2.5：base-model lineage。
- DeepSeek Sparse Attention：architecture lineage。

## 公开贡献证据

- [[company/Naive AI/Zhe Chen|Zhe Chen / czczup]]：Hugging Face activity 显示其直接发布 Naive-N0.5-Flash、FP8 和 FP8-Draft。
- [[company/Naive AI/Weiyun Wang|Weiyun Wang / Weiyun1025]]：Hugging Face commit history 显示其直接上传模型配置与权重。

## Sources

- https://naive.ai/en/research/
- https://github.com/NaiveAI-Labs/Naive-N0.5-Flash
- https://huggingface.co/NaiveAI/Naive-N0.5-Flash
- https://huggingface.co/NaiveAI/Naive-N0.5-Flash/commits/main

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[company/Naive AI/Weiyun Wang|Weiyun Wang]]：https://huggingface.co/NaiveAI/Naive-N0.5-Flash/commits/main
- [[company/Naive AI/Zhe Chen|Zhe Chen]]：[[company/Naive AI/Naive-N0.5-Flash|Naive-N0.5-Flash]]

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/Naive AI/Naive AI|Naive AI]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
