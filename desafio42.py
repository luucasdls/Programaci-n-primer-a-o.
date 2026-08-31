def invertir_palabras(oracion):
    #Si no hay ningun espacio en la oración, significa que queda solo una palabra, la recursividad finaliza.
    if " " not in oracion:
        return oracion
    #Buscamos el primer espacio de la oración
    posicion = oracion.find(" ")
    #Guardamos la primer palabra de la oración
    primera = oracion[:posicion]
    #Las palabras que estan despues del primer espacio las guardamos tambien.
    resto = oracion[posicion + 1:]
    #La primer palabra se guarda en la función, luego seguimos con el resto sucesivamente, hasta que no hayan más espacios.
    return invertir_palabras(resto) + " " + primera


oracion = input("Ingrese una oración: ")
#La oración devuelve a la inversa la oración en la forma como fue escrita, por la recursividad que se produjo en las variables (primera y resto).
resultado = invertir_palabras(oracion)

print(resultado)