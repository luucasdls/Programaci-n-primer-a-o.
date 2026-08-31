Nombre = str(input("¿Cual es tú nombre?"))
Apellido = str(input("¿Cual es tú apellido?"))
Nacimiento = int(input("¿En qué año naciste?"))
Actual = int(input("¿En qué año estas respondiendo esto?"))
EdadUs = Actual - Nacimiento
print("El usuario", Nombre , Apellido , "Nació en el año de" , Nacimiento , "Y tiene", EdadUs , "Años de edad.")