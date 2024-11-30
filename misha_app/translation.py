import langid
from deep_translator import GoogleTranslator


def sepate_text(text):
    # split text into pieces of 5000 characters each
    if len(text) > 4999:
        text_parts = [text[i:i + 4999] for i in range(0, len(text), 4999)]
        return text_parts
    else: return text


def translate_text(text_parts, lang):
    translated_text = []
    for i in range(0, len(text)):
        translated_text.append(GoogleTranslator(source='auto', target=lang).translate(text_parts[i]))
    return translated_text


def get_language(text):
    lang, confidence = langid.classify(text) 
    return lang

if __name__ == "__main__":
    file = (open("parser.txt", "r", encoding="utf8"))
    text = sepate_text(file.read())
    print(translate_text(text, "ru"))

# красиво оформить переведенное