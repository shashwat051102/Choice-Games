from crewai import Agent
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
import openai

import os

load_dotenv()
# api_key = os.getenv("GROQ_API_KEY")
# llm = ChatGroq(api_key=api_key, model="groq/llama-3.3-70b-versatile")

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key not found in environment variables.")

openai.api_key = api_key
llm = ChatOpenAI(api_key=api_key, model="gpt-4.1-mini")

summary_agent = Agent(
    role="Summary_agent",
    goal="Summarize the story based on the user {prompt} and provide a concise overview of the narrative.",
    llm=llm,
    backstory="User is a writer who wants to create a story. The story should be engaging and interactive, allowing the user to make choices that influence the direction of the narrative.",
    memory=None,
    verbose=True,
)