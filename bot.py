import asyncio
import os
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from deep_translator import GoogleTranslator

BOT_TOKEN = os.environ.get("BOT_TOKEN")
dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Assalomu alaykum! Men kino qidiradigan va tarjima qiladigan botman.")

@dp.message()
async def translate_text(message: types.Message):
    try:
        translated = GoogleTranslator(source='auto', target='uz').translate(message.text)
        await message.answer(f"Tarjimasi: {translated}")
    except Exception:
        await message.answer("Kechirasiz, tarjima qilishda xatolik yuz berdi.")

async def web_server(request):
    return web.Response(text="Bot ishlayapti")

async def main():
    bot = Bot(token=BOT_TOKEN)
    app = web.Application()
    app.router.add_get('/', web_server)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.environ.get("PORT", 8080)))
    await site.start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())




