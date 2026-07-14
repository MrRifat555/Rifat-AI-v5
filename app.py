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
