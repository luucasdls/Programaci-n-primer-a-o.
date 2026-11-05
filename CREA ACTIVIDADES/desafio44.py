libros = []
opcion = 0
def añadir_libros():
    libro = input("Nombre del libro")
    autor = input("Nombre del autor")
    libros.append([
         libro,
         autor
    ])
    print("Libro añadido correctamente.")
def borrar_libros():
    borrar = input("Nombre del libro a borrar") 
    for libro in libros:
        if libro[0] == borrar:
            libros.remove(libro)
            print("Libro eliminado.")
            break
    else:
        print("Ese libro no existe, intenta con otro nombre.")

def ver_libros():
    print("Mostrando la biblioteca actualmente.")
    for libro in libros:
        print(
            "-", libro[0],
            "-", libro[1]
        )
def buscar_libros():
    buscar = input("Ingresa el libro a buscar.")
    for libro in libros:
        if libro[0] == buscar:
            print("El libro", buscar,
                   "se encuentra en la libreria.")
            break
    else:
        print("El libro", buscar,
              "no esta en la libreria, intenta con otro nombre.")
while opcion != 5:
    print("\nBienvienido a la biblioteca de CREA.")
    print("1- Añadir un libro en la biblioteca.")
    print("2- Borrar un libro de la biblioteca.")
    print("3- Ver todos los libros de la biblioteca.")
    print("4- Buscar un libro en la biblioteca.")
    print("5- Salir de la biblioteca.")
    opcion =  int(input("Elige una opción que necesites."))
    if opcion == 1:
        añadir_libros()
    elif opcion == 2:
        borrar_libros()
    elif opcion == 3:
        ver_libros()
    elif opcion == 4:
        buscar_libros()
    elif opcion == 5:
        print("Cerrando la biblioteca, ¡Vuelva pronto!")
    else:
        print("Opción incorrecta, intenta nuevamente.")

