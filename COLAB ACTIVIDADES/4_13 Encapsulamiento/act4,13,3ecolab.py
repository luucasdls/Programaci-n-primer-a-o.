class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__libros = []

    def agregar_libro(self, libro):
        self.__libros.append(libro)

    def obtener_libros(self):
        return self.__libros

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo

def titulos_libros(autor):
    libros = autor.obtener_libros()
    titulos = []

    for libro in libros:
        titulos.append(libro.titulo)

    return titulos

autor = Autor("Gabriel García Márquez")

libro1 = Libro("Cien años de soledad")
libro2 = Libro("El amor en los tiempos del cólera")

autor.agregar_libro(libro1)
autor.agregar_libro(libro2)

print(titulos_libros(autor))