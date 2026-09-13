---
type: project
name: 3FS
parent: DeepSeek-Infra
layer: distributed-storage
open_source: true
---
# 3FS

## 项目简介
3FS 是 DeepSeek 开源的高性能分布式文件系统，面向训练/推理数据访问、checkpoint 与大规模 AI workload 的高吞吐存储路径，重点使用 RDMA、NVMe SSD 与现代网络/存储能力降低 GPU 数据等待。

## GitHub
https://github.com/deepseek-ai/3FS

## 主要维护者 / 组织
由 [[DeepSeek]] / deepseek-ai 维护。人物关系应以仓库公开作者和长期贡献为准，不从公司归属反推具体模块负责人。

## 生态关系
[[DeepSeek-Infra]] · [[Mooncake]] · [[NIXL]] · distributed storage。3FS 位于持久化/分布式存储层，而 Mooncake 更专注 serving KV cache，NIXL 更专注数据移动抽象。
