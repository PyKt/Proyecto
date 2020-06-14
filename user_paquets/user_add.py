import hashlib
import datetime

import mysql

import user_paquets.db_connector as conexion

db_conections = conexion.connector()
database = db_conections[0]
cursor = db_conections[1]


class Usuarios:

    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):

        passwd_encryp = hashlib.sha384()
        passwd_encryp.update(self.password.encode('utf8'))

        fecha = datetime.datetime.now()

        try:
            cursor.execute("INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)",
                           (self.nombre, self.apellidos, self.email, passwd_encryp.hexdigest(), fecha))
            database.commit()
            print("Cuentra creada exitosamente.")


        except mysql.connector.Error:

            print(f"Error en email: {self.email}")

        return cursor

    def login(self):

        sql = "SELECT * FROM usuarios WHERE email = %s AND PASSWORD = %s"

        passwd_encryp = hashlib.sha384()
        passwd_encryp.update(self.password.encode('utf8'))
        usuario = (self.email, passwd_encryp.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()
        return result
