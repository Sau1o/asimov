import streamlit as st
from langchain.memory import ConversationBufferMemory

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

TIPOS_ARQUIVOS_VALIDOS = [
    'Site', 'Youtube', 'Pdf', 'Csv', 'Txt'
]

CONFIG_MODELOS = {'Groq': {'modelos': ['llama-3.1-70b-versatile', 'gemma2-9b-it', 'mixtral-8x7b-32768']},
                  'OpenAI': {'modelos': ['gpt-4o-mini', 'gpt-4o', 'o1-preview', 'o1-mini']}}

MENSAGENS_EXEMPLO = [
    ('user', 'Olá'),
    ('assistant', 'Tudo bem?'),
    ('user', 'Tudo ótimo'),
]


def pagina_chat():
    st.header('🤖 Bem Vindo ao Oráculo!!', divider=True)

    mensagens = st.session_state.get('mensagens', MENSAGENS_EXEMPLO)
    for mensagem in mensagens:
        chat = st.chat_message(mensagem[0])
        chat.markdown(mensagem[1])

    input_usuario = st.chat_input('Fale com o Oráculo.')
    if input_usuario:
        mensagens.append(('user', input_usuario))
        st.session_state['mensagens'] = mensagens
        st.rerun()


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


def main():
    pagina_chat()
    with st.sidebar:
        side_bar()


if __name__ == '__main__':
    main()
