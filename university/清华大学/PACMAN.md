---
type: research-institution
name: PACMAN
organization: 清华大学
aliases: ["PACMAN Lab", "PACMAN Group", "Parallel Architecture & Compiler technology of Mobile, Accelerated, and Networked systems Group"]
linked_people:
  - "company/清程极智/翟季冬 Jidong Zhai"
  - "university/清华大学/Wenguang Chen"
  - "company/字节跳动/何家傲 Jiaao He"
  - "company/字节跳动/郑立言 Liyan Zheng"
  - "company/深度求索/黄可钊 Kezhao Huang"
  - "community/vllm-project/vLLM/Chen Zhang"
  - "company/清程极智/马子轩 Zixuan Ma"
  - "company/清程极智/唐适之 Shizhi Tang"
  - "company/清程极智/师天麾 Tianhui Shi"
  - "university/清华大学/Qihao Zhang"
  - "university/清华大学/Mingshu Zhai"
  - "university/清华大学/Haojie Wang"
  - "university/清华大学/Zan Zong"
areas: [high-performance-computing, ai-compiler, distributed-training, llm-serving, quantization, kv-cache, heterogeneous-computing]
projects: [FastMoE, BaGuaLu, GLM-130B, FastDecode, Jenga, Chitu, QFactory, Lethe]
website: https://pacman.cs.tsinghua.edu.cn/
last_verified: "2026-09"
---
# PACMAN

PACMAN 是清华大学计算机系高性能计算研究所的系统研究团队，名称来自 **Parallel Architecture & Compiler technology of Mobile, Accelerated, and Networked systems**。当前公开 faculty 核心为 [[company/清程极智/翟季冬 Jidong Zhai|翟季冬]] 与 [[university/清华大学/Wenguang Chen|陈文光]]。

## 技术演化
对 AI Infra 图谱最重要的不是传统 HPC 本身，而是 PACMAN 已形成一条连续技术链：

`parallel / compiler / performance → distributed MoE training → 100B-scale pretraining → heterogeneous LLM serving → quantization / KV cache / scheduling`

### 大模型训练阶段
- [[community/thu-pacman/FastMoE/FastMoE|FastMoE]] / FasterMoE / SmartMoE：从 MoE expert placement、all-to-all communication、load balancing 等问题切入大模型系统。
- [[community/thu-pacman/BaGuaLu/BaGuaLu|BaGuaLu]]：面向超大规模预训练与国产超算。
- [[university/清华大学/GLM-130B|GLM-130B]]：KEG 主导模型，PACMAN 负责关键系统协作。官方 GLM-130B 资料明确记录 PACMAN 帮助处理 3D pipeline、显存、硬件故障和异构平台训练问题。

### 推理 / serving 阶段
- [[university/清华大学/FastDecode|FastDecode]]：CPU/GPU heterogeneous pipeline，针对 KV cache 与 attention 的 memory-bound 路径。
- [[community/vllm-project/Jenga/Jenga|Jenga]]：SOSP 2025，跨 PACMAN 与 Berkeley / vLLM 人才网络的异构显存管理系统。
- [[community/thu-pacman/QFactory/QFactory|QFactory]]：USENIX ATC 2025，面向量化 LLM serving 的 Qtile Graph 编译 / kernel 路线。
- [[community/thu-pacman/Lethe/Lethe|Lethe]]：AAAI 2026，面向 reasoning-intensive serving 的 layer/time adaptive KV cache pruning。
- UltraAttn：SC 2025，hierarchical context-tiling 的 attention parallelization。
- FlowPrefill、SpecRouter、FastCache：2026 前后的 prefill scheduling、multi-level speculative decoding 与 multimodal KV-cache compression 研究，显示 PACMAN 已从训练系统持续推进到 serving 热路径。

## 人才扩散
PACMAN 官方 alumni 页面提供了非常清晰的 2024–2025 迁移：
- [[company/字节跳动/郑立言 Liyan Zheng|郑立言]]、[[company/字节跳动/何家傲 Jiaao He|何家傲]]：2025 PhD → ByteDance。
- [[company/深度求索/黄可钊 Kezhao Huang|黄可钊]]：2025 PhD → DeepSeek。
- [[community/vllm-project/vLLM/Chen Zhang|Chen Zhang]]：2025 PhD → Berkeley Postdoc，并通过 Jenga 接入 vLLM / Berkeley systems 网络。
- [[company/清程极智/唐适之 Shizhi Tang|唐适之]]、[[company/清程极智/师天麾 Tianhui Shi|师天麾]]：2024 PhD → QingCheng.AI，把 PACMAN 系统技术带入赤兔 / 八卦炉产业化。

因此 PACMAN 是当前仓库里一个非常典型的“学术 systems → 大厂 infra / startup / 开源 serving”人才路由器。

## 与 KEG 的交叉
[[university/清华大学/KEG|KEG]] 与 PACMAN 不应因同属清华而合并。两者最强交叉发生在具体项目：FastMoE、BaGuaLu、GLM-130B。KEG 提供模型 / 预训练目标，PACMAN 提供并行、编译、通信与系统优化能力。

## Sources
- https://pacman.cs.tsinghua.edu.cn/
- https://pacman.cs.tsinghua.edu.cn/~zjd/
- https://pacman.cs.tsinghua.edu.cn/~zjd/people/
- https://pacman.cs.tsinghua.edu.cn/~zjd/category/mlsys/
- https://keg.cs.tsinghua.edu.cn/glm-130b/zh/posts/glm-130b/
