from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline import kb_main_menu
from loader import dp


@dp.message_handler(commands=["start"])
async def start_bot(message: types.Message):
    await message.answer(f"Эхо без состояния."
                         f"Сообщение:\n"
                         f"{message.text}", reply_markup=kb_main_menu())
