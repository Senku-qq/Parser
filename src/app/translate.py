from googletrans import Translator
text = open("parser.txt", "r", encoding="utf-8") 
print(text.readline())
translated_text = Translator()
text.close()
translated_text.translate("hello", dest="ja")