from user_paquets import actions

# Proyecto Python y Mysql/Mariadb:


while True:

    print("""
    - Login
    - Registro\n
    - Salir
""")
    
    opcion = str(input("Escriba la opcion: ")).lower()

    call_pakets = actions.Acciones()


    if opcion == "registro":
        call_pakets.registro()

    elif opcion == "login":
        call_pakets.login()

    elif opcion == "salir":
        exit("saliendo del programa")
        
    else:
        print("Opcion no reconocida")
        
