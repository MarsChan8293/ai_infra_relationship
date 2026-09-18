---
type: project
name: LPLB
companies: ["深度求索"]
company_relation: company-led
layer: moe-load-balancing
open_source: true
repository: https://github.com/deepseek-ai/LPLB
areas: [moe, expert-parallel, load-balancing, gpu-systems, nvshmem, inference]
people:
  - "community/deepseek-ai/DeepSeek-Infra/Huanqi Cao"
last_verified: "2026-09"
---
# LPLB

LPLB（Linear-Programming-Based Load Balancer）是 DeepSeek 开源的 MoE Expert Parallel 动态负载均衡组件。它针对 batch 级 workload 波动，用线性规划决定 token 到 redundant expert 的动态重定向，属于 [[DeepEP]] / [[EPLB]] 之上的负载均衡控制层。

## 技术关系
- [[EPLB]]：LPLB 直接复用 EPLB 的 expert reordering / replication placement 思路，并把静态负载均衡扩展到动态 batch 波动。
- [[DeepEP]]：可从 DeepEP buffer 获取实时 workload statistics；跨 GPU 同步路径使用 NVLink / NVSHMEM。
- NVIDIA mathDx：内置 LP solver 使用 cuSolverDx / cuBLASDx；README 明确标注当前仍处于 early research stage。

## 人物
- [[Huanqi Cao]]：项目 package metadata 唯一显式作者，公开邮箱 `caohuanqi@deepseek.com`。该证据证明项目作者身份与 DeepSeek 专业邮箱关联，不自动升级为 maintainer / team lead。

## Sources
- https://github.com/deepseek-ai/LPLB
- https://github.com/deepseek-ai/LPLB/blob/main/README.md
- https://github.com/deepseek-ai/LPLB/blob/main/pyproject.toml
- https://github.com/deepseek-ai/LPLB/commit/0490f79452f7ef277e814449600b1b1dd4c663b3
