# Research Operators Quick Guide

仓库统一使用三种一级研究方法：`EXPAND`、`DISCOVER`、`VERIFY`。完整设计与约束见 `docs/research-action-planner.md`。

## EXPAND

从一个明确的 seed（人物、项目、公司、学校、实验室、社区或团队）沿 typed relations 向外扩张。

```bash
python3 scripts/plan-research.py --seed "武永卫" --operator expand --budget 8
```

适合替代过去分别实现的人物 BFS、项目 BFS、学校 BFS。图距离只是 soft signal，不是硬截止。

## DISCOVER

扫描整个异构图的 coverage gap、frontier、bridge 和 target-type novelty，主动决定下一步值得研究哪里。

```bash
python3 scripts/plan-research.py --operator discover --budget 10
```

适合每日无人值守研究以及“还有哪些重要实体/关系没有覆盖”的问题。

## VERIFY

验证、补强或反证已有关系与弱证据，并跟进 history 中的 partial / unresolved dimensions。

```bash
python3 scripts/plan-research.py --operator verify --budget 10
```

适合 maintainer 身份、current affiliation、advisor/student、直接技术协作等不能靠弱信号推断的关系。对 `project`，VERIFY 还会处理 `verify_project_freshness`：当 `last_verified` 缺失或明显过旧时，重新核验项目 `status`、官方 `repository/docs`、`integrations` 与治理变化。

## 混合模式

```bash
python3 scripts/plan-research.py \
  --seed "Mooncake" \
  --operator expand \
  --operator verify \
  --budget 10
```

不显式传 `--operator` 时，global 模式运行 `DISCOVER + VERIFY`；传入 `--seed` 时加入 `EXPAND`。

## Project v3 与 Research Operators

- Project 的 `integrations` 直接参与 `related_projects` coverage，已确认的集成不会被 planner 反复当作缺口。
- `areas` 只作为技术相关性信号，不因为共享 area 自动创建 Project ↔ Project 或 Person ↔ Person 强边。
- `last_verified` 是项目 freshness 的 canonical 时间字段；不再依赖 `snapshot.as_of`。
- `verify_project_freshness` 永远属于 VERIFY，即使当前运行带有 EXPAND seed。

## 不变量

- Operator 解释“为什么查”，relation 解释“查什么”，strategy 解释“去哪查”。
- `action_id` 始终保持 `<node-id>::<relation>`，绝不包含 operator。
- `action_key` 始终按 source family + relation + target family 聚合，绝不包含 operator。
- 同一个 research objective 无论由 EXPAND、DISCOVER 还是 VERIFY 触发，都共享 cooldown 与历史。
- 搜索结果只有达到证据阈值才能写成节点或边；贡献者不自动等于 maintainer，同校不自动等于同学，兼容不自动等于人物直接合作。
