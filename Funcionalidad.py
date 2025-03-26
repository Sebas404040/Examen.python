def registrar_artista():
    import json
    print("Ingrese la siguiente informacion:")
    nombre_artista=input("Nombre del artista: ")
    Pais_origen=input("Origen: ")
    años_actividad=input("Años de actividad: ")
    año_primer_disco=input("Año del primer disco que llego a las listas: ")
    print("Elija y escriba uno de los paises ya registrados: ")
    with open("paises.json", "r") as archivo1:
        mostrar_paises=json.load(archivo1)
        for clave in mostrar_paises.items():
            print ("pais")

    decicion_pais=input("Pais: ")
    ventas_raclamadas=input("Ventas: ")




def registrar_pais():
    import json
    from Intermediarios import paises
    codigo_iso=input("ISO: ")
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
    