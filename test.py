def states_tree_to_attributes(attributes, level: dict):
    for key, val in level.items():
        attributes[key] = 1

        if val:
            states_tree_to_attributes(attributes, val)


c = {
    "a": "", 
    "b": {
        "c": {
            "f": ""
            }
        },
        "d": ""
    }

d = {}
states_tree_to_attributes(d, c)
print(d)