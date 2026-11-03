class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

raiz = Nodo(10)

izquierdo = Nodo(5)
izquierdo_1 = Nodo(2)
izquierdo_2 = Nodo(7)

derecho = Nodo(15)
derecho_1 = Nodo(12)
derecho_2 = Nodo(20)

raiz.izquierdo = izquierdo
izquierdo.izquierdo = izquierdo_1
izquierdo.derecho = izquierdo_2

raiz.derecho = derecho
derecho.izquierdo = derecho_1
derecho.derecho = derecho_2

def orden(nodo):
    if nodo is None:
        return
    print(nodo.valor)
    orden(nodo.izquierdo)
    orden(nodo.derecho)

orden(raiz)