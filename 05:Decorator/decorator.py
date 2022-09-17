import datetime


def decor(path_to_logger=''):  # Задание 2
    def decor_(any_function):  # Задание 1
        def new_function(*args, **kwargs):
            call_time = datetime.datetime.now()
            name_func = any_function.__name__
            arguments = f'Args:{args}_Kwargs:{kwargs}'
            result = any_function(*args, **kwargs)
            with open(f'{path_to_logger}logger.txt', 'a') as f:
                new_log = f'call_time: {call_time}, name_function:{name_func}, arguments:{arguments}, result:{result}\n'
                f.write(new_log)
            return result
        return new_function
    return decor_
