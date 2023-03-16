import os
from datetime import datetime

def logger(old_function):

    current = os.getcwd()
    file_name = 'main.log'
    path = os.path.join(current, file_name)

    cache = {}

    def new_function(*args, **kwargs):
        key = f'{args}_{kwargs}'
        if key in cache:
            return cache[key]
        time_ = str(datetime.now())
        name_ = old_function.__name__
        result = old_function(*args, **kwargs)
        arg = f'{args}, {kwargs}'
        cache[key] = f'{time_} {name_} {arg} {result} '

        with open(path, 'a', encoding='utf-8') as file:
            for k,v in cache.items():
                file.write(v)
        return result

    return new_function

def logger_param(file_name):
    def __logger(old_function):

        current = os.getcwd()
        path = os.path.join(current, file_name)

        cache = {}

        def new_function(*args, **kwargs):
            key = f'{args}_{kwargs}'
            if key in cache:
                return cache[key]
            time_ = str(datetime.now())
            name_ = old_function.__name__
            result = old_function(*args, **kwargs)
            arg = f'{args}, {kwargs}'
            cache[key] = f'{time_} {name_} {arg} {result} '

            with open(path, 'a', encoding='utf-8') as file:
                for k,v in cache.items():
                    file.write(v)
            return result

        return new_function
    return __logger