#Pedimos al usuario que de su altura y peso, cada input con su respectiva variable.
Peso = float(input("¿Cuanto pesas?"))
Altura = float(input("¿Cual es tu estatura?"))
if Altura > 0:    
    imc = Peso / Altura**2
    print("El IMC de usted es:" ,imc)
else:
    print("La altura debe ser mayor a 0")