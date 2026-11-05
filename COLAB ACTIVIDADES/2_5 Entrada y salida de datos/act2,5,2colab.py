Numero1 = int(input("Dame un número."))
Numero2 = int(input("Dame otro número porfavor."))
Suma = Numero1 + Numero2
Resta = Numero1 - Numero2
División = Numero1 / Numero2
Multiplicación = Numero1 * Numero2
print("La suma es:", Suma)
print("La resta es:", Resta)
print("La multiplicación es:", Multiplicación)
if Numero2 != 0:
    print("La división es:", Numero1 / Numero2)
else:
    print("No se puede dividir entre cero.")