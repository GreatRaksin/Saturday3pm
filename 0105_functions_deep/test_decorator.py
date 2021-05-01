import time


def timer(function):
    def wrapper(url):
        start = time.time()
        # этот код исполняется ДО выполнения функции, переданной в декоратор

        function(url)  # фукнция исполняется

        # вот этот код исполняется ПОСЛЕ выполнения фукнции, переданной в декоратор
        end = time.time()
        print(f'Время подключения: {end - start}')
    return wrapper


def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper