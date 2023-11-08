# Solicita ao usuário que insira a senha
senha_inserida = str(input("Insira a senha: ")).strip()

# Verifica se a senha inserida é igual à senha desejada
senha_correta = "123456Ab"

if senha_inserida == senha_correta:
    print("Acesso Liberado")
else:
    print("Acesso Negado")
