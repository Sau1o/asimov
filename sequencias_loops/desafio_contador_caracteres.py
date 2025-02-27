# Crie um código que conta o número de vogais de um bloco de texto
# qualquer. O código deve desconsiderar letras maiúsculas/minúsculas
# ou seja, "a" e "A" contam da mesma forma.
# O texto pode ser colado diretamente como um string no código.

texto = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean diam odio, posuere nec dui vel, sagittis pretium est. Mauris quis arcu ante. Praesent sollicitudin sem quis vehicula tincidunt. Aenean lobortis odio non nunc imperdiet, ut interdum sapien sodales. Vestibulum ultrices sem dolor, eget molestie neque vulputate nec. Morbi vehicula maximus odio ac dictum. Curabitur lobortis ultrices gravida. Integer libero eros, tincidunt vitae porta eu, semper lobortis nisl."""

texto = texto.lower()
lista_vogais = []
print(texto)
quantidade = 0
for letra in ['a', 'e', 'i', 'o', 'u']:
    lista_vogais.append(texto.count(letra))
    print(f'Quantidade da vogal {letra} é: {texto.count(letra)}')
print(f'Total de vogais: {sum(lista_vogais)}')
