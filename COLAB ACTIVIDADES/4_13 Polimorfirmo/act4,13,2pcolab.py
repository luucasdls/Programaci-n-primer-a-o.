class Autor:
    def biografia(self):
        print("Soy un autor y me dedico a crear obras.")


class Escritor(Autor):
    def biografia(self):
        print("Soy un escritor y me dedico a escribir libros.")


escritor = Escritor()


escritor.biografia()


super(Escritor, escritor).biografia()
