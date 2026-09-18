---
type: project
name: profile-data
companies: ["深度求索"]
company_relation: company-led
layer: systems-profiling
open_source: true
repository: https://github.com/deepseek-ai/profile-data
areas: [profiling, moe, expert-parallel, prefill, decode, overlap, production-inference]
last_verified: "2026-09"
---
# profile-data

profile-data 是 DeepSeek 对外公开的 training / inference profiling 数据仓库。它不是通用 profiler，而是解释 DeepSeek 实际 MoE 通信-计算 overlap 与 production inference 配置的证据型项目。

## 公开配置
- Training：展示 [[DualPipe]] forward / backward chunks 的 computation-communication overlap。
- Prefill：EP32 / TP1，双 micro-batch overlap。
- Decode：EP128 / TP1，双 micro-batch overlap；README 将 all-to-all 实现直接指向 [[DeepEP]]。

因此该节点更适合作为 `DualPipe ↔ DeepEP ↔ production inference` 的系统证据桥，而不是强行扩成 maintainer 网络。

## Sources
- https://github.com/deepseek-ai/profile-data
- https://github.com/deepseek-ai/profile-data/blob/main/README.md
