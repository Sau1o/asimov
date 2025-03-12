import streamlit as st
import openai
from dotenv import load_dotenv, find_dotenv

import re
from unidecode import unidecode

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

    texto_completo = ''
    for resposta_stream in resposta:
        texto = resposta_stream.choices[0].delta.content
        if texto:
            texto_completo += texto
    return texto_completo


def salvar_mensagens(mensagens):
    if len(mensagens) == 0:
        return False
    nome_mensagem = ''
    for mensagem in mensagens:
        if mensagem['role'] == 'user':
            nome_mensagem = mensagem['content'][30]
            break
    nome_arquivo = unidecode(nome_mensagem)
    nome_arquivo = re.sub('\W+', '', nome_arquivo).lower()


def pagina_principal():
    if not 'mensagens' in st.session_state:
        st.session_state.mensagens = []

    mensagens = st.session_state['mensagens']
    st.header('🤖 Coelho ChatBot', divider=True)

    for mensagem in mensagens:
        chat = st.chat_message(mensagem['role'])
        chat.markdown(mensagem['content'])

    prompt = st.chat_input('Fale com o chat.')
    if prompt:
        nova_mensagem = {'role': 'user', 'content': prompt}
        chat = st.chat_message(nova_mensagem['role'])
        chat.markdown(nova_mensagem['content'])
        mensagens.append(nova_mensagem)

        st.chat_message('assistant')
        placeholder = chat.empty()
        texto_completo = ''

        placeholder.markdown("▌")
        texto_completo = geracao_texto(mensagens)

        placeholder.markdown(texto_completo + "▌")
        placeholder.markdown(texto_completo)
        nova_mensagem = {'role': 'assistant',
                         'content': texto_completo}
        mensagens.append(nova_mensagem)

        st.session_state['mensagens'] = mensagens


pagina_principal()
