# Desafio 01
# Crie uma função chamada ler_datas, que recebe um texto qualquer e extrai todas
# as datas que estejam escritas no formato DD/MM/AAAA (como objetos datetime).
# Use o texto abaixo como

# exemplo:

import re
import datetime

texto = """
A reunião está marcada para o dia 15/03/2023.
Lembre-se de entregar o relatório até 28/02/2023.
O evento acontecerá em 10/04/2023 no auditório principal.
"""

padrao = '[0-9]{2}/[0-9]{2}/[0-9]{4}'

datas = []

for data_str in re.findall(padrao, texto):
    data = datetime.datetime.strptime(data_str, '%d/%m/%Y')
    datas.append(data)
print(datas)
