import re
import logging
import datetime
import time
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram import F, Router
from aiogram.types import Message, FSInputFile, CallbackQuery

from main import main
import keyboard as s_kb

router = Router()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

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

settings = Settings()

@router.message(CommandStart())
async def cmd_start(msg: Message):
    await msg.answer("Hello!👋\nSend me a LINK and I will summarize webpage for you\n"\
"Or send DOCUMENT to summarize it\n"\
"Type /settings to customize parameters!")

@router.message(Command("settings"))
async def cmd_settings(msg: Message):
    await msg.answer("You can choose volume and language of summary", reply_markup=s_kb.settings)

@router.message(F.text)
async def parsing(msg: Message):
    username = msg.from_user.username
    logging.info(f"Username: @{username} | Message: {msg.text}")
    
    if re.search(settings.URL_REGEX, msg.text):
        start = time.time()
        await msg.reply("Analyzing the text...")

        summary_name = "ABSTRACT" + datetime.datetime.now().strftime(r"%m_%d_%H-%M-%S") + ".txt"
        summary = main(msg.text, filename=summary_name, prefered_language=settings.lang, percent=settings.percent)
        end = time.time() - start
        if summary:
            parsed = FSInputFile(summary_name)
            await msg.reply_document(parsed, caption=f"Here are your summary (Time: {end} sec)")
        else:
            await msg.reply("I can't parse this page :(")

    elif msg.text in settings.lang_codes.values():
        settings.lang = msg.text
        logging.info(f"Language: {settings.lang}")
        await msg.reply("Lenguage set to " + settings.lang)
    else:
        await msg.answer("Send me a valid URL or language code")


@router.callback_query(lambda callback: callback.data.isdigit() and int(callback.data) in range(100))
async def set_volume_handler(callback: CallbackQuery):
    settings.percent = int(callback.data) / 100
    logging.info(f"Volume: {settings.percent}")

@router.callback_query(F.data == "custom")
async def set_custom_language_handler(msg: Message):
    await msg.answer("Send me a language code")

@router.callback_query(lambda callback: callback.data in settings.lang_codes.values())
async def set_language_handler(callback: CallbackQuery):
    settings.lang = callback.data
    logging.info(f"Language: {settings.lang}")
