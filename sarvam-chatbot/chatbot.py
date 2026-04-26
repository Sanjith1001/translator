import streamlit as st
from dotenv import load_dotenv
from src.chat import chat

load_dotenv()

LANGUAGE_CODES = {
    "Auto-detect": None,
    "Hindi": "hi-IN",
    "Tamil": "ta-IN",
    "Telugu": "te-IN",
    "Malayalam": "ml-IN",
    "Kannada": "kn-IN",
    "Bengali": "bn-IN",
    "Marathi": "mr-IN",
    "Gujarati": "gu-IN"
}

st.set_page_config(page_title="Indian Language Chatbot", page_icon="🇮🇳")


def apply_theme(theme_name: str) -> None:
    if theme_name == "System":
        return

    if theme_name == "Light":
        st.markdown(
            """
            <style>
                .stApp { background-color: #f8fafc; color: #0f172a; }
                [data-testid="stSidebar"] { background-color: #e2e8f0; }
            </style>
            """,
            unsafe_allow_html=True,
        )
    elif theme_name == "Dark":
        st.markdown(
            """
            <style>
                .stApp { background-color: #0b1220; color: #e2e8f0; }
                [data-testid="stSidebar"] { background-color: #111827; }
            </style>
            """,
            unsafe_allow_html=True,
        )


st.title("🇮🇳 Indian Language Chatbot")
st.caption("Powered by Sarvam AI - 22 Indian languages")

with st.sidebar:
    st.header("Settings")
    selected_theme = st.selectbox("Theme", ["System", "Light", "Dark"], index=0)
    selected_language = st.selectbox("Response Language", list(LANGUAGE_CODES.keys()))
    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.session_state.history = []
        st.rerun()

apply_theme(selected_theme)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "history" not in st.session_state:
    st.session_state.history = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg["role"] == "user" and "lang" in msg:
            st.caption(f"🌐 Detected: {msg['lang']}")

if prompt := st.chat_input("Type in any language..."):
    forced_lang_code = LANGUAGE_CODES[selected_language]
    try:
        reply, lang_code, updated_history = chat(
            prompt,
            history=st.session_state.history,
            forced_language=forced_lang_code,
        )
        st.session_state.history = updated_history
    except Exception as e:
        lang_code = "en-IN"
        reply = f"Error: {str(e)}"

    # Store for display
    st.session_state.messages.append({"role": "user", "content": prompt, "lang": lang_code})
    st.session_state.messages.append({"role": "assistant", "content": reply})

    # Render
    with st.chat_message("user"):
        st.markdown(prompt)
        st.caption(f"🌐 Detected: {lang_code}")
    with st.chat_message("assistant"):
        st.markdown(reply)