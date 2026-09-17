---
type: project
name: DistServe
organization: Peking University / LLMServe
linked_people:
  - "community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu"
  - "company/深度求索/Yinmin Zhong"
  - "university/北京大学/Xin Jin"
layer: disaggregated-llm-serving
open_source: true
repository: https://github.com/LLMServe/DistServe
areas: [llm-serving, prefill-decode-disaggregation, scheduling, slo, distributed-inference, kv-cache]
last_verified: "2026-09"
---
# DistServe

DistServe 是北京大学系统团队的 LLM serving 项目，核心思想是把 prefill 与 decode 解耦，并分别优化资源配置、并行策略和 SLO，从而提升 goodput。论文发表于 OSDI 2024，代码由 `LLMServe/DistServe` 开源。

## 刘胜与网络
- [[company/深度求索/Yinmin Zhong|Yinmin Zhong]] 与 [[community/deepseek-ai/DeepSeek-Infra/刘胜与 Shengyu Liu|刘胜与]] 是论文前两位作者；仓库 `setup.py` 也将两人列为 package authors。
- [[university/北京大学/Xin Jin|Xin Jin]]：论文作者，也是刘胜与在北大 Computer Systems Research Group 的导师。

DistServe 是刘胜与从“系统调度 / serving architecture”进入更底层 GPU kernel 之前的重要节点：它关注 prefill/decode resource interference，而后续 FlashMLA / DeepSelect 则深入到 attention / TopK kernel 热路径。

## Sources
- https://www.usenix.org/conference/osdi24/presentation/zhong-yinmin
- https://github.com/LLMServe/DistServe
- https://github.com/LLMServe/DistServe/blob/main/setup.py
- https://interestinglsy.github.io/
