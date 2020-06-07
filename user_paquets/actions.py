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

    def login(self):
        print("Iniciar sesion: ")

        email = input("Ingrese su correo electronico: ")
        password = input("Ingrese su contraña: ")
        usuario = modelo.Usuarios('', '', email, password)

        login = usuario.login()
        try:
            if email == login[3]:
                print(f"Bienvenido: {login[1]}, sesion iniciada {login[5]}")
                self.proximasAcciones(login)

        except Exception as err:
            print(type(err).__name__)
            print("Usuario o passwd incorrectos.")

    def proximasAcciones(self, usuario):
        print("""
        Seleccione la opcion:
        
        * Crear notas (1)
        * Mostrar notas (2)
        * Eliminar notas (3)
        * Salir (0)
        """)

        opciones = True

        while opciones:

            try:
                opciones = int(input("SELECCIONE LA OPCION: "))

            except:
                input("Solo puedes seleccionar numeros.\nPreciones ENTER para continuar")


            if opciones == 1:
                print("DOCUMENTO SIN TITULO\n")

            elif opciones == 2:
                print("DOCUMENTO ARCHIVADO\n")

            elif opciones == 3:
                print("DOCUMENTO A ELIMINAR\n")

            elif opciones == 0:
                exit(f"Saliendo...{usuario[1]}")

