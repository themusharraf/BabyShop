from aiogram import types

btn = [
    [types.KeyboardButton(text="O'g'il 🙍‍♂️"), types.KeyboardButton(text="Qiz 🙍‍♀️")],
    [types.KeyboardButton(text="Admin 👮‍♂️")]

]
button = types.ReplyKeyboardMarkup(keyboard=btn, resize_keyboard=True, input_field_placeholder="Tanlang:")
