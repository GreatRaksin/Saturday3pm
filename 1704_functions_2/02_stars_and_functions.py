def multiply(n, n1, n2):
    print(n * n1 * n2)


fruits = ['lemon', 'pear', 'watermelon', 'grape']

# ТАК НЕ НАДО: print(fruits[0], fruits[1], fruits[2], fruits[3])
# НАДО ВОТ ТАК:
print(*fruits)


def insert_into_list(*numbers):
    l = []
    l.append(numbers)
    return numbers


'''
*args - * позволяет передать функции неопределенное количество
аргументов.
**kwargs - **keyword arguments - позволяет передать функции 
неопределенное количество !именованных! аргументов
'''


def fun(**kwargs):
    print(f'Type of argument is {type(kwargs)}')
    print(kwargs)
    for key, value in kwargs.items():
        print(f'{key} == {value}')


fun(name='Colt', surname='Steel', hobby='Programming')
