---
type: person
name: Haojie Wang
current_affiliations: ["Tsinghua University", "PACMAN Lab, Tsinghua University"]
schools:
  - "清华大学"
roles: [Assistant Researcher]
areas: [ai-compiler, program-analysis, high-performance-computing, llm-serving, speculative-decoding, kv-cache]
confidence: verified
last_verified: "2026-09"
relations:
  - '{"target":"company/清程极智/翟季冬 Jidong Zhai","type":["same-lab","paper-coauthor","research-collaboration"],"confidence":"high","evidence":["https://pacman.cs.tsinghua.edu.cn/~zjd/author/haojie-wang/","https://pacman.cs.tsinghua.edu.cn/~zjd/"]}'
---
# Haojie Wang

清华大学计算机系助理研究员，PACMAN 研究网络成员。博士与本科均毕业于清华，当前公开研究兴趣为 AI compiler、program analysis 与 HPC。

## AI Infra 主线
其工作从 EinNet、PowerFusion、Korch 等 tensor compiler / kernel orchestration，继续延伸到更直接的 LLM serving：
- SpecRouter：multi-level speculative decoding 的 adaptive routing。
- FastCache：multimodal LLM serving 的轻量 KV-cache compression。
- ChituDiffusion / dynamic diffusion LLM inference：继续把 compiler / runtime 方法用于新型生成 workload。

因此 Haojie Wang 是 PACMAN “编译器 → serving runtime”迁移里值得保留的中间层人物。

## Sources
- https://pacman.cs.tsinghua.edu.cn/~zjd/author/haojie-wang/
- https://pacman.cs.tsinghua.edu.cn/~zjd/
