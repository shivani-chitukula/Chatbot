import streamlit as st
from dotenv import load_dotenv
import os

from utils.llm import generate_response_stream
from utils.memory import (
    init_memory,
    add_message,
    display_chat,
    get_last_user_message,
    replace_last_ai_message
)

load_dotenv()

# for tracing in LangSmith
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "chatbot-project"

st.title("Hey, how can I assist you today?")

st.sidebar.title("Settings")

#model selection
model_choice = st.sidebar.selectbox(
    "Select Model",
    ["Groq", "Ollama"]
)

temperature = st.sidebar.slider(
    "Temperature", 0.0, 1.0, 0.7,
    help="Controls randomness."
)

max_tokens = st.sidebar.slider(
    "Max Tokens", min_value=50, max_value=1000, value=300,
    help="Maximum length of the response."
)
role = st.sidebar.selectbox(
    "Assistant Role",
    ["Default", "Teacher", "Interviewer", "Code Expert"]
)


#initialising memory

init_memory()

if st.session_state.get("regenerate", False):
    last_input=get_last_user_message()

    if last_input:
        full_response=""

        for chunk in generate_response_stream(
            last_input,
            model_choice,
            temperature,
            max_tokens,
            st.session_state.chat_history,
            role
        ):
            full_response+=chunk

        replace_last_ai_message(full_response)

    st.session_state["regenerate"]=False
    st.rerun()


display_chat()

#user entry
user_input=st.chat_input("Ask something...")

if user_input:
    st.chat_message("user").write(user_input)
    add_message("user", user_input)

    response_placeholder=st.chat_message("assistant").empty()
    full_response=""

    #streaming response
    for chunk in generate_response_stream(
        user_input,
        model_choice,
        temperature,
        max_tokens,
        st.session_state.chat_history,
        role
    ):
        full_response+=chunk
        response_placeholder.write(full_response)

    add_message("ai", full_response)

#regenerate button
if st.session_state.chat_history and st.session_state.chat_history[-1][0]=="ai":
    if st.button("🔄 Regenerate"):
        st.session_state["regenerate"]=True
        st.rerun()