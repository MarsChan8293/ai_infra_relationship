---
type: project
name: GLM-130B
organization: Tsinghua KEG / PACMAN / THUNLP / Zhipu AI
linked_people:
  - "company/字节跳动/何家傲 Jiaao He"
  - "company/智谱/唐杰 Jie Tang"
  - "company/智谱/曾奥涵 Aohan Zeng"
  - "company/智谱/杜政晓 Zhengxiao Du"
  - "company/智谱/郑勤锴 Qinkai Zheng"
  - "company/清程极智/翟季冬 Jidong Zhai"
  - "company/清程极智/马子轩 Zixuan Ma"
  - "university/清华大学/Wenguang Chen"
areas: [foundation-models, large-scale-pretraining, distributed-training, heterogeneous-hardware, inference-efficiency]
layer: pretraining-system-model-codesign
open_source: true
repository: https://github.com/THUDM/GLM-130B
last_verified: "2026-09"
---
# GLM-130B

GLM-130B 是清华 KEG 发起的 130B 中英双语稠密预训练模型，也是理解 [[university/清华大学/KEG|KEG]] 与 [[university/清华大学/PACMAN|PACMAN]] 如何发生真实系统协作的关键节点。

## 组织分工
官方项目材料明确列出：
- KEG：Aohan Zeng、Xiao Liu 为学生负责人，杜政晓、郑勤锴等参与模型、数据、训练稳定性与评测。
- PACMAN：马子轩、何家傲、孙桢波、翟季冬、陈文光作为技术贡献者。
- THUNLP / BMInf：参与大模型训练与系统支持。
- Zhipu.AI：提供计算资源并有工程贡献者参与。
- 项目总负责：[[company/智谱/唐杰 Jie Tang|唐杰]]。

## 系统意义
项目官方回顾写明，在 100B 级预训练过程中遇到随机硬件故障、显存压力、Megatron / DeepSpeed 3D pipeline、optimizer state 恢复、TCP 阻塞以及异构加速器适配等问题，PACMAN 团队参与解决这些系统瓶颈。

因此 GLM-130B 在本图谱里不仅是模型节点，也是 `model research ↔ large-scale systems` 的交叉证据。

## 技术谱系
`GLM → GLM-130B → ChatGLM / CodeGeeX → GLM-4.x`

同时系统侧可观察到：
`FastMoE / BaGuaLu → GLM-130B large-scale training → PACMAN LLM serving / compiler / memory optimization`

## Sources
- https://keg.cs.tsinghua.edu.cn/glm-130b/posts/glm-130b/
- https://keg.cs.tsinghua.edu.cn/glm-130b/zh/posts/glm-130b/
- https://pacman.cs.tsinghua.edu.cn/~zjd/

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[company/字节跳动/何家傲 Jiaao He|何家傲（Jiaao He）]]：[[university/清华大学/GLM-130B|GLM-130B]]：官方项目页把何家傲列入 PACMAN contributors，连接 MoE / distributed training 与 100B 级模型训练系统协作。
- [[company/智谱/唐杰 Jie Tang|唐杰（Jie Tang）]]：GLM / [[university/清华大学/GLM-130B|GLM-130B]] / ChatGLM
- [[company/智谱/曾奥涵 Aohan Zeng|曾奥涵（Aohan Zeng）]]：[[university/清华大学/GLM-130B|GLM-130B]]：2022–2023 学生负责人 / Lead Contributor；Model Implementation、Model Architecture、Training Stability 核心贡献
- [[company/智谱/杜政晓 Zhengxiao Du|杜政晓（Zhengxiao Du）]]：[[university/清华大学/GLM-130B|GLM-130B]]：2022–2023 Model Implementation / Architecture
- [[company/智谱/郑勤锴 Qinkai Zheng|郑勤锴（Qinkai Zheng）]]：[[university/清华大学/GLM-130B|GLM-130B]]：2022 Tsinghua KEG contributor
- [[company/清程极智/翟季冬 Jidong Zhai|翟季冬（Jidong Zhai）]]：[[university/清华大学/GLM-130B|GLM-130B]]：官方回顾明确记录 PACMAN 团队帮助 KEG 解决 100B 级训练的 pipeline、显存、故障与异构平台问题，形成 [[university/清华大学/KEG|KEG]] ↔ PACMAN 的直接协作。
- [[company/清程极智/马子轩 Zixuan Ma|马子轩（Zixuan Ma）]]：[[university/清华大学/GLM-130B|GLM-130B]]：官方项目材料列为 PACMAN contributor，同时进入 ICLR 2023 GLM-130B 作者网络。
- [[university/清华大学/Wenguang Chen|陈文光（Wenguang Chen）]]：[[university/清华大学/GLM-130B|GLM-130B]]：官方项目贡献团队将陈文光列入 Tsinghua PACMAN contributors，连接大模型训练中的并行 / 系统优化。

<!-- END AUTO PROJECT PEOPLE -->
