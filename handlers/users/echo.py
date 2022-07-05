from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp

@dp.message_handler()
async def bot_echo(message: types.Message):
    await message.answer(f"Эхо без состояния."
                         f"Сообщение:\n"
                         f"{message.text}")