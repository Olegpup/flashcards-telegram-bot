from aiogram.dispatcher.filters.state import State, StatesGroup
from numpy import isin


class FSMNode:
    def __init__(self, value, parent, nodes):
        self.value: str = value
        self.parent: FSMNode = parent
        self.nodes: list = nodes


def _init_fsm_tree(name: str, states_tree_: dict) -> type:
    states_tree = states_tree_  # TODO Remove/replace?
    attributes = dict()

    _states_tree_to_attributes(attributes, states_tree, None)

    first = list(states_tree.keys())[0]
    root = FSMNode(first, None, states_tree[first].nodes)

    attributes.update({"states_tree_root": root})

    return type(name, (StatesGroup, ), attributes)


def _states_tree_to_attributes(attributes, level: dict, parent: FSMNode or None):
    for key, val in level.items():
        attributes[key] = State()

        if val:
            _states_tree_to_attributes(attributes, val, level[key])

        level[key] = FSMNode(key, parent, list(val.values())) 


CategoriesMenu = _init_fsm_tree(
    "CategoriesMenu",
    {
        "categories": {"a": {"b": {"c": {}}, "f": {}}},
        "decks": {},
        "deck": {},
        "cards": {}
    }
)
