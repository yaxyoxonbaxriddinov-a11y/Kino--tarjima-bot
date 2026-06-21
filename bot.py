import asyncio
import os
import google.generativeai as genai
from aiogram import Bot, Dispatcher
from aiohttp import web

# 1. Sozlamalar
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# 2. Modelni chaqirish (agar 1.5-flash xato bersa, 'gemini-1.5-pro' deb yozib ko'ring)
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. Bot va Dispatcher
bot = Bot(token=os.environ.get("BOT_TOKEN"))
dp = Dispatcher()

# 4. Xabarlarni qabul qilish
@dp.message()
async def chat_handler(message):
    try:
        response = model.generate_content(message.text)
        await message.answer(response.text)
    except Exception as e:
        await message.answer(f"❌ Xatolik yuz berdi: {str(e)}")

# 5. Render server qismi
async def handle(request):
    return web.Response(text="Bot ishlayapti")

async def run_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

# 6. Ishga tushirish
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await asyncio.gather(dp.start_polling(bot), run_server())

if __name__ == "__main__":
    asyncio.run(main())




