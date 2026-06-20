import asyncio
import os
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Tokenni muhit o'zgaruvchisidan olamiz
BOT_TOKEN = os.environ.get("BOT_TOKEN")

dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer(
        "Assalomu alaykum! Men kino qidiradigan botman."
    )

# Render uchun oddiy veb-server
async def web_server(request):
    return web.Response(text="Bot ishlayapti")

async def main():
    bot = Bot(token=BOT_TOKEN)
    
    # Veb-serverni ishga tushirish
    app = web.Application()
    app.router.add_get('/', web_server)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', int(os.environ.get("PORT", 8080)))
    await site.start()
    
    # Botni ishga tushirish
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

