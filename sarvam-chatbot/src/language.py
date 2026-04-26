from .client import client

LANGUAGE_NAMES = {
    "hi-IN": "Hindi",   "ta-IN": "Tamil",     "te-IN": "Telugu",
    "ml-IN": "Malayalam","kn-IN": "Kannada",   "bn-IN": "Bengali",
    "mr-IN": "Marathi", "gu-IN": "Gujarati",  "pa-IN": "Punjabi",
    "od-IN": "Odia",    "as-IN": "Assamese",  "ur-IN": "Urdu",
    "en-IN": "English"
}

def detect_language(text: str) -> str:
    """Returns BCP-47 code: hi-IN, ta-IN, ml-IN, etc."""
    response = client.text.identify_language(input=text)
    return response.language_code