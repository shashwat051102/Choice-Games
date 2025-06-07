import streamlit as st
from Agents.Story_agent import Story_agent
from Task.Story_task import Story_task
from crewai import Crew


st.title("Choice BAsed Game")

# Initialize messages in session state if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

if prompt:= st.chat_input("Enter the initial story"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    
    with st.chat_message("assistant"):
        crew_instance = Crew(
            agents=[Story_agent],
            tasks=[Story_task],
            verbose=True,
        )
        # Only pass lists of dicts with str values for messages
        messages = [
            {"role": msg["role"], "content": str(msg["content"])}
            for msg in st.session_state.messages
        ]
        response = crew_instance.kickoff(
            {"prompt": prompt, "messages": messages},
        )
        # Ensure response is a string before displaying and storing
        if not isinstance(response, str):
            response = str(response)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})