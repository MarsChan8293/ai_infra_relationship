---
type: company
name: 深度求索（DeepSeek）
title: 深度求索（DeepSeek）
aliases: [深度求索, DeepSeek]
focus: frontier-models
projects: [DeepSeek-Infra, 3FS, DeepEP, DeepGEMM, FlashMLA, DeepJIT]
---
# 深度求索（DeepSeek）

## 公司简介
深度求索（DeepSeek）是中国 frontier-model lab，以高效训练、MoE、reasoning 与系统协同著称。它在 AI Infra 图谱中的特殊之处，是把模型创新持续下沉为独立开源系统组件，包括 EP communication、GEMM/attention kernels、分布式存储和 xPU JIT，从而形成模型与基础设施共同演化的技术栈。

## 主要贡献的社区项目
- [[community/DeepSeek-Infra/DeepSeek-Infra|DeepSeek Infra]]：公司对外开源的 systems stack 集合。
- [[community/DeepSeek-Infra/DeepEP|DeepEP]]：MoE expert-parallel communication。
- [[community/DeepSeek-Infra/DeepGEMM|DeepGEMM]]：GEMM / MoE GPU kernels。
- [[community/DeepSeek-Infra/FlashMLA|FlashMLA]]：MLA / attention kernels。
- [[community/DeepSeek-Infra/3FS|3FS]]：distributed storage。
- [[community/DeepSeek-Infra/DeepJIT|DeepJIT]]：xPU kernel JIT/runtime。

以上均属于 **company-led / deepseek-ai maintained** 关系，但具体人物责任仍按各仓库公开作者和维护记录分别建模。

## 核心人物
- [[梁文锋 Liang Wenfeng]]：创始人 / CEO；High-Flyer → DeepSeek
- [[陈德里 Deli Chen]]：Senior Researcher；V1/V2/V3/V4/R1/Coder/MoE 核心贡献
- [[郭达雅 Daya Guo]]：2023–2026 DeepSeek researcher；Coder / V2 / V3 / R1 等核心贡献
- [[邵智宏 Zhihong Shao]]：Research Scientist；DeepSeekMath、GRPO、R1 / reasoning
- [[Jiashi Li]]、[[刘胜与 Shengyu Liu]]：[[FlashMLA]] / [[DeepGEMM]] 等公开项目作者，连接模型架构与 GPU kernel

## 模型与 Infra
[[DeepSeek-V3]] · [[DeepSeek-R1]] · [[DeepSeek-Infra]] · [[DeepEP]] · [[DeepGEMM]] · [[FlashMLA]] · [[3FS]] · [[DeepJIT]]

## 图谱中的连接
[[vLLM]] · [[SGLang]] · [[FlashInfer]] · [[Mooncake]]。DeepSeek 的重要图谱特征是模型作者与系统作者并非简单一一对应，因此按论文/仓库公开作者分别建边。

## 跨公司关系
- [[郭达雅 Daya Guo]] ↔ [[刘大一恒 Dayiheng Liu]]：EMNLP 2023 论文合著，后来分别进入 DeepSeek 与 Qwen 核心网络。
- [[MoonEP]] ↔ [[DeepEP]]：项目级 inspiration 关系，不等于人物直接共事。

## Sources
- https://arxiv.org/abs/2412.19437
- https://arxiv.org/abs/2501.12948
- https://github.com/deepseek-ai
