# Research Operator Queue

由 `scripts/plan-research-v3.py` 自动生成。仓库只保留三个一级研究方法：`EXPAND`、`DISCOVER`、`VERIFY`。Operator 解释为什么查；relation 解释查什么；strategy 解释去哪查。

- Operators: DISCOVER, VERIFY
- Seed: none (global mode)
- Candidate actions: 1720
- Selected actions: 10
- History records: 721

## Selected portfolio

| Rank | Operator | Trigger | Source | Type | Relation | Target | Bucket | Priority | History | Why |
| ---: | --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- |
| 1 | VERIFY | history_followup | [[community/Ascend/CANN/CANN|CANN]] | project | maintainers | person | exploitation | 9.429 | partial | coverage 0/4；source type Project；infra: serving/inference, kernel, distributed；opens underrepresented target types |
| 2 | DISCOVER | coverage_gap | [[community/NVIDIA/CUTLASS/CUTLASS|CUTLASS]] | project | maintainers | person | exploration | 9.259 | new | coverage 0/4；source type Project；infra: serving/inference, scheduler, kernel；opens underrepresented target types |
| 3 | DISCOVER | coverage_gap | [[community/BerriAI/LiteLLM/LiteLLM|LiteLLM]] | project | maintainers | person | exploration | 9.258 | new | coverage 0/4；source type Project；infra: serving/inference, kv-cache, kernel；opens underrepresented target types |
| 4 | DISCOVER | coverage_gap | [[community/volcano-sh/Volcano/Volcano|Volcano]] | project | maintainers | person | exploration | 9.258 | new | coverage 0/4；source type Project；infra: serving/inference, kv-cache, scheduler；opens underrepresented target types |
| 5 | DISCOVER | coverage_gap | [[university/Massachusetts Institute of Technology/HAN Lab|HAN Lab]] | research | key_people | person | exploration | 8.135 | new | coverage 0/4；source type Research Institution；infra: serving/inference, kv-cache, scheduler；opens underrepresented target types |
| 6 | DISCOVER | coverage_gap | [[university/University of Washington/SyFI Lab|SyFI Lab]] | research | key_people | person | exploration | 8.115 | new | coverage 0/4；source type Research Institution；infra: serving/inference, scheduler, kernel；opens underrepresented target types |
| 7 | DISCOVER | bridge | [[university/Carnegie Mellon University/Catalyst Group|Catalyst Group]] | research | projects | project, community | bridge | 8.042 | new | coverage 0/3；source type Research Institution；infra: serving/inference, kernel, quantization；opens underrepresented target types |
| 8 | VERIFY | weak_evidence | [[university/清华大学/Weimin Zheng|Weimin Zheng]] | person | project_contribution | project, community | verification | 6.520 | success | coverage 1/3；source type Person；infra: serving/inference, kv-cache, distributed；bridge 9.2 |
| 9 | VERIFY | weak_evidence | [[university/北京邮电大学/北京邮电大学|北京邮电大学]] | school | projects | project, community | verification | 5.477 | new | coverage 0/2；source type School；infra: kv-cache；opens underrepresented target types |
| 10 | VERIFY | weak_evidence | [[university/电子科技大学/电子科技大学|电子科技大学]] | school | projects | project, community | verification | 5.368 | new | coverage 0/2；source type School；infra: kv-cache；opens underrepresented target types |

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
