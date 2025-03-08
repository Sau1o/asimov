from transformers import AutoTokenizer, AutoModel, pipeline

nome_modelo = 'FacebookAI/xlm-roberta-base'

modelo = AutoModel.from_pretrained(nome_modelo)
tokenizador = AutoTokenizer.from_pretrained(nome_modelo)

inputs = tokenizador(
    'A linguagem <mask> é uma ferramenta inovadora.', return_tensors='pt')
print(inputs)
