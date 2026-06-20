import asyncio
import os
import google.generativeai as genai
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Google Gemini API sozlamasi (Render'dagi GOOGLE_API_KEY dan foydalanadi)
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Assalomu alaykum! Men Gemini AI botman. Istalgan savolingizni bering!")

@dp.message()
async def chat_handler(message: types.Message):
    # Gemini'dan javob olish
    try:
        response = model.generate_content(message.text)
        await message.answer(response.text)
    except Exception as e:
        await message.answer("Kechirasiz, hozir texnik xatolik yuz berdi.")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


