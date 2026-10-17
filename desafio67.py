try:
    numero1 = int(input("Dame un número."))
    numero2 = int(input("Dame un número."))

    division = numero1 / numero2

    print ("El resultado da:", division)
except ZeroDivisionError:
    print("No podes dividir entre cero.")
except ValueError:
    print("Solo podes colocar números enteros.")
