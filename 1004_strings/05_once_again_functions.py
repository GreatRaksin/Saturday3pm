'''
процедура - набор команд, исполнение которых
приводит к результату

функция - именованный набор команд, возвращающий
результат своей работы как объект

метод - именованный набор команд, возвращающий
результат своей работы как объект (работает с классами)
'''
import sqlite3


db = sqlite3.connect('main.db')


def normalize_phone_number(phone):
    """ превращает номер телефона в нормальный вид"""
    res = ''
    restrictedSymbols = '+-() .!'
    for symbol in phone:
        if symbol not in restrictedSymbols:
            res += symbol
    return res


def insert_into_db(phone, connection):
    cur = connection.cursor()
    query = '''INSERT INTO phones (number) 
    VALUES (?)'''
    cur.execute(query, (phone,))
    connection.commit()
    connection.close()


phone = input('Введите номер телефона (без пробелов): ')

normal = normalize_phone_number(phone)
insert_into_db(normal, db)
