import user_paquets.user_add as modelo


class Acciones:

    def registro(self):
        print("Inicio de registro: ")

        nombre = str(input("Nombre: "))
        apellido = str(input("Apellidos: "))
        email = str(input("Ingrese su correo electronico: "))
        password = str(input("Ingrese su contraña: "))
        usuario = modelo.Usuarios(nombre, apellido, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print("Cuentra creada exitosamente!")

    def login(self):
        print("Iniciar sesion: ")

        email = input("Ingrese su correo electronico: ")
        password = input("Ingrese su contraña: ")
        print("Bienvenido usuario")
