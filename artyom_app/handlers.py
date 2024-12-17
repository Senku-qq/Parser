import re
import logging

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
        await msg.reply("Analyzing the text...")

        #ADDED BY MISHA
        summary = main(msg.text, "result.txt")
        if summary:
            text = ""
            parsed = FSInputFile('result.txt')
            await msg.reply_document(parsed, caption='Here are your summary')
        else:
            await msg.reply("I can't parse this page :(")
        #END
    else:
        await msg.reply(f"It is not a link >:(, but {msg.text}")