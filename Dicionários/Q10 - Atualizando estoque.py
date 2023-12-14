# Dado o dicionário de estoque
estoque = {
    'maçã': 10,
    'banana': 5,
    'laranja': 8,
    'uva': 12
    }

# Cria um novo dicionário para armazenar as novas frutas e quantidades
novas_frutas = {}

# Solicita ao usuário o nome e a quantidade de mais 3 frutas
for _ in range(3):
    nome_fruta = str(input("Digite o nome da fruta: "))
    quantidade_fruta = int(input("Digite a quantidade: "))
    novas_frutas[nome_fruta] = quantidade_fruta

# Atualiza o estoque com as novas frutas
estoque.update(novas_frutas)

# Imprime o estoque atualizado
print(f"Estoque Atualizado: {estoque}")
