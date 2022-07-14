from keyboards.user import *
from consts.c_handlers import *
from .fsm import CategoriesMenu
from aiogram import types
from loader import dp


@dp.callback_query_handler(lambda callback: callback.data.startswith("view_card"),
                           state=CategoriesMenu.cards)
async def view_card(callback: types.CallbackQuery):
    await CategoriesMenu.card.set()
    user_id = callback.from_user.id
    category = callback.data.split(":")[1]
    deck = callback.data.split(":")[2]
    frontSide = callback.data.split(":")[3]

    cards, = list(filter(lambda cat: cat["deckName"] == deck,
                         (await find_one(ACCOUNTS, {"userId": user_id}))["categories"][category]))
    cards = cards["cards"]
    card, = list(filter(lambda c: c["frontSide"] == frontSide, cards))

    message_text = f"{card['frontSide']}\n\n{card['backSide']}"
    await callback.message.edit_text(message_text,
                                     reply_markup=await kb_card_menu(
                                         user_id=user_id,
                                         category=category,
                                         deck=deck))
