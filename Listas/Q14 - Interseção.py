# Dadas as listas
lista1 = [5, 1, 9, 3, 4, 7]
lista2 = [1, 8, 2, 7, 5, 0]

# Inicializa uma nova lista vazia para armazenar os números presentes em ambas as listas
numeros_comuns = []

# Percorre a primeira lista
for numero in lista1:
    # Verifica se o número está presente na segunda lista
    if numero in lista2:
        # Adiciona o número à nova lista se estiver presente em ambas as listas
        numeros_comuns.append(numero)

# Imprime a nova lista contendo os números comuns
print(f"Números presentes em ambas as listas: {numeros_comuns}")
