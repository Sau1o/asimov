# Crie um código que simula um baralho de cartas.
# O código deve conter as seguintes funções:

# gerar_baralho -> retorna um baralho novo. Parâmetros da função
# definem quantas cópias retornar (1 baralho, 2 baralhos, ...),
# se o baralho deve conter coringas, e se deve ser embaralhado
# antes de ser retornado.

# mostrar_baralho -> exibe a quantidade de cartas no baralho e
# mostra quais são.

# dar_as_cartas -> distribui as cartas do baralho entre X
# jogadores, de forma que cada jogador recebe Y cartas.

# mostrar_jogadores -> exibe a quantidade de cartas na mão de
# cada jogador e mostra quais são.

# A partir dessas funções, o código deve:
# - gerar o baralho e exibi-lo
# - dar as cartas para os jogadores
# - exibir o baralho após as cartas terem sido distribuídas
# - exibir a mão de cada jogador

# DICA: utilize os símbolos ♠ ♥ ♦ ♣ para representar os naipes.
# DICA: utilize a função random.shuffle (módulo random) para embaralhar.

import random


def gerar_baralho(n_copias=2, coringas=True, embaralhado=True):
    baralho = []

    naipes = list('♠♥♦♣')
    numeros = list('A23456789') + ['10'] + list('JQK')

    for _ in range(n_copias):
        for naipe in naipes:
            for numero in numeros:
                carta = numero + naipe
                baralho.append(carta)
        if coringas:
            baralho.extend(['JK1', 'JK2'])

    if embaralhado:
        random.shuffle(baralho)

    return baralho


def mostrar_baralho(baralho):
    print(f'Há {len(baralho)} cartas no baralho')
    print('Cartas:')
    print(', '.join(baralho))


def dar_as_cartas(baralho, n_jogadores=4, n_cartas=5):
    jogadores = {}

    for i in range(n_jogadores):
        mao = []
        while len(mao) < n_cartas:
            carta = baralho.pop(0)
            mao.append(carta)
        nome_jogador = f'Jogador {i+1}'
        jogadores[nome_jogador] = mao

    return jogadores


def mostrar_jogadores(jogadores):
    for jogador, mao in jogadores.items():
        print(f'Há {len(mao)} cartas na mão do jogador {jogador}')
        print('Cartas:')
        for carta in mao:
            print(f' -> {carta}')


baralho = gerar_baralho()
mostrar_baralho(baralho)

jogadores = dar_as_cartas(baralho)

mostrar_baralho(baralho)
mostrar_jogadores(jogadores)
