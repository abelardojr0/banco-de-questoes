# Dada a lista
lista_numeros = [2, 8, 15, 5, 3, 6, 1]

# Inicializa uma lista vazia para armazenar os elementos menores ou iguais a 5
lista_atualizada = []

# Percorre a lista original e adiciona à lista_atualizada apenas os elementos menores ou iguais a 5
for numero in lista_numeros:
    if numero <= 5:
        lista_atualizada.append(numero)

# Imprime a lista atualizada
print(f"Lista atualizada: {lista_atualizada}")
