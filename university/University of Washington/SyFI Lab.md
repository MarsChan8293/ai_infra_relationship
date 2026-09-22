---
type: research-institution
name: "SyFI Lab"
aliases: ["Systems for Future Intelligence Lab"]
organization: "University of Washington"
linked_people: []
areas: [ai-infrastructure, llm-serving, distributed-training, gpu-systems, multimodal-serving, agentic-systems]
website: https://syfi.cs.washington.edu/
country: "USA"
city: "Seattle, WA"
last_verified: "2026-09"
---
# SyFI Lab

University of Washington SyFI Lab（Systems for Future Intelligence）研究面向未来 AI 的高效、灵活和可靠基础设施。其公开研究已经形成很清晰的 inference / serving 主线，而不是泛化的机器学习研究集合。

## AI Infra 主线

- **NanoFlow**：OSDI 2025 LLM serving system，以 intra-device parallelism 和异步 CPU scheduling 提升吞吐。
- **FlashInfer-Bench**：面向 AI-driven LLM systems 的 inference-kernel / systems benchmark。
- **M\***：模块化 multimodal model serving system。
- **VoxServe**：面向 SpeechLM 的 streaming-centric serving。
- **VibeServe**：使用 AI agents 端到端生成面向具体模型、硬件和 workload 的 serving runtime。
- 研究还覆盖 coding-agent serving workload、训练系统和 inference reliability。

这些工作使 SyFI 成为仓库里连接“传统 serving runtime → multimodal / agent workload → AI 自动生成系统”的重要研究种子。

## 边界

论文共同作者或同属 UW 不自动等于 SyFI 正式成员；人物节点需在后续 EXPAND 中分别核验实验室主页、个人主页或明确项目 affiliation。

## 关键人物

- [[university/University of Washington/SyFI Lab/Baris Kasikci|Baris Kasikci]]：SyFI Director；Associate Professor。
- [[university/University of Washington/SyFI Lab/Stephanie Wang|Stephanie Wang]]：SyFI Director；Assistant Professor。
- [[university/University of Washington/SyFI Lab/Kan Zhu|Kan Zhu]]：PhD student；2026 TraceLab 第一作者，直接连接 coding-agent workload 与 LLM serving。
- [[university/University of Washington/SyFI Lab/Mat Jacob|Mat Jacob]]：PhD student；参与 TraceLab 与 Piper，连接 LLM serving workload 与 distributed training。

人物身份来自 SyFI 官方 People 页面；项目参与来自 SyFI 官方 2026 publication 列表。

## Sources
- https://syfi.cs.washington.edu/
- https://syfi.cs.washington.edu/publications/
- https://syfi.cs.washington.edu/publications/nanoflow/
- https://syfi.cs.washington.edu/blog/2026-05-12-introducing-vibeserve/
