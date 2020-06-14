import notes_pakets.corp_notes as modelo


class Action:

    def new_note(self, usuario):
        print(f"Hola {usuario[1]}\nIniciamos")

        title = input("Introduce el titulo de nota: ")
        description = input("Ingrese la nota a guardar: ")

        nota = modelo.Note(usuario[0], title, description)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"Se a creado la nota {nota.titulo}")

        else:
            print(f"La nota no se guardo{usuario[1]}")

    def mostrar(self, usuario):
        print(f"{usuario[1]} estas son tus notas")

        nota = modelo.Note(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print(f"""
            ###########################
            {nota[2]}
            {nota[3]}            
            
            """)

    def borrar(self, usuario):
        print(f"\n Bien {usuario[1]}, selecciona la nota a borrar")

        nota = modelo.Note(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Se elimino la nota {nota.titulo}")
