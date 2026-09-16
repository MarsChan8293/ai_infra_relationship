---
type: research-institution
name: SuDIS
organization: 浙江大学
aliases: ["SUDIS Lab", "Sustainable Data Intelligence and Data Systems", "SuDIS@ZJU"]
areas: [data-systems, efficient-ai, llm-inference, kv-cache, speculative-decoding, moe-inference]
people:
  - "university/浙江大学/Huan Li"
  - "university/浙江大学/Lidan Shou"
  - "university/浙江大学/Jue Wang"
  - "university/浙江大学/Zheng Li"
projects: ["HMI", "FloE"]
website: https://sudis-zju.github.io/
country: China
city: Hangzhou
last_verified: "2026-09"
---
# SuDIS（Zhejiang University）

## 研究组简介
SuDIS 是浙江大学的 Sustainable Data Intelligence and Data Systems research group。浙江大学李环官方主页明确将其称为“我们的课题组（SUDIS Lab）”，公开方向包括 Data-centric AI 与 Efficient AI；SuDIS 官方站点也将自己定义为浙江大学的数据智能与数据系统研究组。

## AI Infra 主线
本仓库只跟踪 SuDIS 中与推理系统直接相关的部分：
- multi-tenant model serving / resource sharing；
- MoE inference 的显存与参数搬运；
- speculative / parallel decoding；
- KV-cache compression；
- 面向 vLLM / SGLang 等 serving stack 的系统优化。

## 人物与项目
- [[university/浙江大学/Huan Li|Huan Li]]、[[university/浙江大学/Lidan Shou|Lidan Shou]]：SuDIS / 浙江大学数据系统与 Efficient AI faculty 网络。
- [[university/浙江大学/Jue Wang|Jue Wang]]：浙江大学博士校友，参与 HMI、FloE 等 inference systems 工作，后进入 Together AI。
- [[university/浙江大学/Zheng Li|Zheng Li]]：FloE 共同第一作者之一，工作直接针对 memory-constrained MoE inference。
- [[university/浙江大学/HMI|HMI]]、[[university/浙江大学/FloE|FloE]]：当前图谱中最直接的 inference-system 项目节点。

## Sources
- https://person.zju.edu.cn/lihuan
- https://sudis-zju.github.io/en/
- https://longaspire.github.io/publication/
