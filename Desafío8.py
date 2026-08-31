#Desafío 8, encontrando multiplos de números enteros.
try:
    Numero = int(input("Escriba un número entero porfavor."))
    #Formula para encontrar el operador módulo.
        # Verifica si es múltiplo de 2.
    if Numero % 2 == 0:
        print ("El numero entero es multiplo de 2.")
    else:
        print("El número no es múltiplo de 2.")
        # Verifica si es múltiplo de 3.
    if Numero % 3 == 0:
        print ("El numero entero es multiplo de 3.") 
    else:
        print("El número no es múltiplo de 3.")
        # Verifica si es múltiplo de 5.
    if Numero % 5 == 0:
        print ("El numero entero es multiplo de 5.") 
    else:
        print("El número no es múltiplo de 5.")
        # Verifica si es múltiplo de 7.
    if Numero % 7 == 0:
        print ("El numero entero es multiplo de 7.")
    else:
        print("El número no es múltiplo de 7.")
        # Verifica si es múltiplo de 9.
    if Numero % 9 == 0:
        print ("El numero entero es multiplo de 9.")
    else:
        print("El número no es múltiplo de 9.")
        # Verifica si es múltiplo de 10.
    if Numero % 10 == 0:
        print ("El numero entero es multiplo de 10.")
    else:
        print("El número no es múltiplo de 10.") 
        # Verifica si es múltiplo de 11.
    if Numero % 11 == 0:
        print ("El numero entero es multiplo de 11.") 
    else:
        print("El número no es múltiplo de 11.")
except:
        print ("Esto no es un número entero, intenta de nuevo.")
