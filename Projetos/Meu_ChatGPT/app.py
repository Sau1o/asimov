import streamlit as st
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()


def geracao_texto(mensagens):
    resposta = client.chat.completions.create(
        messages=mensagens,
        model='gpt-4o-mini',
        temperature=0,
        max_tokens=1000,
        stream=True,
    )

    print('Assistant: ', end='')
    texto_completo = ''
    for resposta_stream in resposta:
        texto = resposta_stream.choices[0].delta.content
        if texto:
            print(texto, end='')
            texto_completo += texto
    print()

    mensagens.append({'role': 'assistant', 'content': texto_completo})
    return mensagens


def pagina_principal():
    st.header('🤖 Coelho ChatBot', divider=True)

    mock_msgs = [{'role': 'user', 'content': 'pergunta 1'},
                 {'role': 'assistant', 'content': 'resposta 1'},
                 {'role': 'user', 'content': 'pergunta 2'},
                 {'role': 'assistant', 'content': 'resposta 2'}]

    for mensagem in mock_msgs:
        chat = st.chat_message(mensagem['role'])
        chat.markdown(mensagem['content'])

    prompt = st.chat_input('Fale com o chat.')
    if prompt:
        nova_mensagem = {'role': 'user', 'content': prompt}
        chat = st.chat_message(mensagem['role'])
        chat.markdown(nova_mensagem['content'])


pagina_principal()

if __name__ == '__main__':

    print('Bem-vindo ao meu ChatBot com ChatGpt:')
    print('Digite q para sair e encerrar a conversa')
    mensagens = []
    # while True:
    #     input_usuario = input('User: ')
    #     if (input_usuario == 'q'):
    #         break
    #     mensagens.append({'role': 'user', 'content': input_usuario})
    #     mensagens = geracao_texto(mensagens)
