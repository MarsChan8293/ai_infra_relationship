# Ecosystem Research Action Planner

## 核心模型：三个 Research Operators

仓库的研究调度统一收敛为三个一级操作符：`EXPAND`、`DISCOVER`、`VERIFY`。

它们不是新的实体类型，也不会替代现有 typed relation。三层语义固定为：

- **Operator**：为什么发起这次调查。
- **Relation**：具体调查什么关系。
- **Strategy**：优先去哪里找证据。

因此一个 research action 可以理解为：

`operator × source entity × relation × target family × source strategy`

### EXPAND：从已知种子向外扩张

适用于“从某个人 / 项目 / 公司 / 学校 / 实验室出发继续探索”的任务。

典型用法：

```bash
python3 scripts/plan-research.py --seed "武永卫" --operator expand --budget 8
python3 scripts/plan-research.py --seed "Mooncake" --operator expand --budget 8
```

`EXPAND` 复用实体 family 对应的 relation templates，例如人物的 `affiliation`、`project_contribution`、`technical_collaborator`、`academic_lineage`，项目的 `maintainers`、`originating_org`、`related_projects`。

seed 距离只作为 soft signal，不作为硬 BFS 截止条件。开放世界研究中，远端但高价值的候选仍可进入队列。

### DISCOVER：从全图缺口和边疆发现下一步

适用于“现在整个图谱最值得补哪里”“还有哪些公司 / 项目 / 实验室 / 人物没有覆盖”等全局任务。

典型用法：

```bash
python3 scripts/plan-research.py --operator discover --budget 10
```

`DISCOVER` 主要使用这些图信号生成和排序候选：

- typed relation coverage gap
- AI Infra relevance
- target-type novelty
- bridge value
- frontier potential
- evidence quality
- uncertainty
- relative research cost
- redundancy / hub penalty

它负责 global graph completion，而不是要求用户先提供一个 seed。

### VERIFY：补强、反证和跟进已有证据

适用于“这个人到底是不是 maintainer”“当前 affiliation 是否仍成立”“某条边证据太弱”“上一次 partial 还有哪些维度未解决”等任务。

典型用法：

```bash
python3 scripts/plan-research.py --operator verify --budget 10
```

VERIFY 优先处理：

- weak / missing primary evidence
- partial history 的 unresolved dimensions
- unresolved / rejected 后满足 retry 条件的关系
- contributor 与 maintainer、同校与同学、兼容与直接协作等容易角色膨胀的关系
- 需要刷新或确认的 current affiliation / governance role

VERIFY 的目标首先是提高证据质量；结果可以是 success、partial、unresolved 或 rejected，不要求为了“成功率”制造新节点或更强关系。

## Operator 与 action identity

Operator 是 action 的触发语义，不参与 action identity。

稳定 identity 继续保持：

`action_id = <node-id>::<relation>`

`action_key = <source-family>:<relation>:<target-family-set>`

例如 `Mooncake::maintainers` 无论是通过 `EXPAND`、`DISCOVER` 还是 `VERIFY` 被调度，仍然是同一个 research objective，因此共享 cooldown、partial follow-up 和 empirical yield 历史。不要把 operator 拼进 `action_id` 或 `action_key`。

生成 action 会附带：

```yaml
operator: expand | discover | verify
trigger:
  kind: seed | coverage_gap | frontier | bridge | weak_evidence | history_followup
```

`trigger` 解释候选为什么出现；它同样不是 action identity。

## 与 relation templates 的关系

三个 operator 是最小的一级研究方法，现有 relation templates 保留。不同 family 仍使用不同关系模板：

- Person：affiliation、project contribution、technical collaborator、academic lineage
- Company：key people、projects、academic links
- School：labs/groups、key people、projects、spinouts
- Research Institution：key people、projects、parent/partner org
- Project：maintainers、originating org、related projects
- Community：core people、projects、member orgs
- Team：key people、parent org、projects

因此不会把“学校缺项目”和“人物缺项目贡献”误认为同一种 gap。

## 与 bucket 的关系

现有 bucket 暂时保留作为调度标签，而不是一级研究方法：

- `exploitation`
- `exploration`
- `bridge`
- `verification`

例如 `operator: discover + bucket: bridge` 表示该任务来自全图发现，同时有较高桥接价值；`operator: expand + bucket: exploitation` 表示从 seed 向一个证据较强的邻域继续扩张。

## 两层 planner

当前 daily planner 继续分成两个确定性阶段：

1. `scripts/generate-research-queue.py` 生成 graph-only candidate actions，并给出 operator / trigger。
2. `scripts/plan-research.py` 读取 durable action history，应用 cooldown / partial follow-up / empirical yield，再重新做 heterogeneous portfolio selection。

日常与 Agent 自动化应调用：

```bash
python3 scripts/plan-research.py --budget 10 --limit 60
```

默认 global 模式以 `DISCOVER + VERIFY` 为主；提供 `--seed` 时会加入 `EXPAND`。可以用一个或多个 `--operator` 限定本轮研究方法。

## Action history

Durable history 位于：

`research/action-history.json`

每次 Agent **实际执行**一个 action 后都应追加一条记录；仅仅被 planner 选中不算执行。

status 有四种：

- `success`：主要研究目标获得足够证据，并产生可用图谱/证据增量。
- `partial`：没有完全解决原 action，但得到明确的高价值子结果。
- `unresolved`：进行了有效调查，但当前证据阈值下无法建立请求关系。
- `rejected`：候选关系被反证、明显不成立，或不应在没有实质新证据时重试。

`partial` 必须尽可能记录：

- `resolved_dimensions`
- `unresolved_dimensions`

新记录可附带可选 `operator` 字段，用于统计不同研究方法的产出；旧 history 不需要迁移。

## Cooldown

默认 exact-action cooldown：

- `success`: 1 day
- `partial`: 2 days
- `unresolved`: 7 days
- `rejected`: 30 days

cooldown 以稳定 `action_id` 为准，因此同一 relation 即使换了 operator 也不会绕过历史抑制。

## Empirical yield

planner 会按稳定 `action_key` 汇总历史。默认 reward 从可审计 delta 派生：

- new node: +2
- new edge: +1
- evidence upgraded: +0.5
- verified claim: +0.75
- resolved dimension: +0.5
- rejected claim: -0.25

历史只对 graph score 做小幅调整，并做强 small-sample shrinkage。后续历史足够多时，可进一步统计 `operator × relation` 的实际 yield，但不改变 action identity。

## 推荐工作流

### 每日全局研究

```bash
python3 scripts/audit-graph.py --root . --output generated
python3 scripts/plan-research.py --budget 10 --limit 60
```

用途：自动寻找 coverage gap、frontier、bridge，并穿插 evidence verification。

### 从人物 / 项目 / 组织定向深挖

```bash
python3 scripts/plan-research.py \
  --seed "Ion Stoica" \
  --operator expand \
  --budget 8
```

用途：替代过去按实体类型分别实现的人物 BFS、项目 BFS、学校 BFS。它们统一为 heterogeneous typed expansion。

### 图谱证据体检

```bash
python3 scripts/plan-research.py \
  --operator verify \
  --budget 10
```

用途：集中处理弱证据、partial follow-up、角色膨胀风险和待确认 current state。

### 混合运行

```bash
python3 scripts/plan-research.py \
  --seed "Mooncake" \
  --operator expand \
  --operator verify \
  --budget 10
```

用途：一边沿 seed 扩张，一边优先验证本地邻域中的弱关系。

## Agent 执行约束

对 selected action：

1. 优先官方主页、官方仓库、governance/CODEOWNERS/MAINTAINERS、论文、学校/研究机构一手资料。
2. action 只授权“调查”，不授权无证据创建节点或边。
3. 兼容、赞助、同校、同公司或简单共同出现在某列表中，不自动升级成人物直接关系。
4. 在当前 action 中发现的二级线索不要无限递归；把它留给下一次 planner。
5. 执行后必须记录 outcome，即使结果是 unresolved 或 rejected。
6. partial 必须保存其已解决与未解决子问题。
7. 修改后继续运行 graph / relation / schema audits。

## 输出

主要输出保持兼容：

- `generated/research-actions.json`：机器可读、history-aware action queue。
- `generated/research-queue.md`：人工 review 视图，展示 operator。
- `generated/research-history-summary.json`：cooldown、partial 和 action-key yield 汇总。
- `generated/research-priority.json`：旧文件名兼容层。

## Schema 影响

本次 operator 固化仍然**不要求批量修改已有 Markdown frontmatter**。

相关 non-node schema：

- `schema/research-action.yaml`
- `schema/research-action-history.yaml`

Durable execution ledger：

- `research/action-history.json`

人物、公司、学校、项目、社区等现有 node schema 不需要迁移。
