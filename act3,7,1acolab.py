libros = [105, 203, 101, 304, 150]

libros_ordenados = sorted(libros, reverse=True)

print("Lista original:", libros)
print("Lista ordenada:", libros_ordenados)

#Se usa sorted porque preserva la lista original y crea una copia alternativa, sort borra la lista original y la copia remplaza a la original.