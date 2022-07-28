from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from consts.c_kb import *
from .utils import back_button


def kb_distribution_menu():
    kb = InlineKeyboardMarkup(row_width=1)

    kb.add(*[
        InlineKeyboardButton(text="schedule", callback_data="view_scheduled_distribution"),
        InlineKeyboardButton(text="solo", callback_data="view_solo_distribution"),
        back_button()
    ])

    return kb
