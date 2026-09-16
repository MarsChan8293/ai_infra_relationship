---
type: project
name: Speculators
layer: speculative-decoding-training
open_source: true
repository: https://github.com/vllm-project/speculators
areas: [speculative-decoding, online-training, hidden-state-transfer, vllm, distributed-training]
governance: vLLM Project ecosystem
last_verified: "2026-09"
---
# Speculators

## 项目简介
Speculators 是 vLLM Project 生态中的 speculative decoding draft-model training framework，覆盖 hidden-state 生成、draft model 训练与直接部署到 vLLM 的端到端路径。

## Mooncake 关系
2026 年 Speculators 引入 `hs_connectors` 多节点在线训练插件。官方 README 明确说明 Mooncake backend 用 distributed store 在 vLLM inference workers 与 trainer 之间跨节点传输 hidden states，使在线 speculative-model training 不依赖共享文件系统。

这条边把 [[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] 从 KV cache / serving data plane 延伸到了 speculative decoding 的训练数据平面。

## Sources
- https://github.com/vllm-project/speculators
- https://github.com/kvcache-ai/Mooncake
