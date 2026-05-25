# Multi-agent vs Subagent 模式对比

本文档详细对比 CrewAI 中两种 Agent 协作模式的区别。

---

## 一、架构对比

### Multi-agent 模式

```
    任务定义 (预先编排)
         │
         ▼
    ┌─────────┐    ┌─────────┐    ┌─────────┐
    │ Agent A │───▶│ Agent B │───▶│ Agent C │
    │ (研究员) │    │ (分析师) │    │ (撰稿人) │
    └─────────┘    └─────────┘    └─────────┘
         │              │              │
         └──────────────┴──────────────┘
                        │
                   最终输出
```

**特点：**
- 所有 Agent 地位平等
- 任务流程预先定义
- 适合固定工作流
- 每个 Agent 执行特定任务

### Subagent 模式

```
    用户请求
         │
         ▼
    ┌─────────────┐
    │   Manager   │◀─────────────────────────────┐
    │  (主 Agent) │                              │
    └──────┬──────┘                              │
           │ 任务分解                            │ 结果返回
           ├─────────────────┬─────────────────┐ │
           ▼                 ▼                 ▼ │
    ┌──────────┐      ┌──────────┐      ┌──────────┐
    │Subagent 1│      │Subagent 2│      │Subagent 3│
    │ (研究员) │      │ (分析师) │      │ (撰稿人) │
    └──────────┘      └──────────┘      └──────────┘
```

**特点：**
- Manager Agent 是核心控制者
- 任务动态分解和委派
- 适合复杂、不确定的任务
- Manager 负责协调和整合

---

## 二、核心区别

| 维度 | Multi-agent | Subagent |
|------|-------------|----------|
| **控制方式** | 外部编排器 (Crew) | 内部 Manager Agent |
| **Agent 地位** | 平等协作 | 层级关系 (主从) |
| **任务分配** | 预定义，静态 | 动态决策，按需委派 |
| **通信方式** | Agent 间可互相通信 | 只与 Manager 通信 |
| **灵活性** | 较低，需预先设计流程 | 高，可动态调整策略 |
| **可预测性** | 高，流程确定 | 较低，依赖 Manager 决策 |
| **错误处理** | 需要外部处理 | Manager 可动态调整 |
| **适用场景** | 固定工作流、流水线作业 | 复杂任务、需要决策的场景 |
| **Token 消耗** | 相对可控 | 可能较高 (Manager 决策) |
| **实现复杂度** | 简单 | 中等 |

---

## 三、代码实现对比

### Multi-agent 模式 - 预定义任务流程

```python
from crewai import Agent, Task, Crew, Process

# 定义 Agent
researcher = Agent(role="研究员", ...)
analyst = Agent(role="分析师", ...)
writer = Agent(role="撰稿人", ...)

# 预定义任务
task1 = Task(description="研究...", agent=researcher)
task2 = Task(description="分析...", agent=analyst, context=[task1])
task3 = Task(description="撰写...", agent=writer, context=[task2])

# 创建 Crew (外部编排器)
crew = Crew(
    agents=[researcher, analyst, writer],
    tasks=[task1, task2, task3],
    process=Process.sequential  # 顺序执行
)

result = crew.kickoff()
```

### Subagent 模式 - Manager 动态委派

```python
from crewai import Agent, Task, Crew, Process

# 定义 Manager Agent
manager = Agent(
    role="项目经理",
    allow_delegation=True,  # 允许委派
    ...
)

# 定义 Subagent
researcher = Agent(role="研究员", ...)
analyst = Agent(role="分析师", ...)
writer = Agent(role="撰稿人", ...)

# 只定义主任务，不预定义子任务
main_task = Task(
    description="完成综合报告...",
    agent=manager  # Manager 负责此任务
)

# 使用 hierarchical process
crew = Crew(
    agents=[manager, researcher, analyst, writer],
    tasks=[main_task],
    process=Process.hierarchical,  # 层级模式
    manager_llm=deepseek_llm
)

result = crew.kickoff()
```

---

## 四、执行流程对比

### Multi-agent 执行流程

```
用户输入: "研究RAG技术"
         │
         ▼
    ┌─────────────────────────────────────┐
    │ Crew 编排器                          │
    │ (按预定义顺序执行)                    │
    └─────────────────────────────────────┘
         │
         ▼
    Task 1: 研究员执行研究任务
         │
         ▼
    Task 2: 分析师执行分析任务 (依赖 Task 1)
         │
         ▼
    Task 3: 撰稿人执行写作任务 (依赖 Task 2)
         │
         ▼
    最终输出
```

### Subagent 执行流程

```
用户输入: "研究RAG技术"
         │
         ▼
    ┌─────────────────────────────────────┐
    │ Manager Agent                        │
    │ 1. 分析任务                          │
    │ 2. 决定需要哪些专家                   │
    │ 3. 动态创建子任务                     │
    └─────────────────────────────────────┘
         │
         ├──────────────────┬──────────────────┐
         ▼                  ▼                  ▼
    委派给研究员        委派给分析师        委派给撰稿人
    (研究任务)          (分析任务)          (写作任务)
         │                  │                  │
         └──────────────────┴──────────────────┘
                            │
                            ▼
                    Manager 整合结果
                            │
                            ▼
                       最终输出
```

---

## 五、选择建议

### 选择 Multi-agent 当：

- 任务流程固定、可预测
- 需要精确控制每个步骤
- Agent 之间有明确的依赖关系
- 需要并行执行多个独立任务
- 希望降低 Token 消耗
- **示例：** 数据处理流水线、内容生产流水线

### 选择 Subagent 当：

- 任务复杂，需要动态决策
- 无法预先确定需要哪些步骤
- 需要根据中间结果调整策略
- 需要一个"智能协调者"来管理流程
- 任务需要灵活的错误处理和重试
- **示例：** 复杂研究项目、多步骤决策任务、客户服务场景

---

## 六、示例文件

本目录下提供了完整的代码示例：

- [multi_agent.py](file:///c:/Users/Administrator/Desktop/test/trae_test/CrewAI/multi_agent.py) - Multi-agent 串行模式
- [multi_agent_parallel.py](file:///c:/Users/Administrator/Desktop/test/trae_test/CrewAI/multi_agent_parallel.py) - Multi-agent 并行模式
- [subagent_hierarchical.py](file:///c:/Users/Administrator/Desktop/test/trae_test/CrewAI/subagent_hierarchical.py) - Subagent 层级模式
