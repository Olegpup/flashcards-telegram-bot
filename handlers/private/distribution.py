from keyboards.distribution import *
from consts.c_handlers import *
from .fsm import CategoriesMenu
from loader import dp
from aiogram import types
from .utils import is_admin  # TODO create decorator for admin check, maybe...


@dp.callback_query_handler(lambda callback: is_admin(callback.from_user.id), text="view_distribution")
async def view_categories(callback: types.CallbackQuery):
    await CategoriesMenu.categories.set()
    await callback.message.edit_text(CATEGORIES_MESSAGE, reply_markup=kb_distribution_menu())
