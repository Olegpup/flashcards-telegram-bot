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
    current_state = await state.get_state()  # TODO If state is not declared will be None
    class_name, state_name = current_state.split(":")
    fsm_class = globals()[class_name]
    
    states_tree_root = getattr(fsm_class, "states_tree_root")
    current_node = find_node(states_tree_root, state_name)
    parent = current_node.parent

    if parent:
        await getattr(fsm_class, parent.value).set()

        current_state = await state.get_state()  # TODO If state is not declared will be None
        _, state_name = current_state.split(":")
    else:
        await state.finish()

    handler = globals()[f"view_{state_name}"]  # TODO Deal with case when None
    
    # TODO correct callback data for first back
    # It has MESSAGE_handler, not callback
    await handler(callback)
