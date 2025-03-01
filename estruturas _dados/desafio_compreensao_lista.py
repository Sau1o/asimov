# Desafio 01
# Converta o loop para uma compreensão de lista:

valores = [30, 50, 120]

triplos = []

for valor in valores:
    triplo = valor * 3
    triplos.append(triplo)

print(f'Triplos com for: {triplos}')

triplos = [valor*3 for valor in valores]

print(f'Triplos com compreensão de lista: {triplos}')
