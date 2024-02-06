from aiogram import types

btn_turi = [
    [types.KeyboardButton(text="O'g'il 🙍‍♂️"), types.KeyboardButton(text="Qiz 🙍‍♀️")],
    [types.KeyboardButton(text="Admin 👮‍♂️")]

]
button = types.ReplyKeyboardMarkup(keyboard=btn_turi, resize_keyboard=True, input_field_placeholder="Tanlang:")

btn_girl1 = [
    [types.KeyboardButton(text="Ustki kiyim"),types.KeyboardButton(text="Shim")],
    [types.KeyboardButton(text="Bosh kiyim"),types.KeyboardButton(text="Oyoq Kiyim")],
]
button_girl = types.ReplyKeyboardMarkup(keyboard=btn_girl1, resize_keyboard=True, input_field_placeholder="Tanlang:")
