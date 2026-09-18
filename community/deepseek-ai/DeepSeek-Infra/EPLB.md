---
type: project
name: EPLB
linked_people:
  - "company/深度求索/Shaoyuan Chen"
companies: ["深度求索"]
company_relation: company-led
layer: expert-parallel-load-balancing
open_source: true
repository: https://github.com/deepseek-ai/EPLB
areas: [moe, expert-parallel, load-balancing, inference, distributed-systems]
people:
  - "company/深度求索/Shaoyuan Chen"
last_verified: "2026-09"
linked_companies:
  - "company/深度求索/深度求索"
---
# EPLB

EPLB（Expert Parallelism Load Balancer）是 DeepSeek-V3 / R1 Expert Parallel 系统中的 expert placement / replication 算法实现。它依据历史或估计的 expert load，复制高负载 expert，并把 replicas 放置到 GPU / node 上，以降低 MoE 的负载偏斜与跨节点流量。

## 策略
- **Hierarchical Load Balancing**：利用 group-limited expert routing，先平衡 nodes，再做 node 内 replica placement，适合较小 EP size 的 prefill。
- **Global Load Balancing**：全局进行 expert replication / placement，适合更大 EP size 的 decode。

## 人物
- [[company/深度求索/Shaoyuan Chen|Shaoyuan Chen]]：EPLB 初始提交的公开 author。这里记录 project contribution，不据此单独推断长期 maintainer 身份。

## 后续
[[LPLB]] 在 EPLB 基础上继续解决 per-batch dynamic imbalance，并与 [[DeepEP]] 的实时通信统计结合。

## Sources
- https://github.com/deepseek-ai/EPLB
- https://github.com/deepseek-ai/EPLB/blob/main/README.md
- https://github.com/deepseek-ai/EPLB/commit/f9bc62e84182eee311ec97c3ec3ce38f5073a646

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[company/深度求索/Shaoyuan Chen|Shaoyuan Chen]]：[[community/deepseek-ai/DeepSpec/DeepSpec|DeepSpec]] / DSpark：2026 DSpark 作者网络成员，进入 DeepSeek speculative decoding 全栈研究线；与 [[company/深度求索/梁文锋 Liang Wenfeng|梁文锋（Wenfeng Liang）]] 同属论文作者网络。
- [[community/deepseek-ai/DeepSeek-Infra/EPLB|EPLB...

<!-- END AUTO PROJECT PEOPLE -->

<!-- BEGIN AUTO COMMUNITY COMPANY LINKS -->
## 关联公司（自动汇总）

以下关系由公司页与本社区/项目页的显式元数据双向汇总。仅表示可核验的组织级关联，不因员工个人贡献自动推断公司治理或所有权。

- [[company/深度求索/深度求索|深度求索]]：公司页与社区/项目页均有显式记录；关系：`company-led`。

<!-- END AUTO COMMUNITY COMPANY LINKS -->
