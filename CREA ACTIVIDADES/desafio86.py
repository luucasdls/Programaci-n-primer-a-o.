libro1 = input("¿Qué libro quieres pedir prestado?(El préstamo dura 15 días, si quiere renovarlo, tramitar en dicho caso.)")
nombre_prestatario = input("¿Cuál es tu nombre?")
fecha_prestamo = input("¿En qué fecha fue prestado?(En formato DD/MM/AA)")

with open("prestamos.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Libro prestado: " + libro1 + "\n")
    archivo.write("=====================\n")
    archivo.write("Usuario prestatario: " + nombre_prestatario + "\n")
    archivo.write("=====================\n")
    archivo.write("Fecha del préstamo: " + fecha_prestamo + "\n")