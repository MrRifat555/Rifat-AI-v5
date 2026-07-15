import streamlit as st
import tempfile

from ai import ask_ai
from search import search_ai
from image_ai import analyze_image
from pdf_ai import ask_pdf

from database import (
    save_chat,
    load_chat,
    save_memory,
    load_memory
)

from memory import (
    get_memory,
    set_memory
)

from voice import speak
st.set_page_config(
    page_title="🤖 Rifat AI v6",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Rifat AI v6")
st.caption("Powered by Gemini + Supabase")
with st.sidebar:

    st.header("⚙️ Settings")

    google_search = st.toggle(
        "🌐 Google Search",
        value=False
    )

    voice_mode = st.toggle(
        "🔊 Voice",
        value=True
    )

    st.divider()

    uploaded_image = st.file_uploader(
        "🖼️ Upload Image",
        type=["jpg", "jpeg", "png"]
    )

    uploaded_pdf = st.file_uploader(
        "📄 Upload PDF",
        type=["pdf"]
    )
if "messages" not in st.session_state:
    st.session_state.messages = []

USER_ID = "rifat"
memory = get_memory()

memory_text = ""

for key, value in memory.items():
    memory_text += f"{key}: {value}\n"
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])
prompt = st.chat_input("💬 Ask Rifat AI...")
if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    save_chat(
        USER_ID,
        "user",
        prompt
    )

    with st.chat_message("user"):
        st.markdown(prompt)
full_prompt = f"""
Memory:

{memory_text}

User:

{prompt}
"""
with st.spinner("🤖 Thinking..."):

    try:

        # ==========================
        # Image AI
        # ==========================

        if uploaded_image:

            answer = analyze_image(
                uploaded_image,
                prompt
            )

        # ==========================
        # PDF AI
        # ==========================

        elif uploaded_pdf:

            answer = ask_pdf(
                uploaded_pdf,
                prompt
            )

        # ==========================
        # Google Search
        # ==========================

        elif google_search:

            answer = search_ai(
                full_prompt
            )

        # ==========================
        # Normal AI
        # ==========================

        else:

            answer = ask_ai(
                full_prompt
            )

        # ==========================
        # Save Assistant Chat
        # ==========================

        save_chat(
            USER_ID,
            "assistant",
            answer
        )

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
        # ==========================
# Voice Output
# ==========================

if voice_mode and "answer" in locals():

    try:

        audio_file = speak(answer)

        st.audio(audio_file)

    except Exception:

        st.warning("Voice Output Failed")

# ==========================
# Download Chat
# ==========================

chat_text = ""

for msg in st.session_state.messages:

    chat_text += f"{msg['role']}: {msg['content']}\n\n"

st.sidebar.download_button(

    label="📥 Download Chat",

    data=chat_text,

    file_name="rifat_ai_chat.txt",

    mime="text/plain"
)

# ==========================
# Clear Chat
# ==========================

if st.sidebar.button("🗑️ Clear Chat"):

    st.session_state.messages = []

    st.rerun()

# ==========================
# Footer
# ==========================

st.divider()

st.caption(
    "🚀 Rifat AI v6 • Powered by Gemini + Supabase"
)
