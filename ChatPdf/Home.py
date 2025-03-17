import streamlit as st
from pathlib import Path

PASTA_ARQUIVOS = Path(__file__).parent / 'arquivos'


def cria_chain_conversa():
    st.session_state['chain'] = True
    pass


def sidebar():
    uploaded_pdfs = st.file_uploader(
        'Adicione seus arquivos pdf.',
        type=['.pdf'],
        accept_multiple_files=True)
    if not uploaded_pdfs is None:
        for arquivo in PASTA_ARQUIVOS.glob('*.pdf'):
            arquivo.unlink()
        for pdf in uploaded_pdfs:
            with open(PASTA_ARQUIVOS / pdf.name, 'wb') as f:
                f.write(pdf.read())

    label_botao = 'Inicializar ChatBot'
    if 'chain' in st.session_state:
        label_botao = 'Atualizar ChatBot'
    if st.button(label_botao, use_container_width=True):
        if len(list(PASTA_ARQUIVOS.glob('*.pdf'))) == 0:
            st.error('Adicione arquivos pdf para inicializar o chatbot')
        else:
            st.success('Inicializando o ChatBot...')
            cria_chain_conversa()
            st.rerun()


def main():
    with st.sidebar:
        sidebar()


if __name__ == '__main__':
    main()
