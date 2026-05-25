"""
Subagent 模式示例 - 层级式 Agent 协作

与 Multi-agent 模式的区别：
┌─────────────────────────────────────────────────────────────────────────────┐
│                         Multi-agent 模式 (CrewAI)                           │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌─────────┐    ┌─────────┐    ┌─────────┐                                  │
│  │ Agent 1 │───▶│ Agent 2 │───▶│ Agent 3 │  (平等协作，任务驱动)            │
│  └─────────┘    └─────────┘    └─────────┘                                  │
│       │              │              │                                        │
│       └──────────────┴──────────────┘                                        │
│                      │                                                       │
│               Crew 编排器                                                    │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                         Subagent 模式 (Hierarchical)                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                      ┌─────────────┐                                        │
│                      │ Manager     │                                        │
│                      │ (主 Agent)  │                                        │
│                      └──────┬──────┘                                        │
│                             │ 任务委派                                       │
│              ┌──────────────┼──────────────┐                                │
│              ▼              ▼              ▼                                │
│       ┌──────────┐  ┌──────────┐  ┌──────────┐                              │
│       │Subagent 1│  │Subagent 2│  │Subagent 3│  (层级结构，主从关系)        │
│       └──────────┘  └──────────┘  └──────────┘                              │
│              │              │              │                                │
│              └──────────────┴──────────────┘                                │
│                      │ 返回结果                                              │
│                      ▼                                                       │
│               Manager 汇总                                                   │
└─────────────────────────────────────────────────────────────────────────────┘

核心区别：
1. 控制流：Multi-agent 由 Crew 编排，Subagent 由 Manager 动态决策
2. 灵活性：Subagent 可以根据任务动态选择调用哪个子 Agent
3. 责任：Manager Agent 负责任务分解、委派和结果整合
4. 通信：Subagent 模式中，子 Agent 只与 Manager 通信
"""

import os
from crewai import Agent, Task, Crew, LLM, Process

DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")

deepseek_llm = LLM(
    model="deepseek/deepseek-v4-pro",
    base_url="https://api.deepseek.com",
    api_key=DEEPSEEK_API_KEY,
    temperature=0.7,
)

manager = Agent(
    role="项目经理",
    goal="协调子 Agent 完成复杂任务，分解任务、委派工作、整合结果",
    backstory="""你是一位经验丰富的项目经理，擅长：
    1. 分析复杂任务并分解为可执行的子任务
    2. 根据子任务性质选择合适的专家
    3. 整合各专家的输出形成最终答案
    你不会亲自执行具体研究，而是委派给合适的专家。""",
    llm=deepseek_llm,
    allow_delegation=True,
)

researcher = Agent(
    role="研究员",
    goal="深入研究指定主题，提供详实的研究报告",
    backstory="你是一位专注的研究员，擅长收集信息、分析数据、撰写研究报告。",
    llm=deepseek_llm,
)

analyst = Agent(
    role="数据分析师",
    goal="分析数据，提供洞察和建议",
    backstory="你是一位数据分析师，擅长从数据中发现趋势和模式。",
    llm=deepseek_llm,
)

writer = Agent(
    role="技术撰稿人",
    goal="将复杂信息转化为清晰易懂的文章",
    backstory="你是一位技术撰稿人，擅长将专业内容转化为通俗易懂的文章。",
    llm=deepseek_llm,
)

main_task = Task(
    description="""
    请完成以下综合性任务：生成一份关于"2026年RAG技术发展"的完整报告。
    
    你需要：
    1. 委派研究员深入研究RAG技术的最新进展
    2. 委派分析师分析行业趋势和市场数据
    3. 委派撰稿人将研究结果整合成最终报告
    
    作为经理，你需要协调这些专家的工作，确保最终输出是一份完整、连贯的报告。
    """,
    expected_output="一份关于2026年RAG技术发展的完整综合报告，包含技术分析、行业趋势和未来展望",
    agent=manager,
)

crew = Crew(
    agents=[manager, researcher, analyst, writer],
    tasks=[main_task],
    process=Process.hierarchical,
    manager_llm=deepseek_llm,
    verbose=True,
)

print("=" * 60)
print("Subagent 模式 (Hierarchical Process)")
print("=" * 60)
print("\n工作流程：")
print("1. Manager Agent 接收主任务")
print("2. Manager 动态分解任务并委派给合适的 Subagent")
print("3. Subagent 执行任务并返回结果")
print("4. Manager 整合所有结果生成最终输出")
print("\n" + "=" * 60 + "\n")

result = crew.kickoff()
print("\n" + "=" * 60)
print("最终结果：")
print("=" * 60)
print(result)
