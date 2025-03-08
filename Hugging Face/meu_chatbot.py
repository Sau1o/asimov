from transformers import pipeline

chatbot = pipeline(
    "text-generation",
    model="Felladrin/Llama-68M-Chat-v1",
    max_new_tokens=300,
    penalty_alpha=0.5,
    top_k=4,
)

# Mensagem para o chatbot deve ficar no formato abaixo:
# <|im_start|>system
# {system_message}<|im_end|>
# <|im_start|>user
# {user_message}<|im_end|>
# <|im_start|>assistant

# Criando prompt do sistema
mensagem_sistema = 'You are a helpful artificial intelligence assistant.'
prompt_sistema = f'<|im_start|>system\n{mensagem_sistema}<|im_end|>\n'

# Criando prompt do usuário
mensagem_usuario = 'How can I become a Python programmer?'
print('Sua pergunta: ', mensagem_usuario)
prompt_usuario = f'<|im_start|>user\n{mensagem_usuario}<|im_end|>\n'

# Criando prompt final e verificando
conversa = f'{prompt_sistema}{prompt_usuario}<|im_start|>assistant\n'
print(conversa)

# Pegando a resposta do bot
resposta = chatbot(conversa)
print(resposta)

# Formatando a resposta
print(resposta[0]['generated_text'])
resposta_formatada = resposta[0]['generated_text'].split(
    '<|im_start|>assistant\n')[-1].rstrip('<|im_end|>')
print('Resposta do bot: ', resposta_formatada)

# Gerando loop de prompt
conversa = mensagem_sistema
while True:
    mensagem_usuario = input('Escreva sua pergunta (em inglês): ')
    conversa += f'<|im_start|>user\n{mensagem_usuario}<|im_end|>\n<|im_start|>assistant'
    resposta = chatbot(conversa)
    conversa = resposta[0]['generated_text']
    resposta_formatada = conversa.split(
        '<|im_start|>assistant\n')[-1].rstrip('<|im_end|>')
    print(f'Resposta do bot: {resposta_formatada}')
