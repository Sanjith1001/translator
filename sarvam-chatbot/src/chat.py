from typing import Optional

from .client import client
from .config import DEFAULT_CHAT_MODEL, DEFAULT_LANGUAGE, MAX_HISTORY
from .language import LANGUAGE_NAMES, detect_language


def chat(
    user_message: str,
    history: Optional[list[dict[str, str]]] = None,
    forced_language: Optional[str] = None,
) -> tuple[str, str, list[dict[str, str]]]:
    """Generate a response and return (reply, detected_lang_code, updated_history)."""
    active_history = history if history is not None else []

    try:
        lang_code = detect_language(user_message)
    except Exception:
        lang_code = "en-IN"

    respond_in_code = forced_language or lang_code
    respond_in_name = LANGUAGE_NAMES.get(respond_in_code, LANGUAGE_NAMES[DEFAULT_LANGUAGE])

    dynamic_system = {
        "role": "system",
        "content": (
            "You are a helpful assistant. "
            f"Always respond in {respond_in_name}. "
            "Be warm and concise."
        ),
    }

    active_history.append({"role": "user", "content": user_message})

    try:
        response = client.chat.completions(
            model=DEFAULT_CHAT_MODEL,
            messages=[dynamic_system] + active_history[-MAX_HISTORY:],
        )
        reply = response.choices[0].message.content
    except Exception as exc:
        reply = f"Error: {exc}"

    active_history.append({"role": "assistant", "content": reply})
    return reply, lang_code, active_history