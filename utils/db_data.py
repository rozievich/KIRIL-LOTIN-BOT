import psycopg2

con = psycopg2.connect(
    user='postgres',
    database='krill_db',
    password='black0613',
    host='localhost',
    port=5432
)

cur = con.cursor()


def create_table():
    query = '''
    CREATE TABLE IF NOT EXISTS users(
        id serial primary key,
        user_id varchar(50) not null,
        username varchar(54),
        time timestamp default now()
    )
    '''
    cur.execute(query)
    con.commit()


def get_users():
    query = 'SELECT * FROM users'
    cur.execute(query)
    return cur.fetchall()


def get_user(user_id: str):
    query = 'SELECT * FROM users WHERE user_id = %s'
    cur.execute(query, (user_id,))
    return cur.fetchone()


def register(user_id: str, username=None):
    query = 'INSERT INTO users(user_id, username) values (%s, %s)'
    cur.execute(query, (user_id, username))
    con.commit()
