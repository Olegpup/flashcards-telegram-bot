from aiogram.types import KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


common_buttons = []

def kb_main_menu():
    return InlineKeyboardMarkup(resize_keyboard=True).add(*[
        InlineKeyboardButton(text="Categories", callback_data="view_categories"),
        InlineKeyboardButton(text="Settings", callback_data="view_settings"),
        *common_buttons
    ])


def kb_categories_menu():
    return InlineKeyboardMarkup(resize_keyboard=True).add(*[
        InlineKeyboardButton(text="Add category", callback_data="add_category"),
        InlineKeyboardButton(text="Delete category", callback_data="delete_category"),
        InlineKeyboardButton(text="Back", callback_data="view_main_menu"),
        *common_buttons
    ])
