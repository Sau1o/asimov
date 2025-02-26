numero_correto = 20

tentativas = 0
fim_do_jogo = True

while tentativas <= 2 and fim_do_jogo:
    numero = int(input("Chute um número de 0 a 100: "))

    if numero > numero_correto:
        print("O número digitado é maior que o número correto.")
        print(f"Restam {2-tentativas} tentativas")
    elif numero < numero_correto:
        print("O número digitado é menor que o número correto.")
        print(f"Restam {2-tentativas} tentativas")
    else:
        print("Você acertou.")
        fim_do_jogo = False
    tentativas += 1
print("Fim do Jogo")
