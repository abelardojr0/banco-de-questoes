# Solicita ao usuário que insira o nome
nome = str(input("Digite seu nome: "))

# Obtém a hora atual (você pode usar a biblioteca datetime)
hora_atual = int(input("Que horas são? (não inclua os minutos): "))

# Determina o cumprimento com base na hora
if 5 <= hora_atual < 12:
    cumprimento = "Bom dia"
elif 12 <= hora_atual < 18:
    cumprimento = "Boa tarde"
else:
    cumprimento = "Boa noite"

# Exibe o cumprimento com o nome do usuário
print(f"{cumprimento} {nome}")
