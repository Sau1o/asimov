usuario_correto = "Pedro"
senha_correta = "1234"

usuario = input("Digite o nome do usuário: ")
senha = input("Digite a senha:")

if usuario != usuario_correto and senha == senha_correta:
    print("Usuário não encontrado.")
elif usuario == usuario_correto and senha != senha_correta:
    print("Senha Incorreta.")
elif usuario == usuario_correto and senha == senha_correta:
    print("Sucesso")
