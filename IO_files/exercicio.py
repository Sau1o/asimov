# Desenvolva um  script para encontrar um arquivo dentro da pasta home do usuário

from pathlib import Path

caminho = Path.home()

for arquivo in caminho.glob('**/*'):
    if arquivo.is_file():
        if arquivo.name == 'exercicio.py':
            print(arquivo)
