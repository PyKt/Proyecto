import mysql.connector
import datetime
database = mysql.connector.connect(
    host="localhost",
    user="alberto",
    passwd="fava",
    database="users_db",
    port=3306
)

cursor = database.cursor(buffered=True)


class Usuarios:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()
        sql = "INSERT INTO users_db VALUES(null, %s, %s, %s, %s, %s,)"
        usuario = (self.nombre, self.apellidos, self.apellidos, fecha)

        cursor.execute(sql, usuario)
        database.commit()

        return [cursor.rowcount, self]