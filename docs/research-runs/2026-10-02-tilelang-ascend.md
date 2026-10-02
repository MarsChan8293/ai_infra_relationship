# 2026-10-02 TileLang Ascend expansion

## Scope
Targeted expansion to complete TileLang Ascend coverage in `ai_infra_relationship`.

## Primary sources
- https://github.com/tile-ai/tilelang
- https://github.com/tile-ai/tilelang/blob/main/tilelang/ascend/README.md
- https://github.com/tile-ai/tilelang-ascend
- https://github.com/tile-ai/tilelang-mlir-ascend

## Findings
1. TileLang mainline added a supported Huawei Ascend 950 backend on 2026-09-30 with native code generation, Ascend-specific lowering/scheduling/synchronization, Cube/Vector execution and `target="ascend"`.
2. Mainline Ascend 950 is distinct from A2/A3 ecosystem adapters.
3. `tilelang-ascend` targets A2/A3 and exposes Ascend C & PTO plus AscendNPU IR routes; examples include GEMM, Flash/Sparse Attention, dispatch/combine, Lightning Indexer and TopK Selector.
4. `tilelang-mlir-ascend` is the MLIR-based adapter using AscendNPU IR and includes GEMM, FlashAttention and DeepSeek V4 mHC examples.
5. TileLang's Ascend 950 guide says the initial backend was mainly developed by multiple DeepSeek AI contributors and thanks Huawei and the TileLang community. This is recorded as direct implementation/collaboration evidence without additional employment inference.

## Graph changes
- Expanded canonical `TileLang`.
- Added `TileLang-Ascend` and `TileLang-MLIR-Ascend`.
- Added both to the Ascend ecosystem page.
- Added compiler/kernel concept mappings.
- Preserved the Ascend 950 vs A2/A3 support boundary.

Direct user-triggered expansion; no planner action-history append.
