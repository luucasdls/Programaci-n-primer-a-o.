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

autor1.agregar_libro("Harry Potter y la piedra filosofal.")
autor1.agregar_libro("Harry Potter y la cámara secreta.")
autor1.agregar_libro("Harry Potter y el prisionero de Azkaban.")

print("Autor:", autor1.nombre)
print("Libros escritos:")
for libro in autor1.libros:
    print("-", libro)

autor1.eliminar_libro("Harry Potter y la cámara secreta.")

print("\nDespués de eliminar un libro queda así:")
print("Autor:", autor1.nombre)
for libro in autor1.libros:
    print("-", libro)