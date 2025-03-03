import os
import sys
from crewai import Agent, Task
from dotenv import load_dotenv
from crewai import Crew, Process, LLM
from langchain_openai import AzureChatOpenAI

load_dotenv()

## Azure LLM Declaration (GPT-4o)
azure_llm = LLM(
    api_version=os.environ.get("OPENAI_API_VERSION"),
    model="azure/gpt-4o",
)

## Research Agent
researcher = Agent(
  role='Senior Researcher',
  goal='Discover groundbreaking technologies',
  verbose=True,
  llm=default_llm,
  backstory='A curious mind fascinated by cutting-edge innovation and the potential to change the world, you know everything about tech.'
)

## Tak for the researcher
research_task = Task(
  description='Identify the next big trend in AI',
  expected_output='5 paragraphs on the next big AI trend',
  agent=researcher  
)

## Crew 
tech_crew = Crew(
  agents=[researcher],
  tasks=[research_task],
  process=Process.sequential  # Tasks will be executed one after the other
)

# Begin the task execution
tech_crew.kickoff()
