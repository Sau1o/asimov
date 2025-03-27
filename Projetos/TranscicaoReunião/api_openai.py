import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.OpenAI()


def transcreve_audio(caminho_audio, language='pt', response_format='text'):
    with open(caminho_audio, 'rb') as arquivo_audio:
        transcicao = client.audio.transcriptions.create(
            model='gpt-4o-mini-transcribe',
            language=language,
            response_format=response_format,
            file=arquivo_audio
        )
    return transcicao
