---
type: person
name: Zheng Li
aliases: [李政, Zheng Li]
current_affiliations: ["浙江大学"]
areas: [llm-inference, moe-inference, memory-optimization]
last_verified: "2026-09"
relations:
  - '{"target":"university/浙江大学/Lidan Shou","type":["paper-coauthor","mentor-network"],"confidence":"high","evidence":["https://zju-stu-lizheng.github.io/","https://github.com/zju-stu-lizheng","https://proceedings.mlr.press/v267/zhou25j.html"]}'
  - '{"target":"university/浙江大学/Huan Li","type":["research-collaboration"],"confidence":"medium","evidence":["https://zju-stu-lizheng.github.io/","https://github.com/zju-stu-lizheng","https://proceedings.mlr.press/v267/zhou25j.html"]}'
  - '{"target":"university/浙江大学/Jue Wang","type":["paper-coauthor"],"confidence":"high","evidence":["https://zju-stu-lizheng.github.io/","https://github.com/zju-stu-lizheng","https://proceedings.mlr.press/v267/zhou25j.html"]}'
---
# 李政（Zheng Li）

浙江大学计算机科学与技术专业本科、硕士，公开个人主页显示自 2022 年起在 [[Lidan Shou]] 指导下开展研究，关注 database / AI，并明确持续学习和研究 LLM inference。

## FloE
[[Lidan Shou]] 团队 **FloE: On-the-Fly MoE Inference on Memory-constrained GPU** 的共同第一作者之一，论文发表于 ICML 2025。

FloE 聚焦显存受限 GPU 上的 MoE inference：通过压缩 activated expert 内部参数、稀疏预测及计算 / 数据搬运协同，降低 PCIe 带宽和显存压力。论文报告在 Mixtral-8x7B 上可显著降低 expert 参数与显存占用，并在单张 RTX 3090 上相对 DeepSpeed-MII 获得明显 wall-clock inference speedup。

## 人物关系
- [[Lidan Shou]]：硕士导师 / 长期研究指导关系，FloE 共同作者。
- [[Huan Li]]：同属浙江大学数据库、数据智能与 Efficient AI 研究网络。
- [[Jue Wang]]：FloE 共同作者；后者为浙大博士校友并进入 [[Together AI]]。

## 图谱意义
Zheng Li 是浙江大学节点里偏“年轻 systems researcher”的代表之一：其工作从数据库 / AI 研究直接切入 **MoE inference 的 memory / communication bottleneck**，非常贴近本仓库关注的推理优化方向。

## Sources
- https://zju-stu-lizheng.github.io/
- https://github.com/zju-stu-lizheng
- https://proceedings.mlr.press/v267/zhou25j.html
