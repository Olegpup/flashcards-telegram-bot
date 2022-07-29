from aiogram.dispatcher import FSMContext
from keyboards.distribution import *
from consts.c_handlers import *
from .fsm import DistributionMenu
from aiogram import types
from loader import dp


@dp.callback_query_handler(lambda callback: callback.data.startswith("view_distribution"))
async def view_distribution(callback: types.CallbackQuery):
    await DistributionMenu.distribution.set()
    await callback.message.edit_text("text", reply_markup=await kb_distribution_menu())


@dp.callback_query_handler(
    lambda callback: callback.data.startswith("create_distribution"),
    state=DistributionMenu.distribution
)
async def create_distribution(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text("text", reply_markup=await kb_distribution_menu())
