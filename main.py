import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

from keyboards.news_keyboard import news_keyboard
from pars_news import get_content

# 579718364

load_dotenv()

TOKEN = os.getenv('TOKENBOT')
url = 'https://usionline.com/vse-stati'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("Нажмите на кнопку чтобы получить новость", reply_markup=news_keyboard)


@dp.callback_query_handler(text='news')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    # answer_data = query.data
    news = get_content(url)

    await query.answer('Loading')
    await bot.send_photo(chat_id=query.from_user.id, photo=news['image_url'],
                         caption=f"<b>{news['title']}</b>\n\n{news['description']}\n\n{news['date']}",
                         parse_mode='html', reply_markup=news_keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
