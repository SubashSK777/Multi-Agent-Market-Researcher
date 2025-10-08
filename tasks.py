from crewai import Task
from tools import tool
from agents import financial_analyst, market_research_analyst, reporting_analyst

# Financial Analysis Task
financial_analysis = Task(
    description="Analyze the financial performance of {company}",
    expected_output="A detailed financial report including key financial ratios, trends, and forecasts",
    tools=[tool],
    agent=financial_analyst,
)

# Market Analysis Task
market_analysis = Task(
    description="Analyze market trends and competitive landscape for {company}",
    expected_output="A comprehensive market research report detailing market trends, consumer behavior, and competitive analysis",
    tools=[tool],
    agent=market_research_analyst,
)

# Reporting Task
reporting_analysis = Task(
    description="Compile and synthesize data from financial and market research analysts into a comprehensive report",
    expected_output="A detailed report that combines financial performance analysis with market trends and competitive analysis for {company}",
    tools=[tool],
    agent=reporting_analyst,
    async_execution=False
)
