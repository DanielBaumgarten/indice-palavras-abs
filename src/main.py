from abb import ABB
from texto import processar_texto

texto = input("Digite um texto: ")

palavras = processar_texto(texto)

arvore = ABB()

for palavra in palavras:
    arvore.inserir(palavra)