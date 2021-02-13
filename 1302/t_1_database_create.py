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
        c = conn.cursor()  # пытаюсь создать манипулятор для БД
        c.execute(create_table_SQL)  # если получается, направляю запрос через .execute()
    except Error as e:
        print(e)


def create_project(db, project):
    sql = '''INSERT INTO projects (name, begin_date, end_date)
    VALUES (?,?,?)'''
    # вставить в таблицу проекты значения (переменная, переменная, переменная)
    cur = db.cursor()
    cur.execute(sql, project)
    db.commit()
    return cur.lastrowid


def create_task(db, project):
    sql = '''INSERT INTO tasks (name, project_id, status_id, begin_date, end_date)
    VALUES (?,?,?,?,?)'''
    cur = db.cursor()
    cur.execute(sql, project)
    db.commit()
    return cur.lastrowid


def update_task(db, task):
    sql = '''UPDATE tasks
            SET status_id = ?,
            begin_date = ?,
            end_date = ?'''
    conn = db.cursor()
    conn.execute(sql, task)
    db.commit()




db = 'tables.db'
conn = create_connection(db)

with conn:
    '''
    project = ('Создать БД', '2021-02-06', '2021-02-13')
    project_id = create_project(conn, project)
    # сюда сохранится ID проекта
    task_1 = ('Построить таблицы внутри', project_id, 1, '2021-02-06', '2021-02-13')
    task_2 = ('Обновить данные', project_id, 1, '2021-02-13', '2021-02-15')

    create_task(conn, task_1)
    create_task(conn, task_2)'''
    update_task(conn, (2, '2021-02-14', '2021-03-01'))