import random
from struct import pack

lista_palavras_selecionadas = []


def gerar_palavra_aleatoria():
    with open('dicionário de palavras.txt', 'r', encoding='utf-8') as arquivo_com_palavras:
        palavras = arquivo_com_palavras.read().splitlines()
    palavra_selecionada = random.choice(palavras)
    return palavra_selecionada.upper(), len(palavras)


def verificar_existe_lista(palavra):
    if len(lista_palavras_selecionadas) == 0:
        lista_palavras_selecionadas.append(palavra)
        return False
    else:
        if palavra in lista_palavras_selecionadas:
            return True
        else:
            lista_palavras_selecionadas.append(palavra)
            return False


quantidade = 0
entrada = "SIM"
palavra, quantidade_palavras = gerar_palavra_aleatoria()
while entrada == "SIM":
    print(palavra)
    quantidade = 1
    while verificar_existe_lista(palavra):
        if quantidade < quantidade_palavras:
            palavra, quantidade_palavras = gerar_palavra_aleatoria()
            quantidade = quantidade + 1
        else:
            lista_palavras_selecionadas = []

    entrada = input("Deseja continuar? ").upper()





