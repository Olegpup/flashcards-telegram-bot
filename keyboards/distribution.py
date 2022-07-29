from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from consts.c_kb import *
from utils.mongo import *
from .utils import back_button
from config import DISTRIBUTION_PAGE_SIZE


async def kb_distribution_menu():
    kb = InlineKeyboardMarkup(resize_keyboard=True)

    for i in range(DISTRIBUTION_PAGE_SIZE):
        kb.row(InlineKeyboardButton(text=f"{i}", callback_data=f"{i}"))

    kb.row(InlineKeyboardButton(text="create", callback_data="view_solo_distribution"))
    kb.row(
        InlineKeyboardButton(text="<-", callback_data="previous_page"),
        InlineKeyboardButton(text="->", callback_data="next_page"),
    )
    kb.row(back_button())

    return kb
