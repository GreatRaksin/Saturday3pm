'''
1. Количество дней между сегодняшним днем и днем вашего рождения.
Сегодняшний день получать через функцию .today() или .now();
2. Сколько часов прошло с даты вашего рождения. Используйте метод
получения отдельных полей из класса datetime.
3. В какой день недели вы родились. Функция .weekday() возвращает число,
например, понедельник - это 0. Ваша программа должна выводить вместо 0 слово “понедельник”
'''
from datetime import *


def today_and_birthday(y, m, d, h=0, min=0):
    today = datetime.now()  # сохраняю сегодняшнюю дату
    birth = datetime(year=y, month=m, day=d, hour=h, minute=min)
    delta = today - birth
    return delta.days

days = today_and_birthday(2003, 7, 15)  # вот здесь число
print(f'Прошло {days} дней или {days / 365:.2f} лет')
print(f'Прошло {days * 24} часов.')


def translate_weekday(day, lang='rus'):
    days = [
        ['понедельник', 'monday'], ['вторник', 'tuesday'],
        ['среда', 'wednesday'], ['четверг', 'thursday'],
        ['пятница', 'friday'], ['суббота', 'saturday'],
        ['воскресенье', 'sunday']]
    if lang in ['rus', 'ru']:
        return days[day][0]
    else:
        return days[day][1]

birthday = datetime(2003, 5, 13).weekday()
print(translate_weekday(birthday, 'ru'))

days = ['понедельник', 'вторник', 'среда', 'четверг',
        'пятница', 'суббота', 'воскресенье']
print(days[birthday])
