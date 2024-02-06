from aiogram import types

btn = [
    [types.KeyboardButton(text="O'g'il 🙍‍♂️"), types.KeyboardButton(text="Qiz 🙍‍♀️")],
    [types.KeyboardButton(text="Admin 👮‍♂️")]

]
button = types.ReplyKeyboardMarkup(keyboard=btn, resize_keyboard=True, input_field_placeholder="Tanlang:")


but = [
    [types.KeyboardButton(text="Bosh kiyim 🧢"), types.KeyboardButton(text="Ustki kiyim 👕")],
    [types.KeyboardButton(text="Pastki kiyim 👖"), types.KeyboardButton(text="Oyoq kiyim 🥾")],
    [types.KeyboardButton(text="Orqaga qaytish")]
]
buton = types.ReplyKeyboardMarkup(keyboard=but, resize_keyboard=True,input_field_placeholder="Tanlang:")