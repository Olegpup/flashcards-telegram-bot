from keyboards.user import *
from consts.c_handlers import *
from .fsm import CategoriesMenu
from loader import dp
from aiogram import types
from .utils import is_admin


@dp.message_handler(commands=["start"], state="*")
async def start_bot(message: types.Message):
    keyboard = kb_main_menu_admin() if is_admin(message.from_user.id) else kb_main_menu()

    await message.answer(WELCOME_MESSAGE, reply_markup=keyboard)


@dp.callback_query_handler(text="view_categories")
async def view_categories(callback: types.CallbackQuery):
    await CategoriesMenu.categories.set()
    await callback.message.edit_text(CATEGORIES_MESSAGE, reply_markup=await kb_categories_menu(callback.from_user.id))
