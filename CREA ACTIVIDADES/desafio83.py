estudiantes = [
    "Adrián",
    "Beatriz",
    "Carlos",
    "Daniela",
    "Elena",
    "Fernando",
    "Gabriel",
    "Lucia"
]

def busqueda_binaria(estudiantes, buscado):
    inicio = 0
    fin = len(estudiantes) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if estudiantes[medio] == buscado:
            print("Estudiante encontrado:", estudiantes[medio])
            return
    
        elif estudiantes[medio] < buscado:
            inicio = medio + 1

        else:
            fin = medio - 1

    print("El estudiante no se encuentra en la lista.")

busqueda_binaria(estudiantes, "Elena")
print("=========================")
busqueda_binaria(estudiantes, "Juan")

