from transformers import pipeline

modelo = pipeline('fill-mask')

frase = 'The capital of <mask> is Brasilia.'

predicoes = modelo(frase)
for predicao in predicoes:
    resposta = predicao['token_str']
    score = predicao['score']
    frase = predicao['sequence']
    score_ajustado = score * 100
    print(f'Predição:{resposta} com score {score_ajustado:.2f}% -> {frase}')
