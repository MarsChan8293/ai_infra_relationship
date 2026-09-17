# Ecosystem Research Action Queue

由 `scripts/plan-research.py` 自动生成。排序对象是**下一步调查动作**，不是人物、公司、学校或项目的重要性排名。

算法：**Typed Action Planner + Action History + Cooldown + Heterogeneous Portfolio Selection**。基础 expected-gain 分数来自图谱缺口；历史只做轻量 yield 修正，并用 cooldown 阻止同一弱证据 action 在短期内反复占用预算。

- Daily budget: 10
- Seed: none (global ecosystem mode)
- Candidate actions: 1414
- Eligible actions: 1403
- Cooldown-suppressed: 11
- History records: 30
- Selected actions: 10

## Selected actions

| Rank | Source | Type | Research action | Target | Bucket | Priority | History | Why |
| ---: | --- | --- | --- | --- | --- | ---: | --- | --- |
| 1 | [[community/siliconflow/OneDiff/OneDiff|OneDiff]] | project | maintainers | person | exploration | 9.257 | new | coverage 0/4；source type Project；infra: serving/inference, kernel, distributed；opens underrepresented target types |
| 2 | [[community/Ascend/CANN/CANN|CANN]] | project | maintainers | person | exploitation | 9.105 | new | coverage 0/4；source type Project；infra: serving/inference, kernel, distributed；opens underrepresented target types |
| 3 | [[company/月之暗面/checkpoint-engine|Checkpoint Engine]] | project | maintainers | person | bridge | 9.016 | new | coverage 0/4；source type Project；infra: serving/inference, kv-cache, distributed；opens underrepresented target types |
| 4 | [[community/openEuler/openYuanRong/YuanRong TransferEngine|YuanRong TransferEngine]] | project | maintainers | person | exploitation | 8.966 | new | coverage 0/4；source type Project；infra: serving/inference, distributed, ascend；opens underrepresented target types |
| 5 | [[company/Intel/Intel|Intel]] | company | projects | project, community, team | exploration | 8.266 | new | coverage 0/3；source type Company；infra: serving/inference, kv-cache, kernel；opens underrepresented target types |
| 6 | [[company/趋境科技/艾智远 Zhiyuan Ai|艾智远]] | person | project_contribution | project, community | bridge | 8.137 | new | coverage 0/3；source type Person；infra: serving/inference, kv-cache, moe；opens underrepresented target types |
| 7 | [[university/清华大学/Kang Chen|陈康]] | person | project_contribution | project, community | bridge | 8.131 | new | coverage 0/3；source type Person；infra: serving/inference, kv-cache, distributed；opens underrepresented target types |
| 8 | [[community/Ascend/Ascend/Ascend|Ascend]] | community | core_people | person | exploration | 8.015 | new | coverage 0/4；source type Community；infra: serving/inference, kernel, distributed；opens underrepresented target types |
| 9 | [[community/Ascend/MemCache/Pz1116|Pz1116]] | person | affiliation | company, school, research, team | exploration | 7.964 | new | coverage 0/2；source type Person；infra: serving/inference, kv-cache, distributed；opens underrepresented target types |
| 10 | [[community/kvcache-ai/Mooncake/Aionw|Aoi]] | person | affiliation | company, school, research, team | exploitation | 7.951 | new | coverage 0/2；source type Person；infra: serving/inference, kv-cache, distributed；opens underrepresented target types |

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
| 1 | [[community/lightseekorg/TorchSpec/TorchSpec|TorchSpec]] | project | maintainers | 8.907 |
| 2 | [[community/vllm-project/Speculators/Speculators|Speculators]] | project | maintainers | 8.865 |
| 3 | [[community/vllm-project/Jenga/Jenga|Jenga]] | project | originating_org | 8.591 |
| 4 | [[community/FlashML-org/FreeToken/FreeToken|FreeToken]] | project | originating_org | 8.379 |
| 5 | [[community/MooreThreads/torch_musa/torch_musa|torch_musa]] | project | maintainers | 8.354 |
| 6 | [[community/MooreThreads/MATE/MATE|MATE]] | project | maintainers | 8.345 |
| 7 | [[community/Deep-Spark/lmcache-iluvatar/lmcache-iluvatar|lmcache-iluvatar]] | project | maintainers | 8.319 |
| 8 | [[community/MetaX-MACA/mcoplib/mcoplib|mcoplib]] | project | maintainers | 8.313 |
| 9 | [[community/sgl-project/mini-SGLang/mini-SGLang|mini-SGLang]] | project | originating_org | 8.218 |
| 10 | [[university/清华大学/FastDecode|FastDecode]] | project | originating_org | 8.137 |
| 11 | [[community/kvcache-ai/Mooncake/TENT|TENT]] | project | originating_org | 8.125 |
| 12 | [[company/面壁智能/ForgeTrain|ForgeTrain]] | project | maintainers | 8.078 |
| 13 | [[company/面壁智能/MiniCPM|MiniCPM]] | project | maintainers | 8.078 |
| 14 | [[community/cloud-native/Kubernetes/Kubernetes|Kubernetes]] | project | originating_org | 8.033 |
| 15 | [[community/Ascend/TransferQueue/TransferQueue|TransferQueue]] | project | originating_org | 8.010 |
| 16 | [[community/MetaX-MACA/MXDeepEP/MXDeepEP|MXDeepEP]] | project | maintainers | 7.981 |
| 17 | [[community/Ascend/MemCache/tyy0829|tyy0829]] | person | affiliation | 7.951 |
| 18 | [[community/LMCache/LMCache/Roy Huang|Roy Huang]] | person | affiliation | 7.930 |
| 19 | [[community/vllm-project/Speculators/Speculators|Speculators]] | project | originating_org | 7.916 |
| 20 | [[community/vllm-project/vLLM-Ascend/yiz-liu|yiz-liu]] | person | affiliation | 7.875 |
| 21 | [[company/派欧云/李星星|李星星]] | person | project_contribution | 7.867 |
| 22 | [[community/Ascend/MemCache/shilinlee|shilinlee]] | person | affiliation | 7.850 |
| 23 | [[community/vllm-project/vLLM-Ascend/zzzzwwjj|zzzzwwjj]] | person | affiliation | 7.841 |
| 24 | [[university/IBM Research/IBM Research|IBM Research]] | research | key_people | 7.835 |
| 25 | [[community/Ascend/ops-transformer/tangkaidi|tangkaidi]] | person | affiliation | 7.834 |
| 26 | [[community/Ascend/MemCache/nbbb24|nbbb24]] | person | affiliation | 7.760 |
| 27 | [[community/flagos-ai/FlagOS/赵英利 Yingli Zhao|赵英利]] | person | affiliation | 7.706 |
| 28 | [[community/Deep-Spark/iluvatar-corex-ixrt/iluvatar-corex-ixrt|iluvatar-corex-ixrt]] | project | maintainers | 7.679 |
| 29 | [[university/清华大学/Weichao Guo|Weichao Guo]] | person | project_contribution | 7.536 |
| 30 | [[company/清昴智能/关超宇 Chaoyu Guan|关超宇]] | person | project_contribution | 7.514 |

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
| [[community/Ascend/MindIE-SD/MindIE-SD|MindIE-SD]] | maintainers | unresolved | 2026-09-23 | 7.208 |
| [[community/Ascend/MindIE-Motor/MindIE-Motor|MindIE-Motor]] | maintainers | unresolved | 2026-09-23 | 7.166 |
| [[community/vllm-project/vLLM-Ascend/weijinqian0|Jinqian Wei]] | affiliation | partial | 2026-09-18 | 6.102 |
| [[university/上海交通大学/上海交通大学|上海交通大学]] | labs_or_groups | partial | 2026-09-18 | 5.825 |
