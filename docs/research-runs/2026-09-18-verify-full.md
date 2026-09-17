# Full VERIFY Research Run — 2026-09-18

This run executes the VERIFY operator against the full currently eligible portfolio rather than the mixed daily budget.

- Baseline VERIFY actions: **177**
- Evidence-only actions: **145**
- Relationship/semantic actions: **32**
- Durable outcomes: success=6, partial=157, unresolved=14, rejected=0

## Evidence-only policy

For `verify_evidence` actions, this run checked source availability across the full set. Reachability is deliberately recorded as `partial`, not `success`, because a live URL does not by itself prove that every semantic claim on the node is correct. Nodes with no URLs or no reachable sampled source are recorded `unresolved`.

## Semantic outcomes

| Action | Status | Resolved | Unresolved |
|---|---|---|---|
| `company/xAI/xAI::projects` | unresolved | — | xai_led_inference_project |
| `university/清华大学/Weimin Zheng::project_contribution` | success | Mooncake paper contribution | — |
| `community/vllm-project/vLLM-Ascend/weijinqian0::affiliation` | partial | Huawei organizational association via public corporate email; vLLM-Ascend maintainer identity | current_employment_status |
| `company/Fireworks AI/Fireworks AI::key_people` | partial | Lin Qiao: CEO/co-founder | additional_key_people_canonicalization |
| `university/北京邮电大学/北京邮电大学::labs_or_groups` | partial | 网络与交换技术全国重点实验室 | second_high_value_ai_infra_group |
| `company/道客/道客::projects` | success | HAMi contributor/company ecosystem relation | — |
| `university/上海交通大学/上海交通大学::labs_or_groups` | partial | IPADS | NNE_Lab_canonicalization |
| `university/电子科技大学/电子科技大学::labs_or_groups` | partial | Intelligent Computing Systems Laboratory | second_high_value_ai_infra_group |
| `university/西北工业大学/西北工业大学::labs_or_groups` | partial | 边云智能创新实验室 | second_high_value_ai_infra_group |
| `company/商汤科技/商汤科技::projects` | partial | LightLLM employee-contributor network | company_governance_or_ownership |
| `university/南京大学/南京大学::labs_or_groups` | partial | 大模型研究协同创新中心 | second_high_value_ai_infra_group |
| `university/Stony Brook University/Stony Brook University::labs_or_groups` | partial | AI Innovation Institute | second_high_value_ai_infra_group |
| `university/Binghamton University/Binghamton University::labs_or_groups` | unresolved | — | ai_infra_specific_lab |
| `university/Case Western Reserve University/Case Western Reserve University::labs_or_groups` | partial | reSAID Lab candidate | ai_infra_fit; canonicalization |
| `university/Franklin W. Olin College of Engineering/Franklin W. Olin College of Engineering::labs_or_groups` | unresolved | — | ai_infra_specific_lab |
| `university/Lobachevsky State University of Nizhny Novgorod/Lobachevsky State University of Nizhny Novgorod::labs_or_groups` | unresolved | — | ai_infra_specific_lab |
| `university/Massachusetts Institute of Technology/Massachusetts Institute of Technology::labs_or_groups` | partial | HAN Lab | second_high_value_ai_infra_group |
| `university/Nanyang Technological University/Nanyang Technological University::labs_or_groups` | partial | GLINT Lab candidate; Network Systems Lab candidate | ai_infra_fit; canonicalization |
| `university/Seoul National University/Seoul National University::labs_or_groups` | partial | Machine Learning Systems Lab | second_high_value_ai_infra_group |
| `university/Technion - Israel Institute of Technology/Technion - Israel Institute of Technology::labs_or_groups` | unresolved | — | ai_infra_specific_lab |
| `university/UC Davis/UC Davis::labs_or_groups` | partial | GATE Lab | second_high_value_ai_infra_group |
| `university/University of British Columbia/University of British Columbia::labs_or_groups` | partial | Systems and Architectures (STAR) Lab | second_high_value_ai_infra_group |
| `university/华中科技大学/华中科技大学::labs_or_groups` | partial | 智能信息与大数据实验室 candidate | ai_infra_fit; canonicalization |
| `university/江南大学/江南大学::labs_or_groups` | unresolved | — | research_group_not_teaching_lab |
| `university/Georgia Institute of Technology/Georgia Institute of Technology::labs_or_groups` | partial | Systems for Artificial Intelligence Lab | second_high_value_ai_infra_group |
| `university/University of Washington/University of Washington::labs_or_groups` | partial | SyFI Lab | second_high_value_ai_infra_group |
| `university/厦门大学/厦门大学::labs_or_groups` | partial | 谷雨大模型实验室 candidate; 空间感知与计算实验室 candidate | ai_infra_fit; canonicalization |
| `company/RadixArk/RadixArk::projects` | success | SGLang; Miles | — |
| `company/趋境科技/Weiyu Xie::project_contribution` | success | KTransformers maintainer; KTransformers SOSP author | — |
| `university/清华大学/Yongwei Wu::project_contribution` | success | Mooncake; KTransformers | — |
| `company/Meta/Meta::projects` | success | vLLM contributor network | — |
| `company/HPE/HPE::projects` | partial | NIXL employee-contributor network | company_governance_or_ownership |

## Evidence boundary

- Adoption/compatibility is not project ownership.
- Employee participation in an open-source project is recorded as a contributor-network edge unless company governance is directly documented.
- Corporate email proves an organizational association, not necessarily current employment.
- A university-wide AI initiative or teaching lab is not automatically canonicalized as an AI-infrastructure research group.
- Unresolved dimensions remain visible for future VERIFY passes.
