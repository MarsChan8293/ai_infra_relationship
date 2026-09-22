---
type: project
name: Croqtile
layer: compiler
status: active
repository: https://github.com/LancerLab/croqtile
docs: https://lancerlab.github.io/croqtile-tutorial/documentation/
areas:
  - "kernel-dsl"
  - "gpu-kernels"
  - "ai-native-programming"
  - "symbolic-shapes"
  - "compile-time-verification"
  - "autotuning"
hardware:
  - "nvidia"
  - "amd"
  - "cpu"
companies:
  - "燧原科技"
last_verified: "2026-09"
---
# Croqtile

Croqtile 是 [[university/上海交通大学/LANCER Lab|LANCER Lab]] 开源的 AI kernel 编程语言 / compiler DSL。项目把自己定位为 **AI-native GPU kernel language**：语言语法、编译器诊断和 autotuning harness 都围绕 AI agent 编写、修复与优化 kernel 的闭环设计。

在图谱中，Croqtile 位于 **kernel DSL / compiler** 层，而不是 serving engine。它与 [[TileLang]]、[[Triton]]、CUDA/CuTe、CUTLASS 属于相邻的 kernel programming / code generation 技术层，但当前没有证据把这些“对照关系”升级为软件集成关系。

## 编译器设计

README 给出的主编译流水线为：

`Source -> SEMA -> NORM -> VALNO -> INFER -> LATENORM -> CHECK -> CODEGEN -> Target`

其中值得关注的几个点：

- **Syntax-Context Co-Design**：显式表达 tile shape、pipeline depth、warp role 等结构信息，减少 agent 需要读取和生成的 token。
- **Compiler-Harness Co-Design**：编译器返回结构化诊断，包括约束、符号推导与修复提示，让 agent 能把 compiler 作为优化控制环的一部分。
- **VALNO / symbolic shape**：针对动态 shape 传播符号边界，用于 tile decomposition、reduction、MMA 等编译期检查。
- **静态检查**：覆盖 tile shape、shared memory、DMA/TMA、MMA、async barrier、越界访问与 dynamic shape constraint 等。
- **多后端**：官方 README 列出 CUDA/CuTe、HIP 和 C++ targets；完整 GPU feature set 重点覆盖 NVIDIA Hopper 及后续架构能力。

## 面向推理优化的价值

Croqtile 的核心价值不是再造一门“更短的 CUDA”，而是把 **kernel optimization search space 变成 agent 可操作的结构化语言空间**。对于 GEMM、attention、MoE、quantization、fusion 等推理热点，它试图同时保留：

1. tile / warp / pipeline / data movement 的显式硬件控制；
2. 更小的上下文与代码修改面；
3. 编译期资源、shape 和同步约束检查；
4. autotuning / agent harness 可消费的结构化反馈。

README 的 persistent warp-specialized GEMM 示例直接包含 TMA、software pipelining 与 warp-group execution，这使它与本图谱关注的 inference kernel engineering 高度相关。

## LANCER / SJTU / 燧原科技

[[university/上海交通大学/LANCER Lab|LANCER Lab]] 的 GitHub 组织页明确将实验室描述为 [[上海交通大学]] 与 [[company/燧原科技/燧原科技|燧原科技]] 的联合实验室，研究方向是下一代高性能计算的 language / compilation optimization。

Croqtile 近期开源工程也显示出很强的产业编译器投入。2026 年 8–9 月的公开 commit 网络中，[[Xiaofeng Guan]] / Garfee Guan 与 [[Enming Fan]] 是非常活跃的 contributor，[[Heng Shi]] 也直接参与近期维护；这些人物同时通过 Postiz、PresCount、Samoyeds、SPIDER 等工作连接到 compiler optimization、structured sparsity 与 sparse tensor core 路线。

## 关键人物

- [[university/上海交通大学/Xiaofeng Guan|Xiaofeng Guan]]：Croqtile 近期核心工程贡献者；公开 ORCID 记录其长期在燧原科技从事 compiler research，并与 SJTU 保持研究关联。
- [[university/上海交通大学/Enming Fan|Enming Fan]]：Croqtile 近期高频 contributor；Postiz 作者，公开论文使用燧原科技邮箱。
- [[university/上海交通大学/Heng Shi|Heng Shi]]：Croqtile contributor；同时参与 Postiz、Samoyeds、SPIDER，连接 compiler 与 sparse tensor core / MoE kernel 研究。
- [[university/上海交通大学/Jianguo Yao|Jianguo Yao]]：SJTU 教授，与上述人物在 Postiz、Samoyeds、SPIDER 等研究中持续合作，是 LANCER 周边学术网络的重要桥点。

## 与 TileLang / Triton 的关系

Croqtile 官方仓库直接用 Triton、TileLang、CUDA/CuTe 等作为 benchmark / programming-model 对照对象，并保留 `research/tilelang/` 研究目录。这说明它和 [[TileLang]]、[[Triton]] 处于同一竞争与设计空间，但这类 evidence 只支持 **技术邻接 / comparison**，不代表 collaboration 或 integration。

这条边对人才图谱仍然很有价值：它把北大/MSRA 的 TileLang compiler 谱系，与 SJTU/燧原的 LANCER compiler 谱系放在同一个现代 AI kernel DSL 坐标系里。

## 生态工具

- **croqtile-tuner**：AI-agent-driven kernel autotuning harness。
- **croqtile-playground**：WASM/browser IDE，官方 README 指向 `SyntaxArchmage/croqtile-playground`。
- **croqtile-tutorial / website / slides**：由 LancerLab 组织维护的教程与展示材料。

## Sources

- https://github.com/LancerLab/croqtile
- https://github.com/LancerLab
- https://lancerlab.github.io/croqtile-tutorial/documentation/
- https://orcid.org/0000-0003-1120-8889
- https://tcloud.sjtu.edu.cn/pdf/CGO_2025_Postiz.pdf
- https://doi.org/10.1145/3689031.3717455
- https://conf.researchr.org/track/cgo-2025/cgo-2025-papers
