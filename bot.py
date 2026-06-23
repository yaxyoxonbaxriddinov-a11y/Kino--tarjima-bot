
import asyncio
import os
import google.generativeai as genai
from aiogram import Bot, Dispatcher
from aiohttp import web

# Google Gemini sozlamalari
genai.configure(
    api_key=os.environ.get("GOOGLE_API_KEY"),
    client_options={'api_version': 'v1'}
)

model = genai.GenerativeModel("gemini-1.5-flash")

bot = Bot(token=os.environ.get("BOT_TOKEN"))
dp = Dispatcher()

@dp.message()
async def chat_handler(message):
    try:
        response = model.generate_content(message.text)
        await message.answer(response.text)
    except Exception as e:
        await message.answer(f"❌ Xatolik yuz berdi: {str(e)}")

async def run_server():
    app = web.Application()
    app.router.add_get('/', lambda r: web.Response(text="Bot ishlayapti"))
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await asyncio.gather(dp.start_polling(bot), run_server())

if __name__ == "__main__":
    asyncio.run(main())

