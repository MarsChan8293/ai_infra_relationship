---
type: concept
name: Ahead-of-Time Compilation
aliases:
  - AOT Compilation
  - AOT
  - Offline Compilation
  - 提前编译
domain: compiler
topic: kernel-compilation
parent_concepts:
  - Kernel Compiler Pipeline
related_concepts:
  - JIT Kernel Compilation
  - Backend Code Generation
  - Autotuning
projects:
  - NineToothed
last_verified: 2026-09
---

# Ahead-of-Time Compilation

## 一句话定义

Ahead-of-Time Compilation（AOT）在部署/构建阶段提前把 kernel 或程序编译成目标 binary / artifact，而不是在第一次请求时现场编译。

## 解决的问题

[[JIT Kernel Compilation]] 能针对真实 shape 和硬件特化，但会带来首次调用编译延迟、运行时 compiler 依赖、并发编译和 cache 治理问题。对生产 serving，某些高频 kernel 更适合在镜像构建或部署阶段提前生成。

## 核心机制

AOT pipeline 通常：

1. 预先确定 target architecture 和关键 shape/config。
2. 运行 compiler pipeline。
3. 生成 cubin/hsaco/object/shared library 等 artifact。
4. 把 binary 随 package/container 发布。
5. runtime 只做查找、加载和 launch。

## AOT 与 JIT 的取舍

- AOT：启动稳定、运行时依赖少，但难覆盖无限 shape/config。
- JIT：适应性强、可现场 specialization，但有 cold-start 成本。
- 实际系统可以混合使用：常见配置 AOT，长尾 shape JIT，并共享 artifact cache。

## 与 Autotuning 的关系

[[Autotuning]] 可以离线运行，然后把最佳配置以 AOT artifact 固化；也可以在线 JIT + benchmark。Autotuning 是“选参数”，AOT/JIT 是“什么时候编译”。

## 项目实现

[[community/InfiniTensor/NineToothed|NineToothed]] 的 2026 compiler pipeline 已公开 architecture-aware caching、AOT 和 autotuning 路径，因此可作为当前仓库中最直接的 AOT compiler 实现节点。

## Sources

- https://github.com/InfiniTensor/ninetoothed
