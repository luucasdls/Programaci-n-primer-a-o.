biblioteca1 = []
biblioteca2 = []
opcion = 0
def añadir_libros(biblioteca):
    libro = input("Nombre del libro")
    autor = input("Nombre del autor")
    biblioteca.append([
         libro,
         autor
    ])
    print("Libro añadido correctamente.")
def borrar_libros(biblioteca):
    borrar = input("Nombre del libro a borrar") 
    for libro in biblioteca:
        if libro[0] == borrar:
            biblioteca.remove(libro)
            print("Libro eliminado.")
            break
    else:
        print("Ese libro no existe, intenta con otro nombre.")

def ver_libros(biblioteca):
    print("Mostrando la biblioteca actualmente.")
    for libro in biblioteca:
        print(
            "-", libro[0],
            "-", libro[1]
        )
def buscar_libros(biblioteca):
    buscar = input("Ingresa el libro a buscar.")
    for libro in biblioteca:
        if libro[0] == buscar:
            print("El libro", buscar,
                   "se encuentra en la libreria.")
            break
    else:
        print("El libro", buscar,
              "no esta en la libreria, intenta con otro nombre.")
while opcion != 9:
    print("\nBienvienido a la biblioteca de CREA.")
    print("1- Añadir un libro en la biblioteca1.")
    print("2- Añadir un libro en la biblioteca2.")
    print("3- Borrar un libro de la biblioteca1.")
    print("4- Borrar un libro de la bibliotec2.")
    print("5- Ver todos los libros de la biblioteca1.")
    print("6- Ver todos los libros de la biblioteca2.")
    print("7- Buscar un libro en la biblioteca1.")
    print("8- Buscar un libro en la biblioteca2.")
    print("9- Salir de la biblioteca.")
    opcion =  int(input("Elige una opción que necesites."))
    if opcion == 1:
        añadir_libros(biblioteca1)
    elif opcion == 2:
        añadir_libros(biblioteca2)
    elif opcion == 3:
        borrar_libros(biblioteca1)
    elif opcion == 4:
        borrar_libros(biblioteca2)
    elif opcion == 5:
        ver_libros(biblioteca1)
    elif opcion == 6:
        ver_libros(biblioteca2)
    elif opcion == 7:
        buscar_libros(biblioteca1)
    elif opcion == 8:
        buscar_libros(biblioteca2)
    elif opcion == 9:
        print("Cerrando la biblioteca, ¡Vuelva pronto!")
    else:
        print("Opción incorrecta, intenta nuevamente.")
