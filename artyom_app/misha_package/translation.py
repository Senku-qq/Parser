import langid # lib for language detection
from deep_translator import GoogleTranslator


def sepate_text(text):
    """Split text into pieces of 5000 characters each because Google Translator API has a limit of 5000 characters per request
    Args: text - string
    Returns: list of strings (5000 characters each)"""
    if len(text) > 4999:
        text_parts = [text[i:i + 4999] for i in range(0, len(text), 4999)]
        return "".join(text_parts) # list of separeted text parts
    else: return text # I process text in for loop, so I need (it to be a list if it has only one part)


def translate_text(text, lang):
    """Translates text using Google Translator API
    Args: text- string, lang - string(language code)
    Returns: list of strings (translated text)"""
    translated_text = []
    text_parts = sepate_text(text)
    for i in range(0, len(text_parts)):
        translated_text.append(GoogleTranslator(source='auto', target=lang).translate(text_parts[i]))
    return " ".join(translated_text)


def get_language(text):
    """Detects language of the text using langid library
    Args: text - string
    Returns: string(language code)"""
    text_parts = sepate_text(text)
    lang, confidence = langid.classify(text_parts[0][0:500]) 
    return lang


def back_translate(original, text):
    """Back translates text using Google Translator API
    Args: original, text - string
    Returns: list of strings (text translated to original language)"""
    original = sepate_text(original)
    lang = get_language(original[0][0:500])
    return translate_text(sepate_text(text), lang)


# test
if __name__ == "__main__":
    file = (open("parser.txt", "r", encoding="utf8"))
    text = sepate_text(file.read())
    translated = translate_text(text, 'ru')
    translated = translated[0][0:500]
    print(translated)
    print(back_translate(text, translated))

# красиво оформить переведенное