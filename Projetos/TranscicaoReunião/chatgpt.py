import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.OpenAI()


def chat_openai(
    mensagens,
    modelo='gpt-4o-mini',
    temperatura=0,
    stream=False,
):
    resposta = client.chat.completions.create(
        model=modelo,
        messages=mensagens,
        temperature=temperatura,
        stream=stream,
    )
    return resposta


mensagens = [{'role': 'user', 'content': 'O que é uma maçã em 5 palavras?'}]

resposta = chat_openai(mensagens)
print(resposta.choices[0].message.content)
