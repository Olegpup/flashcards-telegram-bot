from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from consts.c_kb import *
from utils.mongo import *
from .utils import back_button


def kb_main_menu():
    kb = InlineKeyboardMarkup(resize_keyboard=True)
    kb.row(InlineKeyboardButton(text=CATEGORIES, callback_data="view_categories"))
    kb.row(InlineKeyboardButton(text=SETTINGS, callback_data="view_settings"))

    return kb


async def kb_categories_menu(user_id: int):
    categories = (await find_one(ACCOUNTS, {"userId": user_id}))["categories"]
    kb = InlineKeyboardMarkup(row_width=3)
    b_list = []
    for category in categories:
        b_list.append(InlineKeyboardButton(text=category, callback_data=f"view_category:{category}"))
    kb.add(*b_list)
    kb.row(InlineKeyboardButton(text=ADD_CATEGORY, callback_data="add_category"))
    kb.row(back_button())

    return kb


async def kb_create_category():
    kb = InlineKeyboardMarkup(row_width=3)
    # kb.row(back_button())

    return kb


async def kb_decks_menu(user_id: int, category: str):
    decks = (await find_one(ACCOUNTS, {"userId": user_id}))["categories"][category]
    kb = InlineKeyboardMarkup(row_width=3)
    b_list = []
    for deck in decks:
        b_list.append(
            InlineKeyboardButton(text=deck["deckName"], callback_data=f"view_deck:{category}:{deck['deckName']}"))
    kb.add(*b_list)
    kb.row(InlineKeyboardButton(text=ADD_DECK, callback_data="add_deck"))
    kb.row(InlineKeyboardButton(text=CATEGORY_SETTINGS, callback_data=f"view_category_settings:{category}"))
    kb.row(back_button())

    return kb


async def kb_category_settings(category: str):
    kb = InlineKeyboardMarkup(row_width=3)
    kb.row(InlineKeyboardButton(text=RENAME_CATEGORY, callback_data=f"rename_category:{category}"))
    kb.row(InlineKeyboardButton(text=DELETE_CATEGORY, callback_data=f"delete_category:{category}"))
    kb.row(back_button())

    return kb


async def kb_rename_category():
    kb = InlineKeyboardMarkup(row_width=3)
    # kb.row(back_button())

    return kb


async def kb_deck_menu(category: str, deck: str):
    kb = InlineKeyboardMarkup(row_width=3)
    kb.row(InlineKeyboardButton(text=VIEW_CARDS_LIST, callback_data=f"view_cards_list:{category}:{deck}"))
    kb.row(InlineKeyboardButton(text=START_DECK_VIEWING, callback_data=f"start_deck_viewing:{category}:{deck}"))
    kb.row(InlineKeyboardButton(text=DECK_SETTINGS, callback_data=f"view_deck_settings:{category}:{deck}"))
    kb.row(back_button(category))

    return kb


async def kb_cards_menu(user_id: int, category: str, deck: str):
    cards, = list(filter(lambda cat: cat["deckName"] == deck,
                         (await find_one(ACCOUNTS, {"userId": user_id}))["categories"][category]))
    cards = cards["cards"]
    kb = InlineKeyboardMarkup(row_width=3)
    b_list = []
    for card in cards:
        b_list.append(InlineKeyboardButton(text=card["frontSide"],
                                           callback_data=f"view_card:{category}:{deck}:{card['frontSide']}"))
    kb.add(*b_list)
    kb.row(InlineKeyboardButton(text=ADD_CARD, callback_data="add_card"))
    kb.row(back_button(category, deck))

    return kb


async def kb_card_menu(user_id: int, category: str, deck: str):
    cards, = list(filter(lambda cat: cat["deckName"] == deck,
                         (await find_one(ACCOUNTS, {"userId": user_id}))["categories"][category]))
    cards = cards["cards"]
    kb = InlineKeyboardMarkup(row_width=3)
    kb.row(InlineKeyboardButton(text=PREVIOUS_CARD, callback_data="next_card"),
           InlineKeyboardButton(text=NEXT_CARD, callback_data="previous_card"))
    kb.row(back_button(category, deck))

    return kb
