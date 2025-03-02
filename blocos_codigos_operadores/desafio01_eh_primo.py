# Desafio 01

# Crie uma função que retorna se um número inteiro n (maior que zero)
# é primo.

# Dica: um número primo é um número que só é divisível por 1 ou por ele mesmo

def eh_primo(n):
    if n <= 2:
        return True

    for numero in range(2, n):
        if n % numero == 0:
            return False
    return True


for n in [1, 5, 10, 13, 15, 17]:
    print(f'{n} é primo: {eh_primo(n)}')
