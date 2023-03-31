"""
Task 7:
relative to user`s country from users_list, make function, that returns special greeting.
-- use map() function
"""

users_list = [
    ('Олександр', 'ua'),
    ('James', 'us'),
    ('Daniella', 'es'),
    ('Someone', 'unknown country'),
]


greetings = {
    'ua': 'Привіт, {}е!',
    'us': 'Hello, {}!',
    'es': 'Hola, {}!',
    'unknown country': 'Hello, {}, but I do not know where are you from!'
}


def weird_waiter():
    """function to make response relative to user`s country"""

    # hellos[x[1]][_] -- accessing building items from dict hellos
    # return list(map(lambda x: greetings[x[1]][0] + x[0] + greetings[x[1]][1], users_list))
    return list(map(lambda user_info:
                    greetings[user_info[1]].format(user_info[0]), users_list))


print(weird_waiter())

# so, we can debate about this solution,
# I also thought about using translating lib from pypi, but this code is cute and ssmple
