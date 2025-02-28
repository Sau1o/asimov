print(80*'=')
print('Bem vindo á locadora de carros')
print(80*'=')
print("O que deseja fazer?")


def mostrar(carros):
    lista_carros = list(carros.items())
    # print(list(enumerate(lista_carros)))
    for i, carro in enumerate(lista_carros):
        print(f'[{i}] {carro[0]} - R$ {carro[1]} / dia')

    print(80*'=')
    return input('0 - CONTINUAR | 1 - SAIR\n')


carros = {
    'Chevrolet Tracker': 120,
    'Chevrolet Onix': 90,
    'Chevrolet Spin': 150,
    'Hyundai HB20': 85,
    'Hyundai Tucson': 120,
    'Fiat Uno': 60,
    'Fiat Mobi': 70,
    'Fiat Pulse': 130
}

fim_do_programa = True

acao = input(
    "0 -> Mostrar portifólio\n1 -> Alugar um carro\n2 -> Devolver um carro\n")

while fim_do_programa:
    if acao == '0':
        teste = mostrar(carros)
        fim_do_programa = False if teste == '0' else True
