from crewai import Task
from Agents.Story_agent import Story_agent


Story_task = Task(
    description="""
    User is a writer who wants to create a story. The story should be engaging and interactive, allowing the user to make choices that influence the direction of the narrative.
    The task is to create an initial story based on the user input and provide choices to continue the story. With respect to the user's choices, generate further story segments and choices.
    Based on User's {prompt}, create an initial story and provide choices to continue the story. With respect to the user's choices, generate further story segments and choices.
    
    
    """,
    expected_output="A story with choices for the user to continue the narrative.",
    agent=Story_agent,
    input_variable="prompt",
)