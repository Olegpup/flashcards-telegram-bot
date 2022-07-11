from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from consts.c_kb import *


def back_button(*args):
    # Redundant map if args contain strings
    callback_data = "back:" + ":".join(map(str, args))

    return InlineKeyboardButton(text=BACK, callback_data=callback_data)
