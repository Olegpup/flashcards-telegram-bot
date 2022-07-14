from keyboards.user import *
from consts.c_handlers import *
from .fsm import CategoriesMenu, AddCategory
from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from utils.mongo import *
from .main_menu import view_categories


@dp.callback_query_handler(lambda callback: callback.data.startswith("view_category"),
                           state=CategoriesMenu.categories)
async def view_decks(callback: types.CallbackQuery):
    await CategoriesMenu.decks.set()
    message_text = f"{DECKS_MESSAGE} \"{callback.data.split(':')[1]}\":"
    await callback.message.edit_text(message_text,
                                     reply_markup=await kb_decks_menu(
                                         user_id=callback.from_user.id,
                                         category=callback.data.split(":")[1]))


@dp.callback_query_handler(lambda callback: callback.data.startswith("add_category"),
                           state=CategoriesMenu.categories)
async def add_category(callback: types.CallbackQuery):
    await AddCategory.adding_category.set()
    message_text = ADDING_CATEGORY_MESSAGE
    await callback.message.edit_text(message_text,
                                     reply_markup=await kb_create_category())


@dp.message_handler(state=AddCategory.adding_category)
async def create_category(message: types.Message, state: FSMContext):
    category_name = message.text
    account = await find_one(ACCOUNTS, {"userId": message.from_user.id})
    account["categories"][category_name] = []

    await update(ACCOUNTS, account["_id"], account)

    await state.finish()
    await CategoriesMenu.categories.set()
    await message.edit_text(CATEGORIES_MESSAGE, reply_markup=await kb_categories_menu(message.from_user.id))
    # TODO bot.edit_text