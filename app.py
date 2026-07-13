from image_ai import analyze_image
from search import search_ai
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
search_mode = st.toggle(
    "🌐 Internet Search",
    value=False
)
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
# ==========================
# AI Response
# ==========================

if prompt:

    # User Message Save
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # ==========================
    # Memory Save
    # ==========================

    if prompt.lower().startswith("আমার নাম"):

        name = prompt.replace("আমার নাম", "").strip()

        if name:
            set_memory("name", name)

    elif prompt.lower().startswith("my name is"):

        name = prompt.replace("my name is", "").strip()

        if name:
            set_memory("name", name)

    # Refresh Memory
    memory = get_memory()

    memory_text = ""

    for key, value in memory.items():

        memory_text += f"{key}: {value}\n"

    full_prompt = f"""
You are Rifat AI.

User Memory:

{memory_text}

User Question:

{prompt}
"""

    # ==========================
    # AI Generate
    # ==========================

    try:

        if search_mode:

    answer = search_ai(full_prompt)

else:

    answer = ask_ai(full_prompt)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        with st.chat_message("assistant"):

            st.markdown(answer)

    except Exception as e:

        st.error("❌ AI Error")

        st.code(str(e))
