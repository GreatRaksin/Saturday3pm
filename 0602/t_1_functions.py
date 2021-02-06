'''
def function_name(parametr1, parametr2):
--->action_1
    action_2
    return result
'''


def YourName():
    print('Hello!')
    name = input('What is your name? ')
    return name


def SayHello(a):
    return f'Hello, {a}!'


# print(YourName, SayHello)
# name = YourName()  # сохраняю результат работы функции YourName() в переменную

# print(SayHello(name))   печатаю результат работы функции SayHello()
'''
Task 1.
Сделайте функцию, которая принимает два числа и действие
+, -, /, *
Функция должна вернуть результат в виде числа.
'''


def calculator(a, b, action):
    a = int(a)
    b = int(b)
    '''Сохраняю числа как числа'''
    if action == '+':
        return a + b
    elif action == '-':
        return a - b
    elif action == '*':
        return a * b
    elif action == '/':
        return a / b
    else:
        return 'Ошибка!'


print(calculator(5, 0, '/'))
