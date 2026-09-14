---
type: company
name: TensorMesh
focus: ai-inference-infrastructure
projects: [LMCache, vLLM]
---
# TensorMesh

## 公司简介
TensorMesh 是围绕 LLM KV cache、disaggregated serving 与 inference memory/data plane 商业化的 AI infrastructure 公司。它承接了 [[LMCache]] 等研究成果，试图把跨 GPU/CPU/远端存储的 KV 管理能力产品化，是“研究系统 → 开源项目 → startup”的另一条典型路径。

## 主要贡献的社区项目
- [[community/LMCache/LMCache/LMCache|LMCache]]：**research → startup core network / commercialization**，公司创始技术网络与 LMCache 核心人物高度重叠。
- [[community/vllm-project/vLLM/vLLM|vLLM]]：通过 KV Connector、disaggregated serving 与相关核心维护/工程人员形成直接贡献网络。

## 核心人物
- [[company/TensorMesh/Junchen Jiang|Junchen Jiang]]：联合创始人、CEO；[[University of Chicago]] Associate Professor；LMCache 共同创建者。
- [[程翊华 Yihua Cheng]]：联合创始人、CTO。
- [[杜昆泰 Kuntai Du]]：联合创始人、Chief Scientist。

## 图谱中的连接
[[LMCache]] · [[vLLM]] · [[University of Chicago]] · KV Connector · disaggregated serving。TensorMesh 与 Berkeley 网络在 PrefillOnly/Jenga 等研究中存在跨校合作，但其创始学术谱系主要是 University of Chicago，不能误标为 Berkeley 系。
