# Desafio 01

# Crie uma função que retorna os valores de duas listas de forma intercalada,
# mesmo quando as listas têm tamanho diferentes. Por exemplo, dadas as listas:

# L1 = [1,2,3]
# L2 = ['a','b','c','d','e']

# A função deve retornar:

# [1,'a', 2, 'b', 3, 'c', 'd', 'e']

from itertools import zip_longest


def intercalar_listas(lista1, lista2):
    return [item for pair in zip_longest(lista1, lista2) for item in pair if item is not None]


# Exemplos de uso:
L1 = [1, 2, 3]
L2 = ['a', 'b', 'c', 'd', 'e']

print(intercalar_listas(L1, L2))  # [1, 'a', 2, 'b', 3, 4]
