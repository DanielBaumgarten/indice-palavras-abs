import re

def processar_texto(texto):

    texto = texto.lower()

    texto = re.sub(r'[^\w\s]', '', texto)

    palavras = texto.split()

    return palavras