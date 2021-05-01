def my_sum(a, b):
    return a + b


s = my_sum  # присвоил функцию переменной
print(s(5, 6))

dictionary = {
    'summ': my_sum
}  # записал функцию в словарь

print(dictionary['summ'](1, 5))
# передал функции, находящейся в словаре, аргументы

print(my_sum(3, 4))  # <- вызов ФУНКЦИИ
print(my_sum)  # <- вызов ОБЪЕКТА
