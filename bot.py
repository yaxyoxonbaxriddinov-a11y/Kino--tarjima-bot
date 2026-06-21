import asyncio
import os
import google.generativeai as genai
from aiogram import Bot, Dispatcher
from aiohttp import web

# 1. Konfiguratsiya
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')
bot = Bot(token=os.environ.get("BOT_TOKEN"))
dp = Dispatcher()

# 2. Bot funksiyalari
@dp.message()
async def chat_handler(message):
    try:
        response = model.generate_content(message.text)
        await message.answer(response.text)
    except Exception:
        await message.answer("Xatolik yuz berdi.")

async def run_bot():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

# 3. Port ochuvchi qism (Render xatosini yo'qotish uchun)
async def handle(request):
    return web.Response(text="Bot ishlayapti")

async def run_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    # Render avtomatik port belgilaydi
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

async def main():
    # Bot va Serverni bir vaqtda ishga tushirish
    await asyncio.gather(run_bot(), run_server())

if __name__ == "__main__":
    asyncio.run(main())


