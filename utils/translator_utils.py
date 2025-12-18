import time
from deep_translator import GoogleTranslator

def translate_text(text, target_lang):
    if not text or not text.strip():
        return text

    try:
        translator = GoogleTranslator(source="de", target=target_lang)
        time.sleep(0.6)
        return translator.translate(text)
    except Exception:
        return text
