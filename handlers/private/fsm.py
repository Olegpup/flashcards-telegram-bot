from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMLeaf():
  def __init__(self, leafs: dict):
    self.leafs = leafs
    self.state = State()


class FSMTree(StatesGroup):
    states_tree = dict()

    def __init__(self, states_tree: dict):
        self.__fill_tree(states_tree)

    def __fill_tree(self, level: dict):
        for key, val in level.items():
            if val:
                setattr(self, key, FSMLeaf(val))
                self.states_tree[key] = {}
              
                self._fill_tree(getattr(self, key).leafs)
            else:
                setattr(self, key, FSMLeaf(val))

                self.states_tree[key] = getattr(self, key)


class SettingsMenu(StatesGroup):
    pass


class CategoriesMenu(StatesGroup):
    categories = State()
    decks = State()
    deck = State()
    cards = State()
