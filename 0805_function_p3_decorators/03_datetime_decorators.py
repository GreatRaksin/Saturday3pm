from datetime import *


def not_at_night(func):
    def wrapper(open, close, obed):
        if open < datetime.now().hour < close:
            func(open, close, obed)
        elif obed == datetime.now().hour:
            print('У нас сейчас обед!')
        else:
            print(f'Мы закрыты! Рабочий день с {open}:00 до {close}:00')
    return wrapper


@not_at_night
def create_task(o, c, i):
    print('Ваш заказ оформлен!')


create_task(9, 23, 13)
create_task(17, 6, 16)
