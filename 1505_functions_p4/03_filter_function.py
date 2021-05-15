mixed = ['греча', 'пшено', 'геркулес', 'лен',
         'пшено', 'греча', 'лен', 'греча', 'лен',
         'геркулес', 'лен', 'геркулес']

# сначала процедурный код
z = 'греча'
zol = []
for item in mixed:
    if z == item:
        zol.append(item)

print(zol)

# а теперь функциональный
zolushka = list(filter(lambda x: x == 'лен', mixed))
print(zolushka)

# достать только те числа, которые делятся на 2
# процедурка
numbers = [7, 17, 45, 12, 23, 16, 78, 32, 20, 11, 17, 55, 43]
even1 = []
for element in numbers:
    if element % 2 == 0:
        even1.append(element)
print(even1)

# функционалка
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)
