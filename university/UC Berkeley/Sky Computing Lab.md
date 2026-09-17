---
type: research-institution
name: Sky Computing Lab
organization: UC Berkeley
aliases: ["SkyLab", "Berkeley Sky Computing Lab", "UC Berkeley Sky Computing Lab"]
linked_people: []
areas: [cloud-computing, distributed-systems, llm-serving, ai-systems, agent-systems, heterogeneous-computing]
projects: [Ray, vLLM, SGLang, Jenga, MoE-Lightning, FreeToken]
website: https://sky.cs.berkeley.edu/
last_verified: "2026-09"
---
# Sky Computing Lab

Sky Computing Lab 是 UC Berkeley 的 systems / cloud / AI systems 研究组织，由 [[company/Inferact/Ion Stoica|Ion Stoica]] 领导。对本图谱而言，它是 AMPLab / RISELab 之后 Berkeley systems 网络进入现代 LLM serving 与 agent infrastructure 的核心承接层。

## AI Infra 技术主线

`AMPLab / RISELab → Sky Computing Lab → Ray / vLLM / SGLang → inference / agent systems`

重点分支包括：
- [[community/vllm-project/vLLM/vLLM|vLLM]]：Berkeley inference serving 代表性项目，Woosuk Kwon、Zhuohan Li、Simon Mo 等均位于 Ion / Sky 研究网络。
- [[community/sgl-project/SGLang/SGLang|SGLang]]：由 Berkeley systems / LMSYS 网络孕育，连接 Lianmin Zheng、Shiyi Cao 等。
- [[community/vllm-project/Jenga/Jenga|Jenga]]：异构 LLM serving memory management，把 Berkeley Sky 与清华 PACMAN / vLLM 人才网络连接起来。
- [[university/UC Berkeley/MoE-Lightning|MoE-Lightning]]：memory-constrained GPU 上的 MoE heterogeneous inference。
- [[community/FlashML-org/FreeToken/FreeToken|FreeToken]]：把 inference runtime 扩展到 GPU / CPU / host DRAM / PCIe 的统一动态执行平台。
- SkyServe：跨 region / cloud、spot + on-demand 的 AI model serving。
- SkyRL / ADRS / SkyDiscover：把系统研究继续推进到 agent training 与 AI-driven systems research。

## 人才与产业扩散
Sky / Berkeley systems 网络持续向开源与公司迁移：
- Ray → [[company/Anyscale/Anyscale|Anyscale]]
- vLLM / serving → [[company/Inferact/Inferact|Inferact]]
- Spark / data systems → [[company/Databricks/Databricks|Databricks]]
- 人才进一步流向 Meta、OpenAI、ByteDance 等模型与基础设施团队。

## 关系边界
Sky Computing Lab 是研究机构节点。人物出现在 `linked_people` 只代表其公开 `current_affiliations` 可解析到 Sky，不自动推断 Ion Stoica 是其正式导师；正式 advisor/student 关系仍需人物主页或 Berkeley 学位档案证据。

## Sources
- https://sky.cs.berkeley.edu/
- https://sky.cs.berkeley.edu/people/
- https://sky.cs.berkeley.edu/publications/
- https://eecs.berkeley.edu/news/new-sky-computing-lab-aims-revolutionize-cloud-industry/
- https://www2.eecs.berkeley.edu/Faculty/Homepages/stoica.html
