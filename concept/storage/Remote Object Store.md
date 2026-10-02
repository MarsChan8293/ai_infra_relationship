---
type: concept
name: Remote Object Store
aliases:
  - Object Storage Backend
  - Remote Object Storage
  - 远程对象存储
domain: storage
topic: distributed-storage
related_concepts:
  - Distributed Storage
  - Storage Tiering
  - Point-to-Point Transfer
projects:
  - Mooncake
  - YuanRong DataSystem
  - LMCache
last_verified: 2026-09
---

# Remote Object Store

## 一句话定义

Remote Object Store 把数据封装成带 key/object identity 的远程对象，由独立存储服务负责放置、查找、生命周期和跨节点访问。

## 解决的问题

当 KV block、tensor、checkpoint 或中间结果需要跨 worker 共享时，直接依赖本地文件或进程内地址无法提供稳定命名和生命周期。Object Store 给上层提供一个与物理节点解耦的数据对象层。

## 核心机制

- object key / metadata。
- remote lookup。
- distributed placement。
- get / put / remove。
- replication / cache。
- zero-copy 或 RDMA data path。
- object lifetime 与 eviction。

## 与文件系统的区别

Distributed file system 使用 path / file / offset 语义；Object Store 更偏 object key + blob/tensor 语义。在 KV Cache 场景中，object key 常与 request、prefix 或 block identity 绑定。

## 项目实现

[[community/kvcache-ai/Mooncake/Mooncake|Mooncake Store]] 提供分布式 KV/object store；[[community/openEuler/openYuanRong/YuanRong DataSystem|YuanRong DataSystem]] 提供 Object / Stream / KV 数据语义；[[community/LMCache/LMCache/LMCache|LMCache]] 通过 Mooncake、S3、Valkey/Redis、filesystem/native L2 等 adapter 连接远端存储层。

## Sources

- https://github.com/kvcache-ai/Mooncake
- https://github.com/openyuanrong/datasystem
- https://github.com/LMCache/LMCache
