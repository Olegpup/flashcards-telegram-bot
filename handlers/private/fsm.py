from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMNode:
    def __init__(self, value, parent, nodes):
        self.value: str = value
        self.parent: FSMNode = parent
        self.nodes: list = nodes


def _init_fsm_tree(name: str, states_tree: dict) -> type:
    attributes = dict()

    root = _connect_nodes(attributes, states_tree, None)

    attributes.update({"states_tree_root": root})

    return type(name, (StatesGroup, ), attributes)


def _connect_nodes(attributes: dict, level: dict, parent: FSMNode or None) -> FSMNode:
    for name, childs in level.items():
        attributes[name] = State()

        current_node = FSMNode(name, parent, [])

        if parent:
            parent.nodes.append(current_node)

        if childs:
            _connect_nodes(attributes, childs, current_node)

        if current_node.parent is None:
            return current_node


def find_node(current_node: FSMNode, name: str) -> FSMNode or None:
    if current_node.value == name:
        return current_node

    for node in current_node.nodes:
        node = find_node(node, name)

        if node:
            return node


CategoriesMenu = _init_fsm_tree(
    "CategoriesMenu",
    {
        "categories": {
            "decks": {
                "deck": {
                    "cards": {}
                }
            }
        }
    }
)

# TODO add function that will raise exception if with something wrong with fsm tree
# will run before bot boot