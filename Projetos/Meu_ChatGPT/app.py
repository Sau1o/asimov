import streamlit as st
import openai
from dotenv import load_dotenv, find_dotenv

from utils_files import *

_ = load_dotenv(find_dotenv())

client = openai.Client()

# INICIALIZAÇÃO ==================================================


def inicializacao():
    if not 'mensagens' in st.session_state:
        st.session_state.mensagens = []
    if not 'conversa_atual' in st.session_state:
        st.session_state.conversa_atual = ''
    if not 'modelo' in st.session_state:
        st.session_state.modelo = 'gpt-4o-mini'

# TABS ==================================================


def tab_conversas(tab):

    tab.button('➕ Nova conversa',
               on_click=seleciona_conversa,
               args=('', ),
               use_container_width=True)
    tab.markdown('')
    conversas = listar_conversas()
    for nome_arquivo in conversas:
        nome_mensagem = desconverte_nome_mensagem(nome_arquivo).capitalize()
        if len(nome_mensagem) == 30:
            nome_mensagem += '...'
        tab.button(nome_mensagem,
                   on_click=seleciona_conversa,
                   args=(nome_arquivo, ),
                   disabled=nome_arquivo == st.session_state['conversa_atual'],
                   use_container_width=True)


def seleciona_conversa(nome_arquivo):
    if nome_arquivo == '':
        st.session_state['mensagens'] = []
    else:
        mensagem = ler_mensagem_por_nome_arquivo(nome_arquivo)
        st.session_state['mensagens'] = mensagem
    st.session_state['conversa_atual'] = nome_arquivo


def tab_configuracoes(tab):
    modelo_escolhido = tab.selectbox('Selecione o modelo',
                                     ['gpt-4o-mini'])
    st.session_state['modelo'] = modelo_escolhido

    # chave = tab.text_input('Adicione sua api key',
    #                        value=st.session_state['api_key'])
    # if chave != st.session_state['api_key']:
    #     st.session_state['api_key'] = chave
    #     salva_chave(chave)
    #     tab.success('Chave salva com sucesso')


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

    nome_mensagem = ''
    for mensagem in mensagens:
        if mensagem['role'] == 'user':
            nome_mensagem = mensagem['content'][:30]
            break
    return nome_mensagem


# PÁGINA PRINCIPAL ==================================================
def pagina_principal():
    if not 'mensagens' in st.session_state:
        st.session_state.mensagens = []

    mensagens = ler_mensagens(st.session_state['mensagens'])
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
        salvar_mensagens(mensagens)
        st.rerun()


# MAIN ==================================================
def main():
    inicializacao()
    pagina_principal()
    tab1, tab2 = st.sidebar.tabs(['Conversas', 'Configurações'])
    tab_conversas(tab1)
    tab_configuracoes(tab2)


if __name__ == '__main__':
    main()
