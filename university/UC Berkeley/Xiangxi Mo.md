---
type: person
name: Xiangxi Mo
aliases: ["Xiangxi Mo"]
schools:
  - "UC Berkeley"
communities: [vLLM]
projects: [Jenga]
areas: [llm-serving, inference-systems, gpu-scheduling, model-serving]
roles: ["vLLM Project Lead (2023-2026)"]
confidence: high
last_verified: "2026-09"
---
# Xiangxi Mo

UC Berkeley systems researcher，研究主线长期围绕 machine-learning serving、GPU inference scheduling 与 open-source inference systems 展开。

## AI Infra 位置
- [[community/vllm-project/Jenga/Jenga|Jenga]]：SOSP 2025 作者，连接 Berkeley systems 与现代 LLM serving memory management。
- [[community/vllm-project/vLLM/vLLM|vLLM]]：其博士工作总结将 vLLM 列为 open-source inference serving 系统主线之一，并记录 2023–2026 担任 vLLM Project Lead。
- InferLine：较早期 prediction-serving 系统，关注多阶段 inference pipeline 的 provisioning、autoscaling 与 latency SLO。
- GPU inference scheduling：参与 Dynamic Space-Time Scheduling 等工作，持续研究 GPU multiplexing 与 inference utilization。

## 图谱意义
Xiangxi Mo 是 Jenga 向 Berkeley inference-serving 历史纵深扩展的重要节点：`InferLine / GPU scheduling → vLLM → Jenga`，能把早期 prediction serving 与当前 LLM serving 连接起来。

## 身份边界
公开材料中偶有 `Xiangxi (Simon) Mo` 的写法，但本仓库已经存在独立的 [[community/vllm-project/vLLM/Simon Mo|Simon Mo]] 节点，因此这里不把 `Simon Mo` 作为 alias，避免错误合并身份。


## 学校关联
- [[university/UC Berkeley/UC Berkeley|UC Berkeley]]：已存在可核验的教育、任职或访问研究关联；具体阶段以正文与 Sources 为准。

## Sources
- https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-36.pdf
- https://arxiv.org/abs/2503.18292
- https://par.nsf.gov/servlets/purl/10245792
- https://rise.cs.berkeley.edu/wp-content/uploads/2020/04/102CameraReadySubmissionGPU_Virtualization-8.pdf
