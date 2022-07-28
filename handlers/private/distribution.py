from keyboards.user import *
from consts.c_handlers import *
from .fsm import DistributionMenu
from aiogram import types
from loader import dp


@dp.callback_query_handler(lambda callback: callback.data.startswith("view_distribution"))
async def view_distribution(callback: types.CallbackQuery):
    await DistributionMenu.distribution.set()
    await callback.message.edit_text(message_text="PASS")
