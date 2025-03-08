from transformers import pipeline

modelos = [
    {
        'nome': 'FacebookAI/xlm-roberta-base',
        'token': '<mask>',
    },
    {
        'nome': 'neuralmind/bert-base-portuguese-cased',
        'token': '[MASK]',
    },
    {
        'nome': 'rufimelo/Legal-BERTimbau-base',
        'token': '[MASK]',
    },
]

for dict_modelo in modelos:
    nome_modelo = dict_modelo['nome']
    token_modelo = dict_modelo['token']
    print(f'Testanto modelo {nome_modelo}')
    modelo = pipeline(task='fill-mask', model=nome_modelo)
    frase = f'Este documento é essencial para a {token_modelo}'
    predicoes = modelo(frase)
    for predicao in predicoes:
        resposta = predicao['token_str']
        score = predicao['score']
        frase = predicao['sequence']
        score_ajustado = score * 100
        print(
            f'Predição:{resposta} com score {score_ajustado:.2f}% -> {frase}')
    input('Aperte enter para o próximo modelo.')
