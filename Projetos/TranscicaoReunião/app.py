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

PASTA_ARQUIVOS = Path(__file__).parent / 'arquivos'
PASTA_ARQUIVOS.mkdir(exist_ok=True)

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
    webrtc_ctx = webrtc_streamer(
        key='recebe_audio',
        mode=WebRtcMode.SENDONLY,
        audio_receiver_size=1024,
        media_stream_constraints={'video': False, 'audio': True}
    )
    if not webrtc_ctx.state.playing:
        return
    container = st.empty()
    container.markdown('Comece a falar...')

    pasta_reuniao = PASTA_ARQUIVOS / datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    pasta_reuniao.mkdir()

    audio_chunck = pydub.AudioSegment.empty()

    while True:
        if webrtc_ctx.audio_receiver:
            container.markdown('Estou gravando.')
            try:
                frames_de_audio = webrtc_ctx.audio_receiver.get_frames(
                    timeout=1)
            except queue.Empty:
                time.sleep(0.1)
                continue
            for frame in frames_de_audio:
                sound = pydub.AudioSegment(
                    data=frame.to_ndarray().tobytes(),
                    sample_width=frame.format.bytes,
                    frame_rate=frame.sample_rate,
                    channels=len(frame.layout.channels)
                )
                audio_chunck += sound
            if len(audio_chunck) > 0:
                audio_chunck.export(pasta_reuniao / 'audio_temp.mp3')
        else:
            break


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
