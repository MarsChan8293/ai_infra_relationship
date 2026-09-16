---
type: project
name: Chitu
aliases: ["赤兔", "Chitu Inference Engine"]
linked_people:
  - "company/清程极智/唐适之 Shizhi Tang"
companies: ["清程极智"]
company_relation: company-originated-and-jointly-open-sourced-with-tsinghua
layer: inference-engine
open_source: true
repository: https://github.com/thu-pacman/chitu
areas: [llm-serving, inference-engine, heterogeneous-compute, quantization, distributed-serving]
people:
  - "company/清程极智/唐适之 Shizhi Tang"
last_verified: "2026-09"
linked_companies:
  - "company/清程极智/清程极智"
---
# Chitu（赤兔）

## 项目简介
Chitu（赤兔）是面向生产部署的大模型推理引擎，重点强调高效率、异构硬件适配、从单机到多节点的可伸缩部署，以及长期运行稳定性。官方仓库在 2026-07 的 v0.6.0 已加入 `chitu.run`，可启动多节点、多实例和 PD 分离等复杂任务。

## 起源与组织关系
- [[company/清程极智/清程极智|清程极智]]：公司官网明确将赤兔列为自研生产级大模型推理引擎，并与清华大学团队联合开源。
- [[company/清程极智/唐适之 Shizhi Tang|唐适之]]：清程极智联合创始人，公开演讲与公司资料均将其与赤兔推理引擎研发直接关联。
- 官方代码仓库位于 `thu-pacman/chitu`，因此项目治理关系不能简化为“公司单独拥有”；本图谱保留清程极智与清华团队联合开源这一事实。

## AI Infra 重点
- 多节点 / 多实例推理部署
- Prefill-Decode 分离
- FP8 / FP4 等低精度推理路径
- 昇腾、沐曦、海光、NVIDIA 等异构算力适配
- 与 [[community/QingCheng-AI/ascend-kernel/ascend-kernel|ascend-kernel]] 的昇腾算子连接

## Sources
- https://github.com/thu-pacman/chitu
- https://www.qc-ai.cn/products/chitu
- https://www.qc-ai.cn/news/te7upl2wkvqrey3703yl6c4x
- https://hangzhou2025.gosim.org/zh/speakers/shizhi-tang/

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[company/清程极智/唐适之 Shizhi Tang|唐适之（Shizhi Tang）]]：[[清程极智]]：负责赤兔（Chitu）推理引擎及并行训练/推理系统、算子优化，在多种异构国产算力上做 LLM inference 优化。

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/清程极智/清程极智|清程极智]]：公司页与社区/项目页均有显式记录；关系：`company-originated-and-jointly-open-sourced-with-tsinghua`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
