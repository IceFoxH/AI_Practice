# Oh-My-ClaudeCode (OMC) 使用指南

> 📅 生成日期：2026-05-29
> 🎯 适用版本：OMC v4.14.4
> 🤖 支持工具：Claude Code / Cursor / OpenClaw

---

## 一、OMC 简介

### 什么是 OMC？

**Oh-My-ClaudeCode**（简称 OMC）是一个为 Claude Code 打造的**多AI编排插件**，它将单个 Claude 转变为一个由 **32 个专业智能体**组成的协作团队。

### 核心价值

| 维度 | 原生 Claude Code | OMC 增强版 |
|------|-----------------|-----------|
| **执行效率** | 串行执行 | 3-5× 更快（并行处理） |
| **Token 消耗** | 全量使用 Opus | 节省 30-50%（智能路由） |
| **任务可靠性** | 中途崩溃需重跑 | 自动恢复（Ralph 模式） |
| **协作能力** | 单模型单打独斗 | 32 个专业智能体协作 |

### 核心理念

> **不用学 Claude Code，直接用 OMC 就行。**
> 
> 你只需描述需求，OMC 自动选择合适的智能体和执行模式。

---

## 二、安装与配置

### 安装方式

#### 方式一：插件市场安装（推荐）
```bash
# 在 Claude Code 中运行：
/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode
/plugin install oh-my-claudecode
```

#### 方式二：npm 全局安装
```bash
npm install -g oh-my-claude-sisyphus@4.14.4
```

#### 方式三：手动安装
```bash
git clone https://github.com/Yeachan-Heo/oh-my-claudecode.git
cd oh-my-claudecode
npm install
```

### 初始化配置
```bash
# 运行设置向导（只需一次）
/omc-setup
```

---

## 三、核心执行模式

OMC 提供 **6 种执行模式**，自动或手动选择最合适的方式完成任务。

### 1. Autopilot（全自动模式）

| 项目 | 说明 |
|------|------|
| **作用** | 端到端全自动执行，从需求到代码 |
| **触发方式** | `autopilot` 关键词或 `/autopilot` 命令 |
| **工作流程** | Architect 规划 → Executor 构建 → QA 测试 → Reviewer 审查 |
| **适用场景** | 完整功能开发、中等复杂度任务 |

**示例：**
```bash
# 方式一：关键词触发
autopilot build a todo app with JWT auth

# 方式二：命令触发
/autopilot "build a payment checkout flow"
```

**特点**：
- ✅ 全自主执行，无需干预
- ✅ 阶段化流水线
- ✅ 完成前自动验证

---

### 2. Ralph（持久模式）

| 项目 | 说明 |
|------|------|
| **作用** | 不达目的不罢休，持续迭代直到完成 |
| **触发方式** | `ralph` 关键词或 `/ralph` 命令 |
| **工作流程** | 规划 → 执行 → 验证 → 循环（最多100次） |
| **适用场景** | 难搞的 bug、高风险重构、必须完成的任务 |

**示例：**
```bash
# 方式一：关键词触发
ralph refactor auth module to JWT with zero downtime

# 方式二：命令触发
/ralph "fix the memory leak in the video player"
```

**特点**：
- ✅ 中断自动恢复
- ✅ 架构师验证签核
- ✅ 最多循环 100 次（可配置）
- ✅ 永不放弃

---

### 3. Ultrawork（最大并行）

| 项目 | 说明 |
|------|------|
| **作用** | 最大并行度执行，多任务同时处理 |
| **触发方式** | `ulw` 或 `ultrawork` 关键词 |
| **工作流程** | 任务拆分 → 并行执行 → 结果合并 |
| **适用场景** | 全栈功能开发、大规模重构、多文件修改 |

**示例：**
```bash
# 方式一：简写关键词
ulw build fullstack SaaS with Stripe + Postgres

# 方式二：完整关键词
ultrawork "fix all TypeScript errors in /src"
```

**特点**：
- ✅ 3-5 个智能体并行工作
- ✅ 文件所有权分区管理
- ✅ 完成后自动合并

---

### 4. Team（团队模式）

| 项目 | 说明 |
|------|------|
| **作用** | N 个智能体共享任务列表协作 |
| **触发方式** | `team` 关键词或 `/team` 命令 |
| **工作流程** | team-plan → team-prd → team-exec → team-verify |
| **适用场景** | 需要多角色协作的复杂任务 |

**示例：**
```bash
# 指定智能体数量
/team 3:executor "implement user management module"

# 三模型并行审查
/ccg "review this PR thoroughly"
```

**特点**：
- ✅ 原子任务认领
- ✅ 智能体间实时通信
- ✅ 结果合成

---

### 5. Deep Interview（深度访谈）

| 项目 | 说明 |
|------|------|
| **作用** | 苏格拉底式提问，澄清模糊需求 |
| **触发方式** | `deep interview` 关键词 |
| **工作流程** | 提问 → 回答 → 追问 → 明确需求 |
| **适用场景** | 需求不明确、模糊的任务 |

**示例：**
```bash
deep interview "build a better search feature"
```

**特点**：
- ✅ 暴露隐藏假设
- ✅ 衡量需求清晰度
- ✅ 避免返工

---

### 6. Planning（规划模式）

| 项目 | 说明 |
|------|------|
| **作用** | 战略访谈式规划工作流 |
| **触发方式** | `plan` 关键词或 Shift+Tab |
| **工作流程** | Recon → Interview → Research → Gap Analysis → Risk Pass → Write Plan → Critic Review |
| **适用场景** | 复杂任务、大型功能开发前规划 |

**示例：**
```bash
plan "design a microservices architecture"
```

**特点**：
- ✅ 7 步结构化规划
- ✅ 风险评估
- ✅ 批评审查

---

## 四、32 个专业智能体

OMC 内置 **32 个专业智能体**，自动匹配任务需求。

### 分析类智能体

| 智能体 | 职责 | 适用场景 |
|--------|------|---------|
| **architect** | 架构设计与规划 | 系统设计、技术选型 |
| **debugger** | 调试与问题定位 | bug 排查、性能分析 |
| **verifier** | 验证与质量保证 | 测试验证、结果确认 |

### 执行类智能体

| 智能体 | 职责 | 适用场景 |
|--------|------|---------|
| **executor** | 代码实现 | 功能开发、bug 修复 |
| **build-fixer** | 构建修复 | CI/CD 失败修复 |

### 搜索与研究类智能体

| 智能体 | 职责 | 适用场景 |
|--------|------|---------|
| **explore** | 代码库探索 | 查找文件、理解代码结构 |
| **librarian** | 文档与资料查阅 | API 文档、最佳实践 |

### 审查类智能体

| 智能体 | 职责 | 适用场景 |
|--------|------|---------|
| **code-reviewer** | 代码审查 | 代码质量、规范检查 |
| **security-reviewer** | 安全审查 | 安全漏洞、合规检查 |
| **qa-tester** | 测试工程师 | 编写测试、验证功能 |

### 设计类智能体

| 智能体 | 职责 | 适用场景 |
|--------|------|---------|
| **designer** | UI/UX 设计 | 界面设计、用户体验 |

---

## 五、MCP 工具集成

OMC 内置多种强大工具：

### 代码分析工具

| 工具 | 功能 | 示例用法 |
|------|------|---------|
| **LSP Integration** | 语言服务协议 | 悬停信息、跳转定义、查找引用 |
| **AST Grep** | 结构化代码搜索替换 | 按语法模式查找，非文本匹配 |
| **Python REPL** | 持久化 Python 环境 | 数据分析、计算、可视化 |

### 状态管理工具

| 工具 | 功能 | 说明 |
|------|------|------|
| **Notepad** | 临时笔记 | 记录想法、待办事项 |
| **Project Memory** | 项目级记忆 | 跨会话持久化 |
| **Session State** | 会话状态 | 保持上下文 |

---

## 六、魔法关键词

只需说出关键词，OMC 自动激活对应模式：

| 关键词 | 效果 | 示例 |
|--------|------|------|
| `auto` | 触发 Autopilot 模式 | `auto build login page` |
| `autopilot` | 全自动执行 | `autopilot create CRUD API` |
| `ralph` | 持久模式 | `ralph fix memory leak` |
| `ulw` | 最大并行 | `ulw migrate database` |
| `ultrawork` | 最大并行（完整） | `ultrawork refactor frontend` |
| `team` | 团队模式 | `team implement feature` |
| `plan` | 规划模式 | `plan design architecture` |
| `ralplan` | 迭代规划共识 | `ralplan redesign payment flow` |

---

## 七、常用命令速查

### 核心命令

| 命令 | 功能 |
|------|------|
| `/omc-setup` | 初始化配置 |
| `/autopilot <prompt>` | 全自动执行 |
| `/ralph <prompt>` | 持久模式执行 |
| `/ultrawork <prompt>` | 最大并行执行 |
| `/team <n>:<agent> <prompt>` | 指定智能体执行 |
| `/ccg <prompt>` | 三模型并行审查 |

### 管理命令

| 命令 | 功能 |
|------|------|
| `/cancel-work` | 取消当前任务 |
| `/check` | 检查任务状态 |
| `/deepwork` | 深度工作循环 |
| `/explore` | 代码库探索 |
| `/librarian` | 文档查阅 |

### 跨模型命令

| 命令 | 功能 |
|------|------|
| `/omc-teams 2:codex <prompt>` | Codex 智能体执行 |
| `/omc-teams 2:gemini <prompt>` | Gemini 智能体执行 |

---

## 八、工作流程示例

### 示例 1：探索新代码库

```bash
# 1. 探索代码库结构
/explore "find auth-related files"

# 2. 查阅相关文档
/librarian "read the main authentication module"

# 3. 生成架构图
/plan "understand the auth flow"

# 结果：快速了解代码库，不污染上下文窗口
```

### 示例 2：实现完整功能

```bash
# 方式一：使用 Autopilot
autopilot "build a user dashboard with charts and filters"

# 方式二：使用 Team 模式
/team 4:executor "implement user dashboard"

# 执行流程：
# 1. Architect → 设计方案
# 2. Executor → 编写代码
# 3. QA → 编写测试
# 4. Reviewer → 代码审查
```

### 示例 3：调试困难问题

```bash
# 使用 Ralph 模式
ralph "fix the race condition in WebSocket handler"

# 使用 UltraDebug 关键词
ultradebug "investigate why the cache is not invalidating"
```

---

## 九、智能模型路由（MSE）

OMC 的 **MSE（Model-Smart-Economy）** 系统自动选择最优模型：

| 任务类型 | 自动选择模型 | 原因 |
|----------|-------------|------|
| **简单任务** | Haiku | 快速、便宜 |
| **中等任务** | Sonnet | 平衡速度与质量 |
| **复杂任务** | Opus | 深度推理、质量优先 |
| **代码审查** | Codex | 专业代码分析 |
| **UI 设计** | Gemini | 创意设计能力 |

**效果**：Token 消耗降低 **30-50%**

---

## 十、HUD 状态栏

OMC 在底部显示实时状态：

```
[OMC] Agents: 3 | Tokens: 1.2k | Mode: Team | Progress: 67%
```

| 指标 | 说明 |
|------|------|
| **Agents** | 当前活跃智能体数量 |
| **Tokens** | 本次会话消耗 |
| **Mode** | 当前执行模式 |
| **Progress** | 任务进度 |

---

## 十一、最佳实践

### 1. 选择合适的模式
- 简单任务 → `auto` 或直接描述
- 复杂功能 → `autopilot` 或 `team`
- 必须完成 → `ralph`
- 大规模 → `ulw`

### 2. 保持上下文干净
- 让子智能体处理文件读取、搜索
- 主会话只看结论，不看原始文件

### 3. 利用魔法关键词
- 无需记住命令，用自然语言关键词即可
- 如：`ralph fix this bug` 比 `/ralph "fix this bug"` 更自然

### 4. 验证后再确认
- OMC 自动验证，但重要任务建议手动确认
- 使用 `/check` 命令检查状态

---

## 十二、配置与自定义

### 配置文件位置
```
.claude/omc/config.yaml
```

### 主要配置项

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| `maxAgents` | 5 | 最大并行智能体数 |
| `maxRetries` | 100 | Ralph 模式最大循环次数 |
| `modelRouting` | true | 启用智能模型路由 |
| `hudEnabled` | true | 显示 HUD 状态栏 |

### 自定义智能体
```yaml
# 在 config.yaml 中添加自定义智能体
customAgents:
  - name: my-specialist
    description: "My custom specialist"
    model: opus
    skills: ["analysis", "design"]
```

---

## 十三、常见问题

### Q1：OMC 和 superpowers-zh 有什么区别？

| 维度 | OMC | superpowers-zh |
|------|-----|---------------|
| **定位** | 多AI编排引擎 | 工作方法论技能集 |
| **核心** | 智能体协作、并行执行 | 开发流程、质量保证 |
| **触发方式** | 魔法关键词 | 自动/手动触发 |
| **适合** | 复杂任务、大规模开发 | 规范流程、代码质量 |

**建议**：两者可以互补使用！

### Q2：如何节省 Token？

- ✅ 启用 MSE 智能路由
- ✅ 使用 `ulw` 并行处理，减少等待时间
- ✅ 让子智能体处理简单任务
- ✅ 利用经验复用机制

### Q3：任务卡住了怎么办？

- 使用 `/cancel-work` 取消任务
- 改用 `ralph` 模式重新执行
- 检查网络连接和 API 配额

---

## 十四、相关资源

- 📦 **GitHub**: https://github.com/Yeachan-Heo/oh-my-claudecode
- 📖 **官方文档**: https://oh-my-claudecode.dev/
- 🛠️ **插件市场**: Claude Code Plugin Marketplace
- 📊 **Changelog**: https://github.com/Yeachan-Heo/oh-my-claudecode/blob/main/CHANGELOG.md

---

> 💡 **提示**: OMC 是一个不断进化的项目，建议定期更新到最新版本以获取最新功能和优化。
