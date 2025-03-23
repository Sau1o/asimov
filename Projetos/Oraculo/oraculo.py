import streamlit as st
from langchain.memory import ConversationBufferMemory

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

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


def carrega_modelo(provedor, modelo, api_key):
    chat = CONFIG_MODELOS[provedor]['chat'](model=modelo, api_key=api_key)
    st.session_state['chat'] = chat


def pagina_chat():
    st.header('🤖 Bem Vindo ao Oráculo!!', divider=True)

    chat_model = st.session_state.get('chat')
    memoria = st.session_state.get('memoria', MEMORIA)
    for mensagem in memoria.buffer_as_messages:
        chat = st.chat_message(mensagem.type)
        chat.markdown(mensagem.content)

    input_usuario = st.chat_input('Fale com o Oráculo.')
    if input_usuario:
        chat = st.chat_message('human')
        chat.markdown(input_usuario)

        chat = st.chat_message('ai')
        resposta = chat.write_stream(chat_model.stream(input_usuario))

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
        carrega_modelo(provedor, modelo, api_key)


def main():
    pagina_chat()
    with st.sidebar:
        side_bar()


if __name__ == '__main__':
    main()
