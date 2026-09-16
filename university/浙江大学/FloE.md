---
type: project
name: FloE
companies: []
company_relation: research-project
layer: moe-inference
open_source: true
repository: https://github.com/zju-stu-lizheng/FloE
areas: [llm-inference, moe, memory-optimization, parameter-offload, pcie, triton]
people:
  - "university/浙江大学/Zheng Li"
  - "university/浙江大学/Jue Wang"
  - "university/浙江大学/Lidan Shou"
last_verified: "2026-09"
---
# FloE

## 项目简介
FloE（On-the-Fly MoE Inference on Memory-constrained GPU）是浙江大学研究网络中的 MoE inference 系统工作，发表于 ICML 2025，并公开了可运行代码。

FloE 针对显存受限 GPU 上的 MoE 推理，通过 expert 内部参数压缩、稀疏激活预测与计算/数据搬运协同来降低 PCIe 与显存压力。公开代码包含 Mixtral 模型修改、Triton kernel、数据传输策略和执行流水线。

## 人物与机构
- [[university/浙江大学/Zheng Li|Zheng Li]]：共同第一作者之一，公开 GitHub 仓库由其账号发布。
- [[university/浙江大学/Jue Wang|Jue Wang]]：论文作者。
- [[university/浙江大学/Lidan Shou|Lidan Shou]]：论文作者 / 浙江大学研究指导网络。
- [[university/浙江大学/SuDIS|SuDIS]]：该项目所在的浙江大学 data systems / Efficient AI 研究生态。

## Sources
- https://github.com/zju-stu-lizheng/FloE
- https://proceedings.mlr.press/v267/zhou25j.html
- https://arxiv.org/abs/2505.05950
