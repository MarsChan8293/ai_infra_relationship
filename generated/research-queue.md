# Research Operator Queue

由 `scripts/plan-research-v3.py` 自动生成。仓库只保留三个一级研究方法：`EXPAND`、`DISCOVER`、`VERIFY`。Operator 解释为什么查；relation 解释查什么；strategy 解释去哪查。

- Operators: DISCOVER, VERIFY
- Seed: none (global mode)
- Candidate actions: 1579
- Selected actions: 10
- History records: 719

## Selected portfolio

| Rank | Operator | Trigger | Source | Type | Relation | Target | Bucket | Priority | History | Why |
| ---: | --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- |
| 1 | DISCOVER | coverage_gap | [[community/deepseek-ai/DeepSeek-Infra/profile-data|profile-data]] | project | maintainers | person | exploration | 8.929 | new | coverage 0/4；source type Project；infra: serving/inference, distributed, moe；opens underrepresented target types |
| 2 | DISCOVER | coverage_gap | [[community/vllm-project/Speculators/Speculators|Speculators]] | project | originating_org | company, school, research, community, team | exploration | 8.008 | new | coverage 0/1；source type Project；infra: serving/inference, kv-cache, distributed；opens underrepresented target types |
| 3 | DISCOVER | coverage_gap | [[community/deepseek-ai/DeepSeek-Infra/deepseek-recipe|deepseek-recipe]] | project | maintainers | person | exploration | 7.882 | new | coverage 0/4；source type Project；infra: serving/inference；opens underrepresented target types |
| 4 | DISCOVER | coverage_gap | [[university/Massachusetts Institute of Technology/HAN Lab|HAN Lab]] | research | key_people | person | exploration | 7.840 | new | coverage 0/4；source type Research Institution；infra: serving/inference, kv-cache, quantization；opens underrepresented target types |
| 5 | DISCOVER | coverage_gap | [[university/University of British Columbia/Systems and Architectures STAR Lab|Systems and Architectures (STAR) Lab]] | research | key_people | person | exploration | 7.358 | new | coverage 0/4；source type Research Institution；infra: serving/inference, kv-cache；opens underrepresented target types |
| 6 | DISCOVER | coverage_gap | [[university/University of Washington/SyFI Lab|SyFI Lab]] | research | key_people | person | exploration | 7.267 | new | coverage 0/4；source type Research Institution；infra: serving/inference, distributed；opens underrepresented target types |
| 7 | VERIFY | weak_evidence | [[university/北京邮电大学/北京邮电大学|北京邮电大学]] | school | projects | project, community | verification | 5.477 | new | coverage 0/2；source type School；infra: kv-cache；opens underrepresented target types |
| 8 | VERIFY | weak_evidence | [[university/电子科技大学/电子科技大学|电子科技大学]] | school | projects | project, community | verification | 5.368 | new | coverage 0/2；source type School；infra: kv-cache；opens underrepresented target types |
| 9 | VERIFY | weak_evidence | [[university/西北工业大学/西北工业大学|西北工业大学]] | school | projects | project, community | verification | 5.368 | new | coverage 0/2；source type School；infra: kv-cache；opens underrepresented target types |
| 10 | VERIFY | weak_evidence | [[university/清华大学/Weimin Zheng|Weimin Zheng]] | person | verify_evidence | evidence | verification | 5.265 | new | source coverage 0/2；evidence quality below target |

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
