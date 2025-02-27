# Criar um jogo que pergunte a capital dos estados, e o jogador precisará responder
# qual é a capital do estado. Antes de continuar o jogo o programa deverá verificar
# se o usuário quer parar ou continuar. Quando ele decidir parar ou quando todas as
# perguntas acabarem, o código mostrará no número bruto e porcentagem de acertos

import random

estados_capitais = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Distrito Federal": "Brasília",
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia",
    "Maranhão": "São Luís",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Paraíba": "João Pessoa",
    "Paraná": "Curitiba",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Norte": "Natal",
    "Rio Grande do Sul": "Porto Alegre",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Santa Catarina": "Florianópolis",
    "São Paulo": "São Paulo",
    "Sergipe": "Aracaju",
    "Tocantins": "Palmas"
}

selecionados = random.sample(list(estados_capitais.items()), 27)
pontos = 0
rodada = 0

print('*'*10)
print('Lembre-se de digitar a primeira letra maiúscula e usar os acentos.')
print("Tudo pronto. Vamos começar.")

for estado in selecionados:

    print(f'Pergunta numero {rodada}.')
    print(f'-> Qual a capital do estado: {estado[0]}')

    resposta = input('Digite sua reposta ou digite q para encerrar o jogo: ')

    if resposta == 'q':
        break
    elif resposta == estado[1]:
        pontos += 1
    rodada += 1

print(f"Fim do jogo\nForam {rodada} rodadas e {pontos} acertos.")
print(f"Um total de acertos de {pontos/rodada*100:.2f}%")
