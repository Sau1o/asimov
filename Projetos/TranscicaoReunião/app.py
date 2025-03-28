from pathlib import Path
from datetime import datetime
import time
import queue

from streamlit_webrtc import WebRtcMode, webrtc_streamer
import streamlit as st

import pydub
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.OpenAI()


def chat_openai(
    mensagem,
    modelo='gpt-4o-mini',
):
    mensagens = [{'role': 'user', 'content': mensagem}]
    resposta = client.chat.completions.create(
        model=modelo,
        messages=mensagens,
    )
    return resposta.choices[0].message.content


def transcreve_audio(caminho_audio, language='pt', response_format='text'):
    with open(caminho_audio, 'rb') as arquivo_audio:
        transcicao = client.audio.transcriptions.create(
            model='gpt-4o-mini-transcribe',
            language=language,
            response_format=response_format,
            file=arquivo_audio
        )
    return transcicao


def tab_gravar_reuniao():
    st.markdown('tab_gravar')


def tab_selecao_reuniao():
    st.markdown('tab_selecao')


def main():
    st.header("Bem vindo ao MeetGPT🎤", divider=True)
    tab_gravar, tab_selecao = st.tabs([
        'Gravar Reunião', ' Ver transcrições salvas'])
    with tab_gravar:
        tab_gravar_reuniao()

    with tab_selecao:
        tab_selecao_reuniao()


if __name__ == '__main__':
    main()
