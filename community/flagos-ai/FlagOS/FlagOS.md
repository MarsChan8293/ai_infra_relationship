---
type: community
name: FlagOS
aliases: [FlagOS, 众智 FlagOS, 智源 FlagOS, 智源社区]
category: heterogeneous-ai-system-stack
repository: https://github.com/flagos-ai
companies: []
company_relation: community-led
areas: [heterogeneous-computing, llm-training, llm-inference, ai-compiler, kernels, communication, benchmarking]
governance: BAAI-initiated multi-organization open-source community
people: [敖玉龙, 赵英利, 曹州, 吕梦思, 白童心, 陈飞宇]
last_verified: 2026-09
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

## 与现有推理生态的连接
FlagOS 的推理侧并不是另起炉灶：[[vllm-plugin-FL]] 直接连接 [[vLLM]]，[[sglang-plugin-FL]] 直接连接 [[SGLang]]；[[FlagGems]] / [[FlagAttention]] 提供算子层能力，[[FlagCX]] 提供通信层能力，[[FlagTree]] 面向多后端编译，[[FlagScale]] 覆盖训推框架层。

## Sources
- https://www.baai.ac.cn/zh-cn/system
- https://hub.baai.ac.cn/view/57616
- https://hub.baai.ac.cn/view/57117
- https://github.com/flagos-ai
- https://docs.flagos.io/en/latest/
