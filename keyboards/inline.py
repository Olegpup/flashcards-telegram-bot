from aiogram.types import KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from consts.c_kb import *


common_buttons = []

def kb_main_menu():
    return InlineKeyboardMarkup(resize_keyboard=True).add(*[
        InlineKeyboardButton(text=CATEGORIES, callback_data="view_categories"),
        InlineKeyboardButton(text=SETTINGS, callback_data="view_settings"),
        *common_buttons
    ])


def kb_categories_menu():
    return InlineKeyboardMarkup(resize_keyboard=True).add(*[
        InlineKeyboardButton(text=ADD_CATEGORY, callback_data="add_category"),
        InlineKeyboardButton(text=DELETE_CATEGORY, callback_data="delete_category"),
        InlineKeyboardButton(text=BACK, callback_data="back"),
        *common_buttons
    ])
