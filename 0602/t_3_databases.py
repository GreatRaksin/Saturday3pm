import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        '''Пробую подключиться к базе, название
        которой мне передает пользователь. В случае
        успеха сообщу об этом'''
        print('Подключено!')
    except Error as e:
        '''Если возникает ошибка, я хочу ее распечатать'''
        print(e)
    finally:
        if connection:
            '''Если у меня все получилось, закрываю подключение'''
            connection.close()


create_connection('test.db')
