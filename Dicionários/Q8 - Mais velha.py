# Dado o dicionário de pessoas
pessoas = {
    'João': 25,
    'Maria': 30,
    'Pedro': 22,
    'Ana': 28
}

# Inicializa variáveis para a pessoa mais velha
nome_mais_velho = ""
idade_mais_velha = float('-inf')  # Inicializa com um valor muito baixo

# Itera sobre o dicionário para encontrar a pessoa mais velha
for nome, idade in pessoas.items():
    if idade > idade_mais_velha:
        idade_mais_velha = idade
        nome_mais_velho = nome

# Imprime o nome da pessoa mais velha
print(f"Pessoa mais velha: {nome_mais_velho}")
