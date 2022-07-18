from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from consts.c_kb import *
from utils.mongo import *
from .utils import back_button


def kb_distribution_menu():
    return InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(*[
        InlineKeyboardButton(text="Once", callback_data=f"view_solo_distribution_menu"),
        InlineKeyboardButton(text="Schedule", callback_data=f"view_schedule_distribution_menu"),
        back_button() # TODO 
    ])
