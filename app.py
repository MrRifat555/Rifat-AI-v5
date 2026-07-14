import streamlit as st
from streamlit_mic_recorder import mic_recorder

from ai import ask_ai
from search import search_ai
from image_ai import analyze_image
from pdf_ai import ask_pdf
from memory import get_memory, set_memory

from gtts import gTTS
import tempfile

# ==========================
# Page Config
# ==========================

st.set_page_config(
    page_title="🤖 Rifat AI",
    page_icon="🤖",
    layout="wide"
)

# ==========================
# Session State
# ==========================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================
# Sidebar
# ==========================

with st.sidebar:

    st.title("🤖 Rifat AI")

    st.write("Professional AI Assistant")

    google_search = st.checkbox(
        "🌐 Google Search",
        value=False
    )

    voice_output = st.checkbox(
        "🔊 Voice Output",
        value=True
    )

    st.divider()

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# ==========================
# Main Screen
# ==========================

st.title("🤖 Rifat AI")

st.caption(
    "Chat • Image • PDF • Search • Memory • Voice"
)

# ==========================
# Upload Files
# ==========================

uploaded_image = st.file_uploader(
    "🖼️ Upload Image",
    type=["jpg", "jpeg", "png"]
)

uploaded_pdf = st.file_uploader(
    "📄 Upload PDF",
    type=["pdf"]
)

if uploaded_image:

    st.image(
        uploaded_image,
        use_container_width=True
    )

# ==========================
# Voice Input
# ==========================

audio = mic_recorder(
    start_prompt="🎤 Speak",
    stop_prompt="⏹️ Stop",
    key="voice"
)

# ==========================
# Chat History
# ==========================

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

# ==========================
# Chat Input
# ==========================

prompt = st.chat_input(
    "Ask Rifat AI..."
)# ==========================
# AI Chat
# ==========================

if prompt:

    # User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # ==========================
    # Save Memory
    # ==========================

    if prompt.startswith("আমার নাম"):

        name = prompt.replace("আমার নাম", "").strip()

        if name:

            set_memory(
                "name",
                name
            )

    elif prompt.lower().startswith("my name is"):

        name = prompt.replace(
            "my name is",
            ""
        ).strip()

        if name:

            set_memory(
                "name",
                name
            )

    # ==========================
    # Load Memory
    # ==========================

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
    # Thinking
    # ==========================

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
            # Assistant Message
            # ==========================

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

            with st.chat_message("assistant"):

                st.markdown(answer)
                            # ==========================
            # Voice Output
            # ==========================

            if voice_output:

                try:

                    tts = gTTS(
                        text=answer,
                        lang="bn"
                    )

                    tmp = tempfile.NamedTemporaryFile(
                        delete=False,
                        suffix=".mp3"
                    )

                    tts.save(tmp.name)

                    st.audio(tmp.name)

                except Exception:

                    st.warning("🔊 Voice Output Failed")

        except Exception as e:

            st.error("❌ AI Error")

            with st.expander("Error Details"):

                st.code(str(e))

# ==========================
# Download Chat
# ==========================

chat_text = ""

for msg in st.session_state.messages:

    chat_text += f"{msg['role']}:\n{msg['content']}\n\n"

st.sidebar.download_button(

    "📥 Download Chat",

    data=chat_text,

    file_name="Rifat_AI_Chat.txt",

    mime="text/plain"
)

# ==========================
# Footer
# ==========================

st.divider()

st.caption(
    "🚀 Rifat AI v5.0 Stable | Powered by Gemini AI"
)
