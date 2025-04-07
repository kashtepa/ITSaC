import psycopg2
from datetime import datetime
def getUsers():
    res =[]
    try:
        conn = psycopg2.connect('postgresql://postgres:1111@localhost:5432/postgres')
        cursor = conn.cursor()

        # Получаем список всех пользователей
        cursor.execute('SELECT * FROM users')
        all_users = cursor.fetchall()
        cursor.close()  # закрываем курсор
        conn.close()  # закрываем соединение
        for user in all_users:
            us = {
                'id': user[0],
                'name': user[1],
                'email': user[2],
                'group': user[3]

            }
            res.append(us)

    except:

        print('Can`t establish connection to database')
    return res

if __name__ == '__main__':
    getUsers()