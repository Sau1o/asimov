from bs4 import BeautifulSoup

with open('asimov_ex.html', 'r') as file:
    conteudo = file.read()
    ex = BeautifulSoup(conteudo, 'lxml')
    # print(ex)
    all_tags = ex.find_all('p')

    for p in all_tags:
        print(p.text)
