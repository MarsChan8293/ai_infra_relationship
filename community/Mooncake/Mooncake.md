---
type: project
name: Mooncake
layer: kv-cache-centric-serving
open_source: true
---
# Mooncake

## 项目简介
Mooncake 是面向 LLM serving 的 KVCache-centric 分布式系统，核心思想是把 prefill/decode 解耦后的 KV cache 作为一级系统资源管理，并利用 CPU DRAM、SSD、NIC 等资源构建分布式 KV 存储与传输路径。它来自清华 MADSys 与 Moonshot/Kimi 的产学协作，并获得 FAST 2025 Best Paper。

## GitHub
https://github.com/kvcache-ai/Mooncake

## 主要维护者 / 组织
由 KVCache.AI 社区维护，研究/工程网络连接清华大学 MADSys 与 [[Moonshot-AI]]。公开论文作者包括 Ruoyu Qin、Zheming Li、Weiran He、Jialei Cui、Heyi Tang、[[任峰 Feng Ren]]、[[马腾 Teng Ma]]、[[Shangming Cai]]、Yineng Zhang、Mingxing Zhang、Yongwei Wu、Weimin Zheng、Xinran Xu。

## 生态关系
[[SGLang]] · [[vLLM]] · [[LMCache]] · [[NIXL]] · [[KTransformers]] · [[Tsinghua University]] · [[Moonshot-AI]]。这是清华系 AI infra 中连接学术系统研究与真实 Kimi serving workload 的关键项目。
