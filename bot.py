import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiohttp import web

# 1. Tokenni faqat bir marta oling
BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Assalomu alaykum! Men ishlayapman.")

# Faqat bitta translate funksiyasi
@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Siz yozdingiz: {message.text}")

# 2. Render uchun oddiy web server
async def health_check(request):
    return web.Response(text="Bot is running")

async def run_bot():
    await dp.start_polling(bot)

async def main():
    app = web.Application()
    app.router.add_get('/', health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    
    # Render avtomatik tayinlagan portdan foydalanamiz
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    
    await asyncio.gather(site.start(), run_bot())

if __name__ == "__main__":
    asyncio.run(main())

