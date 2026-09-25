# Concept Index

Automatically generated from canonical `type: concept` nodes under `concept/`.

- Concepts: 79
- Domains: 9

Stable portal: [[concept]] · Implementation view: [[community/Software|Software]]

## Inference

23 concepts.

### Decoding

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/inference/decoding/Draft-Target Decoding|Draft-Target Decoding]] | Draft Model Speculative Decoding, Draft-and-Verify, Draft Target, 草稿模型投机解码 | Speculative Decoding | 2 | 2 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Draft-Target%20Decoding) |
| [[concept/inference/decoding/Multi-token Prediction|Multi-token Prediction]] | Multi-Token Prediction, MTP, Multi Token Prediction, 多Token预测 |  | 2 | 1 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Multi-token%20Prediction) |
| [[concept/inference/decoding/N-gram Speculation|N-gram Speculation]] | N-gram Speculative Decoding, Prompt Lookup Decoding, Prompt Lookup Speculation, N-gram投机解码 | Speculative Decoding | 1 | 1 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=N-gram%20Speculation) |
| [[concept/inference/decoding/Self-Speculative Decoding|Self-Speculative Decoding]] | Self Speculative Decoding, Self-Drafting, 自投机解码 | Speculative Decoding | 1 | 0 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Self-Speculative%20Decoding) |
| [[concept/inference/decoding/Speculative Decoding|Speculative Decoding]] | Speculative Sampling, Spec Decode, 投机解码, 投机推理 |  | 4 | 2 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Speculative%20Decoding) |

### Kv Cache

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/inference/kv-cache/KV Cache|KV Cache]] | Key-Value Cache, KV缓存 |  | 2 | 2 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=KV%20Cache) |
| [[concept/inference/kv-cache/KV Cache Management|KV Cache Management]] | KV管理, KV缓存管理 | KV Cache | 4 | 2 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=KV%20Cache%20Management) |
| [[concept/inference/kv-cache/KV Cache Offloading|KV Cache Offloading]] | KV Offloading, KV Cache 卸载, KV缓存卸载 | KV Cache Management | 2 | 2 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=KV%20Cache%20Offloading) |
| [[concept/inference/kv-cache/KV Cache Sharing|KV Cache Sharing]] | KV Sharing, Shared KV Cache, KV缓存共享 | KV Cache Management | 2 | 2 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=KV%20Cache%20Sharing) |
| [[concept/inference/kv-cache/KV Cache Transfer|KV Cache Transfer]] | KV Transfer, KV缓存传输 | KV Cache Management | 3 | 3 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=KV%20Cache%20Transfer) |
| [[concept/inference/kv-cache/Prefix Caching|Prefix Caching]] | Automatic Prefix Caching, APC, Prefix KV Caching, 前缀缓存 | KV Cache Management | 2 | 2 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Prefix%20Caching) |
| [[concept/inference/kv-cache/Tiered KV Cache|Tiered KV Cache]] | Hierarchical KV Cache, Multi-tier KV Cache, 分层KV缓存 | KV Cache Management | 2 | 3 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Tiered%20KV%20Cache) |

### Parallelism

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/inference/parallelism/Context Parallelism|Context Parallelism]] | CP, Context Parallel, 上下文并行 | Parallelism | 3 | 1 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Context%20Parallelism) |
| [[concept/inference/parallelism/Data Parallelism|Data Parallelism]] | DP, Replica Parallelism, 数据并行 | Parallelism | 1 | 1 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Data%20Parallelism) |
| [[concept/inference/parallelism/Expert Parallelism|Expert Parallelism]] | EP, MoE Expert Parallelism, 专家并行 | Parallelism | 2 | 2 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Expert%20Parallelism) |
| [[concept/inference/parallelism/Parallelism|Parallelism]] | Model Parallelism, 分布式并行, 并行切分 |  | 6 | 1 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Parallelism) |
| [[concept/inference/parallelism/Pipeline Parallelism|Pipeline Parallelism]] | PP, Pipeline Model Parallelism, 流水线并行 | Parallelism | 1 | 1 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Pipeline%20Parallelism) |
| [[concept/inference/parallelism/Sequence Parallelism|Sequence Parallelism]] | SP, Sequence Parallel, 序列并行 | Parallelism | 2 | 0 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Sequence%20Parallelism) |
| [[concept/inference/parallelism/Tensor Parallelism|Tensor Parallelism]] | TP, Tensor Model Parallelism, 张量并行 | Parallelism | 2 | 1 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Tensor%20Parallelism) |

### Serving

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/inference/serving/Chunked Prefill|Chunked Prefill]] | Prefill Chunking, Chunked Prompt Prefill, 分块预填充 |  | 2 | 1 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Chunked%20Prefill) |
| [[concept/inference/serving/Continuous Batching|Continuous Batching]] | In-flight Batching, Iteration-level Batching, 连续批处理 |  | 2 | 1 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Continuous%20Batching) |
| [[concept/inference/serving/Disaggregated Serving|Disaggregated Serving]] | Disaggregated Inference Serving, 分离式推理服务 |  | 2 | 6 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Disaggregated%20Serving) |
| [[concept/inference/serving/P-D Disaggregation|P-D Disaggregation]] | PD Disaggregation, P/D Disaggregation, Prefill-Decode Disaggregation, Prefill Decode Disaggregation | Disaggregated Serving | 2 | 7 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=P-D%20Disaggregation) |

## Memory

6 concepts.

### Memory Hierarchy

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/memory/HBM|HBM]] | High Bandwidth Memory, 高带宽内存 | Memory Hierarchy | 3 | 4 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=HBM) |
| [[concept/memory/Host Memory|Host Memory]] | CPU Memory, System Memory, Host DRAM, 主机内存 | Memory Hierarchy | 3 | 6 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Host%20Memory) |
| [[concept/memory/Memory Hierarchy|Memory Hierarchy]] | Hierarchical Memory, Multi-tier Memory, 分层内存, 内存层次 |  | 4 | 6 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Memory%20Hierarchy) |

### Memory Pooling

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/memory/CXL Memory|CXL Memory]] | Compute Express Link Memory, CXL Type-3 Memory, CXL内存 |  | 3 | 1 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=CXL%20Memory) |
| [[concept/memory/Memory Pooling|Memory Pooling]] | Memory Pool, Disaggregated Memory Pool, 内存池化 |  | 4 | 4 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Memory%20Pooling) |

### Memory Topology

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/memory/NUMA|NUMA]] | Non-Uniform Memory Access, 非一致内存访问 |  | 3 | 2 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=NUMA) |

## Communication

9 concepts.

### Collective Communication

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/communication/collectives/All-to-All|All-to-All]] | AllToAll, All-to-All Communication, 全互换通信 | Collective Communication | 2 | 3 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=All-to-All) |
| [[concept/communication/collectives/AllGather|AllGather]] | All-Gather, 全收集 | Collective Communication | 3 | 4 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=AllGather) |
| [[concept/communication/collectives/AllReduce|AllReduce]] | All-Reduce, 全归约 | Collective Communication | 3 | 4 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=AllReduce) |
| [[concept/communication/collectives/Collective Communication|Collective Communication]] | Collective Operations, Communication Collectives, 集合通信 |  | 5 | 5 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Collective%20Communication) |
| [[concept/communication/collectives/ReduceScatter|ReduceScatter]] | Reduce-Scatter, 归约分散 | Collective Communication | 3 | 3 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=ReduceScatter) |

### Data Movement

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/communication/data-movement/Data Movement|Data Movement]] | Inference Data Movement, Distributed Data Movement, 数据搬运, 数据移动 |  | 3 | 3 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Data%20Movement) |
| [[concept/communication/data-movement/GPUDirect RDMA|GPUDirect RDMA]] | GDR, GPU Direct RDMA, GPUDirect Remote Direct Memory Access | RDMA | 1 | 2 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=GPUDirect%20RDMA) |
| [[concept/communication/data-movement/Point-to-Point Transfer|Point-to-Point Transfer]] | P2P Transfer, Point-to-Point Communication, P2P Data Movement, 点到点传输 | Data Movement | 3 | 6 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Point-to-Point%20Transfer) |
| [[concept/communication/data-movement/RDMA|RDMA]] | Remote Direct Memory Access, 远程直接内存访问 | Point-to-Point Transfer | 1 | 6 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=RDMA) |

## Scheduling

8 concepts.

### Inference Scheduling

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/inference/scheduling/Autoscaling|Autoscaling]] | Inference Autoscaling, LLM Autoscaling, 自动扩缩容 | Inference Scheduling | 2 | 5 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Autoscaling) |
| [[concept/inference/scheduling/Capacity Planning|Capacity Planning]] | Inference Capacity Planning, LLM Capacity Planning, 容量规划 | Inference Scheduling | 2 | 2 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Capacity%20Planning) |
| [[concept/inference/scheduling/Inference Scheduling|Inference Scheduling]] | LLM Inference Scheduling, 推理调度, LLM推理调度 |  | 3 | 4 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Inference%20Scheduling) |
| [[concept/inference/scheduling/Inference-Aware Routing|Inference-Aware Routing]] | LLM-Aware Routing, Model-Aware Routing, 推理感知路由 | Request Routing | 2 | 5 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Inference-Aware%20Routing) |
| [[concept/inference/scheduling/KV-Aware Routing|KV-Aware Routing]] | KV Cache-Aware Routing, Prefix-Cache Aware Routing, Prefix-Aware Routing, KV感知路由 | Inference-Aware Routing | 3 | 5 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=KV-Aware%20Routing) |
| [[concept/inference/scheduling/Load Balancing|Load Balancing]] | Inference Load Balancing, LLM Load Balancing, 负载均衡 | Inference Scheduling | 3 | 6 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Load%20Balancing) |
| [[concept/inference/scheduling/Load-Aware Routing|Load-Aware Routing]] | Least-Loaded Routing, Load-Sensitive Routing, 负载感知路由 | Inference-Aware Routing | 2 | 4 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Load-Aware%20Routing) |
| [[concept/inference/scheduling/Request Routing|Request Routing]] | Inference Request Routing, 请求路由 | Inference Scheduling | 2 | 6 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Request%20Routing) |

## Kernel

6 concepts.

### Attention

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/kernel/attention/Attention Kernel|Attention Kernel]] | Attention Operator Kernel, 注意力算子, Attention算子 |  | 3 | 4 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Attention%20Kernel) |
| [[concept/kernel/attention/FlashAttention|FlashAttention]] | Flash Attention, IO-Aware Attention | Attention Kernel | 1 | 3 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FlashAttention) |
| [[concept/kernel/attention/PagedAttention|PagedAttention]] | Paged Attention, 分页注意力 | Attention Kernel | 2 | 2 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=PagedAttention) |

### Gemm

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/kernel/gemm/GEMM|GEMM]] | General Matrix Multiplication, Matrix Multiplication Kernel, 通用矩阵乘 |  | 3 | 4 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=GEMM) |
| [[concept/kernel/gemm/Grouped GEMM|Grouped GEMM]] | Grouped Matrix Multiplication, Grouped Matmul, 分组矩阵乘 | GEMM | 3 | 3 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Grouped%20GEMM) |

### Optimization

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/kernel/optimization/Kernel Fusion|Kernel Fusion]] | Operator Fusion, Fused Kernel, 算子融合 |  | 4 | 4 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Kernel%20Fusion) |

## Compiler

8 concepts.

### Kernel Compilation

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/compiler/Ahead-of-Time Compilation|Ahead-of-Time Compilation]] | AOT Compilation, AOT, Offline Compilation, 提前编译 | Kernel Compiler Pipeline | 3 | 1 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Ahead-of-Time%20Compilation) |
| [[concept/compiler/Backend Code Generation|Backend Code Generation]] | Target Code Generation, Codegen, Backend Codegen, 后端代码生成 | Kernel Compiler Pipeline | 2 | 4 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Backend%20Code%20Generation) |
| [[concept/compiler/Compiler Lowering|Compiler Lowering]] | IR Lowering, Kernel Lowering, 编译降级, IR降级 | Kernel Compiler Pipeline | 2 | 4 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Compiler%20Lowering) |
| [[concept/compiler/Kernel Compiler Pipeline|Kernel Compiler Pipeline]] | Kernel Compilation Pipeline, GPU Kernel Compiler Pipeline, 算子编译流水线 |  | 5 | 4 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Kernel%20Compiler%20Pipeline) |

### Kernel Optimization

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/compiler/Autotuning|Autotuning]] | Auto-Tuning, Kernel Autotuning, Auto Tuning, 自动调优 |  | 3 | 3 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Autotuning) |
| [[concept/compiler/Layout Optimization|Layout Optimization]] | Data Layout Optimization, Memory Layout Optimization, Tensor Layout Optimization, 布局优化 |  | 4 | 3 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Layout%20Optimization) |

### Kernel Programming

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/kernel/programming/JIT Kernel Compilation|JIT Kernel Compilation]] | JIT Compilation, Runtime Kernel Compilation, Just-in-Time Kernel Compilation, Kernel JIT |  | 3 | 6 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=JIT%20Kernel%20Compilation) |
| [[concept/kernel/programming/Kernel DSL|Kernel DSL]] | GPU Kernel DSL, Kernel Domain-Specific Language, 算子DSL, Kernel编程语言 |  | 4 | 4 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Kernel%20DSL) |

## Quantization

7 concepts.

### Kv Cache

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/quantization/KV Cache Quantization|KV Cache Quantization]] | Quantized KV Cache, KV Quantization, KV缓存量化 | Quantization | 3 | 2 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=KV%20Cache%20Quantization) |

### Quantization

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/quantization/FP4 Quantization|FP4 Quantization]] | Float4 Quantization, FP4, MXFP4, NVFP4 | Quantization | 3 | 6 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FP4%20Quantization) |
| [[concept/quantization/FP8 Quantization|FP8 Quantization]] | Float8 Quantization, FP8, E4M3, E5M2 | Quantization | 4 | 4 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=FP8%20Quantization) |
| [[concept/quantization/Quantization|Quantization]] | Model Quantization, LLM Quantization, 模型量化 |  | 3 | 8 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Quantization) |
| [[concept/quantization/W8A8|W8A8]] | Weight 8 Activation 8, 8-bit Weight Activation Quantization, 权重8比特激活8比特 | Weight-Activation Quantization | 1 | 3 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=W8A8) |
| [[concept/quantization/Weight-Activation Quantization|Weight-Activation Quantization]] | Weight and Activation Quantization, W-A Quantization, 权重激活量化 | Quantization | 4 | 4 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Weight-Activation%20Quantization) |
| [[concept/quantization/Weight-Only Quantization|Weight-Only Quantization]] | Weight Only Quantization, WOQ, W4A16, W8A16 | Quantization | 2 | 5 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Weight-Only%20Quantization) |

## Hardware

6 concepts.

### Interconnect

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/hardware/interconnect/Hardware Interconnect|Hardware Interconnect]] | Accelerator Interconnect, Device Interconnect, 硬件互联, 加速器互联 |  | 6 | 6 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Hardware%20Interconnect) |
| [[concept/hardware/interconnect/HCCS|HCCS]] | Huawei Cache Coherence System, 昇腾HCCS | Hardware Interconnect | 3 | 2 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=HCCS) |
| [[concept/hardware/interconnect/NVLink|NVLink]] | NVIDIA NVLink, NVLink Interconnect | Hardware Interconnect | 3 | 3 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=NVLink) |
| [[concept/hardware/interconnect/NVSwitch|NVSwitch]] | NVIDIA NVSwitch, NVLink Switch, NVLink Switch Fabric | Hardware Interconnect | 2 | 2 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=NVSwitch) |
| [[concept/hardware/interconnect/PCIe|PCIe]] | PCI Express, Peripheral Component Interconnect Express, PCIe总线 | Hardware Interconnect | 3 | 3 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=PCIe) |
| [[concept/hardware/interconnect/xGMI|xGMI]] | AMD xGMI, Infinity Fabric xGMI, xGMI Interconnect | Hardware Interconnect | 2 | 1 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=xGMI) |

## Storage

6 concepts.

### Data Path

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/storage/Direct Storage IO|Direct Storage I/O]] | Direct Storage, GPU Direct Storage, GPUDirect Storage, GDS |  | 3 | 3 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Direct%20Storage%20I%2FO) |

### Distributed Storage

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/storage/Distributed Storage|Distributed Storage]] | Distributed Storage System, 分布式存储 |  | 3 | 5 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Distributed%20Storage) |
| [[concept/storage/Remote Object Store|Remote Object Store]] | Object Storage Backend, Remote Object Storage, 远程对象存储 |  | 3 | 3 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Remote%20Object%20Store) |

### Kv Cache Storage

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/storage/SSD-Backed KV Cache|SSD-Backed KV Cache]] | SSD KV Cache, NVMe KV Cache, SSD-backed KV, SSD后端KV缓存 |  | 4 | 3 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=SSD-Backed%20KV%20Cache) |

### Storage Media

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/storage/NVMe SSD|NVMe SSD]] | NVMe, NVMe Storage, SSD, NVMe固态盘 |  | 4 | 5 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=NVMe%20SSD) |

### Storage Tiering

| Concept | Aliases | Parent | Related | Projects | Graph |
| --- | --- | --- | ---: | ---: | --- |
| [[concept/storage/Storage Tiering|Storage Tiering]] | Tiered Storage, Multi-tier Storage, 分层存储 |  | 4 | 5 | [focus](https://MarsChan8293.github.io/ai_infra_relationship/graph-explorer/?focus=Storage%20Tiering) |
