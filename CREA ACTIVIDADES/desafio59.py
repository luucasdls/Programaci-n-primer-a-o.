class Libro:
    def __init__(self,titulo,autor,isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn


class LibroDigital(Libro):
    def __init__(self, titulo, autor, isbn,formato,tamaño_archivo):
        super().__init__(titulo, autor, isbn)
        self.formato = formato
        self.tamaño_archivo = tamaño_archivo

    def mostrar_informacion(self):
        print("Titulo:",self.titulo)
        print("Autor:",self.autor)
        print("ISBN:",self.isbn)
        print("Formato:",self.formato)
        print("Tamaño del archivo:",self.tamaño_archivo)

libro = LibroDigital(
    titulo = "Juego de tronos",
    autor = "George R.R Martin",
    isbn = "978-84-01-03242-4",
    formato = "PDF",
    tamaño_archivo = "20 MB"
)

class EBook(LibroDigital):
    def __init__(self, titulo, autor, isbn, formato, tamaño_archivo,enlace_descarga):
        super().__init__(titulo, autor, isbn, formato, tamaño_archivo)
        self.enlace_descarga = enlace_descarga

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Enlace de descarga:", self.enlace_descarga)


libro2 = EBook(
    titulo = "Juego de tronos",
    autor = "George R.R Martin",
    isbn = "978-84-01-03242-4",
    formato = "PDF",
    tamaño_archivo = "20 MB",
    enlace_descarga ="www.juegodetronos.com"
    )

#Con super() podemos tener acceso para reutilizar todas las características y funciones que esten establecidas dentro de la clase padre...
#en este ejemplo, la clase "LibroDigital" utiliza las características de su clase padre (Libro): 'titulo, autor, isbn'... 
#a su vez la clase "EBook" utiliza las características ya heredadas de "LibroDigital" y las añadidas 'formato, tamaño_archivo' a su vez que también reutiliza la función "mostrar_informacion"...
#que se creo en "LibroDigital", para posteriormente añadirle el enlace de descarga en la clase "EBook".

libro.mostrar_informacion()
print("========================")
libro2.mostrar_informacion()