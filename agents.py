# Developing multi agent system for writing an news article

# from crewai import Agent # For creating agents
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI # For accessing gemini 
# from langchain_groq import ChatGroq
# from tools import tool
# import os

# load_dotenv()

# # Calling the gemini models

# os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# # llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",verbose=True, temperature=0)
# groqllm = ChatGroq(model='llama3-8b-8192',temperature=0,verbose=True)

# # Developing a research agent that is responsible to communicate with all the agents to write a blog or article

# researcher = Agent(
#     role="Experienced Researcher",
#     goal= 'Uncover ground breaking technologies in {topic}',
#     memory=True,
#     llm=groqllm,
#     backstory=(
#         "Driven by curiosity, you're at the forefront of innovation, eager to explore and share knowledge that could change the world."
#     ),
#     tools = [tool], # Google Serper Tool
#     allow_delegation=True # This parameter allows the agent to collaborate with other agents
# )

# # Developing writer agent

# writer = Agent(
#     role="Article Writer", # Defining role
#     goal='Narrate compelling tech stories about {topic}', # Defining goal
#     backstory=(
#         "With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new    discoveries to light in an accessible manner."),  # Backstory
#     tools=[tool], # Calling the serper tool
#     verbose=True,
#     llm=groqllm,
#     memory=True,
#     allow_delegation=False # Not Required 
# )

# Non 2024 - Contract Manufacturers in Sauces and Condiments

# from crewai import Agent
# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_groq import ChatGroq
# from tools import tool
# import os

# load_dotenv()

# os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
# os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# # Using Groq LLM for contract manufacturing research
# groqllm = ChatGroq(model='llama3-70b-8192', temperature=0, verbose=True)

# # Research Agent for identifying potential contract manufacturers in food industry
# researcher = Agent(
#     role="Food Industry Market Researcher",
#     goal='Identify and analyze potential contract manufacturers for sauces and condiments near Bangalore and Hosur',
#     memory=True,
#     llm=groqllm,
#     backstory=(
#         "With deep expertise in food manufacturing supply chains, you're skilled at uncovering hidden gems in the contract manufacturing landscape. "
#         "Your mission is to find manufacturers with advanced food science capabilities and regional proximity."
#     ),
#     tools=[tool],
#     allow_delegation=True
# )

# # Writer Agent for documenting research findings
# writer = Agent(
#     role="Technical Report Writer", 
#     goal='Create a comprehensive report on potential contract manufacturers for sauce production', 
#     backstory=(
#         "Specializing in technical writing for food industry procurement, you transform complex research into clear, actionable insights. "
#         "Your reports bridge the gap between technical details and strategic decision-making."
#     ),
#     tools=[tool],
#     verbose=True,
#     llm=groqllm,
#     memory=True,
#     allow_delegation=False
# )

# 2024 - Contract Manufacturers in Sauces and Condiments

from crewai import Agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from tools import tool
import os

load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# Using Groq LLM for 2024 contract manufacturing research
groqllm = ChatGroq(model='llama3-8b-8192', temperature=0.3, verbose=True)

# Research Agent for identifying 2024 contract manufacturers
researcher = Agent(
    role="Food Industry Market Intelligence Specialist",
    goal='Conduct comprehensive research on contract manufacturers for sauces and condiments, focusing on Bangalore and Hosur regions',
    memory=True,
    llm=groqllm,
    backstory=(
        "As a cutting-edge market researcher specializing in food manufacturing"
        "you are dedicated to uncovering the most up-to-date and innovative contract manufacturers. "
        "Your expertise lies in identifying companies with advanced food science capabilities "
        "and current technological trends in sauce and condiment production."
    ),
    tools=[tool],
    allow_delegation=True
)

# Verification Agent to cross-check research findings
verifier = Agent(
    role="Industry Verification Specialist",
    goal='Validate and cross-reference the research findings for accuracy and current relevance',
    llm=groqllm,
    backstory=(
        "A meticulous professional with deep connections in the food manufacturing industry, "
        "you specialize in verifying and validating market research, ensuring only the most "
        "current and accurate information is presented."
    ),
    tools=[tool],
    allow_delegation=False
)

# Writer Agent for documenting research findings
writer = Agent(
    role="Industry Insights Compiler", 
    goal='Create a comprehensive, data-driven report on contract manufacturers for sauce production in 2024', 
    backstory=(
        "An expert technical writer who transforms complex market research into clear, "
        "actionable insights. Your reports capture the current landscape of food manufacturing, "
        "highlighting 2024's most promising contract manufacturing opportunities."
    ),
    tools=[tool],
    llm=groqllm,
    memory=True,
    allow_delegation=False
)