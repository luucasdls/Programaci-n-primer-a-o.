class Autor:
    def __init__(self,nombre, nacionalidad):
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre (self, nuevo_nombre):
        if nuevo_nombre == "":
            print("El nombre no puede estar vacío.")
        else:
            self.__nombre = nuevo_nombre
    @property
    def nacionalidad(self):
        return self.__nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, nueva_nacionalidad):
        if nueva_nacionalidad == "":
            print("La nacionalidad no puede estar vacía.")
        else:
            self.__nacionalidad = nueva_nacionalidad

autor1 = Autor("J.K. Rowling", "Británica.")

print(autor1.nombre)
print(autor1.nacionalidad)
print("TESTEO DE SETTER.")
#Testeo el @nombre.setter
autor1.nombre = ""
#Testeo el @nacionalidad.setter
autor1.nacionalidad = ""






