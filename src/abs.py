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