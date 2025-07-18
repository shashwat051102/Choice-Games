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

Story_agent = Agent(
    role="Story_agent",
    goal="""Create a initial story based on the user {prompt} and give choices to continue the story and with respect to use choices generate further story and choices.
    Also after a choice use the {story} for previous context and generate the next part of the story with choices.
    Make sure to create a fast paced and engaging story that keeps the user interested.
    Choices are numbered and the user can choose a number to continue the story.

    """,
    llm=llm,
    backstory="User is a writer who wants to create a story. The story should be engaging and interactive, allowing the user to make choices that influence the direction of the narrative.",
    memory=None,
    verbose=True,
)