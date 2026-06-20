import asyncio
import os
import google.generativeai as genai
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart

# Google Gemini API
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

BOT_TOKEN = os.environ.get("BOT_TOKEN")
dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Assalomu alaykum! Men aqlli botman. Istalgan savolingizni bering yoki kino qidirish uchun buyruq bering.")

# AGAR FOYDALANUVCHI /tarjima deb yozsa, tarjima qiladi
@dp.message(F.text.startswith("/tarjima"))
async def translate_only(message: types.Message):
    # Bu yerga o'sha eski tarjima kodingizni qo'ysangiz bo'ladi
    await message.answer("Tarjima qilish funksiyasi...")

# AKS HOLDA, HAR QANDAY XABARGA AI JAVOB BERADI
@dp.message()
async def chat_handler(message: types.Message):
    try:
        response = model.generate_content(message.text)
        await message.answer(response.text)
    except Exception:
        await message.answer("Kechirasiz, texnik xatolik.")

async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


