def registrar_artista():
    import json
    print("Ingrese la siguiente informacion:")
    nombre_artista=input("Nombre del artista: ").strip()
    print("Elija y escriba uno de los paises ya registrados: ")
    with open("paises.json", "r") as archivo1:
        mostrar_paises=json.load(archivo1)
        for codigo in mostrar_paises.items():
            print ("Nombre ", codigo["Nombre del pais"])
    decision_pais=input("Elija un pais: ")
    Pais_origen= decision_pais
    años_actividad=input("Años de actividad: ")
    año_primer_disco=input("Año del primer disco que llego a las listas: ")
    print("Cuantos generos pertenece el artista")
    print("Elija y escriba el id de los paises ya registrados: ")
    with open("generos.json", "r") as archivo3:
        mostrar_generos=json.load(archivo3)
        for codigo1 in mostrar_generos.items():
            print ("Nombre ", codigo1["Nombre del pais"])
    decision_genero=input("Elija un genero:")
    gender=decision_genero
    ventas_raclamadas=input("Ventas: ")
    artista= {
        "Nombre del artista": nombre_artista,
        "pais de origen": Pais_origen,
        "años actividad": años_actividad,
        "año de primer disco": año_primer_disco,
        "genero musical": gender,
        "ventas reclamadas": ventas_raclamadas
    }
    with open ("artistas.json", "w") as guardar_artistas:
        json.dump(artista, guardar_artistas, indent=4)
def registrar_pais():
    import json
    from Intermediarios import paises
    from Menu_1 import menu_principal
    codigo_iso=input("ISO: ").strip()
    try:
        with open ("paises.json", "r") as recarga:
            paises=json.load(recarga)
    except(FileNotFoundError, json.JSONDecodeError):
        paises={}

    print("Ingrese los datos del pais:")
    nombre_pais=input("Nombre del pais: ")
    codigo_iso3=input("ISO3: ")
    pais= {
        "Nombre del pais": nombre_pais,
        "Codigo ISO3": codigo_iso3
    }
    paises[codigo_iso]=pais
    with open ("paises.json", "w") as guardar:
        json.dump(paises, guardar, indent=4)
    menu_principal()

def registrar_genero():
    from Menu_1 import menu_principal
    import json
    from Intermediarios import generos
    id_genero=input("Ingrese el ID del genero: ")
    try:
        with open("generos.json", "r") as archivo2:
            generos=json.load(archivo2)
    except (FileNotFoundError, json.JSONDecodeError):
        generos={}
    print ("Ingrese la descripcion del genero")
    descripcion_genero=input("Ingrese una descripcion: ")
    genero={
        "Descripcion del genero": descripcion_genero
    }
    generos[id_genero]=genero
    with open ("generos.json", "w") as guardar2:
        json.dump(generos, guardar2, indent=4)
    menu_principal()
    

