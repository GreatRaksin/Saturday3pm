from functools import reduce

items = [1, 24, 18, 14, 92, 5, 32]
sum_all = reduce(lambda x, y: x + y, items)
print(sum_all)


# вычислить наибольший элемент списка
all_max = reduce(lambda a, b: a if (a > b) else b, items)
print(all_max)


