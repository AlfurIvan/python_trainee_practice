"""Task 2: sort dicts in list by age using sorted & lambda"""


def people_sort():
    peoples = [{'name': 'Oleg', 'age': 23}, {'name': 'Vasya', 'age': 19}]

    sorted_peoples = sorted(peoples, key=lambda peoples: peoples['age'])

    print(sorted_peoples)


people_sort()
