from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline import *
from loader import dp
from consts.c_handlers import *
import pprint


class SettingsMenu(StatesGroup):
    pass

class CategoriesMenu(StatesGroup):
    categories = State()
    collections = State()
    card = State()


@dp.message_handler(commands=["start"])
async def start_bot(message: types.Message):
    await message.answer(WELCOME_MESSAGE, reply_markup=kb_main_menu())


@dp.callback_query_handler(text="view_main_menu")
async def view_categories(callback: types.CallbackQuery):
    await callback.message.edit_text(WELCOME_MESSAGE, reply_markup=kb_main_menu())


@dp.callback_query_handler(text="view_categories")
@dp.callback_query_handler(state=CategoriesMenu.collections)
async def view_categories(callback: types.CallbackQuery):
    await CategoriesMenu.categories.set()

    await callback.message.edit_text(CATEGORIES_MESSAGE, reply_markup=kb_categories_menu())


@dp.callback_query_handler(text="back", state="*")
async def back(callback: types.CallbackQuery, state: FSMContext):
    pprint.pprint(dict(callback))

    current_state = await state.get_state()  # If state is not declared will be None
    class_name, state_name = current_state.split(":")
    fsm = globals()[class_name]

    if list(fsm.__dict__.keys())[1:].index(state_name) == 0:
        await callback.message.edit_text(WELCOME_MESSAGE, reply_markup=kb_main_menu())

        await state.finish()
    else:
        await fsm.previous()
