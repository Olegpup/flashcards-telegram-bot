from aiogram.dispatcher.filters.state import State, StatesGroup


class SettingsMenu(StatesGroup):
    pass


class CategoriesMenu(StatesGroup):
    categories = State()
    decks = State()
    cards = State()