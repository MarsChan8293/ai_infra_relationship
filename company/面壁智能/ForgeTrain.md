---
type: project
name: ForgeTrain
linked_people: []
companies: ["面壁智能"]
areas: [llm-training, cuda-kernels, triton, distributed-training, performance-optimization]
layer: training
repository: https://github.com/OpenBMB/ForgeTrain
status: active
last_verified: "2026-09"
linked_companies:
  - "company/面壁智能/面壁智能"
---
# ForgeTrain

## 项目简介

ForgeTrain 是 OpenBMB 公开的 LLM pretraining framework。官方仓库在 2026-05 发布 v0.1.0，并给出 MiniCPM4-0.5B / 8B 的 H100 训练路径；其实现覆盖 CUDA Graph、Triton fused kernels、通信计算重叠，以及自研 GEMM / FlashAttention kernel。

面壁智能官方产品/研究页面把 ForgeTrain 纳入其持续推进的高效模型与系统工作。本图谱因此把它作为面壁智能 AI Infra 线的 canonical infrastructure project，而不是只在公司正文里保留名字。

## Sources
- https://github.com/OpenBMB/ForgeTrain
- https://www.modelbest.cn/

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/面壁智能/面壁智能|面壁智能]]：公司页与社区/项目页均有显式记录。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
