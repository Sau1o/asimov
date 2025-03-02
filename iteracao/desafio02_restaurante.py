# Desafio 02

# Imagine que você tem um  restaurante com os seguintes items no menu:

import itertools
comidas = {
    'Prato Feito': 24.90,
    'Salada': 21.90,
    'Strogonoff': 29.90,
    'Feijoada': 32.90
}

bebidas = {
    'Água': 3.90,
    'Refrigerante': 5.90,
    'Suco': 7.90
}

# Crie um novo dicionário chamado combos, onde cada chave é uma tupla contendo
# (comida, bebida), e o seu respectivo valor é o preço daquela combinação de
# comida e bebida.


combo = {}

for chave_comida, preco_comida in comidas.items():
    for chave_bebida, preco_bebida in bebidas.items():
        chave_combo = (chave_comida, chave_bebida)
        preco_combo = preco_comida + preco_bebida
        combo[chave_combo] = round(preco_combo)

print(combo)
