---
type: project
name: LiveServe
linked_people:
  - "university/香港中文大学/James Cheng"
  - "university/香港中文大学/Peiqi Yin"
layer: realtime-multimodal-serving
open_source: false
areas: [realtime-serving, multimodal-serving, kv-cache, scheduling, audio-serving, interaction-aware-serving]
people:
  - "university/香港中文大学/Peiqi Yin"
  - "university/香港中文大学/James Cheng"
related_projects: ["vLLM-Omni"]
last_verified: "2026-09"
linked_companies: []
---
# LiveServe

## 项目简介
LiveServe 是面向实时 omni-modal LLM 的 interaction-aware serving 系统，建立在 [[community/vllm-project/vLLM-Omni/vLLM-Omni|vLLM-Omni]] 上。它把用户实际播放进度、speech activity 与 barge-in 事件暴露给 serving pipeline，用这些交互信号改变调度与 KV 管理策略。

## 核心优化
- **Interaction-aware scheduling**：优先 first-audio 与接近 underrun 的 session，并限制生成远超播放进度的 token，减少被用户打断后浪费的计算。
- **Next-use-aware KV management**：避免仅按 LRU 驱逐多轮会话即将复用的 KV，并在用户说话期间预加载下一轮可能需要的 KV。
- 论文在两种 Omni-LM 与混合 workload 上报告 P90 audio TTFP 平均改善约 1.55×、最高 2.21×，completed-request throughput 平均改善约 1.15×。

## 人物
- [[university/香港中文大学/Peiqi Yin|尹沛骐（Peiqi Yin）]]：共同第一作者。
- [[university/香港中文大学/James Cheng|James Cheng]]：论文作者与尹沛骐导师。

## 开源状态
本轮没有找到稳定、可确认的官方公开代码仓库，因此保守标记 `open_source: false`；如果后续公开仓库出现，再升级为正式软件项目关系。

## Sources
- https://arxiv.org/abs/2606.22983
- https://yinpeiqi.github.io/

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[university/香港中文大学/James Cheng|James Cheng]]：[[university/香港中文大学/LiveServe|LiveServe]]：论文作者，研究 realtime omni-modal interaction 中的调度、KV 管理和用户交互反馈。
- [[university/香港中文大学/Peiqi Yin|尹沛骐（Peiqi Yin）]]：[[university/香港中文大学/LiveServe|LiveServe]]：共同第一作者；面向 realtime omni-modal LLM 的 interaction-aware serving，聚焦 barge-in、first-audio latency、KV eviction 与 preload。

<!-- END AUTO PROJECT PEOPLE -->
