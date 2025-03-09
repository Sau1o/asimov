# # Resposta "bruta" sem templating de strings
# import requests

# token = '<YOUR TOKEN>'
# headers = {'Authorization': f'Bearer {token}'}

# modelo = 'mistralai/Mixtral-8x7B-Instruct-v0.1'

# url = f"https://api-inference.huggingface.co/models/{modelo}"
# json = {
#     'inputs': 'Hello, what is your name?'
# }

# response = requests.post(url, json=json, headers=headers)
# print(response)
# print(response.json())

################################################################################
# # Adicionando templating
# from transformers import AutoTokenizer

# chat = [
#     {"role": "user", "content": "Olá, qual o seu nome?"},
#     {"role": "assistant", "content": "Olá, eu sou um modelo de AI. Como posso ajudar?"},
#     {"role": "user", "content": "Gostaria de aprender Python. Você tem alguma dica?"},
# ]

# tokenizer_mixtral = AutoTokenizer.from_pretrained('mistralai/Mixtral-8x7B-Instruct-v0.1')
# template_mixtral = tokenizer_mixtral.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
# print('----- Chat formatado para modelo Mixtral -----')
# print(template_mixtral)

# tokenizer_llama = AutoTokenizer.from_pretrained("Felladrin/Llama-68M-Chat-v1")
# template_llama = tokenizer_llama.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
# print('----- Chat formatado para modelo Llama -----')
# print(template_llama)

################################################################################
# # Resposta ajustada com uso de templating
# import requests
# from transformers import AutoTokenizer

# modelo = 'mistralai/Mixtral-8x7B-Instruct-v0.1'

# chat = [
#     {"role": "user", "content": "Hello, what is your name?"},
# ]

# tokenizer = AutoTokenizer.from_pretrained(modelo)
# chat_str = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)

# url = f"https://api-inference.huggingface.co/models/{modelo}"
# json = {
#     'inputs': chat_str,
#     'options': {'use_cache': False, 'wait_for_model': True},
# }

# response = requests.post(url, json=json)
# print(response.json())

################################################################################
# Resposta ajustada com uso de templating em loop
import requests
from transformers import AutoTokenizer

token = '<YOUR TOKEN>'
headers = {'Authorization': f'Bearer {token}'}

modelo = 'mistralai/Mixtral-8x7B-Instruct-v0.1'
tokenizer = AutoTokenizer.from_pretrained(modelo)
url = f"https://api-inference.huggingface.co/models/{modelo}"
chat = []
while True:
    mensagem = input('Faça sua pergunta em inglês ("q" para sair):')
    if mensagem == 'q':
        break
    chat.append({'role': 'user', 'content': mensagem})
    chat_str = tokenizer.apply_chat_template(
        chat, tokenize=False, add_generation_prompt=True)
    json = {
        'inputs': chat_str,
        'parameters': {'max_new_tokens': 1_000},
        'options': {'use_cache': False, 'wait_for_model': True},
    }
    response = requests.post(url, json=json, headers=headers).json()
    mensagem_chatbot = response[0]['generated_text'].split('[/INST]')[-1]
    print('Resposta do chatbot:', mensagem_chatbot)
    chat.append({'role': 'assistant', 'content': mensagem_chatbot})

print(chat)
