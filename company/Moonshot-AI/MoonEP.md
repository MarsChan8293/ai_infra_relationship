---
type: infra-project
company: Moonshot AI
areas: [expert-parallelism, communication, moe]
open_source: true
---
# MoonEP

## 项目简介
MoonEP 是 Moonshot AI 的 Expert Parallel communication library，通过 dynamic redundant experts 等机制改善 MoE token load 在 ranks 之间的不均衡，服务于大规模 MoE 模型的训练/推理通信效率。

## GitHub
https://github.com/MoonshotAI/MoonEP

## 主要维护者 / 组织
由 [[Moonshot-AI]] / MoonshotAI 组织维护。公开作者包括 Yutian Chen、Cong Li、Yucheng Wang、Ming Wei；完整履历不足时本图谱暂不猜测其学校或直接汇报关系。

## 生态关系
- [[DeepEP]]：MoonEP 官方 acknowledgments 明确称其受到 DeepEP 启发。
- Echo / UltraEP / Alibaba AcclEP：其他 EP communication 实现路线。
- [[Kimi-K2]] / [[Kimi-K3]]：Moonshot MoE 模型与自研通信层的组织连接。
