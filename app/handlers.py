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
        self.lang_codes = ["ar", "bg", "zh", "cs", "da", "nl", "en", "fi", "fr", \
            "de", "el", "he", "hi", "hu", "id", "it", "ja", "ko", "ms", \
            "no", "pl","pt", "ro", "ru", "es", "sv", "th", "tr", "uk", "vi"]

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

    if msg.text in settings.lang_codes:
        settings.lang = msg.text
        logging.info(f"Language: {settings.lang}")
        msg.reply("Lenguage set to " + settings.lang)


@router.callback_query(lambda callback: callback.data.isdigit() and int(callback.data) in range(100))
async def set_volume_handler(callback: CallbackQuery):
    settings.percent = int(callback.data) / 100
    logging.info(f"Volume: {settings.percent}")

@router.callback_query(lambda callback: callback.data in settings.lang_codes)
async def set_language_handler(callback: CallbackQuery):
    settings.lang = callback.data
    logging.info(f"Language: {settings.lang}")

@router.callback_query(F.data == "custom")
async def set_custom_language_handler(msg: Message):
    await msg.answer("Send me a language code")