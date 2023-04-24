import redis

# Conexión con la base de datos de Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Función para agregar una palabra al diccionario
def agregar_palabra():
    palabra = input("Ingrese la palabra que desea agregar: ")
    definicion = input("Ingrese la definición de la palabra: ")
    r.set(palabra, definicion)
    print("La palabra se ha agregado correctamente.")

# Función para mostrar todas las palabras del diccionario
def mostrar_palabras():
    keys = r.keys()
    if keys:
        for key in keys:
            palabra = key.decode('utf-8')
            definicion = r.get(palabra).decode('utf-8')
            print(f"{palabra} - {definicion}")
    else:
        print("No hay palabras en el diccionario.")

# Función para eliminar una palabra del diccionario
def eliminar_palabra():
    palabra = input("Ingrese la palabra que desea eliminar: ")
    if r.delete(palabra):
        print("La palabra se ha eliminado correctamente.")
    else:
        print("La palabra no existe en el diccionario.")

# Función para editar la definición de una palabra en el diccionario
def editar_palabra():
    palabra = input("Ingrese la palabra que desea editar: ")
    definicion = input("Ingrese la nueva definición de la palabra: ")
    if r.exists(palabra):
        r.set(palabra, definicion)
        print("La definición de la palabra se ha actualizado correctamente.")
    else:
        print("La palabra no existe en el diccionario.")

# Función para mostrar el menú principal
def mostrar_menu():
    while True:
        print("\nBienvenido al diccionario")
        print("1. Agregar palabra")
        print("2. Mostrar palabras")
        print("3. Eliminar palabra")
        print("4. Editar palabra")
        print("5. Salir")
        opcion = input("Ingrese la opción que desea: ")
        if opcion == "1":
            agregar_palabra()
        elif opcion == "2":
            mostrar_palabras()
        elif opcion == "3":
            eliminar_palabra()
        elif opcion == "4":
            editar_palabra()
        elif opcion == "5":
            break
        else:
            print("Opción inválida, intente de nuevo.")

# Mostrar el menú principal
mostrar_menu()
