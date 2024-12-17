import re
import logging
import datetime
import time

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram import F, Router
from aiogram.types import Message, FSInputFile

from main import main

router = Router()

URL_REGEX = r'(https?://[^\s]+|www\.[^\s]+)'
@router.message(CommandStart())
async def cmd_start(msg: Message):
    await msg.answer("Welcome to Our Parser Bot! This bot is used for parsing from any link!")

@router.message(F.text)
async def parsing(msg: Message):
    username = msg.from_user.username
    logging.info(f"Username: @{username} | Message: {msg.text}")
    
    if re.search(URL_REGEX, msg.text):
        start = time.time()
        await msg.reply("Analyzing the text...")

        summary_name = "ABSTRACT" + datetime.datetime.now().strftime(r"%m_%d_%H-%M-%S") + ".txt"
        summary = main(msg.text, filename=summary_name, prefered_language="ru", percent=0.4)
        end = time.time() - start
        if summary:
            parsed = FSInputFile(summary_name)
            await msg.reply_document(parsed, caption=f"Here are your summary (Time: {end} sec)")
        else:
            await msg.reply("I can't parse this page :(")
    else:
        await msg.reply(f"It is not a link >:(, but {msg.text}")