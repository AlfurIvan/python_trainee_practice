"""Task 6: select dicts from list_ , where 'name' starts with 'A'"""

import re


def select_big_a():
    list_ = [
        {'name': 'Alex', 'age': 25},
        {'name': 'Oleg', 'age': 23},
        {'name': 'Anna', 'age': 32},
        {'name': 'Igor', 'age': 50},
        {'name': 'Anton', 'age': 17},
    ]

    list_result = []

    for dict_ in list_:
        if re.match(r"^A", dict_["name"]):
            list_result.append(dict_)

    return list_result


print(select_big_a())
