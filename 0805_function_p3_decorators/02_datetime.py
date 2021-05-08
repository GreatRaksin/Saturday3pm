'''
datetime.date(y, m, d) - дата. Атрибуты год, месяц, день
datetime.time(h, m, s, ms) - время. Атрибуты: час, минута, секунда, микросекунда
datetime.timedelta() - разница между двумя точками во времени,
с точностью до микросекунд.
datetime.datetime(y, m, d, h, m, s, ms) - комбинация из времени
и даты
'''
#import datetime as dt
from datetime import *

today = datetime.now()
birthday = datetime(year=2015, month=5, day=28)
print(birthday.date())  # type => <class 'datetime.date'>
print(birthday.time())

print(today - birthday)
# хочу узнать дату за 5 дней до сегодня
print(today - timedelta(days=5))
# хочу узнать текущий день недели
print(today.weekday())  # -> 5  (потому что считаю с нуля)
