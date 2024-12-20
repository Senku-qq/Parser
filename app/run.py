import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
#handlers to handle messages
from handlers import router
import config

#creating bot and dispatcher
bot = Bot(token=config.TOKEN)
dp = Dispatcher()

#start command handler
async def main():
    dp.include_router(router=router)
    await dp.start_polling(bot)

#run the main function and log
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit...")
        