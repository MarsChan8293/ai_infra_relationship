---
type: person
name: Lidan Shou
aliases: [Lidan Shou]
current_affiliations: ["浙江大学"]
schools:
  - "浙江大学"
roles: [Professor, PhD Advisor]
areas: [llm-inference, moe-inference, speculative-decoding, data-systems]
last_verified: "2026-09"
relations:
  - '{"target":"university/浙江大学/Huan Li","type":["research-collaboration","mentor-network"],"confidence":"medium","evidence":["https://person.zju.edu.cn/en/should","https://proceedings.mlr.press/v267/zhou25j.html","https://aclanthology.org/2026.acl-long.1983/"]}'
  - '{"target":"university/浙江大学/Zheng Li","type":["paper-coauthor","mentor-network"],"confidence":"high","evidence":["https://person.zju.edu.cn/en/should","https://proceedings.mlr.press/v267/zhou25j.html","https://aclanthology.org/2026.acl-long.1983/"]}'
---
# Lidan Shou

浙江大学计算机科学与技术学院教授、博士生导师，是浙大数据库 / 数据智能研究网络的重要 faculty 节点。近年来其论文网络已经明显进入 **LLM inference systems**，覆盖 multi-tenant serving、MoE inference 与 speculative decoding。

## LLM inference 主线
- **HMI**：与 [[Huan Li]]、[[Jue Wang]] 等合作，研究多租户 pretrained model inference，通过层级知识管理、parameter swapping、prefetch 与计算流水线优化提升资源利用率。
- **FloE**（ICML 2025）：与 Yuxin Zhou、[[Zheng Li]] 等合作，面向显存受限 GPU 的 MoE 推理，重点解决 activated experts 的参数搬运与 PCIe / memory bottleneck。
- **TokenTiming**（ACL 2026）：参与通用 speculative decoding 研究，通过动态 token alignment 支持 vocabulary 不一致的 draft / target model pair。

## 人物关系
- [[Huan Li]]：长期合作伙伴；公开学术资料显示 Lidan Shou 是其博士导师之一。
- [[Jue Wang]]：博士生 / 校友关系，之后进入 [[Together AI]]；双方继续在 HMI、FloE 等 inference research 网络中重叠。
- [[Zheng Li]]：浙江大学学生，导师为 Lidan Shou，FloE 共同作者。

## 图谱意义
Lidan Shou 这一节点把浙江大学传统数据库研究与当代大模型 serving 问题接了起来。其团队近年的 inference 工作高度集中于 **memory hierarchy、resource sharing、data movement、speculative decoding**，这些问题与 vLLM / SGLang / GPU serving runtime 的核心瓶颈直接同构。


## 学校关联
- [[university/浙江大学/浙江大学|浙江大学]]：已存在可核验的教育、任职或访问研究关联；具体阶段以正文与 Sources 为准。

## Sources
- https://person.zju.edu.cn/en/should
- https://proceedings.mlr.press/v267/zhou25j.html
- https://aclanthology.org/2026.acl-long.1983/
- https://arxiv.org/abs/2504.17449
