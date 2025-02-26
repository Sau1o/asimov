# Dado uma sequencia de números, calcule a soma e média dos números.
# ATENÇÂO: não vale usar a função sum()

numeros = [10, 25, 74, 62, 31, 2]
soma = 0

for numero in numeros:
    soma += numero

print(f'A soma dos números é : {soma}')
print(f'A média é: {soma/len(numeros)}')

# Dado uma sequencia de números, calcule o maior valor da sequência.
# ATENÇÂO: não vale usar a função max()

numeros = [10, 24, 62, 87, 92]

maximo = numeros[0]

for numero in numeros:
    if numero > maximo:
        maximo = numero

print(f'O maior valor é: {maximo}')

# Dado uma  lista de palavras, print todas que tem pelo menos cinco caracteres

palavras = ['casa', 'cachorro', 'gato', 'escola', 'telefone']

for palavra in palavras:
    if len(palavra) >= 5:
        print(palavra)
