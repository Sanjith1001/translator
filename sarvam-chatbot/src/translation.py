from .client import client

def translate_text(text: str, target_language: str,
                   source_language: str = "auto") -> str:
    response = client.text.translate(
        input=text,
        source_language_code=source_language,
        target_language_code=target_language,
        model="sarvam-translate:v1"
    )
    return response.translated_text

def translate_formal(text: str, target_language: str,
                     source_language: str = "auto") -> str:
    response = client.text.translate(
        input=text,
        source_language_code=source_language,
        target_language_code=target_language,
        model="mayura:v1",
        mode="formal"
    )
    return response.translated_text

def translate_colloquial(text: str, target_language: str,
                         source_language: str = "auto") -> str:
    response = client.text.translate(
        input=text,
        source_language_code=source_language,
        target_language_code=target_language,
        model="mayura:v1",
        mode="modern-colloquial"
    )
    return response.translated_text