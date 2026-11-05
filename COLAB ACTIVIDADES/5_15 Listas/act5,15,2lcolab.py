productos = [1,2,3,4,5,6,7,8,9]
busqueda = int(input("¿Qué codigo de productos quieres encontrar?"))
if busqueda in productos:
    print("¡Ese código si esta en la lista! Esta en la posición:", productos.index(busqueda))
else:
    print("Ese código no esta en la lista, intenta otro.")
