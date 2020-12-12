my_str = input('Введите строку: ')
sum = 0
restricted_symbols = [',', '.', '!', '?', '-', ';', ':', ' ']

for letter in my_str:
    if letter not in restricted_symbols:
        sum += 1

print(f'Количество букв: {sum}.')