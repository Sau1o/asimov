# Desafio 03

# Meus amigos possuem os seguintes interesses:

# Gostam de programação: Ricardo, Robert, Pedro, Vinicius
# Gostam de jogar futebol: Mateus, Roberto, Paulo, Vinicius
# Estudam na Asimov Academy: Ricardo, Mateus, Paulo, Pedro

# Usando operações de conjunto, encontre o conjunto de amigos que gostam
# de programação e estudam na Asimov Academy, mas que não gostam de jogar
# futebol

programacao = {'Ricardo', 'Robert', 'Pedro', 'Vinicius'}
futebol = {'Mateus', 'Roberto', 'Paulo', 'Vinicius'}
estudam = {'Ricardo', 'Mateus', 'Paulo', 'Pedro'}

conjunto_final = programacao.intersection(estudam).difference(futebol)

print(conjunto_final)
