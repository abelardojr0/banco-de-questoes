# Cria um dicionário vazio chamado pessoa
pessoa = {}

# Pede ao usuário para preencher os dados
pessoa['nome'] = str(input("Digite o nome: "))
pessoa['idade'] = int(input("Digite a idade: "))
pessoa['altura'] = float(input("Digite a altura (em metros): "))
pessoa['cidade'] = str(input("Digite a cidade: "))

# Imprime o dicionário preenchido
print("Dados da pessoa:")
print("Nome:", pessoa['nome'])
print("Idade:", pessoa['idade'])
print("Altura:", pessoa['altura'])
print("Cidade:", pessoa['cidade'])
