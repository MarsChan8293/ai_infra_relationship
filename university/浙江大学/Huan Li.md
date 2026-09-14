---
type: person
name: Huan Li
aliases: [李环, Huan Li]
current_affiliations: ["浙江大学"]
roles: [Professor, PhD Advisor]
areas: [llm-inference, speculative-decoding, kv-cache, multi-tenant-serving, efficient-ai]
last_verified: "2026-09"
relations:
  - '{"target":"university/浙江大学/Lidan Shou","type":["mentor-network"],"confidence":"medium","evidence":["https://person.zju.edu.cn/lihuan","https://longaspire.github.io/","https://sudis-zju.github.io/zh/"]}'
  - '{"target":"university/浙江大学/Jue Wang","type":["paper-coauthor"],"confidence":"high","evidence":["https://person.zju.edu.cn/lihuan","https://longaspire.github.io/","https://sudis-zju.github.io/zh/"]}'
  - '{"target":"university/浙江大学/Zheng Li","type":["research-collaboration"],"confidence":"medium","evidence":["https://person.zju.edu.cn/lihuan","https://longaspire.github.io/","https://sudis-zju.github.io/zh/"]}'
---
# 李环（Huan Li）

浙江大学计算机科学与技术学院百人计划研究员、博士生导师。2018 年于浙江大学计算机学院获博士学位，2023 年回到浙大任职；当前研究主线已经从数据管理 / Efficient AI 明确延伸到 **大模型高效推理与部署**。

## LLM inference 方向
公开主页将大模型推理优化列为当前重点课题，直接覆盖：
- speculative decoding；
- KV Cache 压缩与管理；
- 多租户场景下的动态序列调度与异构资源优化；
- [[SGLang]]、[[vLLM]]、verl 等框架的深度定制与性能调优。

其个人主页进一步把相关工作归纳为 Efficient AI：multi-tenant reuse、speculative / parallel decoding、KV-cache compression、memory-efficient fine-tuning。

## 代表性 inference 工作
- **HMI**：与 [[Lidan Shou]]、[[Jue Wang]] 等合作的 multi-tenant inference 系统，面向大量 pretrained-model tenants 的 GPU memory / resource sharing 与流水线优化。
- **Draft & Verify**：self-speculative decoding 路线。
- **HybridKV / HARD-KV**：面向大模型 / 多模态大模型的 KV-cache compression。
- **ParallelVLM / LVSpec 等**：多模态模型 speculative / parallel decoding 与推理加速。

## 人物关系
- [[Lidan Shou]]：博士阶段导师之一，之后长期在浙江大学数据库 / 数据智能网络共事与合作。
- [[Jue Wang]]：浙大校友与论文合作者，共同参与 HMI 等 inference systems 工作。
- [[Zheng Li]]：同属浙江大学数据库 / 数据智能与 Efficient AI 研究网络；后者参与 FloE MoE inference。

## 图谱意义
李环是当前浙江大学节点里非常值得持续跟踪的 **“传统 data systems → modern LLM serving”** 连接点。研究问题已经与生产 inference engine 的瓶颈高度重叠，而不是停留在纯模型压缩层。

## Sources
- https://person.zju.edu.cn/lihuan
- https://longaspire.github.io/
- https://sudis-zju.github.io/zh/
- https://arxiv.org/abs/2504.17449
