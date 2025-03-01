import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_carros(carros):
    lista_carros = list(carros.items())
    # print(list(enumerate(lista_carros)))
    for i, carro in enumerate(lista_carros):
        print(f'[{i}] {carro[0]} - R$ {carro[1]} / dia')

    print(80*'=')
    return input('0 - VOLTAR | 1 - SAIR\n')


def alugar_carro(carros):
    lista_carros = list(carros.items())
    print("[ALUGAR] Dê uma olhada em nosso portfólio.")
    print("")

    for i, carro in enumerate(lista_carros):
        print(f'[{i}] {carro[0]} - R$ {carro[1]} / dia')

    print("="*80)
    carro_escolhido = input("Escolha o código do carro:\n")
    dias = input("Quantas diárias deseja alugar?\n")

    return carro_escolhido, dias


def confirma_aluguel(carros, carro_escolhido, dias, carros_alugados):
    id = int(carro_escolhido)
    dias = int(dias)
    carro = list(carros.keys())[id]

    print(f"Você escolheu {carro}.")
    print(
        f"O aluguel das {dias} diárias ficou R${dias*list(carros.values())[id]}")
    print("Deseja confirmar?")
    confirma_aluguel = input("0 - SIM | 1 - NÃO\n")

    if (confirma_aluguel == '0'):
        carros_alugados[carro] = carros.pop(carro)

    else:
        teste = False
        return teste, carros, carros_alugados

    print(" ")
    print(f"Parabéns você alugou o {carro} por {dias} dias")

    print("="*80)

    teste = input("0 - CONTINUAR | 1 - SAIR\n")
    return teste, carros, carros_alugados


def devolver_carro(carros, carros_alugados):
    if carros_alugados == {}:
        print("Nenhum carro disponível para devolução.")
        teste = input("0 - VOLTAR | 1 - SAIR\n")
        return teste, carros, carros_alugados
    else:
        print("Qual carro deseja devolver?\n")
        lista_carros = list(carros_alugados.items())

        for i, carro in enumerate(lista_carros):
            print(f'[{i}] {carro[0]} - R$ {carro[1]} / dia')

        id = int(input("Escolha o código do carro que deseja devolver:\n"))

        carro = list(carros_alugados.keys())[id]
        carros[carro] = carros_alugados.pop(carro)
        print(f"Obrigado por devolver o carro {(carro)}")

        print("="*80)
        teste = input("0 - CONTINUAR | 1 - SAIR\n")
        return teste, carros, carros_alugados


def tela_principal():
    print(80*'=')
    print('Bem vindo á locadora de carros')
    print(80*'=')
    print("O que deseja fazer?")
    return input(
        "0 -> Mostrar portifólio\n1 -> Alugar um carro\n2 -> Devolver um carro\n")
