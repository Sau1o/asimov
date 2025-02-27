# Crie um código que implementa a "Cifra de César", isto é, que
# transforma um string movendo cada letra um certo número de
# passos no alfabeto. O número de passos é dado por uma chave.
# Letras com acentos, espaços e pontuação permanecem iguais.

texto = 'ABCDE'
chave = 2

minusculas = 'abcdefghijklmnopqrstuvwxyz'
maisculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

cifra = ''


def cifrar_caractere(caractere, seq, chave):
    indice_atual = seq.index(caractere)
    novo_indice = indice_atual + chave

    while novo_indice >= len(seq):
        novo_indice = novo_indice - len(seq)

    while novo_indice < 0:
        novo_indice = novo_indice + len(seq)

    return seq[novo_indice]


for caractere in texto:
    if caractere in minusculas:
        caractere_cifra = cifrar_caractere(caractere, minusculas, chave)
    elif caractere in maisculas:
        caractere_cifra = cifrar_caractere(caractere, maisculas, chave)
    else:
        caractere_cifra = caractere
    cifra += caractere_cifra

print(cifra)
