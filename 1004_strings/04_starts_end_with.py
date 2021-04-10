answer = input('Введите да или нет: ')
while answer.startswith(('д', 'Д', 'l', 'L')):
    answer = input('Введите да или нет: ')

answer2 = input('Введите слово, которое заканчивается на букву А: ')
while answer.endswith('А'):
    answer2 = input('Введите слово, которое заканчивается на букву А: ')