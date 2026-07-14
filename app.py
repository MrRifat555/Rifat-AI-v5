import streamlit as st
from pdf_ai import ask_pdf
from streamlit_mic_recorder import mic_recorder
from gtts import gTTS
import tempfile
from ai import ask_ai
from memory import get_memory, set_memory
from search import search_ai
from image_ai import analyze_image

st.set_page_config(
    page_title="🤖 Rifat AI v5",
    page_icon="🤖",
    layout="wide"
)

# Session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Memory
memory = get_memory()

# Sidebar
with st.sidebar:

    st.title("🤖 Rifat AI")

    st.write("Professional AI Assistant")

    google_search = st.checkbox(
        "🌐 Google Search"
    )

    st.divider()

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# Main
st.title("🤖 Rifat AI v5")

st.caption("Chat • Search • Image • PDF • Voice")

uploaded_image = st.file_uploader(
    "🖼️ Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_image:

    st.image(
        uploaded_image,
        use_container_width=True
    )
uploaded_pdf = st.file_uploader(
    "📄 Upload PDF",
    type=["pdf"]
)
# Chat History

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])
st.subheader("🎤 Voice Input")

audio = mic_recorder(
    start_prompt="🎤 Speak",
    stop_prompt="⏹️ Stop",
    key="voice"
)
prompt = st.chat_input(
    "Ask Rifat AI..."
)
# ==========================
# AI Response
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

    # Save Memory
    if prompt.lower().startswith("আমার নাম"):

        name = prompt.replace("আমার নাম", "").strip()

        if name:
            set_memory("name", name)

    elif prompt.lower().startswith("my name is"):

        name = prompt.replace("my name is", "").strip()

        if name:
            set_memory("name", name)

    # Load Memory
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

    try:

with st.spinner("🤖 Rifat AI is thinking..."):

    if uploaded_image:

        answer = analyze_image(
            uploaded_image,
            prompt
        )

    elif uploaded_pdf:

        answer = ask_pdf(
            uploaded_pdf,
            prompt
        )

    elif google_search:

        answer = search_ai(
            full_prompt
        )

    else:

        answer = ask_ai(
            full_prompt
        )        

    # Normal AI
    else:

        answer = ask_ai(
            full_prompt
        )

        # Save AI Response
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

st.caption("🚀 Rifat AI v5 | Powered by Gemini AI")
st.divider()

st.markdown(
    """
Made with ❤️ by Rifat

Powered by Gemini AI
"""
)
