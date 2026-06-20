import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Tokenni xavfsizlik uchun yashirin muhitdan olamiz
BOT_TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer(
        "Assalomu alaykum! Men kino qidiradigan va audio/videolarni 50 dan ortiq tillarga tarjima qilib beradigan aqlli yordamchi botman.\n\n"
        "Hozirda sozlash ishlari ketyapti, tez orada to'liq ishga tushaman!"
    )

async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
