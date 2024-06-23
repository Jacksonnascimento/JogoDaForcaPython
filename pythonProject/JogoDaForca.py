import random
from turtle import pos

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


def existe_letra_palavra(letra, palavra):
    posicoes = []
    for i in range(len(palavra)):
        if palavra[i] == letra:
            posicoes.append(i)
    return posicoes

def mudar_palavra_oculta(oculta, posicao, letra):
    lista_letras = list(oculta)
    lista_letras[posicao] = letra
    return ''.join(lista_letras)

quantidade = 0
entrada = "SIM"
palavra, quantidade_palavras = gerar_palavra_aleatoria()
while entrada == "SIM" or entrada == "S":
    quantidade = 1
    while verificar_existe_lista(palavra):
        if quantidade < quantidade_palavras:
            palavra, quantidade_palavras = gerar_palavra_aleatoria()
            quantidade = quantidade + 1
        else:
            lista_palavras_selecionadas = []
    quantidade_letras = len(palavra)
    print(f"Palavra com {quantidade_letras} letras")
    palavra_oculta = palavra.replace(palavra, '*' * len(palavra))
    acertos = 0
    while len(existe_letra_palavra("*", palavra_oculta)):
        print(f"Palavra: {palavra_oculta}")
        entrada = input("Digite uma letra ").upper()
        posicoes = existe_letra_palavra(entrada, palavra)
        if len(posicoes) == 0:
            print(f"Não existe a letra {entrada} nessa palavra")
        else:
            print(f"Existe a letra {entrada} na palavra")
            acertos = acertos + 1
            for posicao in posicoes:
                palavra_oculta = mudar_palavra_oculta(palavra_oculta, posicao, entrada)

    print(f"A palavra é {palavra}")
    entrada = input("Deseja continuar? ").upper()





