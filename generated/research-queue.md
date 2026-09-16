# Ecosystem Research Action Queue

由 `scripts/generate-research-queue.py` 自动生成。排序对象是**下一步调查动作**，不是人物、公司、学校或项目的重要性排名。

算法：**Typed Action Planner + heterogeneous portfolio selection**。每个动作由 `source entity × relation × target type × source strategy` 构成；优先级综合关系覆盖缺口、AI Infra 相关性、桥梁价值、目标类型新颖性、证据质量、frontier potential、uncertainty、research cost、redundancy/hub penalty 与可选 seed 距离。

- Daily budget: 10
- Seed: none (global ecosystem mode)
- Candidate actions: 1058
- Selected actions: 10

## Selected actions

| Rank | Source | Type | Research action | Target | Bucket | Priority | Why |
| ---: | --- | --- | --- | --- | --- | ---: | --- |
| 1 | [[community/Ascend/msModelSlim/msModelSlim|msModelSlim]] | project | maintainers | person | bridge | 9.418 | coverage 0/4；source type Project；infra: serving/inference, moe, quantization |
| 2 | [[community/Ascend/MindIE-LLM/MindIE-LLM|MindIE-LLM]] | project | maintainers | person | bridge | 9.397 | coverage 0/4；source type Project；infra: serving/inference, kv-cache, scheduler |
| 3 | [[community/Ascend/MindIE-SD/MindIE-SD|MindIE-SD]] | project | maintainers | person | bridge | 9.378 | coverage 0/4；source type Project；infra: serving/inference, kernel, distributed |
| 4 | [[community/Ascend/MindIE-Motor/MindIE-Motor|MindIE-Motor]] | project | maintainers | person | bridge | 9.337 | coverage 0/4；source type Project；infra: serving/inference, kv-cache, scheduler |
| 5 | [[company/清程极智/清程极智|清程极智]] | company | projects | project, community, team | bridge | 8.137 | coverage 0/3；source type Company；infra: serving/inference, scheduler, kernel |
| 6 | [[company/RadixArk/朱邦华 Banghua Zhu|朱邦华]] | person | project_contribution | project, community | bridge | 7.807 | coverage 0/3；source type Person；infra: serving/inference, kernel, distributed |
| 7 | [[company/腾讯/腾讯|腾讯]] | company | projects | project, community, team | exploration | 7.806 | coverage 0/3；source type Company；infra: serving/inference, kv-cache, distributed |
| 8 | [[company/清程极智/唐适之 Shizhi Tang|唐适之]] | person | project_contribution | project, community | bridge | 7.771 | coverage 0/3；source type Person；infra: serving/inference, kernel, distributed |
| 9 | [[university/上海交通大学/Rong Chen|Rong Chen]] | person | project_contribution | project, community | exploitation | 7.755 | coverage 0/3；source type Person；infra: serving/inference, kv-cache, distributed |
| 10 | [[university/上海交通大学/上海交通大学|上海交通大学]] | school | labs_or_groups | research, team | bridge | 7.720 | coverage 0/2；source type School；infra: serving/inference, kv-cache, distributed |

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
| 1 | [[community/deepseek-ai/DeepSeek-Infra/3FS|3FS]] | project | maintainers | 8.929 |
| 2 | [[company/月之暗面/MoonEP|MoonEP]] | project | maintainers | 8.758 |
| 3 | [[community/flagos-ai/sglang-plugin-FL/sglang-plugin-FL|sglang-plugin-FL]] | project | maintainers | 8.645 |
| 4 | [[community/vllm-project/Jenga/Jenga|Jenga]] | project | originating_org | 8.491 |
| 5 | [[community/flagos-ai/FlagTree/FlagTree|FlagTree]] | project | maintainers | 8.329 |
| 6 | [[university/清华大学/FastDecode|FastDecode]] | project | originating_org | 8.037 |
| 7 | [[community/cloud-native/Kubernetes/Kubernetes|Kubernetes]] | project | originating_org | 7.933 |
| 8 | [[community/vllm-project/vLLM-Ascend/管文宇 Guan Wenyu|管文宇]] | person | affiliation | 7.713 |
| 9 | [[university/浙江大学/Jue Wang|Jue Wang]] | person | project_contribution | 7.679 |
| 10 | [[university/浙江大学/Zheng Li|Zheng Li]] | person | project_contribution | 7.679 |
| 11 | [[company/清程极智/马子轩 Zixuan Ma|马子轩]] | person | project_contribution | 7.674 |
| 12 | [[community/vllm-project/vLLM-Ascend/weijinqian0|weijinqian0]] | person | affiliation | 7.657 |
| 13 | [[university/上海交通大学/Xingda Wei|Xingda Wei]] | person | project_contribution | 7.653 |
| 14 | [[community/Ascend/ops-transformer/wangchao661|wangchao661]] | person | affiliation | 7.631 |
| 15 | [[community/Ascend/ops-transformer/Konstantin Berestizshevsky|Konstantin Berestizshevsky]] | person | affiliation | 7.608 |
| 16 | [[university/浙江大学/浙江大学|浙江大学]] | school | labs_or_groups | 7.605 |
| 17 | [[community/flashinfer-ai/FlashInfer/Brian K. Ryu|Brian K. Ryu]] | person | affiliation | 7.586 |
| 18 | [[community/flashinfer-ai/FlashInfer/aleozlx|aleozlx]] | person | affiliation | 7.586 |
| 19 | [[community/vllm-project/vLLM-Ascend/yiz-liu|yiz-liu]] | person | affiliation | 7.581 |
| 20 | [[community/vllm-project/vLLM-Ascend/zzzzwwjj|zzzzwwjj]] | person | affiliation | 7.547 |
| 21 | [[community/Ascend/ops-transformer/tangkaidi|tangkaidi]] | person | affiliation | 7.540 |
| 22 | [[university/University of Chicago/University of Chicago|University of Chicago]] | school | labs_or_groups | 7.506 |
| 23 | [[company/华为/华为|华为]] | company | key_people | 7.486 |
| 24 | [[community/flagos-ai/FlagPerf/FlagPerf|FlagPerf]] | project | maintainers | 7.455 |
| 25 | [[community/flagos-ai/FlagRelease/FlagRelease|FlagRelease]] | project | maintainers | 7.435 |
| 26 | [[community/flagos-ai/FlagOS/赵英利 Yingli Zhao|赵英利]] | person | affiliation | 7.412 |
| 27 | [[community/flagos-ai/vllm-plugin-FL/vllm-plugin-FL|vllm-plugin-FL]] | project | maintainers | 7.407 |
| 28 | [[company/清昴智能/清昴智能|清昴智能]] | company | projects | 7.341 |
| 29 | [[university/UC Berkeley/MoE-Lightning|MoE-Lightning]] | project | originating_org | 7.250 |
| 30 | [[company/xAI/xAI|xAI]] | company | projects | 7.250 |
