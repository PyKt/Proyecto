import mysql.connector


def connector():
    database = mysql.connector.connect(
        host='localhost',
        user='alberto',
        passwd='fava',
        database='users_db',
        port=3306
    )

    cursor = database.cursor(buffered=True)

    return [database, cursor]
