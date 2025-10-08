from crewai import Agent
import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from tools import tool

load_dotenv()

# Base LLM
llm = OpenAI(
    model="gpt-3.5-turbo",
    openai_api_key=os.environ.get("OPENAI_API_KEY"),
    temperature=0.5,
    verbose=True
)

# Market Research Analyst
market_research_analyst = Agent(
    role="Market Research Analyst",
    goal="Provide insights about {company} through market analysis",
    verbose=True,
    memory=True,
    backstory="You are a Market Research Analyst conducting research on {company}. Gather and analyze market data, trends, and competitors.",
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Financial Analyst
financial_analyst = Agent(
    role="Financial Analyst",
    goal="Provide comprehensive financial insights about {company}",
    verbose=True,
    memory=True,
    backstory="You are a Financial Analyst analyzing financial data for {company}. Provide key ratios, trends, forecasts.",
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Reporting Analyst
reporting_analyst = Agent(
    role="Reporting Analyst",
    goal="Create detailed reports based on financial and market research for {company}",
    verbose=True,
    memory=True,
    backstory="You are a Reporting Analyst compiling data from Financial and Market Research Analysts into a comprehensive report.",
    tools=[tool],
    llm=llm,
    allow_delegation=False
)
