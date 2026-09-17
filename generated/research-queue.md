# Research Operator Queue

由 `scripts/plan-research-v3.py` 自动生成。仓库只保留三个一级研究方法：`EXPAND`、`DISCOVER`、`VERIFY`。Operator 解释为什么查；relation 解释查什么；strategy 解释去哪查。

- Operators: DISCOVER, VERIFY
- Seed: none (global mode)
- Candidate actions: 1452
- Selected actions: 10
- History records: 36

## Selected portfolio

| Rank | Operator | Trigger | Source | Type | Relation | Target | Bucket | Priority | History | Why |
| ---: | --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- |
| 1 | DISCOVER | coverage_gap | [[community/lightseekorg/TorchSpec/TorchSpec|TorchSpec]] | project | maintainers | person | exploitation | 8.975 | new | coverage 0/4；source type Project；infra: serving/inference, kv-cache, distributed；opens underrepresented target types |
| 2 | DISCOVER | coverage_gap | [[company/Intel/OpenVINO GenAI|OpenVINO GenAI]] | project | maintainers | person | exploration | 8.944 | new | coverage 0/4；source type Project；infra: serving/inference, kv-cache, scheduler；opens underrepresented target types |
| 3 | DISCOVER | coverage_gap | [[community/vllm-project/Speculators/Speculators|Speculators]] | project | maintainers | person | exploration | 8.933 | new | coverage 0/4；source type Project；infra: serving/inference, kv-cache, distributed；opens underrepresented target types |
| 4 | DISCOVER | coverage_gap | [[company/Intel/xFasterTransformer|xFasterTransformer]] | project | maintainers | person | exploration | 8.708 | new | coverage 0/4；source type Project；infra: serving/inference, distributed, quantization；opens underrepresented target types |
| 5 | DISCOVER | coverage_gap | [[university/清华大学/Haojie Wang|Haojie Wang]] | person | project_contribution | project, community | exploration | 8.279 | new | coverage 0/3；source type Person；infra: serving/inference, kv-cache, kernel；opens underrepresented target types |
| 6 | DISCOVER | bridge | [[company/趋境科技/艾智远 Zhiyuan Ai|艾智远]] | person | project_contribution | project, community | bridge | 8.196 | new | coverage 0/3；source type Person；infra: serving/inference, kv-cache, moe；opens underrepresented target types |
| 7 | VERIFY | weak_evidence | [[company/xAI/xAI|xAI]] | company | projects | project, community, team | verification | 7.482 | new | coverage 0/3；source type Company；infra: serving/inference, kernel；opens underrepresented target types |
| 8 | VERIFY | weak_evidence | [[university/清华大学/Weimin Zheng|Weimin Zheng]] | person | project_contribution | project, community | verification | 6.711 | new | coverage 1/3；source type Person；infra: serving/inference, kv-cache, distributed；bridge 9.2 |
| 9 | VERIFY | weak_evidence | [[company/Fireworks AI/Fireworks AI|Fireworks AI]] | company | key_people | person | verification | 6.509 | new | coverage 0/4；source type Company；infra: serving/inference, kernel；opens underrepresented target types |
| 10 | VERIFY | weak_evidence | [[university/北京邮电大学/北京邮电大学|北京邮电大学]] | school | labs_or_groups | research, team | verification | 6.157 | new | coverage 0/2；source type School；infra: kv-cache；opens underrepresented target types |

## DISCOVER

Global graph completion driven by coverage gaps, novelty, frontier and bridge value.

## VERIFY

Evidence strengthening, contradiction checking and durable-history follow-up.

## Agent execution contract

1. 优先官方主页、官方仓库、governance/CODEOWNERS/MAINTAINERS、论文与机构一手资料。
2. Operator 只授权调查，不授权无证据创建节点或边。
3. contributor 不自动等于 maintainer；同校不自动等于同学；兼容不自动等于人物直接合作。
4. 新发现但超出当前 action 的线索留给下一轮 planner，不无限递归。
5. 执行后用 `scripts/record-research-action.py` 记录 success / partial / unresolved / rejected。
6. `action_id` / `action_key` 永远不包含 operator，同一 objective 跨 operator 共享 cooldown/history。

完整说明：`docs/research-action-planner.md`；快速使用：`docs/research-operators.md`。
