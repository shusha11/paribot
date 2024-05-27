import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
bot = Bot(token='7458928109:AAE5dWF6dEGTcXSh26rLQCvtQ5aDeYx0DXM')
dp = Dispatcher()
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет я F52 бот")

@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())















