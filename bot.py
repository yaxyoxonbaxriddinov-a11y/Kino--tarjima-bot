import asyncio
import os
import google.generativeai as genai
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Google Gemini API sozlamasi
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

BOT_TOKEN = os.environ.get("BOT_TOKEN")
dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Assalomu alaykum! Men aqlli botman. Istalgan savolingizni bering.")

@dp.message()
async def chat_handler(message: types.Message):
    try:
        # AI javob beradi
        response = model.generate_content(message.text)
        await message.answer(response.text)
    except Exception as e:
        await message.answer(f"Xatolik: {str(e)}")

async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

