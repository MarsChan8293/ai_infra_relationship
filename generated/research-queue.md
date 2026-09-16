# Ecosystem Research Action Queue

由 `scripts/generate-research-queue.py` 自动生成。排序对象是**下一步调查动作**，不是人物、公司、学校或项目的重要性排名。

算法：**Typed Action Planner + heterogeneous portfolio selection**。每个动作由 `source entity × relation × target type × source strategy` 构成；优先级综合关系覆盖缺口、AI Infra 相关性、桥梁价值、目标类型新颖性、证据质量、frontier potential、uncertainty、research cost、redundancy/hub penalty 与可选 seed 距离。

- Daily budget: 10
- Seed: none (global ecosystem mode)
- Candidate actions: 1062
- Selected actions: 10

## Selected actions

| Rank | Source | Type | Research action | Target | Bucket | Priority | Why |
| ---: | --- | --- | --- | --- | --- | ---: | --- |
| 1 | [[community/Ascend/msModelSlim/msModelSlim|msModelSlim]] | project | maintainers | person | bridge | 9.418 | coverage 0/4；source type Project；infra: serving/inference, moe, quantization |
| 2 | [[community/Ascend/MindIE-LLM/MindIE-LLM|MindIE-LLM]] | project | maintainers | person | bridge | 9.397 | coverage 0/4；source type Project；infra: serving/inference, kv-cache, scheduler |
| 3 | [[community/Ascend/MindIE-SD/MindIE-SD|MindIE-SD]] | project | maintainers | person | bridge | 9.378 | coverage 0/4；source type Project；infra: serving/inference, kernel, distributed |
| 4 | [[community/Ascend/MindIE-Motor/MindIE-Motor|MindIE-Motor]] | project | maintainers | person | bridge | 9.337 | coverage 0/4；source type Project；infra: serving/inference, kv-cache, scheduler |
| 5 | [[community/vllm-project/vLLM-Ascend/管文宇 Guan Wenyu|管文宇]] | person | affiliation | company, school, research, team | exploration | 7.713 | coverage 0/2；source type Person；infra: serving/inference, distributed, moe |
| 6 | [[university/浙江大学/Jue Wang|Jue Wang]] | person | project_contribution | project, community | exploitation | 7.679 | coverage 0/3；source type Person；infra: serving/inference, distributed, moe |
| 7 | [[university/浙江大学/Zheng Li|Zheng Li]] | person | project_contribution | project, community | exploitation | 7.679 | coverage 0/3；source type Person；infra: serving/inference, distributed, moe |
| 8 | [[community/vllm-project/vLLM-Ascend/weijinqian0|weijinqian0]] | person | affiliation | company, school, research, team | exploitation | 7.657 | coverage 0/2；source type Person；infra: serving/inference, kernel, distributed |
| 9 | [[university/浙江大学/浙江大学|浙江大学]] | school | labs_or_groups | research, team | bridge | 7.605 | coverage 0/2；source type School；infra: serving/inference, kv-cache, kernel |
| 10 | [[university/University of Chicago/University of Chicago|University of Chicago]] | school | labs_or_groups | research, team | bridge | 7.506 | coverage 0/2；source type School；infra: serving/inference, kv-cache, distributed |

## Agent execution contract

对每个 selected action：

1. 优先查官方主页、官方仓库、governance/CODEOWNERS/MAINTAINERS、论文或机构一手资料。
2. 只新增可核验节点/边；兼容、点赞、关注、同校或同公司本身不得自动升级为人物直接关系。
3. 新发现但超出本 action 的线索不要无限递归，留给下一轮 planner。
4. 修改 Markdown 后重新运行 graph audit、typed relation audit 和 schema generation。
5. 记录 rejected/unresolved 线索，避免后续 agent 反复消费同一弱证据。

## Next frontier

| Rank | Source | Type | Action | Priority |
| ---: | --- | --- | --- | ---: |
| 1 | [[community/QingCheng-AI/ascend-kernel/ascend-kernel|ascend-kernel]] | project | maintainers | 9.202 |
| 2 | [[community/Tencent/HPC-Ops/HPC-Ops|HPC-Ops]] | project | maintainers | 9.182 |
| 3 | [[community/deepseek-ai/DeepSeek-Infra/3FS|3FS]] | project | maintainers | 8.929 |
| 4 | [[company/月之暗面/MoonEP|MoonEP]] | project | maintainers | 8.758 |
| 5 | [[community/flagos-ai/sglang-plugin-FL/sglang-plugin-FL|sglang-plugin-FL]] | project | maintainers | 8.645 |
| 6 | [[community/vllm-project/Jenga/Jenga|Jenga]] | project | originating_org | 8.491 |
| 7 | [[community/flagos-ai/FlagTree/FlagTree|FlagTree]] | project | maintainers | 8.329 |
| 8 | [[university/清华大学/FastDecode|FastDecode]] | project | originating_org | 8.037 |
| 9 | [[community/cloud-native/Kubernetes/Kubernetes|Kubernetes]] | project | originating_org | 7.933 |
| 10 | [[community/Ascend/ops-transformer/wangchao661|wangchao661]] | person | affiliation | 7.631 |
| 11 | [[community/Ascend/ops-transformer/Konstantin Berestizshevsky|Konstantin Berestizshevsky]] | person | affiliation | 7.608 |
| 12 | [[community/flashinfer-ai/FlashInfer/Brian K. Ryu|Brian K. Ryu]] | person | affiliation | 7.586 |
| 13 | [[community/flashinfer-ai/FlashInfer/aleozlx|aleozlx]] | person | affiliation | 7.586 |
| 14 | [[community/vllm-project/vLLM-Ascend/yiz-liu|yiz-liu]] | person | affiliation | 7.581 |
| 15 | [[community/vllm-project/vLLM-Ascend/zzzzwwjj|zzzzwwjj]] | person | affiliation | 7.547 |
| 16 | [[community/Ascend/ops-transformer/tangkaidi|tangkaidi]] | person | affiliation | 7.540 |
| 17 | [[company/华为/华为|华为]] | company | key_people | 7.486 |
| 18 | [[community/flagos-ai/FlagPerf/FlagPerf|FlagPerf]] | project | maintainers | 7.455 |
| 19 | [[community/flagos-ai/FlagRelease/FlagRelease|FlagRelease]] | project | maintainers | 7.435 |
| 20 | [[community/flagos-ai/FlagOS/赵英利 Yingli Zhao|赵英利]] | person | affiliation | 7.412 |
| 21 | [[community/flagos-ai/vllm-plugin-FL/vllm-plugin-FL|vllm-plugin-FL]] | project | maintainers | 7.407 |
| 22 | [[company/清昴智能/清昴智能|清昴智能]] | company | projects | 7.341 |
| 23 | [[university/UC Berkeley/MoE-Lightning|MoE-Lightning]] | project | originating_org | 7.250 |
| 24 | [[company/xAI/xAI|xAI]] | company | projects | 7.250 |
| 25 | [[company/趋境科技/艾智远 Zhiyuan Ai|艾智远]] | person | project_contribution | 7.248 |
| 26 | [[company/清昴智能/关超宇 Chaoyu Guan|关超宇]] | person | project_contribution | 7.231 |
| 27 | [[community/deepseek-ai/DeepSeek-Infra/Kuai Yu|Kuai Yu]] | person | affiliation | 7.203 |
| 28 | [[community/deepseek-ai/DeepSeek-Infra/Liang Zhao|Liang Zhao]] | person | affiliation | 7.203 |
| 29 | [[community/deepseek-ai/DeepSeek-Infra/Zhean Xu|Zhean Xu]] | person | affiliation | 7.203 |
| 30 | [[university/浙江大学/Lidan Shou|Lidan Shou]] | person | project_contribution | 7.173 |
