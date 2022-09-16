def flatten_list(list_, result_list):  # преобразование листа любой вложенности в плоский лист

    counter = 0
    while counter < len(list_):
        if type(list_[counter]) is not list:
            result_list.append(list_[counter])
            counter += 1
        else:
            flatten_list(list_[counter], result_list)
            counter += 1
    return result_list


def flat_generator(list_):
    new_list = []
    list_to_generate = flatten_list(list_, new_list)

    start = 0
    end = len(list_to_generate)
    while start < end:
        yield list_to_generate[start]
        start += 1
