import streamlit as st
from langchain.memory import ConversationBufferMemory

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

import tempfile

from loaders import *

TIPOS_ARQUIVOS_VALIDOS = [
    'Site', 'Youtube', 'Pdf', 'Csv', 'Txt'
]

CONFIG_MODELOS = {'Groq':
                  {'modelos': ['gemma2-9b-it'],
                   'chat': ChatGroq},
                  'OpenAI':
                  {'modelos': ['gpt-4o-mini', 'gpt-4o', 'o1-preview', 'o1-mini'],
                   'chat': ChatOpenAI}}

MEMORIA = ConversationBufferMemory()


def carrega_arquivos(tipo_arquivo, arquivo):
    # Mapeia os tipos de arquivo para suas respectivas funções de carregamento
    funcoes_carregamento = {
        'Site': carrega_site,
        'Youtube': carrega_youtube,
        'Pdf': carrega_pdf,
        'Csv': carrega_csv,
        'Txt': carrega_txt
    }

    # Se for 'Site' ou 'Youtube', processa diretamente
    if tipo_arquivo in ['Site', 'Youtube']:
        documento = funcoes_carregamento[tipo_arquivo](arquivo)

    # Se for um arquivo (Pdf, Csv, Txt), usa tempfile
    elif tipo_arquivo in ['Pdf', 'Csv', 'Txt']:
        with tempfile.NamedTemporaryFile(suffix=f".{tipo_arquivo.lower()}", delete=False) as temp:
            temp.write(arquivo.read())
            nome_temp = temp.name
        documento = funcoes_carregamento[tipo_arquivo](nome_temp)

    return documento


def carrega_modelo(provedor, modelo, api_key, tipo_arquivo, arquivo):
    documento = carrega_arquivos(tipo_arquivo, arquivo)

    system_message = '''Você é um assistente amigável chamado Oráculo.
    Você possui acesso às seguintes informações vindas 
    de um documento {}: 

    ####
    {}
    ####

    Utilize as informações fornecidas para basear as suas respostas.

    Sempre que houver $ na sua saída, substita por S.

    Se a informação do documento for algo como "Just a moment...Enable JavaScript and cookies to continue" 
    sugira ao usuário carregar novamente o Oráculo!'''.format(tipo_arquivo, documento)
    template = ChatPromptTemplate.from_messages([
        ('system', system_message),
        ('placeholder', '{chat_history}'),
        ('user', '{input}')
    ])

    chat = CONFIG_MODELOS[provedor]['chat'](model=modelo, api_key=api_key)
    chain = template | chat

    st.session_state['chain'] = chain


def pagina_chat():
    st.header('🤖 Bem Vindo ao Oráculo!!', divider=True)

    chain = st.session_state.get('chain')
    if chain is None:
        st.error('Carrege o Oráculo')
        st.stop()

    memoria = st.session_state.get('memoria', MEMORIA)
    for mensagem in memoria.buffer_as_messages:
        chat = st.chat_message(mensagem.type)
        chat.markdown(mensagem.content)

    input_usuario = st.chat_input('Fale com o Oráculo.')
    if input_usuario:
        chat = st.chat_message('human')
        chat.markdown(input_usuario)

        chat = st.chat_message('ai')
        resposta = chat.write_stream(chain.stream({
            'input': input_usuario,
            'chat_history': memoria.buffer_as_messages
        }))

        memoria.chat_memory.add_user_message(input_usuario)
        memoria.chat_memory.add_ai_message(resposta)
        st.session_state['memoria'] = memoria


def side_bar():
    tabs = st.tabs(['Upload de Arquivos', 'Seleção de Modelos'])
    with tabs[0]:

        tipo_arquivo = st.selectbox("Escolha o tipo de arquivo", [
                                    'Site', 'Youtube', 'Pdf', 'Csv', 'Txt'])

        inputs = {
            'Site': ("Digite a URL do site", st.text_input),
            'Youtube': ("Digite a URL do vídeo", st.text_input),
            'Pdf': ("Faça o upload do arquivo PDF", st.file_uploader, ['.pdf']),
            'Csv': ("Faça o upload do arquivo CSV", st.file_uploader, ['.csv']),
            'Txt': ("Faça o upload do arquivo TXT", st.file_uploader, ['.txt'])
        }

        label, func, *args = inputs[tipo_arquivo]
        arquivo = func(label, *args) if args else func(label)

    with tabs[1]:
        provedor = st.selectbox(
            'Selecione o provedor dos modelo', CONFIG_MODELOS.keys())
        modelo = st.selectbox('Selecione o modelo',
                              CONFIG_MODELOS[provedor]['modelos'])
        api_key = st.text_input(
            f'Adicione a api key para o provedor {provedor}',
            value=st.session_state.get(f'api_key_{provedor}'))

        st.session_state[f'api_key_{provedor}'] = api_key

    if st.button('Inicializar Oráculo', use_container_width=True):
        carrega_modelo(provedor, modelo, api_key, tipo_arquivo, arquivo)

    if st.button('Apagar Histórico de Conversa', use_container_width=True):
        st.session_state['memoria'] = MEMORIA


def main():
    with st.sidebar:
        side_bar()
    pagina_chat()


if __name__ == '__main__':
    main()
