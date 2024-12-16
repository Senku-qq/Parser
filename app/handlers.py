import re
import logging
import requests

from bs4 import BeautifulSoup
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram import F, Router
from aiogram.types import Message, FSInputFile

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
    try:
        if re.search(URL_REGEX, msg.text):  
            url = msg.text
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                with open('parsed_text.txt', 'w+', encoding='utf8') as file:
                    titles = soup.getText()
                    for t in titles:
                        file.writelines(t.text.strip() + '\n')
                    parsed = FSInputFile('parsed_text.txt')
                await msg.reply_document(parsed, caption='Вот твой отпаршенный файлик')
            else:   
                print(f"Ошибка загрузки страницы: {response.status_code}")
        else:
            await msg.send(f"Вижу обычный текст: {msg.text}")
    except requests.exceptions.RequestException as e:
        await msg.reply(f"Не удалось загрузить данные с указанной ссылки: {e}")