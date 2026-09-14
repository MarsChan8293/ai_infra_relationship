# Tyler Michael Smith

社区：[[vLLM]] · [[llm-d]]
当前：[[Red Hat]] Chief Architect, Inference Engineering（llm-d 官方作者资料，截至 2026-09）

## 教育经历
- [[University of Texas at Austin]]：计算机博士，研究高性能稠密线性代数、microkernels、并行与数据移动下界

## 工作经历
- [[Neural Magic]]：推理性能、编译与稀疏模型系统
- [[Red Hat]]：Neural Magic 于 2025 年初并入 Red Hat 后继续从事大规模 LLM inference；当前公开资料将其列为 Chief Architect, Inference Engineering。

## 社区贡献
- [[vLLM]]：Project Lead，负责 CUDA kernels、Fused MoE、collectives、distributed 与 disaggregated inference。
- [[llm-d]]：PD-Disaggregation SIG Lead，与 [[Robert Shaw]] 共同负责 prefill/decode separation、跨实例通信、异构资源利用与 distributed serving。

## 人物关系
- [[Robert Shaw]]：**前 Neural Magic、现 Red Hat 同事 + vLLM 共同维护者 + llm-d PD-Disaggregation SIG 共同负责人**。至少在 2025-02，两人共同被 Red Hat 官方列为 DeepSeek MLA / FP8 vLLM 优化贡献者；截至 2026-09 又共同领导 llm-d PD-Disaggregation 技术域。
- [[community/llm-d/llm-d/Maroon Ayoub|Maroon Ayoub]]：**Red Hat inference engineering 同事 + llm-d disaggregation 邻接协作**。2025 KV-cache routing 工作已有共同作者网络；2026 Maroon 转入 Red Hat 后，两人分别覆盖 KV-disaggregation / agentic serving 与 PD-disaggregation。具体直属关系未公开。
- [[Michael Goin]]：**前 Neural Magic、现 Red Hat 同事 + vLLM 性能工程搭档**。2025-02 同属 DeepSeek MLA / FP8 优化团队；两人当前分别覆盖 distributed/kernels 与 quantization/performance，多次在 vLLM 性能路径交叉。
- [[Lucas Wilkinson]]：**前 Neural Magic、现 Red Hat 同事 + GPU kernel 协作者**。2025-02 与 Tyler 同被 Red Hat credit 于 DeepSeek MLA / FP8 优化；两人在 attention、quantized GEMM、FlashInfer 等底层路径存在持续交集。
- [[Matthew Bonanni]]：**Red Hat 同事 + vLLM kernel/performance 协作者**。截至 2026-09 两人都在 Red Hat 的 vLLM / inference engineering 网络，均关注 C++/CUDA、kernel 与性能；公开来源未确认两人首次共事的精确月份。
- [[Wentao Ye]]：**Red Hat 同事 + vLLM GPU 性能协作者**。Wentao 2025 年加入 Red Hat 后与 Tyler 在 Blackwell、DeepEP / DeepGEMM、MoE / distributed performance 等方向形成交叉；截至 2026-09 仍属同一 Red Hat/vLLM 工程网络。

## Sources
- https://llm-d.ai/community/sigs
- https://llm-d.ai/blog/authors
- https://www.redhat.com/en/blog/enhancing-deepseek-models-mla-and-fp8-optimizations-vllm
- https://www.redhat.com/en/blog/bringing-nemotron-models-red-hat-ai-factory-nvidia
