import time
import random


def timer(func):
    """Показывает время исполнения переданной фукнции"""
    def wrapper(*args):
        start = time.perf_counter()
        res = func(*args)
        end = time.perf_counter()
        run_time = end - start
        print(f'Функция {func.__name__} отработала за {run_time:.10f} с.')
        return res
    return wrapper

# объявление, наполнение и сортировка массива на 100 элементов
# случайными числами от 1 до 1000
array = [random.randint(1, 1000) for i in range(10000)]
array.sort()


@timer
def binary(arr, val):
    first = 0
    last = len(arr) - 1
    mid = len(arr) // 2
    while first <= last and arr[mid] != val:
        if val > arr[mid]:
            first = mid + 1
        else:
            last = mid - 1

        mid = (last + first) // 2
    return mid


@timer
def dummy_f(num_times):
    for _ in range(num_times):
        sum([i ** 2 for i in range(1000)])


dummy_f(10000)
