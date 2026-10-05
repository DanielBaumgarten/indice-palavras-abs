from abs import ABS
from texto import processar_texto

texto = input("Digite um texto: ")

palavras = processar_texto(texto)

arvore = ABS()

for palavra in palavras:
    arvore.inserir(palavra)