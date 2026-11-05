# Lista de estudiantes
Alumnos = []
opcion = 0
def añadir_alumno():
    nombre = input("¿Qué alumnos quieres añadir a la lista?")
    Alumnos.append(nombre)

def borrar_alumno():
    nombre_borrar = input("¿Qué nombre quieres borrar?")
    if nombre_borrar in Alumnos:
        Alumnos.remove(nombre_borrar)
    else:
        print ("El alumno no esta en la lista, intente otro porfavor.")

def enseñar_alumno():
    print("Lista de alumnos, cargando...")
    print(Alumnos)

def cerrar_lista():
    print("Cerrando la lista.")

while opcion != 4:
    print ("1- Agregar alumnos.")
    print("2- Borrar alumnos.")
    print("3- Ver lista de alumnos.")
    print("4- Salir del programa.")
    opcion =int(input("Selecciona la opción que desees."))
    if opcion == 1:
        añadir_alumno()
    elif opcion == 2:
        borrar_alumno()
    elif opcion == 3:
        enseñar_alumno()
    elif opcion == 4:
        cerrar_lista