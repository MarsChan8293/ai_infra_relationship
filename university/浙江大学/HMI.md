---
type: project
name: HMI
companies: []
company_relation: research-project
layer: multi-tenant-inference
open_source: false
areas: [multi-tenant-serving, memory-management, parameter-swapping, prefetch, pipeline]
people:
  - "university/浙江大学/Jue Wang"
  - "university/浙江大学/Huan Li"
  - "university/浙江大学/Lidan Shou"
last_verified: "2026-09"
---
# HMI

## 项目简介
HMI（Hierarchical Knowledge Management for Efficient Multi-Tenant Inference in Pretrained Language Models）是浙江大学研究网络中的 multi-tenant inference 系统工作。

它把模型知识划分为 general / domain-specific / task-specific 层级，并围绕大量 tenant 的参数存储、GPU memory、parameter swapping、prefetch 与 fine-grained pipeline 做资源复用。其系统目标与现代 LLM serving 中的多租户资源管理高度相关。

## 人物与机构
- [[university/浙江大学/Jue Wang|Jue Wang]]、[[university/浙江大学/Huan Li|Huan Li]]、[[university/浙江大学/Lidan Shou|Lidan Shou]]：论文作者网络。
- [[university/浙江大学/SuDIS|SuDIS]]：该工作所在的浙江大学数据系统 / Efficient AI 研究生态。

## 开源状态
截至 2026-09，本轮研究确认了论文与作者关系，但未确认稳定的官方 HMI 代码仓库，因此 `open_source: false` 表示“未确认公开代码”，不是对方法可复现性的评价。

## Sources
- https://arxiv.org/abs/2504.17449
- https://longaspire.github.io/publication/
