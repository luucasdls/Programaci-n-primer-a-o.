def resaltar(texto,palabra, inicio):
    posicion = texto.find(palabra, inicio)
    if posicion == -1:
        return 
    
    print("Encontre",palabra,"en la posición:", posicion)
    return resaltar(texto,palabra,posicion + 1)

texto = ("Me gusta Python , adoro Python , amo a Python")
palabra = ("Python")

(resaltar(texto,palabra, 0))