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

## 为什么不是继续优化 BFS

BFS 适合已知完整图上的邻域遍历，但本仓库面对的是开放世界研究：只有执行一次搜索后，才知道会不会发现新节点、新边或更强证据。因此 `distance` 只作为可选 seed 模式下的软先验，不再是硬截止条件。

planner 当前采用可解释、确定性的 heuristic expected-gain proxy：

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

推荐每日先由 Python planner 生成有限 research actions，再由 ChatGPT/Codex 执行，而不是让 Agent 自由决定全局 BFS。

```bash
python3 scripts/audit-graph.py --root . --output generated
python3 scripts/generate-research-queue.py \
  --root . \
  --generated generated \
  --budget 10 \
  --limit 60
```

主要输出：

- `generated/research-actions.json`：机器可读 action queue，daily agent 的主要输入。
- `generated/research-queue.md`：人工 review 视图。
- `generated/research-priority.json`：旧文件名兼容层，已不再表示 person ranking。

`--seed` 支持任意已知实体类型。例如：

```bash
python3 scripts/generate-research-queue.py \
  --seed "Mooncake" \
  --budget 8
```

seed 模式仍计算图距离，但 `--max-bfs-depth` 只是 soft radius，不会禁止高价值的远端生态发现。

## Portfolio selection

默认一次最多选择 10 个 action，并限制同一 source 每轮只执行一个 action。planner 还使用 source-family 软上限，避免人物数量较多时 daily queue 被 person 节点垄断。如果候选不足，会自动放松类型上限补满预算。

动作会被标成：

- `exploitation`：补已有高价值生态的明显缺口
- `exploration`：打开连接较少但可能扩展新区域的节点
- `bridge`：优先补跨生态连接
- `verification`：优先加强或否定弱证据

## Agent 执行约束

Agent 对 selected action 应遵循：

1. 优先官方主页、官方仓库、governance/CODEOWNERS/MAINTAINERS、论文、学校/研究机构一手资料。
2. action 只授权“调查”，不授权无证据创建节点或边。
3. 兼容、赞助、同校、同公司或简单共同出现在某列表中，不自动升级成人物直接关系。
4. 在当前 action 中发现的二级线索不要无限递归；把它留给下一次 planner。
5. 修改后继续运行现有 graph / relation / schema audits。

## Schema 影响

这次重构不要求批量修改已有 Markdown frontmatter。现有 person/company/school/project/community 等 schema 继续作为 source of truth。

新增的 `schema/research-action.yaml` 是 **non-node schema**，只约束生成的 planner record。因此不需要为现有几百个节点做迁移，也不会要求给每个 Markdown 添加 planner 专用字段。

后续如果开始记录 action 的真实执行结果，可基于稳定的 `action_key` 增加 history，再学习不同 `source family × relation × target family × strategy` 的实际收益；这可以在不修改现有实体 schema 的前提下演进。
