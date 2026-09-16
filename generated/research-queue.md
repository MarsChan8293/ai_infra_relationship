# Ecosystem Research Action Queue

由 `scripts/plan-research.py` 自动生成。排序对象是**下一步调查动作**，不是人物、公司、学校或项目的重要性排名。

算法：**Typed Action Planner + Action History + Cooldown + Heterogeneous Portfolio Selection**。基础 expected-gain 分数来自图谱缺口；历史只做轻量 yield 修正，并用 cooldown 阻止同一弱证据 action 在短期内反复占用预算。

- Daily budget: 10
- Seed: none (global ecosystem mode)
- Candidate actions: 1070
- Eligible actions: 1052
- Cooldown-suppressed: 18
- History records: 20
- Selected actions: 10

## Selected actions

| Rank | Source | Type | Research action | Target | Bucket | Priority | History | Why |
| ---: | --- | --- | --- | --- | --- | ---: | --- | --- |
| 1 | [[community/flagos-ai/sglang-plugin-FL/sglang-plugin-FL|sglang-plugin-FL]] | project | maintainers | person | exploitation | 8.514 | new | coverage 0/4；source type Project；infra: serving/inference, kernel, distributed；opens underrepresented target types |
| 2 | [[community/vllm-project/Jenga/Jenga|Jenga]] | project | originating_org | company, school, research, community, team | bridge | 8.491 | new | coverage 0/1；source type Project；infra: serving/inference, kv-cache, scheduler；opens underrepresented target types |
| 3 | [[community/flagos-ai/FlagTree/FlagTree|FlagTree]] | project | maintainers | person | bridge | 8.198 | new | coverage 0/4；source type Project；infra: serving/inference, kernel；opens underrepresented target types |
| 4 | [[university/清华大学/FastDecode|FastDecode]] | project | originating_org | company, school, research, community, team | exploration | 8.037 | new | coverage 0/1；source type Project；infra: serving/inference, kv-cache, distributed；opens underrepresented target types |
| 5 | [[company/面壁智能/面壁智能|面壁智能]] | company | projects | project, community, team | exploration | 7.997 | new | coverage 0/3；source type Company；infra: serving/inference, quantization, ascend；opens underrepresented target types |
| 6 | [[community/Ascend/ops-transformer/wangchao661|wangchao661]] | person | affiliation | company, school, research, team | exploration | 7.710 | new | coverage 0/2；source type Person；infra: serving/inference, kernel, quantization；opens underrepresented target types |
| 7 | [[community/Ascend/ops-transformer/Konstantin Berestizshevsky|Konstantin Berestizshevsky]] | person | affiliation | company, school, research, team | exploration | 7.687 | new | coverage 0/2；source type Person；infra: serving/inference, kv-cache, kernel；opens underrepresented target types |
| 8 | [[community/flashinfer-ai/FlashInfer/Brian K. Ryu|Brian K. Ryu]] | person | affiliation | company, school, research, team | exploitation | 7.665 | new | coverage 0/2；source type Person；infra: serving/inference, kernel, distributed；opens underrepresented target types |
| 9 | [[community/flashinfer-ai/FlashInfer/aleozlx|aleozlx]] | person | affiliation | company, school, research, team | exploitation | 7.665 | new | coverage 0/2；source type Person；infra: kernel, distributed, moe；opens underrepresented target types |
| 10 | [[company/华为/华为|华为]] | company | key_people | person | bridge | 7.486 | new | coverage 0/4；source type Company；infra: serving/inference, kernel, distributed；opens underrepresented target types |

## Agent execution contract

对每个 selected action：

1. 优先查官方主页、官方仓库、governance/CODEOWNERS/MAINTAINERS、论文或机构一手资料。
2. 只新增可核验节点/边；兼容、点赞、关注、同校或同公司本身不得自动升级为人物直接关系。
3. 新发现但超出本 action 的线索不要无限递归，留给下一轮 planner。
4. 执行后用 `scripts/record-research-action.py` 写入 success / partial / unresolved / rejected outcome。
5. partial 必须记录 resolved_dimensions 与 unresolved_dimensions，不能被压扁成 success/failure。
6. 修改 Markdown 后重新运行 graph audit、typed relation audit 和 schema generation。

## Next eligible frontier

| Rank | Source | Type | Action | Priority |
| ---: | --- | --- | --- | ---: |
| 1 | [[community/cloud-native/Kubernetes/Kubernetes|Kubernetes]] | project | originating_org | 7.933 |
| 2 | [[community/vllm-project/vLLM-Ascend/yiz-liu|yiz-liu]] | person | affiliation | 7.660 |
| 3 | [[community/vllm-project/vLLM-Ascend/zzzzwwjj|zzzzwwjj]] | person | affiliation | 7.626 |
| 4 | [[community/Ascend/ops-transformer/tangkaidi|tangkaidi]] | person | affiliation | 7.619 |
| 5 | [[company/趋境科技/艾智远 Zhiyuan Ai|艾智远]] | person | project_contribution | 7.531 |
| 6 | [[company/清昴智能/关超宇 Chaoyu Guan|关超宇]] | person | project_contribution | 7.514 |
| 7 | [[community/flagos-ai/FlagOS/赵英利 Yingli Zhao|赵英利]] | person | affiliation | 7.491 |
| 8 | [[company/清昴智能/清昴智能|清昴智能]] | company | projects | 7.456 |
| 9 | [[university/上海交通大学/Shengzhong Liu|Shengzhong Liu]] | person | project_contribution | 7.371 |
| 10 | [[company/xAI/xAI|xAI]] | company | projects | 7.365 |
| 11 | [[university/启元实验室/潘泽众 Zezhong Pan|潘泽众]] | person | project_contribution | 7.364 |
| 12 | [[community/flagos-ai/FlagPerf/FlagPerf|FlagPerf]] | project | maintainers | 7.324 |
| 13 | [[community/flagos-ai/FlagRelease/FlagRelease|FlagRelease]] | project | maintainers | 7.304 |
| 14 | [[company/清程极智/汤雄超 Xiongchao Tang|汤雄超]] | person | project_contribution | 7.299 |
| 15 | [[community/deepseek-ai/DeepSeek-Infra/Kuai Yu|Kuai Yu]] | person | affiliation | 7.282 |
| 16 | [[community/deepseek-ai/DeepSeek-Infra/Liang Zhao|Liang Zhao]] | person | affiliation | 7.282 |
| 17 | [[community/deepseek-ai/DeepSeek-Infra/Zhean Xu|Zhean Xu]] | person | affiliation | 7.282 |
| 18 | [[community/flagos-ai/vllm-plugin-FL/vllm-plugin-FL|vllm-plugin-FL]] | project | maintainers | 7.276 |
| 19 | [[company/无问芯穹/无问芯穹|无问芯穹]] | company | projects | 7.257 |
| 20 | [[university/UC Berkeley/MoE-Lightning|MoE-Lightning]] | project | originating_org | 7.250 |
| 21 | [[university/Carnegie Mellon University/Carnegie Mellon University|Carnegie Mellon University]] | school | labs_or_groups | 7.211 |
| 22 | [[company/派欧云/王闻宇 Wayne Wang|王闻宇]] | person | project_contribution | 7.201 |
| 23 | [[community/Project-HAMi/ascend-device-plugin/ascend-device-plugin|HAMi Ascend Device Plugin]] | project | originating_org | 7.134 |
| 24 | [[company/趋境科技/Hongbo Kang|Hongbo Kang]] | person | project_contribution | 7.129 |
| 25 | [[community/vllm-project/vLLM-Ascend/ningjingbengxiaohai|ningjingbengxiaohai]] | person | affiliation | 7.061 |
| 26 | [[community/kvcache-ai/KTransformers/谢威宇 Weiyu Xie|谢威宇]] | person | project_contribution | 7.057 |
| 27 | [[community/vllm-project/vLLM/Nick Hill|Nick Hill]] | person | project_contribution | 7.053 |
| 28 | [[community/vllm-project/vLLM/Michael Goin|Michael Goin]] | person | project_contribution | 7.051 |
| 29 | [[community/vllm-project/vLLM-Ascend/Wang Xiyuan|Wang Xiyuan]] | person | affiliation | 7.047 |
| 30 | [[community/thu-pacman/Chitu/Chitu|Chitu]] | project | maintainers | 7.013 |

## Cooldown / history-suppressed

| Source | Action | Latest outcome | Eligible after | Base |
| --- | --- | --- | --- | ---: |
| [[community/Ascend/msModelSlim/msModelSlim|msModelSlim]] | maintainers | unresolved | 2026-09-23 | 9.418 |
| [[community/Ascend/MindIE-LLM/MindIE-LLM|MindIE-LLM]] | maintainers | unresolved | 2026-09-23 | 9.397 |
| [[community/Ascend/MindIE-SD/MindIE-SD|MindIE-SD]] | maintainers | unresolved | 2026-09-23 | 9.378 |
| [[community/Ascend/MindIE-Motor/MindIE-Motor|MindIE-Motor]] | maintainers | unresolved | 2026-09-23 | 9.337 |
| [[community/QingCheng-AI/ascend-kernel/ascend-kernel|ascend-kernel]] | maintainers | unresolved | 2026-09-23 | 9.202 |
| [[community/Tencent/HPC-Ops/HPC-Ops|HPC-Ops]] | maintainers | unresolved | 2026-09-23 | 9.182 |
| [[community/deepseek-ai/DeepSeek-Infra/3FS|3FS]] | maintainers | unresolved | 2026-09-23 | 8.929 |
| [[company/月之暗面/MoonEP|MoonEP]] | maintainers | unresolved | 2026-09-23 | 8.758 |
| [[community/vllm-project/vLLM-Ascend/weijinqian0|Jinqian Wei]] | affiliation | partial | 2026-09-18 | 7.657 |
| [[company/腾讯/腾讯|腾讯]] | projects | success | 2026-09-17 | 6.771 |
| [[university/浙江大学/Zheng Li|Zheng Li]] | project_contribution | success | 2026-09-17 | 6.408 |
| [[university/上海交通大学/Rong Chen|Rong Chen]] | project_contribution | success | 2026-09-17 | 6.204 |
| [[community/vllm-project/vLLM-Ascend/管文宇 Guan Wenyu|管文宇]] | affiliation | success | 2026-09-17 | 6.146 |
| [[university/上海交通大学/上海交通大学|上海交通大学]] | labs_or_groups | partial | 2026-09-18 | 5.833 |
| [[university/浙江大学/浙江大学|浙江大学]] | labs_or_groups | success | 2026-09-17 | 5.729 |
| [[university/University of Chicago/University of Chicago|University of Chicago]] | labs_or_groups | success | 2026-09-17 | 5.656 |
| [[company/RadixArk/朱邦华 Banghua Zhu|朱邦华]] | project_contribution | success | 2026-09-17 | 5.486 |
| [[company/清程极智/唐适之 Shizhi Tang|唐适之]] | project_contribution | success | 2026-09-17 | 5.448 |
