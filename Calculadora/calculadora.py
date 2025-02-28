import os

fim_do_programa = True

while fim_do_programa:
    print('Entre com a conta que deseja fazer: ')
    entrada = input().replace(" ", "")

    operadores = "+-*/^"
    pos_operador = -1

    # Encontrar o operador na string
    for i, caractere in enumerate(entrada):
        if caractere in operadores:
            pos_operador = i
            break

    if pos_operador == -1:
        print("Erro: Nenhum operador encontrado na entrada.")
        continue  # Volta para o início do loop

    try:
        a = int(entrada[:pos_operador])   # Pega o número antes do operador
        operador = entrada[pos_operador]  # O operador em si
        b = int(entrada[pos_operador+1:])  # Pega o número depois do operador

        if operador == '+':
            resultado = a + b
        elif operador == '-':
            resultado = a - b
        elif operador == '*':
            resultado = a * b
        elif operador == '/':
            resultado = "Erro: divisão por zero!" if b == 0 else a / b
        elif operador == '^':
            resultado = a ** b  # Correção do operador de exponenciação
        else:
            resultado = "Erro: Operador inválido."

    except ValueError:
        resultado = "Erro: Entrada inválida! Use apenas números e operadores."

    print(f'{entrada} = {resultado}')

    tecla = input(
        'Pressione 1 para sair ou Enter para continuar.\n')
    if tecla == '1':
        fim_do_programa = False
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
