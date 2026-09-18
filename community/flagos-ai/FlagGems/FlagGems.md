---
type: project
name: FlagGems
linked_people:
  - "community/flagos-ai/FlagGems/0x45f"
  - "community/flagos-ai/FlagGems/huangyiqun"
  - "community/flagos-ai/FlagGems/tengqm"
  - "community/flagos-ai/FlagOS/白童心"
  - "community/flagos-ai/FlagOS/陈飞宇"
  - "community/flagos-ai/FlagTree/Galaxy1458"
  - "community/flagos-ai/FlagTree/zhzhcookie"
companies: ["杭州先进编译科技有限公司"]
company_relation: community-led
layer: kernel-library
repository: https://github.com/flagos-ai/FlagGems
open_source: true
areas: [triton, kernels, heterogeneous-computing, performance-optimization]
last_verified: 2026-09
linked_companies:
  - "company/杭州先进编译科技有限公司/杭州先进编译科技有限公司"
---
# FlagGems

## 项目简介
FlagGems 是 FlagOS 面向多种 AI 芯片的 Triton 通用算子库，目标是在统一编程接口下扩展不同硬件后端，并为大模型训练和推理提供高性能算子。它处在 serving engine 之下的 kernel 层，是连接多元芯片与上层框架的关键节点。

## GitHub
https://github.com/flagos-ai/FlagGems

## 主要维护者 / 组织
当前官方 `MAINTAINERS.md` 列出 `0x45f`、`huangyiqun`、`Galaxy1458`、`zhzhcookie` 等维护者。[[白童心]] 是 FlagGems 早期发布与技术方向的公开介绍者；[[陈飞宇]] 为公开确认的 FlagGems 项目开发者。这里区分“历史/技术负责人”与“当前 maintainer 列表”。

## 先进编译实验室贡献线
AdvancedCompiler GitHub 账号维护了 AdvancedCompiler/FlagGems fork，并长期以 FlagGems upstream collaborator 身份提交工程 PR。公开 PR 覆盖 W8A8/FP8 matmul、FlashAttention varlen、paged MQA logits、vLLM RMSNorm patch、TopK、TLE operators 与数值稳定性修复等。

这是一条长期工程贡献关系，不表示[[company/杭州先进编译科技有限公司/先进编译实验室|先进编译实验室]]拥有 FlagGems 或参与 FlagOS 项目治理。

## 生态关系
[[FlagOS]] · [[FlagTree]] · [[FlagAttention]] · [[FlagScale]] · [[vllm-plugin-FL]] · [[sglang-plugin-FL]] · [[vLLM]] · [[SGLang]] · [[company/杭州先进编译科技有限公司/先进编译实验室|先进编译实验室]]。

## Sources
- https://github.com/flagos-ai/FlagGems
- https://github.com/flagos-ai/FlagGems/blob/master/MAINTAINERS.md
- https://hub.baai.ac.cn/view/37643
- https://www.baai.ac.cn/zh-cn/system
- https://github.com/AdvancedCompiler/FlagGems
- https://github.com/flagos-ai/FlagGems/pull/4744
- https://github.com/flagos-ai/FlagGems/pull/3287

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/flagos-ai/FlagGems/0x45f|0x45f]]：https://raw.githubusercontent.com/flagos-ai/FlagGems/master/MAINTAINERS.md
- [[community/flagos-ai/FlagGems/huangyiqun|huangyiqun]]：https://raw.githubusercontent.com/flagos-ai/FlagGems/master/MAINTAINERS.md
- [[community/flagos-ai/FlagGems/tengqm|tengqm]]：https://raw.githubusercontent.com/flagos-ai/FlagGems/master/MAINTAINERS.md
- [[community/flagos-ai/FlagOS/白童心|白童心]]：[[FlagGems]]：**项目早期研发 / 技术介绍**；2024 智源大会由其系统介绍 FlagGems 的研发背景、跨后端支持与性能数据。
- [[community/flagos-ai/FlagOS/陈飞宇|陈飞宇]]：[[FlagGems]]：**开源项目开发**；智源官方人物页明确列为项目开发者，2025 公开分享进一步聚焦运行时优化。
- [[community/flagos-ai/FlagTree/Galaxy1458|Galaxy1458]]：项目关联；人物页已明确记录该项目。
- [[community/flagos-ai/FlagTree/zhzhcookie|zhzhcookie]]：项目关联；人物页已明确记录该项目。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/杭州先进编译科技有限公司/杭州先进编译科技有限公司|杭州先进编译科技有限公司]]：公司页与社区/项目页均有显式记录；关系：`community-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
