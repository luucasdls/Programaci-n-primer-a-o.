def notas():
    total = 0
    for i in range(5):
        alumno_nota = int(input("Dame una nota:"))
        total = total + alumno_nota

    promedio = total / 5
    print("LISTA DE PROMEDIOS DE ALUMNOS")
    print("Total de puntaje:", total)
    print("Promedio de las notas:", promedio)

notas()