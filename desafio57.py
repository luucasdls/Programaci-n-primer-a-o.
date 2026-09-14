class Autor:
    def __init__(self,nombre,nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

class Poeta(Autor):
    def __init__(self, nombre, nacionalidad,tipo_poesia):
        super().__init__(nombre, nacionalidad)
        self.tipo_poesia = tipo_poesia

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Nacionalidad:", self.nacionalidad)
        print("Tipo de poesía:", self.tipo_poesia)

poeta1 = Poeta("Pablo Neruda", "Chilena", "Lírica")
poeta2 = Poeta("Federico García Lorca","Española","Lírica")

poeta1.mostrar_datos()
print("====================")
poeta2.mostrar_datos()
#La herencia permite reutilizar atributos y métodos de una clase ya existente, en este caso 'autor' y agregar nuevas características a la nueva clase 'poeta' sin tener que programar todo nuevamente.