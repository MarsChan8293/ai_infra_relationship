# Research Operator Queue

由 `scripts/plan-research-v3.py` 自动生成。仓库只保留三个一级研究方法：`EXPAND`、`DISCOVER`、`VERIFY`。Operator 解释为什么查；relation 解释查什么；strategy 解释去哪查。

- Operators: DISCOVER, VERIFY
- Seed: none (global mode)
- Candidate actions: 1881
- Selected actions: 10
- History records: 727

## Selected portfolio

| Rank | Operator | Trigger | Source | Type | Relation | Target | Bucket | Priority | History | Why |
| ---: | --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- |
| 1 | DISCOVER | bridge | [[community/kserve/KServe/KServe|KServe]] | project | maintainers | person | bridge | 9.656 | new | coverage 0/4；source type Project；infra: serving/inference, scheduler, kernel；opens underrepresented target types |
| 2 | VERIFY | history_followup | [[community/Ascend/msModelSlim/msModelSlim|msModelSlim]] | project | maintainers | person | bridge | 9.635 | unresolved | coverage 0/4；source type Project；infra: serving/inference, moe, quantization；opens underrepresented target types |
| 3 | VERIFY | history_followup | [[community/Ascend/CANN/CANN|CANN]] | project | maintainers | person | exploitation | 9.455 | partial | coverage 0/4；source type Project；infra: serving/inference, kernel, distributed；opens underrepresented target types |
| 4 | DISCOVER | bridge | [[community/NVIDIA/NCCL/NCCL|NCCL]] | project | maintainers | person | bridge | 9.362 | new | coverage 0/4；source type Project；infra: serving/inference, scheduler, distributed；opens underrepresented target types |
| 5 | VERIFY | history_followup | [[community/Ascend/Ascend/Ascend|Ascend]] | community | core_people | person | exploration | 8.315 | partial | coverage 0/4；source type Community；infra: serving/inference, kernel, distributed；opens underrepresented target types |
| 6 | VERIFY | history_followup | [[university/Massachusetts Institute of Technology/HAN Lab|HAN Lab]] | research | projects | project, community | exploitation | 8.246 | partial | coverage 0/3；source type Research Institution；infra: serving/inference, kv-cache, scheduler；opens underrepresented target types |
| 7 | VERIFY | history_followup | [[university/清华大学/Haojie Wang|Haojie Wang]] | person | project_contribution | project, community | exploration | 8.238 | partial | coverage 0/3；source type Person；infra: serving/inference, kv-cache, kernel；opens underrepresented target types |
| 8 | VERIFY | history_followup | [[university/University of Washington/SyFI Lab|SyFI Lab]] | research | projects | project, community | exploitation | 8.229 | partial | coverage 0/3；source type Research Institution；infra: serving/inference, scheduler, kernel；opens underrepresented target types |
| 9 | DISCOVER | bridge | [[university/UC San Diego/Hao AI Lab|Hao AI Lab]] | research | key_people | person | bridge | 8.076 | new | coverage 0/4；source type Research Institution；infra: serving/inference, distributed, disaggregation；opens underrepresented target types |
| 10 | DISCOVER | coverage_gap | [[community/InfiniTensor/qinyiqun|qinyiqun]] | person | affiliation | company, school, research, team | exploration | 7.828 | new | coverage 0/2；source type Person；infra: serving/inference, distributed, moe；opens underrepresented target types |

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
