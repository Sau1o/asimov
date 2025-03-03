import requests
from bs4 import BeautifulSoup

import pandas as pd


def scraping_uf(uf='sp'):
    uf_url = f'https://www.ibge.gov.br/cidades-e-estados/{uf}.html'
    browsers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
    page = requests.get(uf_url, headers=browsers)

    soup = BeautifulSoup(page.content, 'html.parser')
    indicadores = soup.select('.indicador')

    uf_dict = {
        dado.select('.ind-label')[0].text: dado.select('.ind-value')[0].text
        for dado in indicadores
    }

    return uf_dict


estado = scraping_uf('sp')
estado

for indicador in estado:
    if ']' in estado[indicador]:
        estado[indicador] = estado[indicador].split(']')[0][:-8]
    else:
        estado[indicador] = estado[indicador]
estado

df = pd.DataFrame(estado.values(), index=estado.keys())

print(df)
