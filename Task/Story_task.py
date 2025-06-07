from crewai import Task
from Agents.Story_agent import Story_agent


Story_task = Task(
    description="""
    User is a writer who wants to create a story. The story should be engaging and interactive, allowing the user to make choices that influence the direction of the narrative.
    The task is to create an initial story based on the user input and provide choices to continue the story. With respect to the user's choices, generate further story segments and choices.
    Based on User's {prompt}, create an initial story and provide choices to continue the story. With respect to the user's choices, generate further story segments and choices.
    Also after a choice use the {story} for previous context and generate the next part of the story with choices.
    
    Make sure to create a fast paced and engaging story that keeps the user interested.
    
    Choices are numbered and the user can choose a number to continue the story.

    
    """,
    expected_output="A story with choices for the user to continue the narrative. I dont want previous story to be repeated in the response. Only take the context of previous story",
    agent=Story_agent,
    input_variable="prompt",
)