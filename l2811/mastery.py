from datetime import *
from random import randint
from l2811.exponent import Exponential

arr = [randint(-1000000, 1000000) for i in range(10000000)]

def linear(array, number):
    for num in range(len(array)):  # перебираю каждый элемент массива
        if array[num] == number:  # если конкретное число равно искомому
            return num  # вывести индекс этого числа
            # break   прервать работу цикла
def binary(arr, s):
    first = 0
    last = len(arr) - 1
    mid = len(arr) // 2
    while (first <= last) and arr[mid] != s:
        mid = (last + first) // 2

        if s > arr[mid]:
            first = mid + 1
        else:
            last = mid - 1
    return s
def jump(arr, s):
    from math import sqrt
    length = len(arr)
    jump = int(sqrt(length))
    left = 0
    right = 0

    while left < length and arr[left] <= s:
        right = min(length - 1, left + jump)
        if arr[left] <= s <= arr[right]:
            break
        left += jump
    if left >= length or arr[left] > s:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and arr[i] <= s:
        if arr[i] == s:
            return i
        i += 1
    return -1

start = datetime.now()
linear(arr, 50)
end = datetime.now()

print(f'Время работы (линейка): {end - start}')

arr.sort()
start1 = datetime.now()
binary(arr, 98)
end1 = datetime.now()

print(f'Время работы (бинарный): {end1 - start1}')

arr.sort()
start2 = datetime.now()
jump(arr, 98)
end2 = datetime.now()

print(f'Время работы (скачки): {end1 - start1}')

arr.sort()
start3 = datetime.now()
Exponential(arr, 98)
end3 = datetime.now()

print(f'Время работы (экспоненциальный): {end1 - start1}')
