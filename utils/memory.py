import streamlit as st

def init_memory():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history=[]

def add_message(role, message):
    st.session_state.chat_history.append((role, message))

def display_chat():
    for role, message in st.session_state.chat_history:
        if role=="user":
            st.chat_message("user").write(message)
        else:
            st.chat_message("assistant").write(message)


def get_last_user_message():
    for role, msg in reversed(st.session_state.chat_history):
        if role=="user":
            return msg
    return None


def replace_last_ai_message(new_message):
    for i in range(len(st.session_state.chat_history) -1, -1, -1):
        role, _ =st.session_state.chat_history[i]
        if role=="ai":
            st.session_state.chat_history[i]=("ai", new_message)
            break