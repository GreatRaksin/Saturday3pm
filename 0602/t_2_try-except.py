'''
Ошибки (Errors) - это когда накосячили ВЫ
Исключения (Exceptions) - когда косячите НЕ вы
'''


def divider(a, b):
    try:
        '''Попробовать преобразовать числа'''
        a = int(a)
        b = int(b)
        return a / b
    except ZeroDivisionError:
        '''Если пытаются делить на ноль, написать об этом'''
        print('На 0 делить нельзя!')
        return 0
    except (TypeError, ValueError):
        '''Если ввели что-то, что нельзя сделать числом, написать об этом'''
        print('Вы ввели не число!')
        return 0




print(divider(5, 6))
print(divider(1, 'питнацать'))
print(divider(3, 99))
print(divider(4, 0))
print('Этот код не сработает')