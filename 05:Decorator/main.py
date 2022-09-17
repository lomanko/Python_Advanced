from decorator import decor

if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    path = 'logs/'

    # Задание 3
    @decor(path)
    def flat_generator(list_):
        list_to_generate = sum(list_, [])
        start = 0
        end = len(list_to_generate)
        while start < end:
            yield list_to_generate[start]
            start += 1

    flat_generator(nested_list)
