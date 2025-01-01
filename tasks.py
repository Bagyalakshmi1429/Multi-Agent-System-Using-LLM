from crewai import Task
from tools import tool
from agents import researcher, writer

researchtask = Task(
    description=(
        "Research the latest developments and current state of {topic}. "
        "Analyze key trends, scientific evidence, and expert opinions. "
        "Identify the most significant impacts and future implications. "
        "Focus on verifiable facts and credible sources."
    ),
    expected_output='A comprehensive research summary with key findings, trends, and expert insights, including source citations.',
    tools=[tool],
    agent=researcher
)

writertask = Task(
    description=(
        "Create an engaging and informative article about {topic} based on the research provided. "
        "Structure the content logically, use clear language, and maintain reader engagement. "
        "Include relevant examples and expert perspectives while ensuring accuracy."
    ),
    expected_output='A well-structured, engaging article that effectively communicates the key findings to a general audience.',
    tools=[tool],
    agent=writer,
    async_execution=False,
    output_file='article.md'
)
