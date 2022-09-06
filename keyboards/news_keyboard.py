from aiogram import types

news_keyboard = types.InlineKeyboardMarkup(row_width=1)
button_1 = types.InlineKeyboardButton(text="Получить Новость", callback_data='news')
news_keyboard.add(button_1)
