def menu_principal():
    from Funcionalidad import registrar_artista, registrar_pais, registrar_genero
    print("Bienvenido")
    print("""
    1. Registrar artistas
    2. Registrar genero musical
    3. Registrar pais
    4. Informes
    5. Salir
    """)
    try:
        while True:
            print("Ingrese una opcion: ")
            decision_main=int(input("Opcion: "))
            if decision_main>5 or decision_main<1:
                print("Opcion incorrecta, no existe esa opcion")
            elif decision_main==1:
                print("Registrar artistas")
                registrar_artista()
            elif decision_main==2:
                print ("Registrar genero musical")
                registrar_genero()
            elif decision_main==3:
                print ("Registrar pais")
                registrar_pais()
            elif decision_main==4:
                print ("Informes")
            elif decision_main==5:
                print("Saliendo...")
                break
    except (ValueError):
        print("Ingreso un valor no valido")