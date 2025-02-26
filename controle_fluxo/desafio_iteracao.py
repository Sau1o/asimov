# Dado uma sequencia de números, calcule a soma e média dos números.
# ATENÇÂO: não vale usar a função sum()

numeros = [10, 25, 74, 62, 31, 2]
soma = 0

for numero in numeros:
    soma = numero + soma
print(f'A soma dos números é : {soma}')
print(f'A média é: {soma/len(numeros)}')
