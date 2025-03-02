# Com base no for loop abaixo

valores = [1, 2, 3, 4, 5, 10]

quadrados_maiores_que_tres = []
for valor in valores:
    if valor > 3:
        quadrado = valor ** 2
        quadrados_maiores_que_tres.append(quadrado)
print(quadrados_maiores_que_tres)

# Crie uma compreensão de lista que gera a mesma lista quadrados_maiores_que_tres
# Em seguida, use as funções map e filter para fazer a mesma coisa

quadrados_maiores_que_tres = [quadrado **
                              2 for quadrado in valores if quadrado > 3]
print(f"Solução com compreensão de lista: {quadrados_maiores_que_tres}")

r = list(map(lambda x: x ** 2, filter(lambda x: x > 3, valores)))
print(f"Solução com map e filter: {r}")
