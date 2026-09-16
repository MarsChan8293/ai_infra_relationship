# Ecosystem Research Action Queue

由 `scripts/plan-research.py` 自动生成。排序对象是**下一步调查动作**，不是人物、公司、学校或项目的重要性排名。

算法：**Typed Action Planner + Action History + Cooldown + Heterogeneous Portfolio Selection**。基础 expected-gain 分数来自图谱缺口；历史只做轻量 yield 修正，并用 cooldown 阻止同一弱证据 action 在短期内反复占用预算。

- Daily budget: 10
- Seed: none (global ecosystem mode)
- Candidate actions: 1297
- Eligible actions: 1271
- Cooldown-suppressed: 26
- History records: 30
- Selected actions: 10

## Selected actions

| Rank | Source | Type | Research action | Target | Bucket | Priority | History | Why |
| ---: | --- | --- | --- | --- | --- | ---: | --- | --- |
| 1 | [[company/月之暗面/checkpoint-engine|Checkpoint Engine]] | project | maintainers | person | bridge | 9.016 | new | coverage 0/4；source type Project；infra: serving/inference, kv-cache, distributed；opens underrepresented target types |
| 2 | [[community/openEuler/openYuanRong/YuanRong TransferEngine|YuanRong TransferEngine]] | project | maintainers | person | exploitation | 8.966 | new | coverage 0/4；source type Project；infra: serving/inference, distributed, ascend；opens underrepresented target types |
| 3 | [[community/lightseekorg/TorchSpec/TorchSpec|TorchSpec]] | project | maintainers | person | exploitation | 8.907 | new | coverage 0/4；source type Project；infra: serving/inference, kv-cache, distributed；opens underrepresented target types |
| 4 | [[community/vllm-project/Speculators/Speculators|Speculators]] | project | maintainers | person | exploration | 8.865 | new | coverage 0/4；source type Project；infra: serving/inference, kv-cache, distributed；opens underrepresented target types |
| 5 | [[company/Intel/Intel|Intel]] | company | projects | project, community, team | exploration | 8.266 | new | coverage 0/3；source type Company；infra: serving/inference, kv-cache, kernel；opens underrepresented target types |
| 6 | [[community/Ascend/MemCache/Pz1116|Pz1116]] | person | affiliation | company, school, research, team | exploration | 7.964 | new | coverage 0/2；source type Person；infra: serving/inference, kv-cache, distributed；opens underrepresented target types |
| 7 | [[community/kvcache-ai/Mooncake/Aionw|Aoi]] | person | affiliation | company, school, research, team | exploitation | 7.951 | new | coverage 0/2；source type Person；infra: serving/inference, kv-cache, distributed；opens underrepresented target types |
| 8 | [[community/Ascend/MemCache/tyy0829|tyy0829]] | person | affiliation | company, school, research, team | exploitation | 7.951 | new | coverage 0/2；source type Person；infra: serving/inference, kv-cache, distributed；opens underrepresented target types |
| 9 | [[community/LMCache/LMCache/Roy Huang|Roy Huang]] | person | affiliation | company, school, research, team | exploration | 7.930 | new | coverage 0/2；source type Person；infra: serving/inference, kv-cache, kernel；opens underrepresented target types |
| 10 | [[university/IBM Research/IBM Research|IBM Research]] | research | key_people | person | exploration | 7.835 | new | coverage 0/4；source type Research Institution；infra: serving/inference, kv-cache, distributed；opens underrepresented target types |

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
| 1 | [[community/FlashML-org/FreeToken/FreeToken|FreeToken]] | project | originating_org | 8.379 |
| 2 | [[community/sgl-project/mini-SGLang/mini-SGLang|mini-SGLang]] | project | originating_org | 8.218 |
| 3 | [[community/kvcache-ai/Mooncake/TENT|TENT]] | project | originating_org | 8.125 |
| 4 | [[company/面壁智能/ForgeTrain|ForgeTrain]] | project | maintainers | 8.078 |
| 5 | [[company/面壁智能/MiniCPM|MiniCPM]] | project | maintainers | 8.078 |
| 6 | [[community/cloud-native/Kubernetes/Kubernetes|Kubernetes]] | project | originating_org | 8.033 |
| 7 | [[community/Ascend/TransferQueue/TransferQueue|TransferQueue]] | project | originating_org | 8.010 |
| 8 | [[community/vllm-project/Speculators/Speculators|Speculators]] | project | originating_org | 7.916 |
| 9 | [[community/vllm-project/vLLM-Ascend/yiz-liu|yiz-liu]] | person | affiliation | 7.875 |
| 10 | [[community/Ascend/MemCache/shilinlee|shilinlee]] | person | affiliation | 7.850 |
| 11 | [[community/vllm-project/vLLM-Ascend/zzzzwwjj|zzzzwwjj]] | person | affiliation | 7.841 |
| 12 | [[community/Ascend/ops-transformer/tangkaidi|tangkaidi]] | person | affiliation | 7.834 |
| 13 | [[community/Ascend/MemCache/nbbb24|nbbb24]] | person | affiliation | 7.760 |
| 14 | [[community/flagos-ai/FlagOS/赵英利 Yingli Zhao|赵英利]] | person | affiliation | 7.706 |
| 15 | [[company/清昴智能/关超宇 Chaoyu Guan|关超宇]] | person | project_contribution | 7.514 |
| 16 | [[company/清昴智能/清昴智能|清昴智能]] | company | projects | 7.514 |
| 17 | [[community/deepseek-ai/DeepSeek-Infra/Kuai Yu|Kuai Yu]] | person | affiliation | 7.497 |
| 18 | [[community/deepseek-ai/DeepSeek-Infra/Liang Zhao|Liang Zhao]] | person | affiliation | 7.497 |
| 19 | [[community/deepseek-ai/DeepSeek-Infra/Zhean Xu|Zhean Xu]] | person | affiliation | 7.497 |
| 20 | [[company/xAI/xAI|xAI]] | company | projects | 7.423 |
| 21 | [[company/Samsung/Samsung|Samsung]] | company | projects | 7.414 |
| 22 | [[community/flagos-ai/FlagPerf/FlagPerf|FlagPerf]] | project | maintainers | 7.407 |
| 23 | [[community/flagos-ai/FlagRelease/FlagRelease|FlagRelease]] | project | maintainers | 7.387 |
| 24 | [[university/上海交通大学/Shengzhong Liu|Shengzhong Liu]] | person | project_contribution | 7.371 |
| 25 | [[university/启元实验室/潘泽众 Zezhong Pan|潘泽众]] | person | project_contribution | 7.364 |
| 26 | [[community/flagos-ai/vllm-plugin-FL/vllm-plugin-FL|vllm-plugin-FL]] | project | maintainers | 7.359 |
| 27 | [[university/UC Berkeley/MoE-Lightning|MoE-Lightning]] | project | originating_org | 7.350 |
| 28 | [[community/LMCache/LMCache/deng451e|deng451e]] | person | affiliation | 7.323 |
| 29 | [[community/LMCache/LMCache/Zhengfei He|Zhengfei He]] | person | affiliation | 7.318 |
| 30 | [[company/无问芯穹/无问芯穹|无问芯穹]] | company | projects | 7.315 |

## Cooldown / history-suppressed

| Source | Action | Latest outcome | Eligible after | Base |
| --- | --- | --- | --- | ---: |
| [[community/Ascend/msModelSlim/msModelSlim|msModelSlim]] | maintainers | unresolved | 2026-09-23 | 9.418 |
| [[community/Ascend/MindIE-LLM/MindIE-LLM|MindIE-LLM]] | maintainers | unresolved | 2026-09-23 | 9.397 |
| [[community/QingCheng-AI/ascend-kernel/ascend-kernel|ascend-kernel]] | maintainers | unresolved | 2026-09-23 | 9.202 |
| [[community/Tencent/HPC-Ops/HPC-Ops|HPC-Ops]] | maintainers | unresolved | 2026-09-23 | 9.182 |
| [[community/deepseek-ai/DeepSeek-Infra/3FS|3FS]] | maintainers | unresolved | 2026-09-23 | 8.929 |
| [[company/月之暗面/MoonEP|MoonEP]] | maintainers | unresolved | 2026-09-23 | 8.758 |
| [[community/flagos-ai/sglang-plugin-FL/sglang-plugin-FL|sglang-plugin-FL]] | maintainers | unresolved | 2026-09-23 | 8.645 |
| [[community/vllm-project/Jenga/Jenga|Jenga]] | originating_org | success | 2026-09-17 | 8.491 |
| [[university/清华大学/FastDecode|FastDecode]] | originating_org | success | 2026-09-17 | 8.037 |
| [[community/Ascend/MindIE-SD/MindIE-SD|MindIE-SD]] | maintainers | unresolved | 2026-09-23 | 7.208 |
| [[community/Ascend/MindIE-Motor/MindIE-Motor|MindIE-Motor]] | maintainers | unresolved | 2026-09-23 | 7.166 |
| [[university/浙江大学/Zheng Li|Zheng Li]] | project_contribution | success | 2026-09-17 | 6.408 |
| [[university/上海交通大学/Rong Chen|Rong Chen]] | project_contribution | success | 2026-09-17 | 6.204 |
| [[community/vllm-project/vLLM-Ascend/管文宇 Guan Wenyu|管文宇]] | affiliation | success | 2026-09-17 | 6.146 |
| [[community/vllm-project/vLLM-Ascend/weijinqian0|Jinqian Wei]] | affiliation | partial | 2026-09-18 | 6.102 |
| [[community/Ascend/ops-transformer/wangchao661|wangchao661]] | affiliation | success | 2026-09-17 | 6.099 |
| [[community/Ascend/ops-transformer/Konstantin Berestizshevsky|Konstantin Berestizshevsky]] | affiliation | success | 2026-09-17 | 6.085 |
| [[community/flashinfer-ai/FlashInfer/aleozlx|Alex Yang]] | affiliation | success | 2026-09-17 | 6.071 |
| [[community/flashinfer-ai/FlashInfer/Brian K. Ryu|Brian K. Ryu]] | affiliation | success | 2026-09-17 | 6.071 |
| [[company/面壁智能/面壁智能|面壁智能]] | projects | success | 2026-09-17 | 5.804 |
| [[company/腾讯/腾讯|腾讯]] | projects | success | 2026-09-17 | 5.803 |
| [[university/上海交通大学/上海交通大学|上海交通大学]] | labs_or_groups | partial | 2026-09-18 | 5.825 |
| [[university/浙江大学/浙江大学|浙江大学]] | labs_or_groups | success | 2026-09-17 | 5.763 |
| [[university/University of Chicago/University of Chicago|University of Chicago]] | labs_or_groups | success | 2026-09-17 | 5.656 |
| [[company/RadixArk/朱邦华 Banghua Zhu|朱邦华]] | project_contribution | success | 2026-09-17 | 5.486 |
| [[company/清程极智/唐适之 Shizhi Tang|唐适之]] | project_contribution | success | 2026-09-17 | 5.448 |
