---
type: concept
name: Weight-Only Quantization
aliases:
  - Weight Only Quantization
  - WOQ
  - W4A16
  - W8A16
  - 仅权重量化
domain: quantization
topic: quantization
parent_concepts:
  - Quantization
related_concepts:
  - Weight-Activation Quantization
  - GEMM
projects:
  - vLLM
  - LMDeploy
  - ggml
  - llama.cpp
  - QFactory
last_verified: 2026-09
---

# Weight-Only Quantization

## 一句话定义

Weight-Only Quantization 只把模型权重压缩到更低精度，而 activation 通常保持 FP16/BF16 等较高精度，在 GEMM 前或 GEMM 内部完成 dequantization。

## 解决的问题

Decode 阶段常受权重读取带宽限制。把权重从 16bit 压到 8/4/更低 bit 可以显著减少模型占用和 HBM 读取量，同时避免 activation 量化带来的额外精度敏感性。

## 核心机制

典型 kernel 流程是：

1. 从显存读取 packed low-bit weights。
2. 按 group/channel scale 和 zero-point 解码。
3. 在寄存器/shared memory 或 tensor-core compatible layout 中恢复/转换。
4. 与高精度 activation 执行 GEMM。

因此 weight-only 性能很依赖 dequant + GEMM 是否融合；若先完整反量化到 HBM，压缩收益会大幅缩水。

## 常见形式

- W8A16：8-bit weight + 16-bit activation。
- W4A16：4-bit weight + 16-bit activation。
- AWQ / GPTQ / GGUF Q4/Q5/Q6 等属于不同算法/编码族，不应简单当作同一种 format。

## 与 W8A8 的区别

[[W8A8]] 同时把 activation 也降到 8bit，因此更依赖硬件低精度 GEMM 和 activation scale 策略；Weight-Only 主要减少权重带宽和容量压力。

## 项目实现

[[community/vllm-project/vLLM/vLLM|vLLM]] 支持 AWQ/GPTQ、INT4 W4A16、FP8 W8A16 等 weight-only 路径；[[community/InternLM/LMDeploy/LMDeploy|LMDeploy]] 长期提供 weight-only quantization 与低比特 kernel；[[community/ggml-org/ggml/ggml|ggml]] / [[community/ggml-org/llama.cpp/llama.cpp|llama.cpp]] 提供 1.5–8bit 等多种量化权重格式；[[community/thu-pacman/QFactory/QFactory|QFactory]] 面向多量化算法自动生成/优化 dequantization kernel。

## Sources

- https://docs.vllm.ai/en/stable/features/quantization/
- https://github.com/InternLM/lmdeploy
- https://github.com/ggml-org/llama.cpp/wiki/Tensor-Encoding-Schemes
- https://pacman.cs.tsinghua.edu.cn/~zjd/publication/generated/dblp-confusenix-zhang-zsz-25/
