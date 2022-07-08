from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline import *
from loader import dp
from consts.c_handlers import *


@dp.message_handler(commands=["start"])
async def start_bot(message: types.Message):
    await message.answer(WELCOME_MESSAGE, reply_markup=kb_main_menu())


@dp.callback_query_handler(text="view_main_menu")
async def view_categories(callback: types.CallbackQuery):
    await callback.message.edit_text(WELCOME_MESSAGE, reply_markup=kb_main_menu())


@dp.callback_query_handler(text="view_categories")
async def view_categories(callback: types.CallbackQuery):
    await callback.message.edit_text(CATEGORIES_MESSAGE, reply_markup=kb_categories_menu())
