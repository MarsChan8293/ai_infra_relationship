# Ecosystem Research Action Planner

## 目标

仓库的自动研究不再把“人物”作为唯一候选，也不把 BFS 深度当作主要搜索边界。planner 面向整个 AI Infra 异构生态图，将 Person、Company、School、Research Institution、Project、Community、Model Team 等统一视为可研究实体，并对“下一步调查动作”排序。

一个 action 的基本结构是：

`source entity × relation to investigate × target entity family × source strategy`

例如：

- `Mooncake × maintainers × person × governance/CODEOWNERS/GitHub activity`
- `清华大学 × projects × project/community × lab project pages`
- `无问芯穹 × projects × project/community/team × GitHub org + official engineering docs`
- `SGLang × originating_org × company/research/community × repository + official docs`

## 两层 planner

当前 daily planner 分成两个确定性阶段：

1. `scripts/generate-research-queue.py` 生成 graph-only candidate actions。
2. `scripts/plan-research.py` 读取 durable action history，应用 cooldown / partial follow-up / empirical yield，再重新做 heterogeneous portfolio selection。

**日常与 Agent 自动化应调用 `scripts/plan-research.py`。** 旧的 `generate-research-queue.py` 继续保留，作为低层 candidate generator 和兼容入口。

## 为什么不是继续优化 BFS

BFS 适合已知完整图上的邻域遍历，但本仓库面对的是开放世界研究：只有执行一次搜索后，才知道会不会发现新节点、新边或更强证据。因此 `distance` 只作为可选 seed 模式下的软先验，不再是硬截止条件。

基础 candidate score 仍采用可解释、确定性的 heuristic expected-gain proxy：

- typed relation coverage gap
- AI Infra relevance
- target-type novelty
- bridge value
- frontier potential
- evidence quality
- uncertainty
- relative research cost
- redundancy / hub penalty
- optional soft seed-distance penalty

这些值只用于排序 research action，不是实体重要性排名，也不是概率预测。

## Action history

Durable history 位于：

`research/action-history.json`

它不是 generated artifact，不会被 graph rebuild 覆盖。每次 Agent **实际执行**一个 action 后都应追加一条记录；仅仅被 planner 选中不算执行。

每条 history 至少包含：

- `run_id`
- `attempted_at`
- `action_id`
- `action_key`
- `status`
- graph/evidence delta

status 有四种：

- `success`：本 action 的主要研究目标获得了足够证据，并产生可用图谱/证据增量。
- `partial`：没有完全解决原 action，但得到明确的高价值子结果。
- `unresolved`：进行了有效调查，但在当前证据阈值下无法建立请求关系。
- `rejected`：候选关系被反证、明显不成立，或不应在没有实质新证据时重试。

`partial` 是一级状态，不能压成 success/failure。它应尽可能记录：

- `resolved_dimensions`
- `unresolved_dimensions`

例如 Run 2 的 `weijinqian0 -> affiliation`：

- resolved: `identity:Jinqian Wei`, `community_role:Committer`
- unresolved: `employer`, `school`

这样两天 cooldown 后，planner 可以恢复同一 action，同时明确下一次应该继续查什么，而不是重新从零搜索。

## Cooldown

默认 exact-action cooldown：

- `success`: 1 day
- `partial`: 2 days
- `unresolved`: 7 days
- `rejected`: 30 days

cooldown 期间 action 仍保留在 machine-readable candidates 中，但：

`eligible: false`

因此它不会进入 daily portfolio，也不会挤占 Next eligible frontier。Markdown queue 会单独展示 `Cooldown / history-suppressed`。

单条 history 可以通过 `retry_after_days` 覆盖默认值，例如某个项目明确写了“下月发布 governance 文件”时，可以人为设置更长或更短的 retry window。

## Empirical yield

planner 会按稳定的 `action_key` 汇总历史，例如：

`project:maintainers:person`

历史信号包括：

- success / partial / unresolved / rejected 分布
- transparent outcome reward
- mean reward

默认 reward 从可审计 delta 派生：

- new node: +2
- new edge: +1
- evidence upgraded: +0.5
- verified claim: +0.75
- resolved dimension: +0.5
- rejected claim: -0.25

它目前**不会替代 graph score**。历史调整最大只有很小幅度，并对样本数做强 shrinkage：前 1–2 次记录几乎只产生微调，避免两轮数据就把算法“训练歪”。

以后积累足够多 action records 后，可以在不改变 ledger schema 的情况下换成 Thompson Sampling / contextual bandit。

## 异构实体与动作模板

当前脚本将仓库类型归入以下 family：

- `person`
- `company`
- `school`（兼容历史 `university`）
- `research`
- `project`（包括 project / infra-project / model-project / project-collection）
- `community`
- `team`

不同 family 使用不同的研究关系模板。例如：

- Person：affiliation、project contribution、technical collaborator、academic lineage
- Company：key people、projects、academic links
- School：labs/groups、key people、projects、spinouts
- Project：maintainers、originating org、related projects
- Community：core people、projects、member orgs

因此“学校缺项目”和“人物缺项目贡献”不会被当成同一个 gap。

## Daily Agent 模式

推荐流程：

```bash
python3 scripts/audit-graph.py --root . --output generated

python3 scripts/plan-research.py \
  --root . \
  --generated generated \
  --history research/action-history.json \
  --budget 10 \
  --limit 60
```

主要输出：

- `generated/research-actions.json`：机器可读、history-aware action queue。
- `generated/research-queue.md`：人工 review 视图。
- `generated/research-history-summary.json`：cooldown、partial 和 action-key yield 汇总。
- `generated/research-priority.json`：旧文件名兼容层。

`--seed` 支持任意已知实体类型。例如：

```bash
python3 scripts/plan-research.py \
  --seed "Mooncake" \
  --budget 8
```

seed 模式仍计算图距离，但 `--max-bfs-depth` 只是 soft radius，不会禁止高价值远端生态发现。

调试 cooldown 时可用：

```bash
python3 scripts/plan-research.py --as-of 2026-09-23
```

临时查看“完全忽略历史”的基线：

```bash
python3 scripts/plan-research.py --ignore-history
```

## 记录一次 action outcome

推荐让 Agent 使用 recorder，而不是手工编辑 JSON：

```bash
python3 scripts/record-research-action.py \
  'community/vllm-project/vLLM-Ascend/weijinqian0::affiliation' \
  --status partial \
  --run-id 2026-09-16-haes-2 \
  --resolved 'identity:Jinqian Wei' \
  --resolved 'community_role:Committer' \
  --unresolved employer \
  --unresolved school \
  --evidence-upgraded 2 \
  --note 'Identity and community role resolved; employer/school still unverified.'
```

如果 action 当前仍在 `generated/research-actions.json`，recorder 会自动取 `action_key` 和 source name。对历史 action 或已从 candidates 消失的 action，也可显式传 `--action-key`。

## Portfolio selection

默认一次最多选择 10 个 eligible action，并限制同一 source 每轮只执行一个 action。planner 还使用 source-family 软上限，避免人物数量较多时 daily queue 被 person 节点垄断。如果候选不足，会自动放松类型上限补满预算。

动作继续标成：

- `exploitation`
- `exploration`
- `bridge`
- `verification`

history/cooldown 是 eligibility 与小幅 score adjustment，不额外制造第五种 bucket。

## Agent 执行约束

Agent 对 selected action 应遵循：

1. 优先官方主页、官方仓库、governance/CODEOWNERS/MAINTAINERS、论文、学校/研究机构一手资料。
2. action 只授权“调查”，不授权无证据创建节点或边。
3. 兼容、赞助、同校、同公司或简单共同出现在某列表中，不自动升级成人物直接关系。
4. 在当前 action 中发现的二级线索不要无限递归；把它留给下一次 planner。
5. 执行后必须记录 outcome，即使结果是 unresolved 或 rejected。
6. partial 必须保存其已解决与未解决子问题，避免有效信息被二元标签吃掉。
7. 修改后继续运行 graph / relation / schema audits。

## Schema 影响

仍然**不要求批量修改已有 Markdown frontmatter**。

相关 non-node schema：

- `schema/research-action.yaml`
- `schema/research-action-history.yaml`

Durable execution ledger：

- `research/action-history.json`

因此人物、公司、学校、项目、社区等现有 node schema 不需要迁移。
