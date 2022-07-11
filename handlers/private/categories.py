from keyboards.inline import *
from consts.c_handlers import *
from .fsm import CategoriesMenu
from aiogram import types
from loader import dp


@dp.callback_query_handler(lambda callback: callback.data.startswith("view_category"),
                           state=CategoriesMenu.categories)
async def view_decks(callback: types.CallbackQuery):
    await CategoriesMenu.decks.set()
    await callback.message.edit_text(CATEGORIES_MESSAGE,
                                     reply_markup=await kb_decks_menu(
                                        user_id=callback.from_user.id,
                                        category=callback.data.split(":")[1]))
