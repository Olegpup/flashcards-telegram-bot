from aiogram.dispatcher.filters.state import State, StatesGroup


def _init_fsm_tree(name: str, states_tree_: dict) -> type:
    states_tree = states_tree_
    attributes = dict()

    __states_tree_to_attributes(attributes, states_tree)

    attributes.update({"states_tree", states_tree})

    return type(name, (StatesGroup, ), attributes)


def __states_tree_to_attributes(attributes, level: dict):
    for key, val in level.items():
        attributes[key] = State()

        if val:
            __states_tree_to_attributes(attributes, val)


CategoriesMenu = _init_fsm_tree(
    "CategoriesMenu",
    {
        "categories": {},
        "decks": {},
        "deck": {},
        "cards": {}
    }
)
