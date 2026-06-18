# Project Wiki 工作流说明

## 1. 项目定位

`project_wiki`（`git@github.com:JunYan01/project_wiki.git`）是一个**聚合/索引仓库**，本身不含业务代码。它的作用是用 **git submodule（子模块）** 把多个独立仓库"挂"进来统一管理，并对它们跑 graphify 生成知识图谱。

## 2. 目录结构总览

```
project_wiki/
├── .gitmodules              # 子模块注册表（核心配置）
├── .gitignore               # 忽略 .DS_Store / .venv/
├── CLAUDE.md                # 工具偏好：uv > pip；task_steps.md 同步
├── task_steps.md            # 已完成步骤记录（恢复上下文用）
├── WORKFLOW.md              # 本文件
│
├── openclaw/                # 【子模块·指针】源码  git@github.com:openclaw/openclaw.git
├── hermes-agent/            # 【子模块·指针】源码  git@github.com:NousResearch/hermes-agent.git
├── graphify/                # 【子模块·指针】工具  https://github.com/safishamsi/graphify.git
│
├── graphify-out/            # 【产物·普通目录】hermes-agent 的知识图谱输出
├── graphify-out-openclaw/   # 【产物·普通目录】openclaw 的知识图谱输出
│
├── .venv/                   # Python 虚拟环境（gitignored）
└── agent_memory_system_by_ff/
```

**关键概念**：仓库里有两类被追踪的东西——
- **指针（submodule）**：只记录外部仓库的某个 commit，不存实际内容。
- **产物（普通目录）**：`graphify-out*`，跑 graphify 生成的几十 MB json，直接当普通文件追踪。

## 3. 工具偏好（来自 CLAUDE.md）

- 所有 Python 操作一律用 **`uv`**，不用 `pip`。
- graphify 相关命令也用 `uv run` / `uv python` 执行。
- 每完成一个步骤，立即追加到 `task_steps.md`。

## 4. Submodule 日常工作流

### 4.1 新机器 / 新 session 恢复
```bash
git clone --recurse-submodules <project_wiki地址>
# 或已 clone 但子模块为空时补拉：
git submodule update --init --recursive
```

### 4.2 更新已有子模块到各仓库最新
```bash
git submodule update --remote          # 把 3 个子模块拉到各自远程最新 commit
git diff --submodule                   # 查看 commit 变化
git commit -am "更新 submodule 至最新"
git push
```
> git status 里看到 `m openclaw`，就是子模块当前 commit 与 wiki 记录的指针不一致（待提交）。

### 4.3 添加新仓库（如 pi-agent）
```bash
git submodule add <pi-agent 的 git 地址> pi-agent   # SSH 用 git@github.com:..., HTTPS 用 https://...
git commit -am "添加 pi-agent submodule"
git push
```

### 4.4 更新大仓库 / 网络慢时用 shallow fetch（只拉最新，不要历史）

> 像 `openclaw` 这种巨型仓库（4 万+ commits、1.6GB），用 `git submodule update --remote` 会拉取海量历史，在慢/中转链路上极易卡死（长时间无输出、`git index-pack` 进程 CPU 不涨、`.git/objects/pack/` 出现数百 MB 临时 pack）。更新到最新其实**不需要全历史**。

只拉默认分支最新一个 commit（数据量从几百 MB 降到几十 MB）：

```bash
# 1) 确认该子模块默认分支（.gitmodules 未配 branch 时用 default）
git config -f .gitmodules submodule.<name>.branch
git -C <name> symbolic-ref refs/remotes/origin/HEAD | sed 's@refs/remotes/origin/@@'   # 输出如 main

# 2) 浅拉最新（--depth=1）
git -C <name> fetch --depth=1 origin <默认分支>

# 3) 切到最新
git -C <name> checkout FETCH_HEAD

# 4) 回 wiki 层提交新指针
git add <name> && git commit -m "更新 <name> 至最新" && git push
```

**判断依据**：`update --remote` 卡住超过几分钟且 `git index-pack` 进程 CPU 长期不动 → 八成是大仓库全量历史传输，改用上面的 shallow 流程。

## 5. Graphify 知识图谱工作流

### 5.1 安装（仅首次）
```bash
uv venv                                 # 建 .venv（需 Python 3.10+，uv 会拉 3.12）
uv pip install -e "./graphify[all]"     # 可编辑模式安装 + 全部依赖
uv run graphify install                 # 把 graphify skill 注册到 Claude Code
```

### 5.2 跑知识图谱（大规模分块）
- **输出目录命名约定**：`graphify-out-<仓库名>/`（如 `graphify-out` 对应 hermes-agent）。
- **断点续处理规则**（来自 task_steps.md）：
  - 并发度 = 1，逐 chunk 串行处理。
  - 每个 chunk 完成后 **compress 一次上下文**，防溢出。
  - **不要预读**下一个 chunk 的文件列表来"加速"。
  - 进度追踪：`.graphify_progress.json`。
  - chunk 结果：`chunk_N.json` / `.chunk_result_N.json`，最后用 `merge_chunk.py` 合并去重。
- **最终产物**：`GRAPH_REPORT.md`（报告）、`graph.html`（社区级可视化）。

### 5.3 更新产物
源码子模块更新后（见 4.2），对 `graphify-out-<repo>/` 重新跑 graphify，再提交新产物：
```bash
git commit -am "重新生成 <repo> 知识图谱产物"
```

### 5.4 输出目录命名（graphify-out-<repo>）与查询指定

> **graphify 原生输出固定为 `graphify-out/`**——skill 里是硬编码字面量，CLI/skill 都**没有** `--out-dir` 参数（`--obsidian-dir` 只改 vault 子目录）。要按仓库分开存放（`graphify-out-pi` / `graphify-out-openclaw` 等），只能**跑完后手动 `mv`**。这也正是 `graphify-out-openclaw/` 的由来，以及 hermes-agent 的为什么还叫 `graphify-out/`（第一个，没移走）。

多仓库并存的标准流程（⚠️ 不先移走会覆盖上一个仓库的图谱）：
```bash
cd /Users/godccw/Developer/projects/project_wiki
mv graphify-out graphify-out-<上一个repo>     # 1) 先把当前图谱移走保护
# 2) 跑新仓库（在 Claude Code 里触发 skill）：  /graphify <newrepo> --mode deep
mv graphify-out graphify-out-<newrepo>          # 3) 重命名新结果
```

**查询时指定某个仓库的图谱（支持，用 `--graph` 指向具体 graph.json，不是目录名）：**
```bash
.venv/bin/graphify query "你的问题" --graph graphify-out-pi/graph.json
# 默认（不带 --graph）读 graphify-out/graph.json
```

## 6. 命令速查

| 目的 | 命令 |
|------|------|
| 查看子模块状态 | `git submodule status` |
| 全部拉到最新 | `git submodule update --remote` |
| 补拉/初始化 | `git submodule update --init --recursive` |
| 加新仓库 | `git submodule add <url> <name>` |
| 装依赖 | `uv pip install -e "./graphify[all]"` |
| 跑工具 | `uv run graphify ...` |
