try:
    numero1 = int(input("Dame un número:"))
    numero2 = int(input("Dame otro número"))

    suma = numero1 + numero2
    resta = numero1 - numero2 
    division = numero1 / numero2
    multiplicacion = numero1 * numero2
    
    print("La suma del n1 y n2 da:", suma)
    print("La resta del n1 y n2 da:", resta)
    print("La división del n1 y n2 da:", division)
    print("La multiplicación del n1 y n2 da:", multiplicacion)

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

except ValueError:
    print("Error: Solo puedes ingresar números enteros.")

except TypeError:
    print("Error: Los tipos de datos no son compatibles entre si.")