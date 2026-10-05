from no import No

class ABS
    def __init__(self):
        self.raiz= None

def inserir(self, palavra):
    self.raiz = self._inserir(self.raiz, palavra)

def _inserir(self, no, palavra):

    if no is None:
        return No(palavra)

    if palavra < no.palavra:
        no.esquerda = self._inserir(no.esquerda, palavra)

    elif palavra > no.palavra:
        no.direita = self._inserir(no.direita, palavra)

    else:
        no.quantidade += 1

    return no

def buscar(self, palavra):
    return self._buscar(self.raiz, palavra)


def _buscar(self, no, palavra):

    if no is None:
        return None

    if palavra == no.palavra:
        return no

    if palavra < no.palavra:
        return self._buscar(no.esquerda, palavra)

    return self._buscar(no.direita, palavra)
    
def listar_ordenado(self):
    self._inorder(self.raiz)


def _inorder(self, no):

    if no is not None:

        self._inorder(no.esquerda)

        print(
            no.palavra,
            "-",
            no.quantidade
        )

        self._inorder(no.direita)