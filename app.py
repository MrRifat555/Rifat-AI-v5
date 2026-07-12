from memory import get_memory, set_memory
import streamlit as st
from ai import ask_ai
from memory import get_memory, set_memory

# ==========================
# Page Config
# ==========================

st.set_page_config(
    page_title="🤖 Rifat AI v5",
    page_icon="🤖",
    layout="wide"
)

# ==========================
# Sidebar
# ==========================

with st.sidebar:

    st.title("🤖 Rifat AI")

    st.write("Version 5.0")

    st.divider()

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# ==========================
# Session
# ==========================

if "messages" not in st.session_state:

    st.session_state.messages = []

# ==========================
# Memory
# ==========================

memory = get_memory()

memory_text = ""

for key, value in memory.items():

    memory_text += f"{key}: {value}\n"

# ==========================
# Title
# ==========================

st.title("🤖 Rifat AI")

st.caption("Professional AI Assistant")

# ==========================
# Chat History
# ==========================

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

# ==========================
# Chat Input
# ==========================

prompt = st.chat_input("Ask me anything...")
