---
type: community
name: FlagOS
aliases: [FlagOS, 众智 FlagOS, 智源 FlagOS, 智源社区]
linked_people:
  - "community/flagos-ai/FlagOS/吕梦思 Mengsi Lyu"
  - "community/flagos-ai/FlagOS/敖玉龙 Yulong Ao"
  - "community/flagos-ai/FlagOS/曹州"
  - "community/flagos-ai/FlagOS/白童心"
  - "community/flagos-ai/FlagOS/赵英利 Yingli Zhao"
  - "community/flagos-ai/FlagOS/陈飞宇"
  - "company/杭州先进编译科技有限公司/李嘉楠"
  - "company/杭州先进编译科技有限公司/柴赟达"
layer: ecosystem
status: active
repository: https://github.com/flagos-ai/FlagOS
companies: []
company_relation: community-led
areas:
  - "heterogeneous-computing"
  - "llm-training"
  - "llm-inference"
  - "ai-compiler"
  - "kernels"
  - "communication"
  - "benchmarking"
  - "heterogeneous-ai-stack"
  - "ecosystem-integration"
governance: BAAI-initiated multi-organization open-source community
people: [敖玉龙, 赵英利, 曹州, 吕梦思, 白童心, 陈飞宇]
integrations: []
last_verified: "2026-09"
linked_companies: []
---
# 众智 FlagOS 社区

## 社区定位
这里的“智源社区”按本仓库的 AI Infra 口径，指北京智源人工智能研究院联合科研机构、芯片企业、系统厂商与软件团队共同发起的 **众智 FlagOS 社区**。FlagOS 面向异构 AI 芯片构建统一开源系统软件栈，主线覆盖算子、编译器、训练/推理框架、集合通信、跨芯发版与评测。

截至 2026-09，智源公开资料将 [[FlagGems]]、[[FlagTree]]、[[FlagScale]]、[[FlagCX]] 列为四大核心技术库；[[FlagAttention]]、[[FlagRelease]]、[[FlagPerf]] 以及 [[vllm-plugin-FL]]、[[sglang-plugin-FL]] 等组成扩展工具与推理生态。这里不把 BGE、Aquila 等模型项目机械并入 AI Infra 图谱。

## 主要人物
- [[敖玉龙 Yulong Ao]]：2026 年智源 AI 框架研发团队负责人；公开资料明确其负责 FlagScale、FlagCX 与 FlagOS 插件体系。
- [[赵英利 Yingli Zhao]]：FlagScale maintainer；2025 智源大会讲解多元算力大模型分布式训练。
- [[吕梦思 Mengsi Lyu]]：围绕 FlagScale 自动调优与多芯片高效推理部署开展工程工作。
- [[曹州]]：FlagScale / FlagCX maintainer，公开分享 FlagScale 多后端管理与多硬件适配。
- [[白童心]]：智源 AI 算子库 / 编译器方向研究者，FlagGems 早期公开发布与技术介绍的重要人物。
- [[陈飞宇]]：智源 AI 编译研发工程师，FlagGems / FlagAttention 项目开发者。

## 外部贡献网络
- [[company/杭州先进编译科技有限公司/先进编译实验室|先进编译实验室]]：通过 [[FlagTree]] 与 [[FlagGems]] 形成稳定的 compiler / kernel 外部贡献网络；[[company/杭州先进编译科技有限公司/李嘉楠|李嘉楠]]为公开确认的 FlagTree 核心开发贡献者，AdvancedCompiler 账号则长期向 FlagGems upstream 提交工程 PR。这里记录外部技术协作，不推断 FlagOS 对实验室的组织隶属关系。

## 与现有推理生态的连接
FlagOS 的推理侧并不是另起炉灶：[[vllm-plugin-FL]] 直接连接 [[vLLM]]，[[sglang-plugin-FL]] 直接连接 [[SGLang]]；[[FlagGems]] / [[FlagAttention]] 提供算子层能力，[[FlagCX]] 提供通信层能力，[[FlagTree]] 面向多后端编译，[[FlagScale]] 覆盖训推框架层。

## Sources
- https://www.baai.ac.cn/zh-cn/system
- https://hub.baai.ac.cn/view/57616
- https://hub.baai.ac.cn/view/57117
- https://github.com/flagos-ai
- https://docs.flagos.io/en/latest/
- https://flagos.csdn.net/684f83da870cef7360648130.html
- https://github.com/AdvancedCompiler/FlagGems

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/flagos-ai/FlagOS/吕梦思 Mengsi Lyu|吕梦思（Mengsi Lyu）]]：[[赵英利 Yingli Zhao]]：**公开技术协作**；2024 FlagOS Triton & vLLM Workshop 共同介绍 FlagScale 多模态模型压缩与推理实践。
- [[community/flagos-ai/FlagOS/敖玉龙 Yulong Ao|敖玉龙（Yulong Ao）]]：[[FlagOS]]：**社区 / 技术负责人关系**；截至 2026-06 公开资料确认其负责 FlagOS 插件体系实践与核心框架研发。
- [[community/flagos-ai/FlagOS/曹州|曹州]]：https://github.com/flagos-ai/FlagScale/blob/main/MAINTAINERS.md
- [[community/flagos-ai/FlagOS/白童心|白童心]]：[[FlagOS]]：**系统软件栈研发网络**；FlagGems 后续成为 FlagOS 核心技术库之一。
- [[community/flagos-ai/FlagOS/赵英利 Yingli Zhao|赵英利（Yingli Zhao）]]：[[吕梦思 Mengsi Lyu]]：**公开技术协作**；2024 FlagOS Triton & vLLM Workshop 共同分享 FlagScale 多模态压缩与推理实践。
- [[community/flagos-ai/FlagOS/陈飞宇|陈飞宇]]：社区贡献关联；人物页已明确记录该社区。
- [[company/杭州先进编译科技有限公司/李嘉楠|李嘉楠（Jianan Li）]]：2025 FlagOS 技术文章明确写明：李嘉楠来自[[先进编译实验室]]，是 [[community/flagos-ai/FlagTree/FlagTree|FlagTree]] 核心开发贡献者。
- [[company/杭州先进编译科技有限公司/柴赟达|柴赟达（Yunda Chai）]]：[[community/flagos-ai/FlagTree/FlagTree|FlagTree]] / TLE：2026 CNCC 报告题目为“AI编译优化：Triton-tle在国产平台上的适配优化”，直接连接 TLE-Lite / TLE-Struct / TLE-Raw 路线。

<!-- END AUTO PROJECT PEOPLE -->
