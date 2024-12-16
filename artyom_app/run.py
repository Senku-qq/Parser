import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.text)
async def console(msg: Message):
    username = msg.from_user.username
    logging.info(f"Username: @{username} | Message: {msg.text}")


@dp.message(CommandStart())
async def cmd_start(msg: Message):
    await msg.answer("пиривет")

@dp.message(Command('help'))
async def cmd_help(msg: Message):
    await msg.answer('''
Привіт! Скинь мені будь ласка посилання, і я тобі надішлю найголовне з цього сайту (посилання)
\n''')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit...")