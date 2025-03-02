# Desafio  02

# Crie uma compreensão de dicionários a partir de  uma lista de palavras.
# No dicionário resultante, cada chave é a palavra em  letras minúsculas, e
# cada valor associado é o número de caracteres da palavra, sem contar espaços
# em branco.

# Exemplo de lista de palavras e o dicionário resultante:

# palavras = ['Olá', 'Python', 'Juliano', 'Asimov Academy']

# dic_caracteres = {'olá':3,'python':6,'juliano':7, 'asimov academy':13}

palavras = ['Olá', 'Python', 'Juliano', 'Asimov Academy']

dict_caracteres = {palavra.lower(): len(palavra.replace(" ", ""))
                   for palavra in palavras}

print(dict_caracteres)
