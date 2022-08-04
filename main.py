import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
# 579718364

load_dotenv()

TOKEN = os.getenv('TOKENBOT')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    print(message.from_user)
    await message.answer('s')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
