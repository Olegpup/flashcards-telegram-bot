from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from consts.c_kb import *
from utils.mongo import *


common_buttons = []


def kb_main_menu():
    return InlineKeyboardMarkup(resize_keyboard=True).add(*[
        InlineKeyboardButton(text=CATEGORIES, callback_data="view_categories"),
        InlineKeyboardButton(text=SETTINGS, callback_data="view_settings"),
        *common_buttons
    ])


async def kb_categories_menu(user_id: int):
    categories = (await find_one(ACCOUNTS, {"userId": user_id}))["categories"]
    kb = InlineKeyboardMarkup(row_width=3)
    b_list = []
    for category in categories:
        b_list.append(InlineKeyboardButton(text=category, callback_data=f"view_category:{category}"))
    kb.add(*b_list)
    kb.row(InlineKeyboardButton(text=ADD_CATEGORY, callback_data="add_category"))
    kb.row(InlineKeyboardButton(text=BACK, callback_data="back"))

    return kb


async def kb_decks_menu(user_id: int, category):
    decks = (await find_one(ACCOUNTS, {"userId": user_id}))["categories"][category]
    kb = InlineKeyboardMarkup(row_width=3)
    b_list = []
    for deck in decks:
        b_list.append(InlineKeyboardButton(text=deck["deckName"], callback_data=f"view_deck:{category}:{deck['deckName']}"))
    kb.add(*b_list)
    kb.row(InlineKeyboardButton(text=ADD_DECK, callback_data="add_deck"))
    kb.row(InlineKeyboardButton(text=BACK, callback_data="back"))

    return kb


async def kb_cards_menu(user_id: int, category, deck):
    cards, = list(filter(lambda deckName: deckName == deck, (await find_one(ACCOUNTS, {"userId": user_id}))["categories"][category]))
    kb = InlineKeyboardMarkup(row_width=3)
    b_list = []
    for card in cards:
        b_list.append(InlineKeyboardButton(text=card["frontSide"], callback_data=f"view_card:{category}:{deck['deckName']}:{card['frontSide']}"))
    kb.add(*b_list)
    kb.row(InlineKeyboardButton(text=ADD_CARD, callback_data="add_card"))
    kb.row(InlineKeyboardButton(text=BACK, callback_data="back"))

    return kb
