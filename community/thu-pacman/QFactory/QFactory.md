---
type: project
name: QFactory
organization: thu-pacman
linked_people:
  - "company/清程极智/翟季冬 Jidong Zhai"
  - "university/清华大学/Mingshu Zhai"
  - "university/清华大学/Qihao Zhang"
areas: [llm-serving, quantization, kernel-generation, ai-compiler]
layer: quantized-serving-kernel-optimization
open_source: true
last_verified: "2026-09"
linked_companies: []
---
# QFactory

QFactory 是 PACMAN 面向量化大模型 serving 的系统工作，发表于 USENIX ATC 2025。核心问题是不同量化算法 / precision format 往往需要专门 dequantization kernel，导致工程组合爆炸。

QFactory 通过 Qtile Graph 表达与优化 quantized kernels，把量化策略与底层 kernel generation / scheduling 连接起来。对本图谱而言，它代表 PACMAN 从 tensor compiler 研究迁移到 LLM serving 热路径的一条直接路线。

## 人物
- [[university/清华大学/Qihao Zhang|Qihao Zhang]]：论文第一作者 / PACMAN PhD student。
- [[university/清华大学/Mingshu Zhai|Mingshu Zhai]]：论文作者，研究还覆盖 SmartMoE 与 RoMeo。
- [[company/清程极智/翟季冬 Jidong Zhai|翟季冬]]：论文作者 / PACMAN faculty。

## Sources
- https://pacman.cs.tsinghua.edu.cn/~zjd/publication/generated/dblp-confusenix-zhang-zsz-25/
- https://pacman.cs.tsinghua.edu.cn/~zjd/category/mlsys/

<!-- BEGIN AUTO PROJECT PEOPLE -->
## 关联人物（自动汇总）

以下人物由其 `projects:` / `communities:`（含兼容旧字段）反向汇总，只表示公开可核验的项目或社区参与，不自动推断雇佣、同事或治理关系。

- [[company/清程极智/翟季冬 Jidong Zhai|翟季冬（Jidong Zhai）]]：[[community/thu-pacman/QFactory/QFactory|QFactory]]：USENIX ATC 2025，量化 LLM serving / kernel generation。
- [[university/清华大学/Mingshu Zhai|Mingshu Zhai]]：[[community/thu-pacman/QFactory/QFactory|QFactory]]：USENIX ATC 2025 作者，连接 tensor/compiler 研究与量化 LLM serving。
- [[university/清华大学/Qihao Zhang|Qihao Zhang]]：[[community/thu-pacman/QFactory/QFactory|QFactory]]：USENIX ATC 2025 第一作者，面向 quantized LLM serving 的 Qtile Graph / kernel optimization。

<!-- END AUTO PROJECT PEOPLE -->
