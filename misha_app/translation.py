import langid
from deep_translator import GoogleTranslator


def sepate_text(text):
    # split text into pieces of 5000 characters each
    if len(text) > 4999:
        text_parts = [text[i:i + 4999] for i in range(0, len(text), 4999)]
        return text_parts
    else: return [text]


def translate_text(text_parts, lang):
    translated_text = []
    for i in range(0, len(text_parts)):
        translated_text.append(GoogleTranslator(source='auto', target=lang).translate(text_parts[i]))
    return translated_text


<<<<<<< HEAD
def get_language(text):
    lang = langid.classify(text) 
=======
def get_language(text_parts):
    lang, confidence = langid.classify(text_parts[0][0:500]) 
>>>>>>> 6d3175754ebf41b7d7048ad75370c9a4a1c362a6
    return lang


def back_translate(orig, text):
    lang = get_language(orig)
    return translate_text(sepate_text(text), lang)


if __name__ == "__main__":
    file = (open("parser.txt", "r", encoding="utf8"))
    text = sepate_text(file.read())
    print(translate_text(text, 'ru'))

# красиво оформить переведенное