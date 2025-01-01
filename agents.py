# agents.py
from crewai import Agent
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from tools import tool
import os
import litellm

load_dotenv()

# Configure Groq with proper model name
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
llm = ChatGroq(
    model="groq/llama3-8b-8192",  # Using a valid Groq model
    temperature=0,
    verbose=True
)

# Research agent
researcher = Agent(
    role="Experienced Researcher",
    goal='Uncover ground breaking technologies in {topic}',
    memory=True,
    llm=llm,
    backstory=(
        "Driven by curiosity, you're at the forefront of innovation, eager to explore and share knowledge that could change the world."
    ),
    tools=[tool],
    allow_delegation=True
)

# Writer agent
writer = Agent(
    role="Article Writer",
    goal='Narrate compelling tech stories about {topic}',
    backstory=(
        "With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new discoveries to light in an accessible manner."
    ),
    tools=[tool],
    verbose=True,
    llm=llm,
    memory=True,
    allow_delegation=False
)
