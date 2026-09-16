# openYuanRong focused research run — 2026-09-16

## Seed
`openYuanRong`

## Goal
Expand the graph around openYuanRong with emphasis on inference optimization, Ascend/NPU data movement, post-training data planes, governance, and direct integrations. This is a focused seed run rather than a daily global HAES portfolio run.

## High-confidence findings

### 1. openYuanRong is a relevant AI Infra node
- Official openEuler positioning: Serverless distributed compute engine with runtime, function system, and data system.
- YuanRong originated as a Huawei production system; SIGCOMM 2024 paper authors were Huawei Technologies.
- openEuler reports that openYuanRong moved from Huawei internal use into the openEuler open-source ecosystem at the end of 2025.
- 2026 project direction explicitly covers inference, reinforcement learning and Agentic AI infrastructure.

Outcome: created canonical `openYuanRong` project with `company-originated-open-source` relationship to Huawei, without treating current openEuler governance as Huawei-private ownership.

### 2. YuanRong DataSystem has direct inference/post-training integrations
- vLLM-Ascend KV Pool documents YuanRong DataSystem as a backend for AscendStoreConnector.
- TransferQueue documents openYuanRong DataSystem as an optional storage backend with TCP/RDMA, Ascend HCCS, remote H2D/D2H and NPU tensor paths.
- vLLM-Omni provides `YuanrongConnector` backed by YuanRong DataSystem.

Outcome: created canonical `YuanRong DataSystem` project.

### 3. YuanRong TransferEngine is a distinct inference data-plane component
- vLLM-Ascend RFork explicitly installs `openyuanrong-transfer-engine` for weight transfer.
- vLLM-Omni currently registers `YuanrongTransferEngineConnector` as an Ascend NPU-specific P2P connector; this is implemented, not merely an RFC.

Outcome: created canonical `YuanRong TransferEngine` project and linked it to vLLM-Ascend and vLLM-Omni.

### 4. TransferQueue is a valuable downstream bridge
- TransferQueue targets asynchronous streaming data management for post-training / RL.
- Its first pluggable KV backend was openYuanRong.
- openEuler's July 2026 Meetup explicitly identifies Chenghao Rong as a Transfer Queue community Maintainer and covers TransferQueue-on-openYuanRong practice.

Outcome: created canonical `TransferQueue` and `Chenghao Rong` nodes.

### 5. Governance people
- `Yi Liang / 梁义`: openYuanRong Maintainer; Huawei General Serverless Chief Expert / YuanRong Chief Architect; Zhejiang University PhD.
- `Zhancheng Luo / 罗站城`: openYuanRong Maintainer; Huawei system software architect; public bio identifies him as the YuanRong Function System subsystem technical lead.

Outcome: created both as canonical person nodes and connected them to Huawei + openYuanRong.

### 6. vLLM-Omni bridge
Current vLLM-Omni implementation exposes both a YuanRong DataSystem-backed connector and an Ascend NPU YuanRong TransferEngine connector.

Outcome: created canonical `vLLM-Omni` project and attached existing Roger Wang as the high-value maintainer entry point already documented elsewhere in this repository.

## Evidence boundaries
- openEuler SIG repository permission lists contain more repository-level maintainers/committers. This run does not promote all of them to core graph people automatically.
- veRL has an RFC proposing openYuanRong as an optional distributed framework. It is recorded as a research lead, not treated as fully landed framework integration.
- Compatibility and backend support do not create person-to-person collaboration edges.
- Huawei origin is historical/organizational evidence; current openYuanRong governance is modeled as openEuler community governance rather than Huawei-private ownership.

## New canonical nodes
1. openYuanRong
2. YuanRong DataSystem
3. YuanRong TransferEngine
4. TransferQueue
5. vLLM-Omni
6. 梁义 / Yi Liang
7. 罗站城 / Zhancheng Luo
8. 荣程浩 / Chenghao Rong

## Existing nodes strengthened
- Huawei
- vLLM-Ascend
- Roger Wang

## Next frontier
- Identify the direct authors/implementers of vLLM-Ascend YuanRong KV Pool / RFork integration (for example RFC/PR authors) with pair-specific evidence.
- Resolve openYuanRong DataSystem repository-level maintainers beyond SIG-level governance where technically valuable.
- Evaluate `ray-adapter` and openYuanRong's proposed veRL backend only after confirming landed production code.
- Search openYuanRong v0.8+ RL training/inference collaboration paths and parameter-server/data-plane implementations.
- Consider Wu Jie as an additional architecture node if current role and project contribution justify a separate person node.

## Primary sources
- https://www.openeuler.org/zh/projects/yuanrong/
- https://www.openeuler.org/zh/sig/sig-YuanRong
- https://github.com/openyuanrong/runtime
- https://github.com/openyuanrong/datasystem
- https://doi.org/10.1145/3651890.3672216
- https://docs.vllm.ai/projects/ascend/en/main/user_guide/feature_guide/kv_pool.html
- https://docs.vllm.ai/projects/ascend/en/main/user_guide/feature_guide/rfork.html
- https://docs.vllm.ai/projects/vllm-omni/en/latest/design/feature/disaggregated_inference/
- https://github.com/Ascend/TransferQueue/blob/main/docs/storage_backends/openyuanrong_datasystem.md
- https://www.openeuler.org/zh/news/20260728-openYuanrong%20Meetup/20260728-openYuanrong%20Meetup.html
