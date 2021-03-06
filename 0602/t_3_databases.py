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


def create_project(db, project):
    sql = '''INSERT INTO projects (name, begin_date, end_date)
    VALUES (?,?,?)
    '''
    # вставить в таблицу проекты значения (переменная, переменная, переменная)
    cur = db.cursor()
    cur.execute(sql, project)
    db.commit()
    return cur.lastrowid


def create_task(db, project):
    sql = '''INSERT INTO projects (name, begin_date, end_date)
    VALUES (?,?,?)
    '''
    # вставить в таблицу проекты значения (переменная, переменная, переменная)
    cur = db.cursor()
    cur.execute(sql, project)
    db.commit()
    return cur.lastrowid

db = 'tables.db'
create_projects_table = '''CREATE TABLE IF NOT EXISTS projects (
    id integer PRIMARY KEY,
    name text NOT NULL,
    begin_date datetime,
    end_date datetime
)
'''
create_tasks_table = '''CREATE TABLE IF NOT EXISTS tasks (
    id integer PRIMARY KEY,
    name text NOT NULL,
    project_id integer NOT NULL,
    status_id integer NOT NULL,
    begin_date datetime,
    end_date datetime,
    FOREIGN KEY (project_id) REFERENCES projects (id)
)'''

conn = create_connection(db)

# создаем таблицы в БД
if conn is not None:
    create_table(conn, create_projects_table)
    create_table(conn, create_tasks_table)
else:
    print('Ошибка! Не получилось создать подключение к БД')