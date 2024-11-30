from googletrans import Translator
text = open("parser.txt", "r", encoding="utf-8") 
print(text.readline())
translated_text = Translator()
current_language = translated_text.detect('hello')
text.close()
translated_text.translate(text, dest=current_language.lang)