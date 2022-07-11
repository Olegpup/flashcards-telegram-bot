from keyboards.inline import *
from consts.c_handlers import *
from .fsm import CategoriesMenu
from aiogram import types
from loader import dp


@dp.callback_query_handler(lambda callback: callback.data.startswith("view_deck"),
                           state=CategoriesMenu.decks)
async def view_cards(callback: types.CallbackQuery):
    await CategoriesMenu.cards.set()
    await callback.message.edit_text(CATEGORIES_MESSAGE,
                                     reply_markup=await kb_cards_menu(
                                        user_id=callback.from_user.id,
                                        category=callback.data.split(":")[1],
                                        deck=callback.data.split(":")[2]))

