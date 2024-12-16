import langid # lib for language detection
from deep_translator import GoogleTranslator


def sepate_text(text):
    """Split text into pieces of 5000 characters each because Google Translator API has a limit of 5000 characters per request
    Args: text - string
    Returns: list of strings (5000 characters each)"""
    if len(text) > 4999:
        text_parts = [text[i:i + 4999] for i in range(0, len(text), 4999)]
        return text_parts
    else: return [text]


def translate_text(text, lang):
    """Translates text using Google Translator API
    Args: text- string, lang - string(language code)
    Returns: list of strings (translated text)"""
    translated_text = ""
    text_parts = sepate_text(text)
    for i in text_parts:
        translated_text += (GoogleTranslator(source='auto', target=lang).translate(i))
    return translated_text


def get_language(text):
    """Detects language of the text using langid library
    Args: text - string
    Returns: string(language code)"""
    text_parts = sepate_text(text)
    lang, confidence = langid.classify(text_parts[0])
    return lang


def back_translate(original, text):
    """Back translates text using Google Translator API
    Args: original, text - string
    Returns: list of strings (text translated to original language)"""
    lang = get_language(original)
    return translate_text(text, lang)


# test
if __name__ == "__main__":
    text = "Hello, my name is Misha. I am a student. I am studying at the university."
    print(text)
    translated = translate_text(text, 'ru')
    print(translated)
    print(back_translate(text, translated))

# красиво оформить переведенное