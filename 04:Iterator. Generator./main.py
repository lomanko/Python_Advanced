from iterator import FlatIterator
from iterator_any_nested import FlatIteratorAny
from generators import flat_generator

nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
]
nested_list_any = [
        ['a', ['b', 'd'], 'c'],
        ['d', ['e', ['d'], [2]], 'f', 'h', False],
        [1, 2, None],
]


if __name__ == '__main__':

    # Задание 1
    print('Итераторы:')
    for item in FlatIterator(nested_list):  # итератор по списку списков
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]  # comprehension для списка списков
    print(flat_list)

    print('----------')

    # Задание 3
    for item in FlatIteratorAny(nested_list_any):  # итератор по списку любой вложенности
        print(item)

    flat_list_any = [item for item in FlatIteratorAny(nested_list_any)]  # comprehension для списка любой вложенности
    print(flat_list_any)

    print('----------')

    # Задание 2
    print('Генераторы:')
    for i in flat_generator(nested_list):  # генератор для списка списков
        print(i)

    print('----------')

    # Задание 4
    for i in flat_generator(nested_list_any):  # генератор для списка любой вложенности
        print(i)
