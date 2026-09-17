---
type: project
name: Lethe
organization: thu-pacman
linked_people:
  - "company/清程极智/翟季冬 Jidong Zhai"
areas: [llm-serving, kv-cache, reasoning-models, cache-pruning, memory-efficiency]
layer: kv-cache-optimization
open_source: false
last_verified: "2026-09"
linked_companies: []
---
# Lethe

Lethe 是 PACMAN 参与的 reasoning-intensive LLM serving 工作，发表于 AAAI 2026，核心方向是 **layer- and time-adaptive KV cache pruning**。

它说明 PACMAN 的 serving 路线已经从 FastDecode 的异构 CPU/GPU pipeline、Jenga 的 memory management，进一步推进到 reasoning workload 下直接优化 KV cache 生命周期与保留策略。

论文作者包括 Hui Zeng、Daming Zhao、Pengfei Yang、WenXuan Hou、Tianyang Zheng、Hui Li、Weiye Ji、[[company/清程极智/翟季冬 Jidong Zhai|翟季冬]]。当前仓库先保留项目与实验室主干，不因一次合著机械创建全部作者节点。

## Sources
- https://pacman.cs.tsinghua.edu.cn/~zjd/publication/generated/dblp-confaaai-zeng-zyhzljz-26/
- https://pacman.cs.tsinghua.edu.cn/~zjd/author/jidong-zhai/

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[company/清程极智/翟季冬 Jidong Zhai|翟季冬（Jidong Zhai）]]：[[community/thu-pacman/Lethe/Lethe|Lethe]]：AAAI 2026，reasoning-intensive serving 的 adaptive KV-cache pruning。

<!-- END AUTO PROJECT PEOPLE -->
