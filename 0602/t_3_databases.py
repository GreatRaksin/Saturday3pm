import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ создает подключение к БД, БД передается параметром
    :param db_file - файл БД, к которой нужно подключаться
    :return Объект подключения или None
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        '''Пробую подключиться к базе, название
        которой мне передает пользователь. В случае
        успеха сообщу об этом'''
        return connection
    except Error as e:
        '''Если возникает ошибка, я хочу ее распечатать'''
        print(e)

    return connection


def create_table(conn, create_table_SQL):
    """ создает таблицу
    :param conn - к чему подключаемся
    :param create_table_SQL - запрос на создание таблицы
    """
    try:
        c = conn.cursor() # пытаюсь создать манипулятор для БД
        c.execute(create_table_SQL)  # если получается, направляю запрос через .execute()
    except Error as e:
        print(e)
