from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
import requests


flags = requests.get('').json()



flags_button = ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)

btns= [ ]


for flag in flags:
    btns.append(KeyboardButton(text=flag['flag_name']))


flags_button.add(*btns)