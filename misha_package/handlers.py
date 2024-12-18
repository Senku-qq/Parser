import re
import logging
import datetime
import time

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram import F, Router
from aiogram.types import Message , FSInputFile
import keyboards as kb
from main import main
from translation import get_language
router = Router()

prefered_language = 0
percent = 0
URL_REGEX = r'(https?://[^\s]+|www\.[^\s]+)'
link = 0
 
@router.message(CommandStart())
async def cmd_start(msg: Message):
    await msg.answer("Welcome to Our Parser Bot! This bot is used for parsing from any article (link)!\nPlease send a link or document file to make an abstract")
   
@router.message(Command('setting'))
async def setting( msg: Message):
    await msg.answer("Выберите настройки:", reply_markup=kb.setting_menu)
 
@router.message(F.text =='Настройки ⚙️')
async def global_setting( msg:Message):
    await msg.answer("Выберите опцию: ", reply_markup=kb.setting)
 
@router.message(F.text)
async def parsing( msg: Message):
    username = msg.from_user.username
    logging.info(f"Username: @{username} | Message: {msg.text}")
    if prefered_language == 0 and percent == 0:
        await msg.reply('Error: не установленны настройки конспекта\nПожалуйста выберите или создайте конфигурацию конспекта')
    if re.search(URL_REGEX, msg.text):
        start = time.time()
        await msg.reply("Analyzing the text...")

        summary_name = "ABSTRACT" + datetime.datetime.now().strftime(r"%m_%d_%H-%M-%S") + ".txt"
        summary = main(msg.text, filename=summary_name, prefered_language=prefered_language, percent=percent)
        end = time.time() - start
        if summary:
            parsed = FSInputFile(summary_name)
            await msg.reply_document(parsed, caption=f"Here are your summary (Time: {end} sec)")
        else:
            await msg.reply("I can't parse this page :(")
    else:
        await msg.reply(f"It is not a link or document>:(, but {msg.text}")