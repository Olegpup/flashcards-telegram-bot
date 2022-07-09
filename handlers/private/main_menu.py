from keyboards.inline import *
from consts.c_handlers import *
from .common import *
from loader import dp
from aiogram import types


@dp.message_handler(commands=["start"])
async def start_bot(message: types.Message):
    await message.answer(WELCOME_MESSAGE, reply_markup=kb_main_menu())


@dp.callback_query_handler(text="view_categories")
@dp.callback_query_handler(state=CategoriesMenu.collections)
async def view_categories(callback: types.CallbackQuery):
    await CategoriesMenu.categories.set()

    await callback.message.edit_text(CATEGORIES_MESSAGE, reply_markup=kb_categories_menu())

