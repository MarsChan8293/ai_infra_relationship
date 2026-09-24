# Project ↔ Concept Coverage

由 scripts/audit-project-concept-coverage.py 自动生成。Concept 节点的 projects 字段是人工事实源；Project 页的 linked_concepts 是派生反向视图。

- Status: **pass**
- Concepts: 23
- Concepts with project evidence: 21
- Project-like nodes: 150
- Projects linked to concepts: 7
- Concept → Project assertions: 43
- Unresolved project refs: 0
- Reverse-link mismatches: 0

## Projects with the densest Concept coverage

| Project | Layer | Concepts | Count |
| --- | --- | --- | ---: |
| [[community/vllm-project/vLLM/vLLM|vLLM]] | inference-engine | [[concept/inference/decoding/Draft-Target Decoding|Draft-Target Decoding]] · [[concept/inference/decoding/Multi-token Prediction|Multi-token Prediction]] · [[concept/inference/decoding/N-gram Speculation|N-gram Speculation]] · [[concept/inference/decoding/Speculative Decoding|Speculative Decoding]] · [[concept/inference/kv-cache/KV Cache|KV Cache]] · [[concept/inference/kv-cache/KV Cache Management|KV Cache Management]] · [[concept/inference/kv-cache/KV Cache Offloading|KV Cache Offloading]] · [[concept/inference/kv-cache/KV Cache Transfer|KV Cache Transfer]] · [[concept/inference/kv-cache/Prefix Caching|Prefix Caching]] · [[concept/inference/kv-cache/Tiered KV Cache|Tiered KV Cache]] · [[concept/inference/parallelism/Context Parallelism|Context Parallelism]] · [[concept/inference/parallelism/Data Parallelism|Data Parallelism]] · [[concept/inference/parallelism/Expert Parallelism|Expert Parallelism]] · [[concept/inference/parallelism/Parallelism|Parallelism]] · [[concept/inference/parallelism/Pipeline Parallelism|Pipeline Parallelism]] · [[concept/inference/parallelism/Tensor Parallelism|Tensor Parallelism]] · [[concept/inference/serving/Chunked Prefill|Chunked Prefill]] · [[concept/inference/serving/Continuous Batching|Continuous Batching]] · [[concept/inference/serving/Disaggregated Serving|Disaggregated Serving]] · [[concept/inference/serving/P-D Disaggregation|P-D Disaggregation]] | 20 |
| [[community/LMCache/LMCache/LMCache|LMCache]] | kv-cache | [[concept/inference/kv-cache/KV Cache Management|KV Cache Management]] · [[concept/inference/kv-cache/KV Cache Offloading|KV Cache Offloading]] · [[concept/inference/kv-cache/KV Cache Sharing|KV Cache Sharing]] · [[concept/inference/kv-cache/KV Cache Transfer|KV Cache Transfer]] · [[concept/inference/kv-cache/Tiered KV Cache|Tiered KV Cache]] · [[concept/inference/serving/P-D Disaggregation|P-D Disaggregation]] | 6 |
| [[community/sgl-project/SGLang/SGLang|SGLang]] | inference-engine | [[concept/inference/decoding/Draft-Target Decoding|Draft-Target Decoding]] · [[concept/inference/decoding/Speculative Decoding|Speculative Decoding]] · [[concept/inference/kv-cache/KV Cache|KV Cache]] · [[concept/inference/kv-cache/Prefix Caching|Prefix Caching]] · [[concept/inference/serving/Disaggregated Serving|Disaggregated Serving]] · [[concept/inference/serving/P-D Disaggregation|P-D Disaggregation]] | 6 |
| [[community/kvcache-ai/Mooncake/Mooncake|Mooncake]] | kv-cache | [[concept/inference/kv-cache/KV Cache Sharing|KV Cache Sharing]] · [[concept/inference/kv-cache/KV Cache Transfer|KV Cache Transfer]] · [[concept/inference/kv-cache/Tiered KV Cache|Tiered KV Cache]] · [[concept/inference/serving/Disaggregated Serving|Disaggregated Serving]] · [[concept/inference/serving/P-D Disaggregation|P-D Disaggregation]] | 5 |
| [[community/llm-d/llm-d/llm-d|llm-d]] | distributed-serving | [[concept/inference/serving/Disaggregated Serving|Disaggregated Serving]] · [[concept/inference/serving/P-D Disaggregation|P-D Disaggregation]] | 2 |
| [[community/Ascend/MindIE-Motor/MindIE-Motor|MindIE-Motor]] | runtime | [[concept/inference/serving/Disaggregated Serving|Disaggregated Serving]] · [[concept/inference/serving/P-D Disaggregation|P-D Disaggregation]] | 2 |
| [[community/ai-dynamo/Dynamo/Dynamo|NVIDIA Dynamo]] | distributed-serving | [[concept/inference/serving/Disaggregated Serving|Disaggregated Serving]] · [[concept/inference/serving/P-D Disaggregation|P-D Disaggregation]] | 2 |

## Concepts without project evidence

- [[concept/inference/decoding/Self-Speculative Decoding|Self-Speculative Decoding]]
- [[concept/inference/parallelism/Sequence Parallelism|Sequence Parallelism]]

## Mapping by topic

| Topic | Concepts | With project evidence |
| --- | ---: | ---: |
| decoding | 5 | 4 |
| kv-cache | 7 | 7 |
| parallelism | 7 | 6 |
| serving | 4 | 4 |
