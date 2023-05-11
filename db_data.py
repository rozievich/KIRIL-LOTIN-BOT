import os

import psycopg2

con = psycopg2.connect(
    user='postgres',
    database='postgres',
    password=os.getenv('DB_PASS'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT')
)

cur = con.cursor()


def create_table():
    query = '''
    CREATE TABLE IF NOT EXISTS users(
        user_id bigint unique not null,
        name varchar(100) not null,
        username varchar(54) not null,
        time timestamp default now()
    )
    '''
    admin_query = '''
    CREATE TABLE IF NOT EXISTS admins(
        user_id bigint unique not null,
        time timestamp default now()
    ) 
    '''
    cur.execute(query)
    cur.execute(admin_query)
    con.commit()


def get_users():
    query = 'SELECT * FROM users'
    cur.execute(query)
    return cur.fetchall()


def get_user(user_id: int):
    query = 'SELECT * FROM users WHERE user_id = %s'
    cur.execute(query, (user_id,))
    return cur.fetchone()


def register(user_id: int, name: str, username=None):
    query = 'INSERT INTO users(user_id, name, username) values (%s, %s, %s)'
    cur.execute(query, (user_id, name, username))
    con.commit()


def add_admin(user_id: int):
    query = 'INSERT INTO admins(user_id) values (%s)'
    cur.execute(query, (user_id,))
    con.commit()


def get_admins():
    query = 'SELECT * FROM admins'
    cur.execute(query)
    return cur.fetchall()


def get_admin(user_id: int):
    query = 'SELECT * FROM admins WHERE user_id = %s'
    cur.execute(query, (user_id,))
    user = cur.fetchone()
    return user


def delete_admin(user_id: int):
    query = 'DELETE FROM admins WHERE user_id = %s'
    cur.execute(query, (user_id,))
    con.commit()
