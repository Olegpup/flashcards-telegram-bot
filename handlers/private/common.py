# Do not remove
from .fsm import *
from .categories import *
from .decks import *
from .main_menu import *

from keyboards.user import *
from consts.c_handlers import *
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp


@dp.callback_query_handler(lambda callback: callback.data.startswith("back"), state="*")
async def back(callback: types.CallbackQuery, state: FSMContext):
    # No need in callback.data.split

    current_state = await state.get_state()  # TODO If state is not declared will be None
    class_name, state_name = current_state.split(":")
    fsm = globals()[class_name]

    # Attributes starts from 1
    if list(fsm.__dict__.keys()).index(state_name) == 1:
        await callback.message.edit_text(WELCOME_MESSAGE, reply_markup=kb_main_menu())

        await state.finish()
    else:
        await fsm.previous()

        current_state = await state.get_state()
        _, state_name = current_state.split(":")

        handler = globals()[f"view_{state_name}"]  # TODO Deal with case when None
        await handler(callback)
