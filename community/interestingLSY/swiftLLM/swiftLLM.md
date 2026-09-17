---
type: project
name: SwiftLLM
organization: interestingLSY
linked_people:
  - "community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu"
layer: research-llm-inference-engine
open_source: true
repository: https://github.com/interestingLSY/swiftLLM
areas: [llm-serving, inference-engine, triton, paged-attention, scheduling, gpu-kernels]
last_verified: "2026-09"
linked_companies: []
---
# SwiftLLM

SwiftLLM 是刘胜与主导的轻量研究型 LLM inference engine，目标是在约 2k 行核心代码规模下保留接近 vLLM 的关键 serving 能力，方便研究者阅读、修改和验证新的系统想法。

## 技术位置
- control plane / data plane 分离的研究型架构；
- iterative scheduling / selective batching；
- PagedAttention 与 FlashAttention；
- Triton kernel 数据平面；
- 面向单机 NVIDIA GPU 的高性能实验基座。

它是理解刘胜与技术路线的一个“小型剖面”：先用一个可完全掌控的 inference engine 连接 scheduler 与 kernel，再进入 DistServe / LoongServe 的分布式 serving，最终在 DeepSeek 深入 FlashMLA、DeepGEMM、DeepSelect 等生产级 kernel 热路径。

## Sources
- https://github.com/interestingLSY/swiftLLM
- https://interestinglsy.github.io/

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu|刘胜与（Shengyu Liu）]]：[[community/interestingLSY/swiftLLM/swiftLLM|SwiftLLM]]：个人主导的轻量研究型 inference engine，用约 2k 行核心代码连接 scheduler、PagedAttention 与 Triton kernels。

<!-- END AUTO PROJECT PEOPLE -->
