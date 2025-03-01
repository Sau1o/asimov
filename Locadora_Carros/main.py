from utils import *

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

carros_alugados = {}

fim_do_programa = True
tela = 'n'

while fim_do_programa:
    if tela == 'n':
        limpar_tela()
        tela = tela_principal()

    elif tela == '0':
        limpar_tela()
        teste = mostrar_carros(carros)
        fim_do_programa = False if teste == '1' else True
        tela = 'n'

    elif tela == '1':
        limpar_tela()
        carro_escolhido, dias = alugar_carro(carros)
        tela = '3'

    elif tela == '2':
        limpar_tela()
        teste, carros, carros_alugados = devolver_carro(
            carros, carros_alugados)
        tela = 'n'
        fim_do_programa = False if teste == '1' else True

    elif tela == '3':
        limpar_tela()
        teste, carros, carros_alugados = confirma_aluguel(
            carros, carro_escolhido, dias, carros_alugados)
        tela = 'n'
        fim_do_programa = False if teste == '1' else True

print("Obrigado por alugar conosco.")
