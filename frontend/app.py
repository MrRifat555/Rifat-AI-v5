import streamlit as st
from backend.ai.chat import ask_ai

st.set_page_config(
    page_title="Rifat AI v7",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Rifat AI v7")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Ask anything...")

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    reply = ask_ai(prompt)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":reply
        }
    )

    with st.chat_message("assistant"):
        st.write(reply)
