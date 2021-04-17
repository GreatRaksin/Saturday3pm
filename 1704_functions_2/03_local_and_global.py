res = 0

a = int(input('Введите А: '))
b = int(input('Введите В: '))


def rect(a, b):
    res = a * b
    return res


def triang(a, b):
    res = a * b * 0.5
    return res


fig = int(input('1 - квадрат, 2 - треугольник'))
if fig == 1:
    rect(a, b)
    print(res)
else:
    triang(a, b)
    print(res)