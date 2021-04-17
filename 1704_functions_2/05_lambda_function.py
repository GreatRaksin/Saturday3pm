import math


def sq_root(x):
    return math.sqrt(x)


square_root = lambda x: math.sqrt(x)

pi_const = round(math.pi, 2)
# округляю число π до 2 знаков после запятой
print((lambda radius: pi_const * (radius ** 2)) (5))
print((lambda radius: pi_const * (radius ** 2)) (12))
print((lambda radius: pi_const * (radius ** 2)) (26))


def circle_square(radius):
    return pi_const * (radius ** 2)