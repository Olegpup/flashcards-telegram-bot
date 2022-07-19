from keyboards.user import *
from consts.c_handlers import *
from .fsm import CategoriesMenu, AddCategory, RenameCategory
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
async def creating_category(message: types.Message, state: FSMContext):
    category_name = message.text
    account = await find_one(ACCOUNTS, {"userId": message.from_user.id})
    account["categories"][category_name] = []

    await update(ACCOUNTS, account["_id"], account)

    await state.finish()
    await CategoriesMenu.categories.set()

    # await message.edit_text(CATEGORIES_MESSAGE, reply_markup=await kb_categories_menu(message.from_user.id))
    # # TODO bot.edit_text


@dp.callback_query_handler(lambda callback: callback.data.startswith("view_category_settings"),
                           state=CategoriesMenu.decks)
async def category_settings(callback: types.CallbackQuery):
    category = callback.data.split(":")[1]
    message_text = f"{CATEGORY_SETTINGS_MESSAGE} {category}"
    await CategoriesMenu.category_settings.set()
    await callback.message.edit_text(message_text,
                                     reply_markup=await kb_category_settings(category))


@dp.callback_query_handler(lambda callback: callback.data.startswith("delete_category"),
                           state=CategoriesMenu.category_settings)
async def delete_category(callback: types.CallbackQuery):
    category = callback.data.split(":")[1]

    account = await find_one(ACCOUNTS, {"userId": callback.from_user.id})
    account["categories"].pop(category)

    await update(ACCOUNTS, account["_id"], account)

    # await CategoriesMenu.decks.set()
    # await callback.message.edit_text(CATEGORIES_MESSAGE, reply_markup=await kb_categories_menu(callback.from_user.id))


@dp.callback_query_handler(lambda callback: callback.data.startswith("rename_category"),
                           state=CategoriesMenu.category_settings)
async def rename_category(callback: types.CallbackQuery):
    category = callback.data.split(":")[1]

    message_text = RENAMING_CATEGORY_MESSAGE + category
    await RenameCategory.renaming_category.set()
    await callback.message.edit_text(message_text,
                                     reply_markup=await kb_rename_category())


@dp.message_handler(state=RenameCategory.renaming_category)
async def renaming_category(message: types.Message, state: FSMContext):
    category_name = message.text
    account = await find_one(ACCOUNTS, {"userId": message.from_user.id})
    # account["categories"][category_name] = []
    #
    # await update(ACCOUNTS, account["_id"], account)
    #
    # await state.finish()
    # await CategoriesMenu.categories.set()
    #
    # # await message.edit_text(CATEGORIES_MESSAGE, reply_markup=await kb_categories_menu(message.from_user.id))
    # # # TODO bot.edit_text