#genearal imports
import re
import logging
import datetime
import time
import pdfplumber
#aiogram imports
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram import F, Router
from aiogram.types import Message, FSInputFile, CallbackQuery
#our modules imports
from main import main, abstract
import keyboard as s_kb

#creating router
router = Router()
#logging into db/
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

#class to store settings (languages, volume, url regex)
class Settings:
    def __init__(self):
        self.URL_REGEX = r'(https?://[^\s]+|www\.[^\s]+)'
        self.lang = "en"
        self.percent = 0.5
        self.lang_codes = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar',\
                           'armenian': 'hy', 'assamese': 'as', 'aymara': 'ay', 'azerbaijani': 'az',\
                            'bambara': 'bm', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn',\
                            'bhojpuri': 'bho', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca',\
                            'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-CN',\
                            'chinese (traditional)': 'zh-TW', 'corsican': 'co', 'croatian': 'hr',\
                            'czech': 'cs', 'danish': 'da', 'dhivehi': 'dv', 'dogri': 'doi', 'dutch':'nl',\
                            'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'ewe': 'ee', 'filipino': 'tl',\
                            'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka',\
                            'german': 'de', 'greek': 'el', 'guarani': 'gn', 'gujarati': 'gu', 'haitian creole': 'ht',\
                            'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn',\
                            'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'ilocano': 'ilo', 'indonesian': 'id',\
                            'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn',\
                            'kazakh': 'kk', 'khmer': 'km', 'kinyarwanda': 'rw', 'konkani': 'gom', 'korean': 'ko',\
                            'krio': 'kri', 'kurdish (kurmanji)': 'ku', 'kurdish (sorani)': 'ckb', 'kyrgyz': 'ky',\
                            'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lingala': 'ln', 'lithuanian': 'lt',\
                            'luganda': 'lg', 'luxembourgish': 'lb', 'macedonian': 'mk', 'maithili': 'mai',\
                            'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi',\
                            'marathi': 'mr', 'meiteilon (manipuri)': 'mni-Mtei', 'mizo': 'lus',\
                            'mongolian': 'mn', 'myanmar': 'my', 'nepali': 'ne', 'norwegian': 'no',\
                            'odia (oriya)': 'or', 'oromo': 'om', 'pashto': 'ps', 'persian': 'fa',\
                            'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'quechua': 'qu', 'romanian': 'ro',\
                            'russian': 'ru', 'samoan': 'sm', 'sanskrit': 'sa', 'scots gaelic': 'gd', 'sepedi': 'nso',\
                            'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk',\
                            'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw',\
                            'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'tatar': 'tt', 'telugu': 'te', 'thai': 'th',\
                            'tigrinya': 'ti', 'tsonga': 'ts', 'turkish': 'tr', 'turkmen': 'tk', 'twi': 'ak', 'ukrainian': 'uk',\
                            'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh',\
                            'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
#object of settings
settings = Settings()

#start command handler
@router.message(CommandStart())
async def cmd_start(msg: Message):
    await msg.answer("Hello!👋\nSend me a LINK and I will summarize webpage for you\n"\
"Or send DOCUMENT to summarize it\n"\
"Type /settings to customize parameters!")


#settings command handler
@router.message(Command("settings"))
async def cmd_settings(msg: Message):
    await msg.answer("You can choose volume and language of summary", reply_markup=s_kb.settings)


#document handler -> gets the document and saves it to the db/ folder, than summarize it and send summary back
@router.message(F.document)
async def handle_document(msg: Message):
    username = msg.from_user.username
    logging.info(f"Username: @{username} | Message: {msg.document.file_name}")
    start = time.time()
    #download document from user
    document = msg.document
    file_id = document.file_id  # Уникальный ID файла
    file_name = document.file_name or "Безымянный файл" # Имя файла
    file_size = document.file_size or "0"# Размер файла
    file = await msg.bot.get_file(file_id)
    file_path = file.file_path
    #downloading with aiogram
    file = await msg.bot.download_file(file_path, destination=f"db/{file_name}")
    time.sleep(0.5)

    await msg.answer(f"Файл {file_name} размером {file_size} загружен!")

    summary_name = "db/ABSTRACT" + datetime.datetime.now().strftime(r"%m_%d_%H-%M-%S") + "text-from-document" + ".txt"
    text_from_document = ""
    #pd file opening
    if ".pdf" in file_name:
        with pdfplumber.open(f"db/{file_name}") as pdf:
            with open("db/output.txt", "w+", encoding="utf-8") as f :
                for page in pdf.pages:
                    text = page.extract_text()
                    text_from_document += text + "\n"
                f.write(text_from_document)
                
    #txt or other file opening
    else:
        with open(f"db/{file_name}", "r", encoding="utf-8") as doc:
            text_from_document = doc.read()
    #summarizing
    if text_from_document:
        summary = abstract(text_from_document, filename=summary_name, prefered_language=settings.lang, percent=settings.percent)
        if summary:
            end = time.time() - start
            parsed = FSInputFile(summary_name)
            await msg.answer_document(parsed, caption=f"Here are your summary (Time: {end} sec)")
        else:
            await msg.reply("I can't parse this document :(")
    else:
        await msg.reply("I can't parse this document :(")

#message handler -> gets the message, checks if it is a valid URL, than parse, summarize it and send summary back in the file
#also it handles language codes
@router.message(F.text)
async def parsing(msg: Message):
    username = msg.from_user.username
    logging.info(f"Username: @{username} | Message: {msg.text}")
    #checking if the message is a valid URL
    #then parsing and summarizing the text
    if re.search(settings.URL_REGEX, msg.text):
        start = time.time()
        await msg.reply("Analyzing the text...")

        summary_name = "db/ABSTRACT" + datetime.datetime.now().strftime(r"%m_%d_%H-%M-%S") + ".txt"
        summary = main(msg.text, filename=summary_name, prefered_language=settings.lang, percent=settings.percent)
        end = time.time() - start
        if summary:
            parsed = FSInputFile(summary_name)
            await msg.reply_document(parsed, caption=f"Here are your summary (Time: {end} sec)")
        else:
            await msg.reply("I can't parse this page :(")
    #if the message is not a valid URL handle it like language code
    elif msg.text in settings.lang_codes.values():
        settings.lang = msg.text
        logging.info(f"Language: {settings.lang}")
        await msg.reply("Language set to " + settings.lang)
    else:
        await msg.answer("Send me a valid URL or language code")
        logging.info(f"Invalid URL or language code: {msg.text}")

#================
#callback handlers

#volume callback handler -> sets the volume of the summary
@router.callback_query(lambda callback: callback.data.isdigit() and int(callback.data) in range(100))
async def set_volume_handler(callback: CallbackQuery):
    settings.percent = int(callback.data) / 100
    logging.info(f"Volume: {settings.percent}")
    await callback.message.answer(f"Volume set to {settings.percent}")

#custom language callback handler -> sets the custom language
@router.callback_query(F.data == "custom")
async def set_custom_language_handler(msg: Message):
    await msg.answer("Send me a language code")

#display all languages codes
@router.callback_query(F.data == "codes_list")
async def send_codes(callback_query: CallbackQuery):
    lang_codes = "\n".join(settings.lang_codes.values())
    max_message_length = 4096  # Telegram's message character limit
    
    # Split the message into chunks
    chunks = [lang_codes[i:i + max_message_length] for i in range(0, len(lang_codes), max_message_length)]
    
    for chunk in chunks:
        await callback_query.message.answer(chunk)

#language callback handler -> sets the language
@router.callback_query(lambda callback: callback.data in settings.lang_codes.values())
async def set_language_handler(callback: CallbackQuery):
    settings.lang = callback.data
    logging.info(f"Language: {settings.lang}")
    await callback.message.reply(f"Language set to {callback.data}")
