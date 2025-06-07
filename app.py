import patch_sqlite
import streamlit as st
from Agents.Story_agent import Story_agent
from Task.Story_task import Story_task
from crewai import Crew

# Set page configuration
st.set_page_config(
    page_title="Choice Based Game",
    page_icon="🎮",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .chat-card {
        background: #23272f;
        box-shadow: 0 2px 8px rgba(0,0,0,0.25);
        border-radius: 12px;
        padding: 1rem 1.5rem;
        margin-bottom: 1.2rem;
        display: flex;
        align-items: flex-start;
        gap: 1rem;
    }
    .avatar {
        width: 38px;
        height: 38px;
        border-radius: 50%;
        background: #353b48;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.3rem;
        font-weight: bold;
        color: #7ecfff;
    }
    .chat-content {
        flex: 1;
        font-size: 1.1rem;
        line-height: 1.6;
        color: #e6e6e6;
    }
    .title-text {
        font-size: 2.5rem;
        font-weight: bold;
        color: #7ecfff;
        text-align: center;
        margin-bottom: 2rem;
        letter-spacing: 1px;
        text-shadow: 0 2px 8px #000a;
    }
    .sidebar-box {
        background: #23272f;
        border-radius: 10px;
        padding: 1.2rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 1px 4px rgba(0,0,0,0.25);
        color: #e6e6e6;
    }
    .sidebar-box b {
        color: #7ecfff;
    }
    </style>
    """, unsafe_allow_html=True)

# Title with custom styling
st.markdown('<h1 class="title-text">Choice Based Game</h1>', unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "story" not in st.session_state:
    st.session_state.story = ""

# Create two columns for better layout
col1, col2 = st.columns([2, 1])

with col1:
    # Main chat area
    st.markdown("### Story Progress")
    for msg in st.session_state.messages:
        avatar = "🧑" if msg["role"] == "user" else "🤖"
        st.markdown(
            f"""
            <div class="chat-card">
                <div class="avatar">{avatar}</div>
                <div class="chat-content">{msg["content"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

with col2:
    st.markdown('<div class="sidebar-box"><b>Game Information</b><br>Welcome to the Choice Based Game! Enter your story prompt to begin your adventure.</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-box">To continue the story, please copy and paste one of the choices provided in the story into the chat input below.</div>', unsafe_allow_html=True)
    if st.session_state.story:
        with st.expander("View Full Story"):
            st.markdown(st.session_state.story)


# Chat input at the bottom
if prompt := st.chat_input("Enter your story choice or prompt..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(
        f"""
        <div class="chat-card">
            <div class="avatar">🧑</div>
            <div class="chat-content">{prompt}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            crew_instance = Crew(
                agents=[Story_agent],
                tasks=[Story_task],
                verbose=True,
            )
            messages = [
                {"role": msg["role"], "content": str(msg["content"])}
                for msg in st.session_state.messages
            ]
            response = crew_instance.kickoff(
                {"prompt": prompt, "story": st.session_state.story, "messages": messages},
            )
            if not isinstance(response, str):
                response = str(response)

            st.markdown(
                f"""
                <div class="chat-card">
                    <div class="avatar">🤖</div>
                    <div class="chat-content">{response}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.session_state.story += response
            st.session_state.messages.append({"role": "assistant", "content": response})
