# Lista de estudiantes
Alumnos = []
def añadir_alumno(nombre):
    Alumnos.append(nombre)
def borrar_alumno(nombre):
    if nombre in Alumnos:
        Alumnos.remove(nombre)
    else:
        print ("El alumno no esta en la lista, intente otro porfavor.")
def enseñar_alumno():
    print("Lista de alumnos, cargando...")
    for alumno in Alumnos:
        print (alumno)

añadir_alumno ("Jaimito")
añadir_alumno ("Juancito")
añadir_alumno ("Pepito")

enseñar_alumno()

borrar_alumno("Pepito")
borrar_alumno("Kevincito")
enseñar_alumno()