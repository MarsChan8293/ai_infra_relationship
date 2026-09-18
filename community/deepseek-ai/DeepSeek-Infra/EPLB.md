---
type: project
name: EPLB
companies: ["深度求索"]
company_relation: company-led
layer: expert-parallel-load-balancing
open_source: true
repository: https://github.com/deepseek-ai/EPLB
areas: [moe, expert-parallel, load-balancing, inference, distributed-systems]
people:
  - "company/深度求索/Shaoyuan Chen"
last_verified: "2026-09"
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
