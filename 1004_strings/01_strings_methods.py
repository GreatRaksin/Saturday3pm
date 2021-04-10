'''Ошибки'''

print('Hello, I\'m \a Py\tho\n developer!')
'''
\n - новая строка
\t - табуляция (4 пробела)
\a - пробел
\' - заигнорить кавычку
'''  # <- строка?  да

'''Методы'''

name = 'deMid raKsIn'
print(name.title())  # title() - сделать каждое слово (после пробела) с большой буквы
print(name.lower())  # lower() - приводит все символы к нижнему регистру (маленькие)
print(name.upper())  # upper() - приводит все символы к верхнему регистру (капс)
language = ' python '
print(language)
print(language.rstrip().lstrip())
'''
.lstrip() - убирает пробел слева
.rstrip() - убирает пробел справа
.strip() - убирает пробелы с двух сторон
'''

string1 = 'Hello, World!'
print(string1.replace('H', 'J'))
print(string1.split(','))
print(''.join(['р', 'а', 'б', 'о', 'т', 'а']))
'''
.replace('a', 'b') заменяет символ a в строке на символ b
.split(separator) - превращает строчку в список по разделителю, указанному в separator
.join(iterator) - добавляет все символы из iterator к строке
.count(symbol) - посчитать количество symbol в строке
.startswith(x) - начинается ли строка символом x
.endswith(x) - заканчивается ли строка символом x
.count(x) - считает количество вхождений символа x в строке
.swapcase() - меняет большой регистр на маленький и наоборот
'''
