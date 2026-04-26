# Indian Language Chatbot (Sarvam AI)

Multilingual chatbot for Indian languages with automatic language detection, chat memory, and Streamlit UI.

## Features

- Chat in multiple Indian languages using Sarvam AI.
- Auto-detect language with BCP-47 codes (for example hi-IN, ta-IN).
- Conversation memory for up to 10 turns (20 messages).
- Streamlit app with response language controls and theme toggle.
- Translation helper functions for standard, formal, and colloquial styles.

## Project Structure

- `chatbot.py`: Streamlit application.
- `main.py`: CLI chat wrapper.
- `verify.py`: API connectivity check.
- `chat_test.py`: manual chat smoke script.
- `src/client.py`: lazy Sarvam SDK client initialization.
- `src/chat.py`: core chat orchestration.
- `src/language.py`: language detection helpers.
- `src/translation.py`: translation helpers.
- `src/database.py`: SQLite schema scaffold for production persistence.
- `src/models.py`: dataclass models aligned with documented schema.
- `tests/`: unit tests for chat, language, and translation modules.

## Setup

1. Create `.env` in project root:

```env
SARVAM_API_KEY=sk-your-key-here
```

2. Install dependencies with uv:

```bash
uv sync
```

## Run

- Verify API key:

```bash
uv run verify.py
```

- Run CLI:

```bash
uv run main.py
```

- Run Streamlit UI:

```bash
uv run streamlit run chatbot.py
```

## Tests

```bash
uv run python -m unittest discover -s tests -p "test_*.py"
```

## Notes

- The Sarvam SDK call style is `client.chat.completions(...)` (not `.create(...)`).
- Keep `.env` out of version control.
