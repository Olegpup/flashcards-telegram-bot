from aiogram.types import KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


common_buttons = []

def kb_main_menu():
    return InlineKeyboardMarkup(resize_keyboard=True).add(*[
        InlineKeyboardButton(text="Categories", callback_data="view_categories"),
        InlineKeyboardButton(text="Settings", callback_data="view_settings"),
        *common_buttons
    ])
