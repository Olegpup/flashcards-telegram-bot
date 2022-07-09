from keyboards.inline import *
from consts.c_handlers import *
from .fsm import *  # Do not remove
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp


@dp.callback_query_handler(text="back", state="*")
async def back(callback: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()  # TODO If state is not declared will be None
    class_name, state_name = current_state.split(":")
    fsm = globals()[class_name]

    # Attributes starts from 1
    if list(fsm.__dict__.keys()).index(state_name) == 1:
        await callback.message.edit_text(WELCOME_MESSAGE, reply_markup=kb_main_menu())

        await state.finish()
    else:
        await fsm.previous()
