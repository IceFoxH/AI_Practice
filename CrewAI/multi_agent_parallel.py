import os
from crewai import Agent, Task, Crew, LLM, Process

# 配置 DeepSeek API (从环境变量读取，请勿直接硬编码)
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")

# 创建 DeepSeek LLM 实例
deepseek_llm = LLM(
    model="deepseek/deepseek-v4-pro",
    base_url="https://api.deepseek.com",
    api_key=DEEPSEEK_API_KEY,
    temperature=0.7,
)

# 定义多个专家 Agent（并行工作）
researcher1 = Agent(
    role="RAG技术专家",
    goal="研究RAG技术的核心原理和架构",
    backstory="你是一位RAG技术领域的专家，精通检索增强生成技术",
    llm=deepseek_llm,
)

researcher2 = Agent(
    role="AI行业分析师",
    goal="分析AI行业的最新趋势和市场动态",
    backstory="你是一位资深AI行业分析师，对市场趋势有敏锐的洞察力",
    llm=deepseek_llm,
)

researcher3 = Agent(
    role="技术架构师",
    goal="评估技术实现方案和最佳实践",
    backstory="你是一位经验丰富的技术架构师，擅长技术方案评估",
    llm=deepseek_llm,
)

summarizer = Agent(
    role="报告汇总专家",
    goal="汇总所有研究结果，生成综合报告",
    backstory="你是一位擅长整合信息、撰写综合报告的专家",
    llm=deepseek_llm,
)

# 定义并行任务（无依赖关系）
task1 = Task(
    description="研究2026年RAG技术的核心原理、架构演进和关键技术突破",
    expected_output="RAG技术核心原理和架构分析报告",
    agent=researcher1,
)

task2 = Task(
    description="分析2026年AI行业的最新趋势、主要玩家和市场机会",
    expected_output="AI行业趋势分析报告",
    agent=researcher2,
)

task3 = Task(
    description="评估RAG技术在企业应用中的最佳实践和实施建议",
    expected_output="RAG技术最佳实践评估报告",
    agent=researcher3,
)

# 汇总任务（依赖于前三个任务的完成）
summary_task = Task(
    description="汇总以上三份报告，生成一份综合的RAG技术研究报告，包括核心技术、行业趋势和实施建议",
    expected_output="一份完整的综合研究报告，包含执行摘要、核心发现和建议",
    agent=summarizer,
    # 指定依赖关系（等待所有并行任务完成）
    context=[task1, task2, task3]
)

# 创建 Crew，使用并行执行模式
crew = Crew(
    agents=[researcher1, researcher2, researcher3, summarizer],
    tasks=[task1, task2, task3, summary_task],
    process=Process.parallel,  # 真正的并行执行：task1/task2/task3 同时运行
    verbose=True
)

# 运行
result = crew.kickoff()
print(result)
