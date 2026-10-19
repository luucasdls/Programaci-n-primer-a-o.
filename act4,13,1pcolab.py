class Musico:
        def instrumento(self):
            print("El músico toca un instrumento")


class Guitarrista(Musico):
      def instrumento(self):
        print("El guitarrista toca la guitarra")


class Baterista(Musico):
     def instrumento(self):
        print("El baterista toca la batería")


musico = Musico()
guitarrista = Guitarrista()
baterista = Baterista()


musico.instrumento()
guitarrista.instrumento()
baterista.instrumento()


