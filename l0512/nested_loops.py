a = int(input('Для какого числа нужна таблица? '))
b = int(input('ДО какого числа нужна таблица? '))
c = int(input('Сколько нужно таблиц? '))

if b < 1:
    b = 1

for m in range(a, a + c):  # генерация множителей
    for i in range(1, b + 1):  # генерации таблицы
        print(f'{m} * {i} = {m * i}')
    print()