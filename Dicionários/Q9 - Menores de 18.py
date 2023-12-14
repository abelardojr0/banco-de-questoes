# Dada a lista de dicionários de pessoas
pessoas = [
    {'nome': 'Ana', 'idade': 16},
    {'nome': 'João', 'idade': 30},
    {'nome': 'Maria', 'idade': 17}
    ]

# Inicializa uma lista para armazenar os nomes das pessoas com menos de 18 anos
menores_de_18 = []

# Itera sobre a lista de dicionários
for pessoa in pessoas:
    if pessoa['idade'] < 18:
        menores_de_18.append(pessoa['nome'])

# Imprime a lista de nomes das pessoas com menos de 18 anos
print(f"Pessoas com menos de 18 anos: {menores_de_18}")
