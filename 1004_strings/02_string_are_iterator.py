'''Строчки - это итераторы'''
a = 'hello'
b = ['h', 'e', 'l', 'l', 'o']

for letter in a:
    print(letter)

phone = input('Введите номер телефона (без пробелов): ')
db_phone = ''
restrictedSymbols = '+-() .!'
#l = []
for symbol in phone:
    if symbol not in restrictedSymbols:
        db_phone += symbol
        #l.append(symbol)
#db_phone = db_phone.join(l)
print(db_phone)

'''string = input('Введите строку: ')
what = input('Какой символ нужно убрать?')
l = ''
for letter in string:
    if letter not in what:
        l += letter
print(l)'''
