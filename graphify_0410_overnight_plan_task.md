# Graphify Overnight Execution Plan (2026-04-10)

## 目标
对 openclaw 目录（12,035 文件，~7.5M 词）完成 graphify 知识图谱构建。

## 当前进度
- **AST**: 59,635 nodes, 123,806 edges (已完成)
- **语义提取**: chunks 0-9 已完成 (611 nodes, 763 edges, 68 hyperedges)
- **待处理**: chunks 10-52 (43 个 chunks)
- **结果文件**: `graphify-out/.graphify_semantic_new.json`

## 执行规则

### 1. 并发控制
- **严格 1 并发**：每次只调度 1 个 Agent
- 每个 chunk 约需 3-5 分钟（~200-400s）
- 43 chunks 预计总耗时 ~3.5 小时

### 2. 上下文管理
- 每个 chunk 完成后：
  1. 提取 JSON 结果并追加到 `graphify-out/.graphify_semantic_new.json`
  2. 更新 `graphify-out/.graphify_progress.json`（断点续传状态文件）
  3. 不在上下文中保留 agent 的完整输出，只保留统计摘要

### 3. 权限预审批
需要用户预先授权的目录和操作：
- **读取**: `openclaw/` 整个目录（所有子目录）
- **写入**: `graphify-out/` 目录
- **执行**: `$(cat graphify-out/.graphify_python)` 即 `.venv/bin/python`
- **Agent 调度**: 每次调度 1 个 background agent

### 4. 速率限制处理（GLM 5小时限制）
- 如果遇到 429 错误（速率限制）：
  1. 记录失败 chunk 编号到 `.graphify_progress.json`
  2. 等待 10 分钟后重试
  3. 如果连续 3 次重试仍失败，暂停并通知用户
- 如果遇到 GLM 会话超时：
  1. 断点续传机制会自动跳过已完成的 chunks
  2. 用户重新启动后从断点继续

## 断点续传机制

### 状态文件: `graphify-out/.graphify_progress.json`
```json
{
  "total_chunks": 53,
  "completed_chunks": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
  "failed_chunks": [],
  "current_chunk": null,
  "last_updated": "2026-04-10T...",
  "total_nodes": 611,
  "total_edges": 763,
  "total_hyperedges": 68
}
```

### 恢复流程
1. 读取 `.graphify_progress.json` 获取已完成的 chunks
2. 找到下一个未完成的 chunk
3. 继续以 1 并发调度
4. 每完成一个 chunk 更新 progress 文件

### Chunk 状态检查
```bash
# 快速检查哪些 chunks 已完成
$(cat graphify-out/.graphify_python) -c "
import json
p = json.load(open('graphify-out/.graphify_progress.json'))
remaining = [i for i in range(p['total_chunks']) if i not in p['completed_chunks']]
print(f'已完成: {len(p[\"completed_chunks\"])}/{p[\"total_chunks\"]}')
print(f'剩余: {remaining}')
"
```

## 每个 Chunk 的执行循环

```
对于每个未完成的 chunk N:
  1. 读取 chunk_N.json 获取文件列表
  2. 调度 1 个 Agent (background)
  3. 等待完成
  4. 提取 JSON 结果
     - 成功 → 追加到 .graphify_semantic_new.json, 标记 completed
     - 429 错误 → 标记 failed, 等待 10 分钟重试
     - 其他错误 → 标记 failed, 继续下一个
  5. 更新 .graphify_progress.json
  6. 输出一行摘要（chunk N: X nodes, Y edges | 总计: Z nodes）
```

## 完成后步骤

所有 53 chunks 完成后自动执行：
1. Step 3C: 合并 AST + semantic → `.graphify_extract.json`
2. Step 4: Build graph, cluster, analyze
3. Step 5: Label communities
4. Step 6: Generate HTML
5. Step 8: Token reduction benchmark
6. Step 9: Save manifest, clean up, report
