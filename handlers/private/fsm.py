from aiogram.dispatcher.filters.state import State, StatesGroup


class SettingsMenu(StatesGroup):
    pass


class CategoriesMenu(StatesGroup):
    categories = State()
    collections = State()
    card = State()
