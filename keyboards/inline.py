from aiogram.types import KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def kb_main_menu():
    btn_view_categories = InlineKeyboardButton(text="Categories", callback_data="view_categories")
    btn_view_settings = InlineKeyboardButton(text="Settings", callback_data="view_settings")

    return InlineKeyboardMarkup(resize_keyboard=True).add(btn_view_categories, btn_view_settings)
