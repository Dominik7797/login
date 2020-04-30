from psycopg2.extras import RealDictCursor
import database_common


@database_common.connection_handler
def get_users(cursor: RealDictCursor, user_name) -> list:
    query = """
        SELECT *
        FROM users
        WHERE user_name = %(user_name)s;"""
    cursor.execute(query, {"user_name": user_name})
    return cursor.fetchall()


@database_common.connection_handler
def insert_register(cursor: RealDictCursor, users: dict):
    query = """
        INSERT INTO users (user_name, password)
        VALUES (%(u_name)s, %(p_word)s);"""
    cursor.execute(query, {
        'u_name': users['user_name'],
        'p_word': users['password']
    })
    return
