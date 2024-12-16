import re
import logging
import requests

from bs4 import BeautifulSoup
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram import F, Router
from aiogram.types import Message

router = Router()

URL_REGEX = r'(https?://[^\s]+|www\.[^\s]+)'

@router.message(CommandStart())
async def cmd_start(msg: Message):
    await msg.answer("Welcome to Our Parser Bot! This bot is used for parsing from any article (link)!")

@router.message(F.text)
async def parsing(msg: Message):
    username = msg.from_user.username
    logging.info(f"Username: @{username} | Message: {msg.text}")
#   ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    if re.search(URL_REGEX, msg.text):  
        await msg.reply("Вы отправили ссылку!")
    else:
        await msg.reply(f"Вижу обычный текст: {msg.text}")