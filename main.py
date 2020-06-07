from user_paquets import actions

# Proyecto Python y Mysql/Mariadb:

print("""
    -Login
    -Registro
""")

opcion = str(input("Escriba la opcion: ")).lower()

call_pakets = actions.Acciones()

if opcion == "registro":
    call_pakets.registro()

elif opcion == "login":
    call_pakets.login()
