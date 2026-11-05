class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self,libro):
        self.libros.append(libro)

    def eliminar_libro(self,libro):
        if libro in self.libros:
            self.libros.remove(libro)

autor1 = Autor("J.K. Rowling")

class Libro:
    def __init__(self,titulo,genero,isbn):
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
libro1 = Libro(
    "Harry Potter y la piedra filosofal.",
    "Fantasía.",
    "978-84-9838-266-2"
)

libro2 = Libro(
    "Harry Potter y la cámara secreta.",
    "Fantasía.",
    "978-84-9838-267-9"
)

libro3 = Libro(
    "Harry Potter y el prisionero de Azkaban.",
    "Fantasía.",
    "978-987-800-012-1"
)

autor1 = Autor("J.K. Rowling", [libro1, libro2, libro3])

autor1.agregar_libro(libro1)
autor1.agregar_libro(libro2)
autor1.agregar_libro(libro3)


print("Autor:", autor1.nombre)
print("Libros escritos:")
for libro in autor1.libros:
    print("-", libro.titulo)
    print("Género:", libro.genero)
    print("ISBN:", libro.isbn)



