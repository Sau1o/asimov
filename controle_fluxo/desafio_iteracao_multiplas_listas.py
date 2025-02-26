# Dado duas listas, printe todos os valores que aparecerem duplicados

lista_1 = [1, 2, 5, 8, 10]
lista_2 = [1, 8, 4, 6, 7]

lista_nova = []
for numero in lista_1:
    if numero in lista_2:
        lista_nova.append(numero)
print(lista_nova)
