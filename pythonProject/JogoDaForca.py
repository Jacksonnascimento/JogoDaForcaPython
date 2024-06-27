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


lista_membros = ["Cabeça", "Tronco", "Braço esquerdo", "Braço direito", "Perna esquerda", "Perna direita"]


def montar_corpo(quantidade_erros, quantidade_corpos, resultado):
    if quantidade_erros - 1 == 0 and quantidade_corpos == 1:
        resultado = f"Corpo {quantidade_corpos} com o (s) membro (s): {lista_membros[quantidade_erros - 1]}"
        quantidade_erros += 1
        return quantidade_erros, quantidade_corpos, resultado
    elif (quantidade_erros - 1) < 6:
        resultado = resultado + ", " + lista_membros[quantidade_erros - 1]
        quantidade_erros += 1
        return quantidade_erros, quantidade_corpos, resultado
    else:
        quantidade_corpos += 1
        resultado = f"Corpo {quantidade_corpos} com o (s) membro (s): {lista_membros[0]}"
        quantidade_erros = 2  # Começa novamente com o segundo membro
        return quantidade_erros, quantidade_corpos, resultado


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
    lista_letras_opinadas = []
    quantidade_erros = 1
    quantidade_corpos = 1
    resultado = ''
    while len(existe_letra_palavra("*", palavra_oculta)):
        print(f"Palavra: {palavra_oculta}")
        entrada = input("Digite uma letra ").upper()
        while entrada in lista_letras_opinadas:
            entrada = input(f"A letra {entrada} já foi escolhida. Digite outra letra ").upper()
        lista_letras_opinadas.append(entrada)
        posicoes = existe_letra_palavra(entrada, palavra)
        if len(posicoes) == 0:
            print(f"Não existe a letra {entrada} nessa palavra")
            quantidade_erros, quantidade_corpos, resultado = montar_corpo(quantidade_erros, quantidade_corpos,
                                                                          resultado)
            print(resultado)
        else:
            print(f"Existe a letra {entrada} na palavra")
            acertos = acertos + 1
            for posicao in posicoes:
                palavra_oculta = mudar_palavra_oculta(palavra_oculta, posicao, entrada)

    lista_letras_opinadas = []
    print(f"A palavra é {palavra}")
    entrada = input("Deseja continuar? ").upper()
