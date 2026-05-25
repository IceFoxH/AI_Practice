import os
from crewai import Agent, Task, Crew, LLM

# 配置 DeepSeek API (从环境变量读取，请勿直接硬编码)
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")

# 创建 DeepSeek LLM 实例
deepseek_llm = LLM(
    model="deepseek/deepseek-v4-pro",
    base_url="https://api.deepseek.com",
    api_key=DEEPSEEK_API_KEY,
    temperature=0.7,
)

# 定义两个 Agent，使用 DeepSeek LLM
researcher = Agent(
    role="研究员",
    goal="研究指定主题的最新进展",
    backstory="你是一位资深 AI 研究员",
    llm=deepseek_llm,
)

writer = Agent(
    role="撰稿人",
    goal="将研究结果写成简洁的文章",
    backstory="你是一位擅长科技写作的撰稿人",
    llm=deepseek_llm,
)

# 定义任务（必须包含 expected_output 字段）
research_task = Task(
    description="研究 2026 年 RAG 技术的最新进展",
    expected_output="一份关于 2026 年 RAG 技术最新进展的研究报告，包含关键技术趋势、主要工具和公司、以及行业影响分析",
    agent=researcher,
)

write_task = Task(
    description="基于研究结果，写一篇 500 字的技术摘要",
    expected_output="一篇约 500 字的技术摘要文章，语言简洁明了，适合技术人员阅读",
    agent=writer,
)

# 组建 Crew 并运行
crew = Crew(agents=[researcher, writer], tasks=[research_task, write_task])
result = crew.kickoff()
print(result)
